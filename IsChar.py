char = input("Enter character:")

if (len(char) == 1 and ('A' <= char <= 'Z' or 'a'<= char <= 'z')):
    print("{} is an alphabet".format(char))
else:
    print("{} is not an alphabet".format(char))