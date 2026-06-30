def digsum(string):
    sum = 0
    for ch in string:
        if ch.isdigit():
            sum+=int(ch)
    return sum

string = input("Enter a string:")

sum = digsum(string)
print(sum)