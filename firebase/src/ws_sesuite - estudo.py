'''
    Executa ações no SE Suite utilizando WebServices:
        Cria Equipe
        Coloca usuário em Papel funcional
        Executa atividade de processo

    by: Alvarso Adriano Beck
    em: 07/2022
    Retorno esperado:
        <SOAP-ENV:Envelope xmlns:SOAP-ENV=http://schemas.xmlsoap.org/soap/envelope/ xmlns:xsd=http://www.w3.org/2001/XMLSchema xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance xmlns:SOAP-ENC=http://schemas.xmlsoap.org/soap/encoding/>
           <SOAP-ENV:Body>
              <addUserToRoleResponse xmlns="urn:generic">
                 <Status>SUCCESS</Status>
                 <Detail>Record added</Detail>
                 <Code>1</Code>
              </addUserToRoleResponse>
           </SOAP-ENV:Body>
        </SOAP-ENV:Envelope>
    https://realpython.com/python-requests/#authentication
'''
import requests
import pandas as pd
import os
import sys
import urllib3
import tokens

#from requests.auth import HTTPBasicAuth
#from getpass import getpass
#import logging
#from requests_toolbelt.utils import dump
#import base64
#import json
#sys.path.append(r'C:\Users\beck_\OneDrive\Documents\eclipse-workspace\HashTagHello\src')
#from passwd import sesuite_ws_user, sesuite_ws_passwd

AMBIENTE = 'QAS'

HELP = r'''
    União Química Farmacêutica Nacional
    Programa desevolvido por Alvaro Adriano Beck em 08/2022
   
    Forma de uso:
    webservice ação fonte_de_dados
    webservice fonte_de_dados ação
 
    Exemplos:
        webservice -aur -pe c:\temp\planilha.xls
        webservice -h
 
    Ambiente:
    -loc <ambiente>
        QAS
        DEV
 
    Fonte de dados:
    -pe <caminho completo + nome da planilha>
        Indicar o caminho completo e o nome da planilha Excel com os dados - xls ou xlsx.
 
    Ação:
    -h      -> Mostra esse texto de ajuda
    -m      -> Lista os códigos de módulos do SE Suite
   
	-aur	-> Para adicionar um usuário a um papel funcional
				Fonte de dados com 2 colunas:
					papel_funcional
					login
	-eap	-> Para executar uma atividade de processo
				Fonte de dados com 4 colunas:
					instancia
					atividade
					acao
					usuario
	-kna	-> Para criar uma atividade no Kanban
				Fonte de dados com 7 colunas:
					worksid
					atvtype
					priority
					title
					description
					idusrreporter
					idusrcreator
	-ceq	-> Para criar uma nova equipe
				Fonte de dados com 4 colunas:
					idequipe
					nmequipe
					modulo
						Lista do código dos módulos separados por vírgula
	pfeq	-> Para criar um novo papel funcional
				Fonte de dados com 4 colunas:
					idRole
					nmRole
					idPai
					modulo
'''

MODULOS = r'''
CD   NMISOSYSTEM
---  -------------------------
-1   Generic
0    Configuration
17   Waste Management
34   Inspection Web Manager
41   Project Web Manager
49   Forms
63   Waste Management-b
70   Archival - Manager
71   Capture - Manager
72   Protocol - Manager
73   Document - Manager
90   Audit - Manager
94   Portfolio Manager
98   Action - Manager
101  Process - Manager
104  Workflow Manager
107  Item Management - Manager
109  Asset Management
113  Waste Management-s
114  Object
115  ISOSYSTEM Calibration 5
116  SPC - Manager
126  Maintenance Manager
129  Training - Manager
132  FMEA
135  MSA - Manager
138  Performance Manager
141  APQP
144  BI Manager
146  Service Request - Manager
149  Supply - Manager
153  Administration
160  Incident - Manager
171  Competence - Manager
174  SE Action Plan
180  Storeroom - Manager
202  Problem - Manager
205  Time Control - Manager
212  Survey
213  Survey
214  Survey
215  Risk - Manager
227  Requirement - Manager
252  Waste Management-v
267  Meeting - Manager
271  Knowledge base - Manager
275  Kanban - Manager
279  Supplier - Manager
283  Customer - Manager
'''


