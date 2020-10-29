string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0
for char in string:
    if vowels.__contains__(char):
        count += 1

print(count)
