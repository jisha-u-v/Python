import subprocess
res=subprocess.run(['cat','test.txt'],stderr=subprocess.PIPE,text=True)
print(res.stderr)