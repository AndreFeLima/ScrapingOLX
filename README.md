# Código de Raspagem do Site da OLX
Este repostório contém um código inicial para raspagem de dados da OLX especificamente da url https://www.olx.com.br/estado-rn?q=casas+em+natal&o. 

O objetivo principal é raspar o título e o valor dos anuncios dispostos na ulr. 

## Funcionamento do Código
O site estrutura os cards de anúncio da seguinte forma:
*   O título de cada card possui a classe: **typo-body-large olx-adcard__price font-semibold**
*   O valor de cada card possui a classe:  **typo-body-large olx-adcard__title font-semibold**

Com isso, o código busca dentre os elementos do DOM os que possuem essas classes, os guarda os textos de cada elemento em um dataframe e salva as informações em **dados.csv**

## Tecnologias e Bibliotecas
*   `Python 3.x`
*   `Selenium`
*   `Pandas`

## Como Executar

1. Clone este repositório:
   ```bash
   git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)
    
2. Ative um ambiente que possua as bibliotecas Pandas e Selenium.

3. Execute no terminal dentro do diretório do projeto:
   ```bash
   python3 scrapping.py