'''
    O Twilio só liga para números verificados, grátis.
    Para ligar par qualquer número, precisa pagar.
    
    https://www.twilio.com/docs/voice/tutorials/how-to-make-outbound-phone-calls/python
    https://www.twilio.com/docs/voice/twiml
    
'''

from twilio.rest import Client

### Variáveis:
#lista_meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']
metaVendas = 55000
# Your Account SID and Auth Token from twilio.com/console
account_sid = "<token>"
auth_token  = "<token>"
call_from = '+17404957079'
call_to = '+5519991161909'
call_to2 = '+5519991210718'
mensagem = '''<Response>
<Say language='pt-BR'>
    Saudações!
    Aqui é o Alvaro enviando uma mensagem automatizada.
</Say>
</Response>'''

cliente = Client(account_sid, auth_token)

ligacao = cliente.calls.create(
                        to=call_to2,
                        from_=call_from,
                        twiml=mensagem
                    )

print(ligacao.sid)