def criar_equipe(planilha: 'caminho completo e nome da planilha de dados (.xls ou .xlsx)'):
    '''Cria equipes assocando elas a módulos.
    
    Parameters:
        planilha (string): caminho completo e nome da planilha de dados (.xls ou .xlsx)
        
    Returns:
        resultado (dictionary): item#, [id, nm, mod, result]
    '''
    resultado_final = {}
    base_url = urlbase +'/apigateway/se/ws/gn_ws.php'
    tabela = pd.read_excel(planilha)
    for i in (len(tabela)):
        data_request = f'''
            <soapenv:Envelope xmlns:soapenv=http://schemas.xmlsoap.org/soap/envelope/ xmlns:urn="urn:generic">
                <soapenv:Header/>
                <soapenv:Body>
                    <urn:newTeam>
                        <urn:IDTEAM>{tabela.loc[i, 'idequipe']}</urn:IDTEAM>
                        <urn:NMTEAM>{tabela.loc[i, 'nmequipe']}</urn:NMTEAM>
                        <urn:COMPONENT>{tabela.loc[i, 'modulo']}</urn:COMPONENT>
                    </urn:newTeam>
                </soapenv:Body>
            </soapenv:Envelope>
        '''
        data_request = data_request.encode(encoding='utf-8')
        response = requests.post(url=base_url, headers=headers, data=data_request, verify=False)
        if response.status_code == 200:
            resultado_final.update({i:[tabela.loc[i, 'idequipe'],tabela.loc[i, 'nmequipe'],tabela.loc[i, 'modulo'],'Sucesso.']})
        else:
            resultado_final.update({i:[tabela.loc[i, 'idequipe'],tabela.loc[i, 'nmequipe'],tabela.loc[i, 'modulo'],'Erro na execução: '+response.content.decode('utf-8')]})
    return(resultado_final)


def criar_pfunc(planilha):
	resultado_final = {}
	base_url = urlbase +'/apigateway/se/ws/gn_ws.php'
	tabela = pd.read_excel(planilha)
	for i in range(len(tabela)):
		data_request = f'''
			<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:generic">
				<soapenv:Header/>
				<soapenv:Body>
					<urn:newRole>
						<urn:IdRole>{tabela.loc[i, 'idRole']}</urn:IdRole>
						<urn:NmRole>{tabela.loc[i, 'nmRole']}</urn:NmRole>
						<urn:IdRoleOwner>{tabela.loc[i, 'idPai']}</urn:IdRoleOwner>
						<urn:Components>
							<urn:item>{tabela.loc[i, 'modulo']}</urn:item>
						</urn:Components>
					</urn:newRole>
				</soapenv:Body>
			</soapenv:Envelope>
		'''
		data_request = data_request.encode(encoding='utf-8')
		response = requests.post(url=base_url, headers=headers, data=data_request, verify=False)
		if response.status_code == 200:
			resultado_final.update({i:[tabela.loc[i, 'idRole'],tabela.loc[i, 'nmRole'],tabela.loc[i, 'idPai'],tabela.loc[i, 'modulo'],'Sucesso.']})
		else:
			resultado_final.update({i:[tabela.loc[i, 'idRole'],tabela.loc[i, 'nmRole'],tabela.loc[i, 'idPai'],tabela.loc[i, 'modulo'],'Erro na execução: '+response.content.decode('utf-8')]})
	return(resultado_final)


