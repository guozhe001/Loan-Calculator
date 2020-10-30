numbers = []
while True:
    s = input()
    if s == ".":
        break
    numbers.append(float(s))
print(min(numbers))
