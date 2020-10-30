import sys

args = sys.argv
if len(args) < 3:
    print("The script should be called with two arguments, the first and the second number to be multiplied")
else:
    x = float(args[1])
    y = float(args[2])
    print(x * y)

