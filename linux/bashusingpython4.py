import subprocess
# Popen()  it give use more option to execute the commands
# wait -- used to wait until the completion of the execution of the command

p1=subprocess.Popen(['ls','-la'])
print('complete') #here this print will execute before the execution of command


p1=subprocess.Popen(['ls','-la'])
p1.wait()
print('complete') #here this print will execute after the execution of command