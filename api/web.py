# Fonte https://www.youtube.com/watch?v=HrGLX7JUVoQ
# Importando as bibliotecas
import requests
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup

def my_method(ticker):
    # URL com a tabela de dados
    url = f"https://www.fundamentus.com.br/proventos.php?papel={ticker}&tipo=2"

    # Obtendo o conteúdo da página em formato de texto

    # https://stackoverflow.com/questions/68259148/getting-404-error-for-certain-stocks-and-pages-on-yahoo-finance-python
    headers = { 
        'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
        'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
        'Accept-Language' : 'en-US,en;q=0.5',
        'DNT'             : '1', # Do Not Track Request Header 
        'Connection'      : 'close'
    }
    data = requests.get(url, headers=headers, timeout=5).text
    soup = BeautifulSoup(data,"html.parser")

    # Procurando a tabela da página
    table = soup.find('table') # em html uma tabela é representada pela tag <table>

    # Definindo dataframe
    df = pd.DataFrame(columns=['Data', 'Valor', 'Tipo', 'Data de Pagamento', 'Por quantas ações'])

    # Obtendo todas as linhas da tabela
    for row in table.tbody.find_all('tr'): # em html uma linha da tabela é representada pela tag <tr>
        # Obtendo todas as colunas em cada linha
        columns = row.find_all('td')  # em html uma coluna da tabela é representada pela tag <td>
        if(columns != []):
            data = columns[0].text.strip(' ')
            valor = columns[1].text.strip(' ')
            tipo = columns[2].text.strip(' ')
            data_pagamento = columns[3].text.strip(' ')
            quantidade_acoes = columns[4].text.strip(' ')
            df = pd.concat([df, pd.DataFrame.from_records([{'Data': data,  'Valor': valor, 'Tipo': tipo, 'Data de Pagamento': data_pagamento, 'Por quantas ações': quantidade_acoes}])], ignore_index=True)

    result = df.head(20)

    # Convert DataFrame to JSON
    json_data = result.to_json(orient='records')
    return json_data
