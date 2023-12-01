def open_file():
    f = open("input","r")
    return f

j = 0

dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
dict2 = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

with open_file() as file:
    k = file.readlines()
    i = 0
    while i < 1000:
        str = []
        f = k[i]
        if f in dict2:
            str.append(dict[f])
            str2 = str[0] + str[-1]
            j += str2
        i += 1        
print(j)