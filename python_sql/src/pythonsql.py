### Importações:
import pyodbc

# Conexão:
dados_conexao = (
#    "Driver={SQL Server};"
    "Driver={PostgreSQL Unicode};"
    "Server=localhost;"
    "Port=5432;"
    "Database=testeaabeck;"
    "CHARSET=UTF8;"
    "UID=postgres;"
    "PWD=aaBeck;"
)

conexao = pyodbc.connect(dados_conexao)
print('Conexão Bem Sucedida')

cursor = conexao.cursor()

id = 2
cliente = 'Lira Python'
produto = 'Carro'
data = '25/08/2021'
preco = 5000
quantidade = 1

comando = f"""
INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    ({id}, '{cliente}', '{produto}', '{data}', {preco}, {quantidade})
"""

cursor.execute(comando)
cursor.commit()

print('Comando executado com sucess!')