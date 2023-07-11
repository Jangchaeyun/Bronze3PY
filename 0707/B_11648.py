num = input()

happy_phase = 0

multiple = 1

while True:
    if len(str(num)) == 1:
        print(happy_phase)
        break

    for digit in num:
        multiple *= int(digit)

    happy_phase += 1
    num = str(multiple)
    multiple = 1
