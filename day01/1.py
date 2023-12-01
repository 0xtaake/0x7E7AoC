def open_file():
    f = open("input","r")
    return f

def check_sum_line(line):
    i = 0
    for j in line:
        if j.isnumeric():
            i += int(j)
    return i

i = 0

f = open_file()

lines = f.readlines()

for line in lines:
    i += int(check_sum_line(line))

print(i)