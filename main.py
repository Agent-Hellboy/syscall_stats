import subprocess

command = ["/bin/bash", "./script.sh", "strace"]

binary = str(input("enter the name of binary"))

# appending the binary name in the list
command.append(binary)

subprocess.run(command)
