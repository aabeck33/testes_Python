'''
Problema:
    Enviar e-mail com informações de faturamento de cada loja de uma rede
Solução:
    Abrir a base de dados
    Analisar a base de dados com as informações (Código da venda, Data da venda, ID loja,
    ID produto, Quantidade, Valor unitário, Valor total)
    Tratamento dos dados
    Gerar os dados a serem enviados (Faturamento por loja / Quantidade de produtos vendidos /
    Ticket médio por loja)
    Enviar e-mail com as informações
'''
### Importações:
import pandas as pd
# Para enviar e-mail pelo Outlook:
import win32com.client as win32
# Para enviar e-mail pelo Google:
import smtplib
import email.message
from passwd import passwd

### Definições:
pd.set_option('display.max_columns', None)
def enviar_email(): 
    corpo_email = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{fatLoja.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{qtprodLoja.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{tktMedio.to_html(formatters={'Tkt Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>aaBeck.'.</p>
'''
    msg = email.message.Message()
    msg['Subject'] = 'Teste de Relatório de Vendas'
    msg['From'] = 'alvaroabeck@gmail.com'
    msg['To'] = 'alvaroabeck@gmail.com'
    password = passwd
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')

### Variáveis:
tabela_vendas = pd.read_excel('../dataSource/Vendas.xlsx')

### Main:
# Cálculo do faturamento por loja
fatLoja = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()

# Cálculo da quantidade de produtos vendudos por loja
qtprodLoja = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()

# Cálculo da quantidade de produtos vendudos por loja
tktMedio = (fatLoja['Valor Final'] / qtprodLoja['Quantidade']).to_frame()
tktMedio = tktMedio.rename(columns={0: 'Tkt Médio'})

# enviar um email com o relatório pelo Outlook
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'alvaroabeck@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>Segue o Relatório de Vendas por cada Loja.</p>

<p>Faturamento:</p>
{fatLoja.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<p>Quantidade Vendida:</p>
{qtprodLoja.to_html()}

<p>Ticket Médio dos Produtos em cada Loja:</p>
{tktMedio.to_html(formatters={'Tkt Médio': 'R${:,.2f}'.format})}

<p>Qualquer dúvida estou à disposição.</p>

<p>Att.,</p>
<p>Lira</p>
'''

### Resultados:
#print(fatLoja)
#print('- ' * 50)
#print(qtprodLoja)
#print('- ' * 50)
#print(tktMedio)
#mail.Send()
#print('Email Enviado')
enviar_email()