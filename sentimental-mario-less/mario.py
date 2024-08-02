from cs50 import get_int


while True:
    height = get_int("height: ")
    if (height >= 1 and height <= 8):
        break


for i in range(1, height+1):
    for j in range(height - i):
        print(" ", end="")
    for k in range(i):
        print("#", end="")

    print()
