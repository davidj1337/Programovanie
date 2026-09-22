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


static int readHexNumber(const char *text, unsigned long *number)
{
    if (text[0] != '0' || (text[1] != 'x' && text[1] != 'X'))
    {
        return 0;
    }

    const char *digits = text + 2;

    if (!isxdigit((unsigned char)*digits))
    {
        return 0;
    }

    char *end;

    unsigned long value = strtoul(digits, &end, 16);

    if (*end != '\0')
    {
        return 0;
    }

    *number = value;

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

        char *equal = strchr(line, '=');

        if (equal == NULL)
        {
            printf("%s\n", line);
            continue;
        }

        *equal = '\0';

        char *savedResultText = equal + 1;

        unsigned long expectedResult;
        unsigned long savedResult;

        int expressionOk = evaluateExpression(line, &expectedResult);
        int resultOk = readHexNumber(savedResultText, &savedResult);

        if (expressionOk &&
            resultOk &&
            expectedResult == savedResult)
        {
            printf("%s=%s\n", line, savedResultText);
        }
        else
        {
            printf("%s\n", line);
        }
    }

    return 0;
}