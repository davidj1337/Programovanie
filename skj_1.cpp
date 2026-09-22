#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "static_lib.h"

void generuj(int m, int n)
{
    srand(time(NULL));

    int rows = m;
    int numbers = n;
    unsigned int number = 0;

    const char operators[] = {'&', '|', '^'};

    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < numbers; j++)
        {
            number = 10 + rand() % (1000 - 10 + 1);

            printf("0x%x", number);

            if (j < numbers - 1)
            {
                char op = operators[rand() % 3];
                printf("%c", op);
            }
        }

        printf("\n");
    }
}