def execute_activity(planilha: 'caminho completo e nome da planilha de dados (.xls ou .xlsx)'):
    '''Executa uma atividade de uma instância de um processo.
    
    Parameters:
        planilha (string): caminho completo e nome da planilha de dados (.xls ou .xlsx)
        
    Returns:
        resultado (dictionary): item#, [instance, activity, action, user, result]
    '''
    resultado_final = {}
    base_url = urlbase +'/apigateway/se/ws/wf_ws.php'
    tabela = pd.read_excel(planilha)
    for i in (len(tabela)):
        data_request = f'''
            <soapenv:Envelope xmlns:soapenv=http://schemas.xmlsoap.org/soap/envelope/ xmlns:urn="urn:workflow">
                <soapenv:Header/>
                <soapenv:Body>
                    <urn:executeActivity>
                        <urn:WorkflowID>{tabela.loc[i, 'instancia']}</urn:WorkflowID>
                        <urn:ActivityID>{tabela.loc[i, 'atividade']}</urn:ActivityID>
                        <urn:ActionSequence>{tabela.loc[i, 'acao']}</urn:ActionSequence>
                        <urn:UserID>{tabela.loc[i, 'usuario']}</urn:UserID>
                    </urn:executeActivity>
                </soapenv:Body>
            </soapenv:Envelope>
        '''
        response = requests.post(url=base_url, headers=headers, data=data_request, verify=False)
        if response.status_code == 200:
            resultado_final.update({i:[tabela.loc[i, 'instancia'],tabela.loc[i, 'atividade'],tabela.loc[i, 'acao'],tabela.loc[i, 'usuario'],'Sucesso.']})
        else:
            resultado_final.update({i:[tabela.loc[i, 'instancia'],tabela.loc[i, 'atividade'],tabela.loc[i, 'acao'],tabela.loc[i, 'usuario'],'Erro na execução: '+response.content.decode('utf-8')]})
    return(resultado_final)


def cancel_wf(planilha):
	resultado_final = {}
	base_url = urlbase +'/apigateway/se/ws/wf_ws.php'
	tabela = pd.read_excel(planilha)
	for i in range(len(tabela)):
		data_request = f'''
			<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:workflow">
				<soapenv:Header/>
				<soapenv:Body>
					<urn:cancelWorkflow>
						<urn:WorkflowID>{tabela.loc[i, 'instancia']}</urn:WorkflowID>
						<urn:Explanation>{tabela.loc[i, 'justificativa']}</urn:Explanation>
						<urn:UserID>{tabela.loc[i, 'usuario']}</urn:UserID>
					</urn:cancelWorkflow>
				</soapenv:Body>
			</soapenv:Envelope>
		'''
		data_request = data_request.encode(encoding='utf-8')
		response = requests.post(url=base_url, headers=headers, data=data_request, verify=False)
		if response.status_code == 200:
			resultado_final.update({i:[tabela.loc[i, 'instancia'],tabela.loc[i, 'justificativa'],tabela.loc[i, 'usuario'],'Sucesso.']})
		else:
			resultado_final.update({i:[tabela.loc[i, 'instancia'],tabela.loc[i, 'justificativa'],tabela.loc[i, 'usuario'],'Erro na execução: '+response.content.decode('utf-8')]})
	return(resultado_final)


def kanban_newatv(planilha):
	resultado_final = {}
	base_url = urlbase +'/apigateway/se/ws/tsk_ws.php'
	tabela = pd.read_excel(planilha)
	for i in range(len(tabela)):
		data_request = f'''
			<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:task">
				<soapenv:Header/>
				<soapenv:Body>
					<urn:createTask>
						<urn:Workspace>{tabela.loc[i, 'worksid']}</urn:Workspace>
						<urn:TaskType>{tabela.loc[i, 'atvtype']}</urn:TaskType>
						<urn:Priority>{tabela.loc[i, 'priority']}</urn:Priority>
						<urn:Title>{tabela.loc[i, 'title']}</urn:Title>
						<urn:Sprint></urn:Sprint>
						<urn:Attribute></urn:Attribute>
						<urn:Description>{tabela.loc[i, 'description']}</urn:Description>
						<urn:IdReporter>{tabela.loc[i, 'idusrreporter']}</urn:IdReporter>
						<urn:IdCreator>{tabela.loc[i, 'idusrcreator']}</urn:IdCreator>
						<urn:IdAssignee>{tabela.loc[i, 'idassignee']}</urn:IdAssignee>
					</urn:createTask>
				</soapenv:Body>
			</soapenv:Envelope>
		'''
		#Definir os códigos de retorno de erro
		data_request = data_request.encode(encoding='utf-8')
		response = requests.post(url=base_url, headers=headers, data=data_request, verify=False)
		if response.status_code == 200:
			#resultado_final.update({i:[tabela.loc[i, 'worksid'],tabela.loc[i, 'atvtype'],tabela.loc[i, 'priority'],tabela.loc[i, 'title'],'Sucesso.']})
			resultado_final = response.text
		else:
			resultado_final.update({i:[tabela.loc[i, 'worksid'],tabela.loc[i, 'atvtype'],tabela.loc[i, 'priority'],tabela.loc[i, 'title'],'Erro na execução: '+response.content.decode('utf-8')]})
	return(resultado_final)


