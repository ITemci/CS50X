from cs50 import get_float


while True:
    change = get_float("Change: ")
    if (change > 0):
        break
coins = 0


change *= 100

quarters = change // 25
change %= 25
coins += quarters

dimes = change//10
change %= 10
coins += dimes


nickle = change//5
change %= 5
coins += nickle


coins += change


print(int(coins))
