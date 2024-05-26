'''
    awesomeapi: https://docs.awesomeapi.com.br/
'''

### Importações
import requests


#requisicao = requests.get('https://testeaabeck-default-rtdb.firebaseio.com/.json')

informacao = '{"Nome": "Candioto"}'
#requisicao = requests.post('https://testeaabeck-default-rtdb.firebaseio.com/.json', data=informacao)

informacao = '{"Nome": "Daniel", "Sobrenome": "Candioto", "Idade": "60"}'
requisicao = requests.patch('https://testeaabeck-default-rtdb.firebaseio.com//-N7kZrGjLq7N94GuJsGY.json', data=informacao)

#requisicao = requests.delete('https://testeaabeck-default-rtdb.firebaseio.com//-N7kZrGjLq7N94GuJsGY.json')


print(requisicao)
print(requisicao.json())