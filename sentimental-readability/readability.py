from cs50 import get_string

text = get_string("Text: ")

# print index rounded to nearest int
# if index > 16 print grade 16+
# if index < 1 print before grade 1


def main():
    letter = letters(text)
    word = words(text)
    sentence = sentences(text)

    L = letter / word * 100
    S = sentence / word * 100

    index = round(0.0588 * L - 0.296 * S - 15.8)

    if (index >= 16):
        print("Grade 16+")
    elif (index < 1):
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


def letters(text):
    letter = 0
    for x in text:
        x = x.upper()
        if (ord(x) >= 65 and ord(x) <= 90):
            letter += 1
    return letter


def words(text):
    wordCount = 0

    for x in text:
        if (x == " "):
            wordCount += 1

    wordCount += 1
    return wordCount


def sentences(text):
    sentCount = 0
    for x in text:
        if (x == "." or x == "!" or x == "?"):
            sentCount += 1

    return sentCount


main()
