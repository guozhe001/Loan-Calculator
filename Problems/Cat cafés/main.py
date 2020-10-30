cat_coffee = []
while True:
    a = input()
    if a == "MEOW":
        break
    split = a.split(" ")
    cat_coffee.append({"name": split[0], "count": int(split[1])})

coffee = None
for c in cat_coffee:
    coffee = (c if c["count"] > coffee["count"] else coffee) if coffee else c

print(coffee["name"])
