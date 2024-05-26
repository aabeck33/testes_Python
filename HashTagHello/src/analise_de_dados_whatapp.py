'''
Problema: Analisar dados e enviar mensagem via Whatsapp
Solução:
    Entrar no site da loja Magazine Luiza (https://ri.magazineluiz.com.br)
    Baixar os dados a serem analisados
    
'''
### Importações:
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import urllib

### Definicições:

### Variáveis:
service = Service('../other/chromedriver')
#servico = Service(ChromeDriverManager().install())
#navegador = webdriver.Chrome(service=servico) # depois disso já vem os gets
contatos_df = pd.read_excel('../dataSource/Enviar.xlsx')
print(contatos_df)

### Main:
service.start()
navegador = webdriver.Remote(service.service_url)
''' Comentado apenas para testes da segunda parte.
navegador.get('https://ri.magazineluiza.com.br')
navegador.find_element(By.XPATH, '//*[@id="Form1"]/header/div/div/div/div[1]/button').click()
time.sleep(3)
# Usar .send_keys para enviar um texto para um campo texto - 'g' é o campo de busca do Google.
navegador.find_element(By.XPATH, '//*[@id="heading-mobile-3"]/button').click()
time.sleep(3)
navegador.find_element(By.XPATH, '//*[@id="collapse-mobile-3"]/div/ul/li[2]/a').click()
time.sleep(3)
navegador.find_element(By.XPATH, '//*[@id="52UstABBxF8k7Q9IXxA3iw=="]').click()
time.sleep(5)
'''
navegador.get('https://web.whatsapp.com/')
while len(navegador.find_elements(By.ID, 'side')) < 1:
    time.sleep(1)
for i, mensagem in enumerate(contatos_df['Mensagem']):
    pessoa = contatos_df.loc[i, 'Pessoa']
    numero = contatos_df.loc[i, 'Número']
    texto = urllib.parse.quote(f'Oi {pessoa}! {mensagem}')
    link = f'https://web.whatsapp.com/send?phone={numero}&text={texto}'
    navegador.get(link)
    while len(navegador.find_elements(By.ID, 'side')) < 1:
        time.sleep(1)
    navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div').send_keys(Keys.RETURN)
    time.sleep(10)
navegador.quit()

'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = 'https://www.google.com.br/'
navegador = webdriver.Chrome()
navegador.get(url)
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dolar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
'''