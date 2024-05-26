'''

'''
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

corpo_email = '''
Prezados,

Quando tiverem uma resposta da proposta, favor entrar em contato.

Abs,
Lira
(21)99999-9999
(11) 99878-3298
(19) 3276-7013
'''


telnum = '+5519991161909'
telnum_ajustado = phonenumbers.parse(telnum, None)
print (telnum_ajustado)

local = geocoder.description_for_number(telnum_ajustado, 'pt-br')
print(local)

tel_formulario = '19991210718'
tel_formulario_ajustado = phonenumbers.parse(tel_formulario, 'BR')
print(tel_formulario_ajustado)

tel_formulario_formatado = phonenumbers.format_number(tel_formulario_ajustado, phonenumbers.PhoneNumberFormat.NATIONAL)
print(tel_formulario_formatado)

operadora = carrier.name_for_number(telnum_ajustado, 'pt-br')
print(operadora)

for telefone in phonenumbers.PhoneNumberMatcher(corpo_email, 'BR'):
    print(telefone)