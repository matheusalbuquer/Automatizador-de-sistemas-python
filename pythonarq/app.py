import pyautogui
from time import sleep

# 1 - Clicar e digitar meu usuario
pyautogui.click(676,380,duration=0.2)
pyautogui.write('jhonatan')
# 2 - clicar e diginha minha senha
pyautogui.click(680,416, duration=0.2)
pyautogui.write('123456')
# 3 - clicar em "Entrar"
pyautogui.click(588,434,duration=0.2)
# 4- Extrair cada produto
with open ('produtos.txt', 'r') as arquivos:
    for linha in arquivos:
        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]
        #    1 -clicar e digitar produto
        pyautogui.click(399,372,duration=0.2)
        pyautogui.write(produto)
        #    2 - clicar e digitar quantidade
        pyautogui.click(387,396,duration=0.2)
        pyautogui.write(quantidade)
        #    3 - clicar em digitar preço
        pyautogui.click(399,426,duration=0.2)
        pyautogui.write(preco)
        #    4 - clicar em registrar 
        pyautogui.click(313,581,duration=0.2)
        sleep(1)