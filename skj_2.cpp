#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#include "compute.h"


static int evaluateExpression(const char *expression, unsigned long *result)
{
    const char *p = expression;
    char *end;

    if (p[0] != '0' || (p[1] != 'x' && p[1] != 'X'))
    {
        return 0;
    }

    p += 2;

    if (!isxdigit((unsigned char)*p))
    {
        return 0;
    }

    unsigned long value = strtoul(p, &end, 16);
    p = end;

    while (*p != '\0')
    {
        char op = *p;

        if (op != '&' && op != '|' && op != '^')
        {
            return 0;
        }

        p++;

        if (p[0] != '0' || (p[1] != 'x' && p[1] != 'X'))
        {
            return 0;
        }

        p += 2;

        if (!isxdigit((unsigned char)*p))
        {
            return 0;
        }

        unsigned long nextNumber = strtoul(p, &end, 16);
        p = end;

        if (op == '&')
        {
            value = value & nextNumber;
        }
        else if (op == '|')
        {
            value = value | nextNumber;
        }
        else
        {
            value = value ^ nextNumber;
        }
    }

    *result = value;

    return 1;
}


int compute(FILE *file)
{
    char line[4096];

    while (fgets(line, sizeof(line), file) != NULL)
    {
        line[strcspn(line, "\r\n")] = '\0';

        if (line[0] == '#')
        {
            printf("%s\n", line);
            continue;
        }

        if (strchr(line, '=') != NULL)
        {
            printf("%s\n", line);
            continue;
        }

        unsigned long result;

        if (evaluateExpression(line, &result))
        {
            printf("%s=0x%lx\n", line, result);
        }
        else
        {
            printf("#%s\n", line);
        }
    }

    return 0;
}