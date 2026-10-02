from selenium import webdriver as wb 
from selenium.webdriver .common.by import By 
import pandas as pd

search = input("Digite o nome da pesquisa: ").replace(' ', '+')

driver = wb.Chrome()
driver.implicitly_wait(10) # Tempo de espera máximo para a página ou elemento carregar
df = pd.DataFrame(columns=["Título", "Valor", "Metro_Quadrado", "Quartos", "Banheiros", "Vagas_Garagem"])

i = 0

def process_detais(details):
    data = {
        "Vagas_Garagem"       : '',
        "Quartos"             : '',
        "Banheiros"           : '',
        "Metros_Quadrados"    : ''
        }

    for detail in details:
        text = detail.get_attribute("aria-label").split()
        if "vagas" in text or "vaga" in text:
            if "mais" in text:
                data['Vagas_Garagem'] = '+' + text[0]
            else:
                data['Vagas_Garagem'] = text[0]
        elif "quartos" in text or "quarto" in text:
            if "mais" in text:
                data['Quartos'] = '+' + text[0]
            else:
                data['Quartos'] = text[0]
        elif "banheiros" in text or "banheiro" in text:
            if "mais" in text:
                data['Banheiros'] = '+' + text[0]
            else:
                data['Banheiros'] = text[0]
        elif "metros" in text:
            data['Metros_Quadrados'] = text[0]
        else:
            print ("\033[1;31mElemento em details não faz referência a nenhum valor-padrão.\033[0m")
            print (text)
            print ("\033[1;31m=====================================================================")

    return data 
        

print("\033[1mRaspando os dados do site...\033[0m")

while True:
    driver.get(f"https://www.olx.com.br/estado-rn?q={search}&o={i}")

    if len(driver.find_elements(By.XPATH, "//div[@class='AdNotFound-module-scss-module__YGp7Ka__wrapper']")) != 0:
        break 
    
    # Buscando valor da casa e nomes no DOM
    values = driver.find_elements(By.XPATH,"//h3[@class='typo-body-large olx-adcard__price font-semibold']")
    names = driver.find_elements(By.XPATH,"//h2[@class='typo-body-large olx-adcard__title font-semibold']")
    cards_details = driver.find_elements(By.XPATH, "//div[@class='olx-adcard__details']")


    for (value, title, card_details) in zip(values, names, cards_details):
        details = card_details.find_elements(By.XPATH, "./div[@class='olx-adcard__detail']")
        details_values = process_detais (details)


        df.loc[len(df)] = [ title.text,
                            value.text,
                            details_values["Metros_Quadrados"], 
                            details_values["Quartos"], 
                            details_values["Banheiros"], 
                            details_values["Vagas_Garagem"]
                        ]
    i+=1

if len(df) < 1: 
    print (f"\033[1;31mNenhum anúncio foi carregado, verifique a url ou tente executar novamente.\033[0m")

else:
    print (f"Foram carregados \033[1;32m{len(df)}\033[0m anúncios em \033[1;32m{i}\033[0m {"página" if i < 2 else "páginas"}.")
    df.to_csv("dados.csv")
    print ("\033[1mDados salvos em \033[0m\033[1;32mdados.csv \033[0m\033[0m")