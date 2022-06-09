import pyautogui
o="No"

while o=="No":
    o=pyautogui.confirm('Have you clik inside textboc to write',buttons=['Yes','No'])

for i in range(1, 50):
    pyautogui.write('your acc has been hacked',interval=0.1)
    pyautogui.press('enter')