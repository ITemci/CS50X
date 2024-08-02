#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int letters(string text);
int words(string text);
int sentences(string text);

int main(void)
{
    string text = get_string("Text: ");

    // counting letters, words and sentences using functions from the bottom of document and assigning them to variables
    int letters_count = letters(text);
    int words_count = words(text);
    int sentence_count = sentences(text);

    // finging L and S using variable above
    float L = (float) letters_count / (float) words_count * 100;
    float S = (float) sentence_count / (float) words_count * 100;

    // finding index by applying Coleman-Liau index formula
    int index = round((0.0588 * L) - (0.296 * S) - 15.8);

    // outputing the result
    if (index >= 16)
    {
        printf("Grade 16+\n");
    } 
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

int letters(string text)
{
    int letter = 0;
    int text_len = strlen(text);

    for (int i = 0; i < text_len; i++)
    {
        int x = toupper(text[i]);
        if (x >= 65 && x <= 90)
        {
            letter++;
        }
    }

    return letter;
}

int words(string text)
{
    int words = 0;
    int text_len = strlen(text);

    for (int i = 0; i < text_len; i++)
    {
        if (text[i] == ' ')
        {
            words++;
        }
    }

    words++;
    return words;
}

int sentences(string text)
{
    int sentence = 0;
    int text_len = strlen(text);

    for (int i = 0; i < text_len; i++)
    {
        char x = text[i];
        if (x == '.' || x == '!' || x == '?')
        {
            sentence++;
        }
    }

    return sentence;
}