def kanban_assocwf(planilha):
	resultado_final = {}
	base_url = urlbase +'/apigateway/se/ws/tsk_ws.php'
	tabela = pd.read_excel(planilha)
	for i in range(len(tabela)):
		data_request = f'''
			<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:task">
				<soapenv:Header/>
				<soapenv:Body>
					<urn:insertAssociation>
						<urn:Identification>{tabela.loc[i, 'identification']}</urn:Identification>
						<urn:AssociationType>1</urn:AssociationType>
						<urn:AssociationId>{tabela.loc[i, 'associationID']}</urn:AssociationId>
					</urn:insertAssociation>
				</soapenv:Body>
			</soapenv:Envelope>
		'''
		data_request = data_request.encode(encoding='utf-8')
		response = requests.post(url=base_url, headers=headers, data=data_request, verify=False)
		if response.status_code == 200:
			resultado_final.update({i:[tabela.loc[i, 'identification'],tabela.loc[i, 'associationID'],'Sucesso.']})
		else:
			resultado_final.update({i:[tabela.loc[i, 'identification'],tabela.loc[i, 'associationID'],'Erro na execução: '+response.content.decode('utf-8')]})
	return(resultado_final)

def kanban_updattrib(planilha):
	resultado_final = {}
	base_url = urlbase +'/apigateway/se/ws/tsk_ws.php'
	tabela = pd.read_excel(planilha)
	for i in range(len(tabela)):
		data_request = f'''
			<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:urn="urn:task">
				<soapenv:Header/>
				<soapenv:Body>
					<urn:updateTaskAttrib>
						<urn:TaskId>{tabela.loc[i, 'idtask']}</urn:TaskId>
						<urn:AttributeId>{tabela.loc[i, 'idattrib']}</urn:AttributeId>
						<urn:AttributeValue>{tabela.loc[i, 'valattrib']}</urn:AttributeValue>
					</urn:updateTaskAttrib>
				</soapenv:Body>
			</soapenv:Envelope>
		'''
		data_request = data_request.encode(encoding='utf-8')
		response = requests.post(url=base_url, headers=headers, data=data_request, verify=False)
		if response.status_code == 200:
			resultado_final.update({i:[tabela.loc[i, 'idtask'],tabela.loc[i, 'idattrib'],'Sucesso.']})
		else:
			resultado_final.update({i:[tabela.loc[i, 'idtask'],tabela.loc[i, 'idattrib'],'Erro na execução: '+response.content.decode('utf-8')]})
	return(resultado_final)


