"""


"""

import os


# list to store the lines of output after running stract command in shell
lines = []

with open("file.txt", "r") as f:
    lines = [line.rstrip() for line in f]


func = dict()  # dictionary to store number of times a particular function is called
for item in lines:
    flag = 0
    s = ""
    for c in item:
        # inside this loop if the function is encountered for the first time
        if c == "(":
            flag = 1
            break
        s += c
    if flag == 1:
        func[s] = func.get(s, 0) + 1


for i, j in func.items():
    print("systemcall name", i, "\t\tnumber of calls", j)


if __name__ == "__main__":
    os.system("python3 main.py && python3 util.py {}")
    file = open("file.txt", "r+")
    file.truncate(0)
    exit(0)
