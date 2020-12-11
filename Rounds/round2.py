def countValid1(rule, password):
    numbers = rule.split(" ")[0]
    low = int(numbers.split("-")[0])
    high = int(numbers.split("-")[1])
    char = rule.split(" ")[1]
    if high >= password.count(char) >= low:
        return True


def countValid2(rule, password):
    numbers = rule.split(" ")[0]
    low = int(numbers.split("-")[0]) - 1
    high = int(numbers.split("-")[1]) - 1
    char = rule.split(" ")[1]
    one = password[low] == char and password[high] != char
    two = password[low] != char and password[high] == char
    return one or two


aFile = open('../inputs/passwords.txt', 'r')
Lines = aFile.readlines()
count = 0
for line in Lines:
    rule = line.split(":")[0]
    password = line.split(":")[1].strip()
    if countValid2(rule, password):
        count += 1

print(count)
