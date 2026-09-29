/*
Zadání
Použijte přípravu, spojíme ls a stat dohromady.
1. Upravte svůj ls tak, by vypisoval opakovaně zadané soubory – cca 1x za 2–3 sekundy. Při spuštění si zadáte třídění dle velikosti nebo jména, viz příklad na githubu, parametr -u si vynutí opačný směr třídění.
Pokud nějaký soubor zmizí, budou informace o něm jen otazníky.

2. Pokud se při výpisu souborů zjistí, že došlo ke změně velikosti souboru, tak se na stderr vypíše ----- soubor a následují jen nová data. Soubory neudržujte stále otevřené, otevření jen při změně.
Pokud nějaký soubor nebude mít (ztratí) právo pro čtení, indikujte to ve výpise.
Pro účely zobrazení stderr použijte druhý terminál. V něm si zjistěte tty a to použijte pro přesměrování stderr v prvním terminálu na druhý.
myls ........ 2>/dev/pts/xy
*/


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/param.h>
#include <sys/stat.h>
#include <unistd.h>
#include <fcntl.h>
#include <time.h>

struct file_info_t
{
    char file_name[MAXPATHLEN];
    struct stat file_stat;
    off_t old_size;
    int exists;
    int readable;
};

void get_rights(mode_t mode, char *rights)
{
    for (int i = 0; i < 9; i++)
    {
        rights[i] = '-';
    }

    rights[9] = '\0';

    if (mode & S_IRUSR)
    {
        rights[0] = 'r';
    }
    if (mode & S_IWUSR)
    {
        rights[1] = 'w';
    }
    if (mode & S_IXUSR)
    {
        rights[2] = 'x';
    }
    if (mode & S_IRGRP)
    {
        rights[3] = 'r';
    }
    if (mode & S_IWGRP)
    {
        rights[4] = 'w';
    }
    if (mode & S_IXGRP)
    {
        rights[5] = 'x';
    }
    if (mode & S_IROTH)
    {
        rights[6] = 'r';
    }
    if (mode & S_IWOTH)
    {
        rights[7] = 'w';
    }
    if (mode & S_IXOTH)
    {
        rights[8] = 'x';
    }
}

int cmp_file_names(const void *f1, const void *f2)
{
    file_info_t *file1 = (file_info_t *)f1;
    file_info_t *file2 = (file_info_t *)f2;

    return strcmp(file1->file_name, file2->file_name);
}

int cmp_file_sizes(const void *f1, const void *f2)
{
    file_info_t *file1 = (file_info_t *)f1;
    file_info_t *file2 = (file_info_t *)f2;

    off_t size1 = 0;
    off_t size2 = 0;

    if (file1->exists)
    {
        size1 = file1->file_stat.st_size;
    }

    if (file2->exists)
    {
        size2 = file2->file_stat.st_size;
    }

    if (size1 < size2)
    {
        return -1;
    }

    if (size1 > size2)
    {
        return 1;
    }

    return 0;
}

void print_new_data(file_info_t *file, off_t new_size)
{
    int fd = open(file->file_name, O_RDONLY);

    if (fd < 0)
    {
        return;
    }

    if (lseek(fd, file->old_size, SEEK_SET) < 0)
    {
        close(fd);
        return;
    }

    off_t remaining = new_size - file->old_size;
    char buffer[1024];

    while (remaining > 0)
    {
        int to_read = sizeof(buffer);

        if (remaining < to_read)
        {
            to_read = remaining;
        }

        int count = read(fd, buffer, to_read);

        if (count <= 0)
        {
            break;
        }

        write(STDERR_FILENO, buffer, count);
        remaining -= count;
    }

    close(fd);
}

void update_file(file_info_t *file)
{
    struct stat new_stat;

    if (stat(file->file_name, &new_stat) < 0)
    {
        file->exists = 0;
        file->readable = 0;
        file->old_size = 0;
        memset(&file->file_stat, 0, sizeof(file->file_stat));
        return;
    }

    file->exists = 1;

    if (access(file->file_name, R_OK) == 0)
    {
        file->readable = 1;
    }
    else
    {
        file->readable = 0;
    }

    off_t new_size = new_stat.st_size;

    if (new_size != file->old_size)
    {
        fprintf(stderr, "----- %s\n", file->file_name);

        if (new_size > file->old_size && file->readable)
        {
            print_new_data(file, new_size);
        }

        file->old_size = new_size;
    }

    file->file_stat = new_stat;
}

void print_file(file_info_t *file)
{
    if (!file->exists)
    {
        printf("%12s %9s %24s %s\n", "?", "?", "?", file->file_name);
        return;
    }

    char rights[10];
    get_rights(file->file_stat.st_mode, rights);

    struct tm *file_time = localtime(&file->file_stat.st_ctime);

    printf("%12lld %9s %24.24s ",
           (long long)file->file_stat.st_size,
           rights,
           asctime(file_time));

    if (!file->readable)
    {
        printf("[NO READ] ");
    }

    printf("%s\n", file->file_name);
}

int main(int argc, char *argv[])
{
    if (argc <= 1)
    {
        printf("Use: %s [-n] [-s] [-u] file ...\n", argv[0]);
        printf("  -n  sort by file name\n");
        printf("  -s  sort by file size\n");
        printf("  -u  reverse sort order\n");
        return 1;
    }

    int sort_names = 0;
    int sort_size = 0;
    int reverse = 0;

    file_info_t *files = (file_info_t *)malloc(sizeof(file_info_t) * argc);

    if (files == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }

    int file_count = 0;

    for (int i = 1; i < argc; i++)
    {
        if (strcmp(argv[i], "-n") == 0)
        {
            sort_names = 1;
        }
        else if (strcmp(argv[i], "-s") == 0)
        {
            sort_size = 1;
        }
        else if (strcmp(argv[i], "-u") == 0)
        {
            reverse = 1;
        }
        else if (argv[i][0] != '-')
        {
            memset(&files[file_count], 0, sizeof(file_info_t));
            strncpy(files[file_count].file_name, argv[i], MAXPATHLEN - 1);
            files[file_count].file_name[MAXPATHLEN - 1] = '\0';

            struct stat info;

            if (stat(files[file_count].file_name, &info) == 0)
            {
                files[file_count].file_stat = info;
                files[file_count].old_size = info.st_size;
                files[file_count].exists = 1;

                if (access(files[file_count].file_name, R_OK) == 0)
                {
                    files[file_count].readable = 1;
                }
                else
                {
                    files[file_count].readable = 0;
                }
            }
            else
            {
                files[file_count].old_size = 0;
                files[file_count].exists = 0;
                files[file_count].readable = 0;
            }

            file_count++;
        }
    }

    if (file_count == 0)
    {
        printf("No file specified.\n");
        free(files);
        return 1;
    }

    while (1)
    {
        for (int i = 0; i < file_count; i++)
        {
            update_file(&files[i]);
        }

        if (sort_names)
        {
            qsort(files, file_count, sizeof(file_info_t), cmp_file_names);
        }

        if (sort_size)
        {
            qsort(files, file_count, sizeof(file_info_t), cmp_file_sizes);
        }

        printf("\n");

        if (!reverse)
        {
            for (int i = 0; i < file_count; i++)
            {
                print_file(&files[i]);
            }
        }
        else
        {
            for (int i = file_count - 1; i >= 0; i--)
            {
                print_file(&files[i]);
            }
        }

        fflush(stdout);
        sleep(2);
    }

    free(files);
    return 0;
}
