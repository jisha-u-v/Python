# poll
from concurrent.futures import process
import subprocess
p1=subprocess.Popen(['ping','-c 5','flipkart.com'],stdout=subprocess.PIPE,text=True)
while True:
    output=p1.stdout.readline()
    if output:
        print(output.strip())
    res=p1.poll()
    if res is not None:
        break