def add_user_role(planilha: 'caminho completo e nome da planilha de dados (.xls ou .xlsx)'):
    '''Adiciona um usuário a um papel funcional
    
    Parameters:
        planilha (string): caminho completo e nome da planilha de dados (.xls ou .xlsx)
        
    Returns:
        resultado (dictionary): item#, [user, idrole, result]
    '''
    #usuario = 'abeck'
    #papel_funcional = 'ITSM-INCSOL_GOV'
    resultado_final = {}
    base_url = urlbase +'/apigateway/se/ws/gn_ws.php'
    tabela = pd.read_excel(planilha)
    for i in (len(tabela)):
        data_request = f'''
            <soapenv:Envelope xmlns:soapenv=http://schemas.xmlsoap.org/soap/envelope/ xmlns:urn="urn:generic">
                <soapenv:Header/>
                <soapenv:Body>
                    <urn:addUserToRole>
                        <urn:IdRole>{tabela.loc[i, 'papel_funcional']}</urn:IdRole>
                        <urn:IdUser>{tabela.loc[i, 'login']}</urn:IdUser>
                        <urn:IsDefault>2</urn:IsDefault>
                    </urn:addUserToRole>
                </soapenv:Body>
            </soapenv:Envelope>
        '''
        #session = requests.session()
        #session.auth = (username, password)
        #response = requests.get(base_url, headers=headers, data=data_request, auth=('username', getpass()))
        response = requests.post(url=base_url, headers=headers, data=data_request, verify=False)
        #response = requests.post(url=base_url, headers=headers, data=data_request, verify=False, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            if response.text.find(r'<Code>1</Code>') != -1:
                #print('Sucesso!!!')
                resultado_final.update({i:[tabela.loc[i, 'login'],tabela.loc[i, 'papel_funcional'],'Sucesso.']})
            elif response.text.find(r'<Code>49</Code>') != -1:
                #print('Papel funcional não informado')
                resultado_final.update({i:[tabela.loc[i, 'login'],tabela.loc[i, 'papel_funcional'],'Papel funcional não informado.']})
            elif response.text.find(r'<Code>48</Code>') != -1:
                #print('Papel funcional inexistente')
                resultado_final.update({i:[tabela.loc[i, 'login'],tabela.loc[i, 'papel_funcional'],'Papel funcional inexistente.']})
            elif response.text.find(r'<Code>7</Code>') != -1:
                #print('Identificador do usuário nulo')
                resultado_final.update({i:[tabela.loc[i, 'login'],tabela.loc[i, 'papel_funcional'],'Identificador do usuário nulo.']})
            elif response.text.find(r'<Code>12</Code>') != -1:
                #print('Usuário inexistente')
                resultado_final.update({i:[tabela.loc[i, 'login'],tabela.loc[i, 'papel_funcional'],'Usuário inexistente.']})
            elif response.text.find(r'<Code>30</Code>') != -1:
                #print('Valor inválido. Campo: IsDefault')
                resultado_final.update({i:[tabela.loc[i, 'login'],tabela.loc[i, 'papel_funcional'],'Valor inválido. Campo: IsDefault.']})
            else:
                #print('Erro desconhecido!')
                resultado_final.update({i:[tabela.loc[i, 'login'],tabela.loc[i, 'papel_funcional'],'Erro desconhecido!']})
            #print(f'Usuário: {tabela.loc[i, "login"]} / Papel funcional: {tabela.loc[i, "papel_funcional"]} / Resultado: {resultado}')
        else:
            #print(f'Erro na execução: {response}')
            resultado_final.update({i:[tabela.loc[i, 'login'],tabela.loc[i, 'papel_funcional'],'Erro na execução: '+response.content.decode('utf-8')]})
    return(resultado_final)

