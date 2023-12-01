def open_file():
    f = open("input","r")
    return f

j = 0

with open_file() as file:
    k = file.readlines()
    i = 0
    while i < 1000:
        str = ""
        f = k[i]
        for m in f:
            if m.isdigit():
                str += m
        str2 = str[0] + str[-1]
        j += int(str2)
        i += 1

print(j)