#include <cs50.h>
#include <stdio.h>

void calc_years(int x, int y);

int main(void)
{
    // Declaring variables
    int start_size, end_size;

    // Prompt for start size
    do
    {
        start_size = get_int("Start size: ");
    }
    while (start_size < 9);

    // Prompt for end size
    do
    {
        end_size = get_int("End size: ");
    }
    while (end_size < start_size);

    // Calculate number of years until we reach threshold

    calc_years(start_size, end_size);
}

void calc_years(int x, int y)
{
    int population = x;
    int years = 0;

    while (!(population >= y))
    {
        population = population + (int) (population / 3) - (int) (population / 4);
        years++;
    }

    printf("Years: %i\n", years);
}
