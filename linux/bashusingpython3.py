import subprocess
res=subprocess.run(['echo','hi mu name ashish'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
print(res.stdout)