from pyautogui import typewrite
from time import sleep

# msg = input("Enter the message: ")
delay = float(input("How much delay do you want between messages? "))


def regular_spam(msg, delay):
    """
    Automates de keyboard presses of the current value followed by the inputed 
    msg value and also sets a delay between consequent message
    """
    # typewrite(format_time() + msg + '\n')
    typewrite(msg + '\n')                    #uncomment if you want the spam message without date and time
    sleep(delay)




filepath = 'tt.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       regular_spam(line, delay)
       line = fp.readline()
       cnt += 1