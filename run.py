import os
import schedule, time
import subprocess
import datetime

cmd = os.getcwd()+"/main.exe"
cmd1 = os.getcwd()+"/push.bat"
 
# Functions setup
def main():
  try:
   print("start at: %s:%s:%s" % (times().hour, times().minute, times().second))
   result = subprocess.run(cmd,shell=True)
   subprocess.call(cmd1)
   print("end at: %s:%s:%s" % (times().hour, times().minute, times().second))
  except Exception as e:
   print(e)
   
def times():
 e = datetime.datetime.now()
 return e

# Task scheduling
# After every 10mins hello_world() is called.


x = input('Enter your minute: ')

schedule.every(int(x)).minutes.do(main)

print("start schedule with time: "+str(x))


while True:

	# Checks whether a scheduled task
	# is pending to run or not
	schedule.run_pending()
	time.sleep(1)
