# Passo a passo
# Passo 1 - Entrar no sistema
# Passo 2 - fazer login
# Passo 3 - importar base de dados
# Passo 4 - Cadastra o produto
# Passo 5 - Repetir até acabar a lista de produtos

import pyautogui
import time

# pyautogui.click - clicar com o mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.hotkey - combinação de teclas (ctrl+c)
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.70   # tempo de execussão

# Passo 1

pyautogui.press("win")
pyautogui.write("Google Chrome")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click(x=381, y=538)
#pyautogui.write("dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(5)

# Passo 2

pyautogui.click(x=203, y=363)
# pyautogui.hotkey("ctrl", "a") para selecionar se precisar
pyautogui.write("erikaroniela9@gmail.com")
pyautogui.press("tab") # muda para o campo de senha
pyautogui.write("minha senha")
pyautogui.click(x=382, y=494)

time.sleep(5)

# Passo 3

import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Passo 4
for linha in tabela.index:

    # Código do Produto
    pyautogui.click(x=169, y=269)

    codigo = str(tabela.loc[linha, "codigo"]) # string = texto
    pyautogui.write(codigo)

    # Marca do Produto
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    # Tipo do Produto
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    # Categoria do Produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    # Preço Unitário do Produto
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    # Custo do Produto
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    # OBS

    # OBS
    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])  # Corrigir a variável de custo para obs
    if obs != "nan":
        pyautogui.write(obs)

    # Clicar no botão enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000) # para voltar ao inicio

      
    