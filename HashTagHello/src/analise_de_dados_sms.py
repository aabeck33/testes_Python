'''
Problema:
    Avisar via SMS quando um vendedor atingir sua cota para ganhar o
    prêmio de vendas - o primeiro vendedor que atingir R$ 55.000,00 ganha o prêmio.
Solução:
    Abrir os arquivos de vendas (xls)
    Para cada arquivo de resultado de vendas:
        Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000
        Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês e as vendas do vendedor
        Caso não seja maior do que 55.000 não quero fazer nada
'''
### Importações:
import pandas as pd
from twilio.rest import Client

### Variáveis:
#lista_meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']
metaVendas = 55000
# Your Account SID and Auth Token from twilio.com/console
account_sid = "ACede5d963ac128b718d2fe1277192292c"
auth_token  = "900faf669539ed73b311607db34a9bbd"
sms_from = '+17404957079'
sms_to = '+5519991161909'
client = Client(account_sid, auth_token)

### Main:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'../dataSource/{mes}.xlsx')
    if (tabela_vendas['Vendas'] > metaVendas).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        valorVenda = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        message = client.messages.create(
            to=sms_to,
            from_=sms_from,
            body=f'No mês {mes} existe o vendedor {vendedor} que vendeu R$ {valorVenda},00')
### Resultado:
        print(message.sid)
        print(f'No mês {mes} existe o vendedor {vendedor} que vendeu R$ {valorVenda},00')
