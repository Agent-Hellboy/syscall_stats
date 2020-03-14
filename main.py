import subprocess
lis=['/bin/bash','./script.sh','strace']
cmd2=str(input("enter the name of binary"))
lis.append(cmd2)
subprocess.run(lis)
