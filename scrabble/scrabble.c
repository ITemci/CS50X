#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};
int letters[] = {65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90};

// Getting letters array lenght
int letters_len = sizeof(letters) / sizeof(letters[0]);

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);

    // Printing the winner

    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }
    else if (score1 < score2)
    {
        printf("Player 2 wins!\n");
    }
    else
        printf("Tie!\n");
}

int compute_score(string word)
{
    // Compute and return score for string
    // Declaring some variables needed later in the program
    int sum = 0;
    int lenght = strlen(word); // finding the lenght of the word
    int x;                     // position in word as int

    // iterating through word
    for (int i = 0; i < lenght; i++)
    {
        x = toupper(word[i]);

        // iterate through letters array
        for (int j = 0; j < letters_len; j++)
        {
            // comparing values of x to value in letters to get the letter position in alphabetical order
            if (x == letters[j])
            {
                // adding to sum the value from array points at the same index as the letter in array letters
                sum += POINTS[j];
                break;
            }
        }
    }
    // returning sum
    return sum;
}
