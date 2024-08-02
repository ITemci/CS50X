#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;
void to_binary(int i);
void print_bulb(int bit);

int main(void)
{
    // TODO
    string text = get_string("Message: ");
    int lenght = strlen(text);
    // declaring variable text_dec to store int values of chars according to ascii
    int text_dec[lenght];

    // iterating throgh text and converting each char to int
    for(int i = 0; i < lenght ; i++)
    {
        text_dec[i] = (int) text[i];
        // converting each element of text_dec array to binary using function to_binary and outputing it
        to_binary(text_dec[i]);

    }

}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

// turn text into decimal numbers
// take decimals, and convert them into binary as 8 bits
// print result using print_bulb function


// converting int to binary
void to_binary(int number)
{
    for (int i = 7; i >= 0; i--) {
        int bit = (number >> i) & 1;

        // calling function print_bulb to print right emoji depending if bit is 0 or 1
       print_bulb(bit);
    }
    printf("\n");
}
