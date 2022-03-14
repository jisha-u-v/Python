import subprocess
from sys import stdout
# communicate --- is used to get the output,error and give input to the command.
p1=subprocess.Popen(['echo','welcome to ust'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
res=p1.communicate()
print(res)