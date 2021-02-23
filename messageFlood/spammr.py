import pyautogui, time

time.sleep(5)

print('LETS GOOOOOO')

f= open('data/bee.txt','r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
  
  
  
  