if __name__ == '__main__':
    #requests.packages.urllib3.disable_warnings()
    urllib3.disable_warnings()
    #logging.captureWarnings(True)
    resultado = None

    if AMBIENTE == 'QAS':
        urlbase = 'https://sesuiteqas.uniaoquimica.com.br'
        userToken = QAS_TOKEN
    elif AMBIENTE == 'PRD':
        urlbase = 'https://sesuite.uniaoquimica.com.br'
        userToken = PRD_TOKEN
    elif AMBIENTE == 'DEV':
        urlbase = 'https://sesuitedev.uniaoquimica.com.br'
        userToken = DEV_TOKEN
    else:
        urlbase = ''
        userToken = ''
 
    headers = {
        'Content-Type': 'text/xml;charset=ISO-8859-1'
        ,'Authorization': userToken
    #        ,'Content-Type': 'text/xml;charset=utf-8'
    }

    if len(sys.argv) == 1 or '-h' in sys.argv:
		print(HELP)
	elif '-m' in sys.argv:
		print(MODULOS)
	elif '-aur' in sys.argv and '-pe' in sys.argv and 'xls' in sys.argv[sys.argv.index('-pe') + 1]:
		planilha = sys.argv[sys.argv.index('-pe') + 1]
		if os.path.exists(planilha):
			resultado = add_user_role(planilha)
		else:
			resultado = 'Fonte de dados inválida!'
	elif '-eap' in sys.argv and '-pe' in sys.argv and 'xls' in sys.argv[sys.argv.index('-pe') + 1]:
		planilha = sys.argv[sys.argv.index('-pe') + 1]
		if os.path.exists(planilha):
			resultado = execute_activity(planilha)
		else:
			resultado = 'Fonte de dados inválida!'
	elif '-kna' in sys.argv and '-pe' in sys.argv and 'xls' in sys.argv[sys.argv.index('-pe') + 1]:
		planilha = sys.argv[sys.argv.index('-pe') + 1]
		if os.path.exists(planilha):
			resultado = kanban_newatv(planilha)
		else:
			resultado = 'Fonte de dados inválida!'
	elif '-kaw' in sys.argv and '-pe' in sys.argv and 'xls' in sys.argv[sys.argv.index('-pe') + 1]:
		planilha = sys.argv[sys.argv.index('-pe') + 1]
		if os.path.exists(planilha):
			resultado = kanban_assocwf(planilha)
		else:
			resultado = 'Fonte de dados inválida!'
	elif '-kua' in sys.argv and '-pe' in sys.argv and 'xls' in sys.argv[sys.argv.index('-pe') + 1]:
		planilha = sys.argv[sys.argv.index('-pe') + 1]
		if os.path.exists(planilha):
			resultado = kanban_updattrib(planilha)
		else:
			resultado = 'Fonte de dados inválida!'
	elif '-ceq' in sys.argv and '-pe' in sys.argv and 'xls' in sys.argv[sys.argv.index('-pe') + 1]:
		planilha = sys.argv[sys.argv.index('-pe') + 1]
		if os.path.exists(planilha):
			resultado = criar_equipe(planilha)
		else:
			resultado = 'Fonte de dados inválida!'
	elif '-cwf' in sys.argv and '-pe' in sys.argv and 'xls' in sys.argv[sys.argv.index('-pe') + 1]:
		planilha = sys.argv[sys.argv.index('-pe') + 1]
		if os.path.exists(planilha):
			resultado = cancel_wf(planilha)
		else:
			resultado = 'Fonte de dados inválida!'
	elif '-cpf' in sys.argv and '-pe' in sys.argv and 'xls' in sys.argv[sys.argv.index('-pe') + 1]:
		planilha = sys.argv[sys.argv.index('-pe') + 1]
		if os.path.exists(planilha):
			resultado = criar_pfunc(planilha)
		else:
			resultado = 'Fonte de dados inválida!'
	else:
		print(HELP)
	print(resultado)

    #print(resultado.status_code)
    #print(response.text)
    #print(response.request.headers)
    #print(resultado.headers)
    #print(response.json)
    #print(response)
    #print(sys.argv)
    '''
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))
    '''
    #data = dump.dump_all(resultado)
    #print(data.decode('utf-8'))
    #raw_request = get_raw_request(resultado)
    #print(raw_request)
    '''
    base64_sesuite_ws_passwd = sesuite_ws_passwd
    base64_bytes = base64_sesuite_ws_passwd.encode('ascii')
    sesuite_ws_passwd_bytes = base64.b64decode(base64_bytes)
    password = sesuite_ws_passwd_bytes.decode('ascii')

    base64_sesuite_ws_user = sesuite_ws_user
    base64_bytes = base64_sesuite_ws_user.encode('ascii')
    sesuite_ws_user_bytes = base64.b64decode(base64_bytes)
    username = sesuite_ws_user_bytes.decode('ascii')
    '''
    '''
	resultado = execute_activity(r'c:\temp\exec_atv.xlsx')
	print(resultado.text)
	#tree = ET.parse(resultado.text)
	tree = ET.ElementTree(ET.fromstring(resultado.text))
	root = tree.getroot()
	for row in root.iter('{urn:workflow}Detail'):
		print(row.tag, row.attrib)
	'''
# pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org <biblioteca>