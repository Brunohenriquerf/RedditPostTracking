# Importar bibliotecas
from selenium import webdriver
from time import sleep
import selenium
from selenium.webdriver.chrome.options import Options
import pandas as pd
from pandas import DataFrame
from IPython.display import display


# Definir tamanho da janela e ignorar erros
options = Options()
options.headless = False
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('window-size=1200,800')



# Selecionar navegador e opções
navegador = webdriver.Chrome(options=options, executable_path="C:\\Users\\bruno\\Desktop\\chromedriver.exe")

# Acessar o site

navegador.get("https://git.sebdoe.com/reddittracker/")

# Esperar a pagina carregar
sleep(3)

# Preparar array para receber informações
receptor = []

# Abrir site e inserir "https://www.reddit.com/r/EscapefromTarkov/comments/vqo4qn/lockpick_is_it_really_a_necessity/" no campo xpath "//*[@id="redditPostInput"]"
navegador.find_element("xpath", "//*[@id='redditPostInput']").send_keys("https://www.reddit.com/r/EscapefromTarkov/comments/vqo4qn/lockpick_is_it_really_a_necessity/")
# Esperar 3 segundos
sleep(3)

for i in range(1,60):
# Coletar informações
    col1 = str(navegador.find_element("xpath", "//*[@id='postScore']").text)                   
    col2 = str(navegador.find_element("xpath", "//*[@id='postUpvotes']").text)
    col3 = str(navegador.find_element("xpath", "//*[@id='postDownvotes']").text)
    col4 = str(navegador.find_element("xpath", "//*[@id='postAwards']").text)
    col5 = str(navegador.find_element("xpath", "//*[@id='postComments']").text)  
    receptor.append((col1,
                        col2,
                        col3,
                        col4,
                        col5))
    sleep(60)

# Definir as colunas que receberão os dados
cols=['col1', 'col2', 'col3', 'col4', 'col5']
# Preparar o dataframe
df = pd.DataFrame(receptor, columns=cols)
# Mostrar o dataframe no VS Code
display(df) 

# Trocar nome da coluna col1 para Score
df.rename(columns={'col1':'Score'}, inplace=True)
# Trocar nome da coluna col2 para Upvotes
df.rename(columns={'col2':'Upvotes'}, inplace=True)
# Trocar nome da coluna col3 para Downvotes
df.rename(columns={'col3':'Downvotes'}, inplace=True)
# Trocar nome da coluna col4 para Awards
df.rename(columns={'col4':'Awards'}, inplace=True)
# Trocar nome da coluna col5 para Comments
df.rename(columns={'col5':'Comments'}, inplace=True)

# Converter e salvar a tabela em CSV no local raiz deste código
df.to_csv(path_or_buf='C:\\Users\\bruno\\Desktop\\PostData.csv', sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label='Minutos passados', mode='w', encoding=None, compression='infer', quoting=None, quotechar='"', line_terminator=None, chunksize=None, date_format=None, doublequote=True, escapechar=None, decimal='.', errors='strict', storage_options=None)        
                
