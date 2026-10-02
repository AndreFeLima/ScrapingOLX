from selenium import webdriver as wb 
from selenium.webdriver .common.by import By 
import pandas as pd

search = input("Digite o nome da pesquisa: ").replace(' ', '+')

driver = wb.Chrome()
driver.implicitly_wait(10) # Tempo de espera máximo para a página ou elemento carregar
df = pd.DataFrame(columns=["Título", "Valor"])

i = 0
print("\033[1mRaspando os dados do site...\033[0m")

while True:
    driver.get(f"https://www.olx.com.br/estado-rn?q={search}&o={i}")

    # Buscando valor da casa e nomes no DOM
    values = driver.find_elements(By.XPATH,"//h3[@class='typo-body-large olx-adcard__price font-semibold']")
    names = driver.find_elements(By.XPATH,"//h2[@class='typo-body-large olx-adcard__title font-semibold']")


    # Quando a busca não retornar nenhum elemento a página não tem anúncio, o laço quebra
    if len(values) == 0 or len(names) == 0:break 

    for (value, name) in zip(values, names):
        df.loc[len(df)] = [name.text,value.text]
    
    i+=1

if len(df) : 
    print (f"\033[1;31mNenhum anúncio foi carregado, verifique a url ou tente executar novamente.\033[0m")

else:
    print (f"Foram carregados \033[1;32m{len(df)}\033[0m anúncios em \033[1;32m{i}\033[0m {"página" if i < 2 else "páginas"}.")
    df.to_csv("dados.csv")
    print ("\033[1mDados salvos em \033[0m\033[1;32mdados.csv \033[0m\033[0m")