#include <cs50.h>
#include <stdio.h>

void print_hash(int hash);

int main(void)
{
    int height;

    do
    {
        height = get_int("Introduce pyramid height: ");
    }
    while (height < 1 || height >= 9);

    int space = height - 1;
    int hash = 1;

    // initiating a for loop that will run as many times as user asks
    for (int i = 0; i < height; i++)
    {
        // initiating a for loop that will print a empty space as many times as is the input value - 1
        for (int j = 0; j < space; j++)
        {
            printf(" ");
        }

        // decrementing the space variable
        space--;

        // calling function print_has to print #, the space, then one more time, then incrementing valye of hash variable
        print_hash(hash);
        printf("  ");
        print_hash(hash);
        hash++;

        // changing the line
        printf("\n");
    }
}

// initiating the print_hash function that prints # as many time as variable hash says in a for loop
void print_hash(int hash)
{
    for (int k = 0; k < hash; k++)
    {
        printf("#");
    }
}
