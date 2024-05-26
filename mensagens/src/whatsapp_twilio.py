'''
    O Twilio só liga para números verificados, grátis.
    Para ligar para qualquer número, precisa pagar.
    
    https://www.twilio.com/docs/voice/tutorials/how-to-make-outbound-phone-calls/python
    https://www.twilio.com/docs/voice/twiml
    
'''

from twilio.rest import Client

account_sid = '<token>'
auth_token = '<token>'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+14155238886',
  body='Alvaro, a aprovação a seguir requer sua atenção premente: https://sesuite.uniaoquimica.com.br/se/v26175/workflow/api/execute_activity.php?activityoid=507436w1',
  to='whatsapp:+5519991161909'
)

print(message.sid)