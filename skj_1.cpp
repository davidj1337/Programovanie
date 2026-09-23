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

#############################################################################
#
# Operating Systems - static + dynamic libraries
#
#############################################################################

# =========================
# STATIC LIBRARY
# =========================

TARGET1 = main1/generuj

STATIC_LIBNAME = static_lib
STATIC_LIBFILE = static_lib/lib$(STATIC_LIBNAME).a


# =========================
# DYNAMIC LIBRARIES
# =========================

TARGET2 = main2/main

DYN_LIBNAME = compute
DYN_LIBFILE1 = dyn_lib1/lib$(DYN_LIBNAME).so
DYN_LIBFILE2 = dyn_lib2/lib$(DYN_LIBNAME).so


# =========================
# BUILD ALL
# =========================

all: $(TARGET1) $(DYN_LIBFILE1) $(DYN_LIBFILE2) $(TARGET2)


# =========================
# STATIC LIBRARY
# =========================

$(STATIC_LIBFILE): static_lib/static_lib.o
	@echo "\nCreating static library...\n"
	ar r $@ $^
	@echo "\nStatic library created: '$(STATIC_LIBFILE)'.\n"


# =========================
# PROGRAM USING STATIC LIBRARY
# =========================

$(TARGET1): main1/main.cpp $(STATIC_LIBFILE)
	@echo "\nCreating static application...\n"
	g++ -g -Wall -Werror -Istatic_lib -Lstatic_lib $< -l$(STATIC_LIBNAME) -o $@
	@echo "\nApplication '$(TARGET1)' is ready.\n"


# =========================
# DYNAMIC LIBRARY 1
# =========================

$(DYN_LIBFILE1): dyn_lib1/compute.o
	@echo "\nCreating dynamic library 1...\n"
	g++ -g -Wall -Wextra $^ -shared -o $@
	@echo "\nDynamic library created: '$(DYN_LIBFILE1)'.\n"


# =========================
# DYNAMIC LIBRARY 2
# =========================

$(DYN_LIBFILE2): dyn_lib2/compute.o
	@echo "\nCreating dynamic library 2...\n"
	g++ -g -Wall -Wextra $^ -shared -o $@
	@echo "\nDynamic library created: '$(DYN_LIBFILE2)'.\n"


# =========================
# PROGRAM USING DYNAMIC LIBRARY
# =========================

$(TARGET2): main2/main.cpp $(DYN_LIBFILE1)
	@echo "\nCreating dynamic application...\n"
	g++ -g -Wall -Wextra -Idyn_lib1 -Ldyn_lib1 $< -l$(DYN_LIBNAME) -o $@
	@echo "\nApplication '$(TARGET2)' is ready.\n"


# =========================
# CLEAN
# =========================

clean:
	rm -rf $(TARGET1) $(TARGET2) \
	$(STATIC_LIBFILE) \
	$(DYN_LIBFILE1) $(DYN_LIBFILE2) \
	static_lib/*.o dyn_lib1/*.o dyn_lib2/*.o
