'''
https://pyautogui.readthedocs.io/en/latest/
'''
### Importações
import pyautogui
import time

### Definições:
pyautogui.PAUSE = 0.5

### Veriáveis:

### Main:
pyautogui.alert('Vamos iniciar uma automação, não use o computador enquanto isso!')
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.hotkey('altleft', 'f4')
pyautogui.hotkey('winleft', 'd')
pyautogui.moveTo(1500,150)
pyautogui.mouseDown()
pyautogui.moveTo(1700,450)
pyautogui.mouseUp()
time.sleep(1)

'''
Para pegar a posição do cursor:
    import time
    time.sleep(3)
    pyautogui.positio()
'''