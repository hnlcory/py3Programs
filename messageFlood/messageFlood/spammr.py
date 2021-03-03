import pyautogui, time

time.sleep(5)

print('LETS GOOOOOO')

f= open('data/army.txt','r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
  
  
  
  
