from pyautogui import typewrite
from time import sleep
from datetime import datetime

#Variables
msg = input("Enter the message: ")
n = input("How many times ?: ")
delay = input("How much delay do you want? ")

def format_time():
    t = datetime.now()
    s = t.strftime('%Y-%m-%d %H:%M:%S.%f')
    return "date: " + s[5:-7] + "-> "

print(format_time())



print("t minus")

sleep(5)
count = 5
while(count != 0):
	print(count)
	sleep(1)
	count -= 1

print("Fire in the hole!!!")

for i in range(0,int(n)):
    for k in range(9):
        typewrite(format_time() + msg + '\n')
        sleep(0.8)
    sleep(5)               # discord wait time. Fuck discord, all my homies hate discord