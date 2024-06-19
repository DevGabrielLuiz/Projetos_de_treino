import pyautogui
import time


pyautogui.PAUSE = 2 #obriga o pyautogui esperar esse tempo em segundo para executar a proxima linha de codigo
# abrir a ferramenta/ o sistema/ o programa
pyautogui.press("Win")
pyautogui.write("Login.xlsx ")
pyautogui.press("Backspace")#tecla de apagar
pyautogui.press("Enter")
#preencher o login
time.sleep(5)
pyautogui.position()#devolve a posição do seu mouse nas cordenadas x e y do seu computador
#preenchendo o usuario
pyautogui.click(450, 280)
pyautogui.write("Gabriel")
# preencher a senha
pyautogui.click(450, 350)
pyautogui.write('12345')
# clicar em fazer login
pyautogui.click(500,420)
