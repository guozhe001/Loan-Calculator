a = input()

result = ""
i = 0
for char in a:
    if char.isupper() and i > 0:
        result += "_"
    result += str.lower(char)
    i += 1

print(result)
