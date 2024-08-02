#include <cs50.h>
#include <math.h>
#include <stdio.h>

int doubles_sum(long nr);
int evens_sum(long nr);
int get_first(long i);
bool get_last(int sum);

int main(void)
{
    long card_nr;
    int digits = 0;

    // Asking user for card number
    do
    {
        digits = 0;
        card_nr = get_long("Number: ");
        get_first(card_nr);
        long temp = card_nr;
        // counting the letters in number
        while (temp != 0)
        {
            temp /= 10;
            digits++;
        }
    }
    // checking the number lenght
    while (digits < 13 || digits > 16);

    // finding first digit
    int first_digit = get_first(card_nr);

    // finding the total sum and printing it
    int doubledSum = doubles_sum(card_nr);
    int summed = evens_sum(card_nr);
    int totalSum = doubledSum + summed;

    // finding if last digit of sum is 0
    bool legit = get_last(totalSum);

    // checking if card_nr ends in 0, then it will determin which card is and print name
    if (legit)
    {
        if ((first_digit == 34 || first_digit == 37) && digits == 15)
        {
            printf("AMEX\n");
        }
        else if ((first_digit >= 51 && first_digit <= 55) && digits == 16)
        {
            printf("MASTERCARD\n");
        }
        else if ((first_digit >= 40 && first_digit <= 49) && (digits == 13 || digits == 16))
        {
            printf("VISA\n");
        }
    }
    else
        printf("INVALID\n");
}

int get_first(long i)
{
    // dividing to 10 to get first 2 digit
    while (i >= 100)
    {
        i /= 10;
    }
    return i;
}

bool get_last(int sum)
{

    if (sum % 10 == 0)
        return true;
    else
        return false;
}

int doubles_sum(long nr)
{
    int position = 0;
    int sum = 0;
    while (nr > 0)
    {
        // Get the last digit
        int digit = nr % 10;

        // Check if it's the second digit from the end
        if (position % 2 == 1)
        {
            int doubledDigit = digit * 2;
            if (doubledDigit >= 10)
            {
                doubledDigit = (doubledDigit % 10) + (doubledDigit / 10);
            }

            sum += doubledDigit;
        }

        // Move to the next digit
        nr /= 10;
        position++;
    }
    return sum;
}

int evens_sum(long nr)
{
    int position = 0;
    int sum1 = 0;
    while (nr > 0)
    {
        // Get the last digit
        int digit = nr % 10;

        // Check if it's the last digit from the end
        if (position % 2 == 0)
        {

            sum1 += digit;
        }

        // Move to the next digit
        nr /= 10;
        position++;
    }
    return sum1;
}
