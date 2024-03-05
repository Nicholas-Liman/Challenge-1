import sys
import subprocess
import json

#Funções Globais

def limpar_tela(): #Funçao limpar tela universal
    subprocess.run(['cls' if sys.platform == 'win32' else 'clear'], shell=True)

def voltar(dados_usuario): #Função voltar
    print()
    print('Caso deseje voltar a seleção do portal, digite "Voltar"')
    print()
    print('Caso deseje deslogar e voltar ao início, digite "Logout"')
    print()
    print('Caso deseje sair, digite sair "Sair"')
    print()
    voltar = input('O que deseja fazer?  ')
    voltar = str(voltar)
        
    if voltar.lower() == "voltar":
        limpar_tela()
        portal(dados_usuario)
    
    elif voltar.lower() == "logout":
        limpar_tela()
        checar_cadastro(dados_usuario)
        
    elif voltar.lower() == "sair":
        limpar_tela()
        print()
        print('Você saiu do programa')
        
        exit()
        
    else:
        print()
        print('Você não digitou uma das opções validas')
        voltar(dados_usuario)

def validar_numero(mensagem): #Confirma que so existam numeros em inputs numerais
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada

        except ValueError:
            limpar_tela()
            print('')
            print("Por favor, insira apenas números.")

#Funções de Arquivo

def salvar_dados_arquivo(nome_arquivo, dados): #Salva os dados em Json
    try:
        with open(nome_arquivo, 'r') as arquivo_existente:
            dados_existente = json.load(arquivo_existente)
    except FileNotFoundError:
        dados_existente = {}

    email = dados.get('E-mail', None)

    if email is not None:
        if email in dados_existente:
            print(f'O e-mail {email} já possui um cadastro.')
        else:
            dados_existente[email] = dados
            with open(nome_arquivo, 'w') as arquivo:
                json.dump(dados_existente, arquivo, indent=2)
                print(f'Cadastro do e-mail {email} salvo com sucesso.')

def ler_dados(nome_arquivo): #Lê o json
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            return dados
    except FileNotFoundError:
        return {}

def guardar_dados(nome_funcao, retorno, dados_usuario): #Manipula os dados para salvar em json
    dados_usuario[nome_funcao] = retorno

#Funções de Cadastro

def checar_cadastro(dados_usuario):
    print('')
    print('|/////////////////////////|  SALESFORCE  |/////////////////////////|')
    print('|/////////////|  Você já é um usuário Salesforce?  |///////////////|')
    print('')
    
    possui_cadastro = input("Sim, Não:   ")

    if possui_cadastro.lower() == "sim":
        limpar_tela()
        print('')
        email = input("Seja bem-vindo. Por favor, indique seu e-mail:  ")
        print('')
        senha = input("Certo, agora digite sua senha:  ")

        # Load existing user data from the file
        dados_armazenados = ler_dados('cadastro_usuario.json')

        if dados_armazenados and email in dados_armazenados:
            if senha == dados_armazenados[email]['Senha']:
                limpar_tela()
                print('')
                print('Login bem-sucedido!')
                return dados_armazenados[email]
            else:
                limpar_tela()
                print('')
                print('E-mail ou senha incorretos. Tente novamente.')
                return checar_cadastro(dados_usuario)
        else:
            limpar_tela()
            print('')
            print('Não há dados de cadastro encontrados para o e-mail informado. Realize o cadastro primeiro.')
            return checar_cadastro(dados_usuario)

    elif possui_cadastro.lower() == "nao":
        limpar_tela()
        return {}

    else:
        limpar_tela()
        print('')
        print("Para selecionar as opções, digite Sim ou Não")
        return checar_cadastro(dados_usuario)

def intencao_cadastro(dados_usuario): #Verifica se o usuario quer se cadastrar
    limpar_tela()

    print('')
    print("Será necessário fazer seu cadastro. Você concorda em se cadastrar?")
    intencao = input("Sim, Não?   ")
    intencao = str(intencao)

    limpar_tela()

    if intencao.lower() == "sim":
        limpar_tela()
        reg_email(dados_usuario)

    elif intencao.lower() == "nao":
        limpar_tela()

        print('')
        print('Sem problemas, quando quiser, estaremos à disposição!')
        print()
        print('Você saiu do programa')
        print()
        exit()

    else:
        limpar_tela()

        print('')
        print("Para selecionar as opções, digite Sim ou Não")
        intencao_cadastro()

def reg_email(dados_usuario): #Recebe e verifica email
    
    print('')
    email = input("Por favor, indique seu e-mail:  ")

    if "@" in email and ".com" in email:
    
            limpar_tela()
            
            print('')
            email2 = input("Agora confirme seu e-mail:  ")
            
            limpar_tela()
        
            if email == email2:
                print('')
                print('Seu e-mail foi cadastrado com sucesso')
                guardar_dados('E-mail', email, dados_usuario)
                reg_senha(dados_usuario)
            else:
                print('')
                print('Os e-mails digitados são diferentes')
                reg_email(dados_usuario)
    else:
        limpar_tela()

        print('O E-mail digitado é inválido certifique-se que ele está correto')
        reg_email(dados_usuario)

def reg_senha(dados_usuario): #Recebe e verifica senha
    
    print('')
    senha = input("Por favor crie uma senha:  ")
    
    limpar_tela()
    
    print('')
    senha2 = input("Agora confirme sua senha:  ")
    
    limpar_tela()
    
    if senha == senha2:
        print('')
        print('Sua senha foi registrada com sucesso')
        guardar_dados('Senha', senha, dados_usuario)
        salvar_dados_arquivo('cadastro_usuario.json', dados_usuario)
        logar(dados_usuario)
    else:
        limpar_tela()
        
        print('')
        print('As senhas digitadas são diferentes')
        reg_senha(dados_usuario)
  
def logar(dados_usuario):
    print('')
    print('Gostaria de fazer o login?')
    login = input("Sim, Nao? ")
    if login.lower() == "sim":
        limpar_tela()
        manuseio_login(dados_usuario)
    elif login.lower() == "nao":
        limpar_tela()
        print('')
        print('Sem problemas, quando quiser, estaremos a disposição!')
        print()
        print('Você saiu do programa')
        print()
        exit()
    else:
        limpar_tela()
        print('')
        print("Para selecionar as opções digite Sim ou Nao")
        logar(dados_usuario)
                
#Fim do Cadastro

#Funções de menu

def portal(dados_usuario): #Função Portal
    print('|//////////////////////////////////////////////////////////////////|')
    print('|------------------------| SALESFORCE |----------------------------|')
    print('|//////////////////////////////////////////////////////////////////|')
    print('|////////////////| Bem vindo ao portal SALESFORCE |////////////////|')
    print('|//////////////////////////////////////////////////////////////////|')
    print('|///////////////| Qual serviço você deseja acessar?|///////////////|')
    print('|//////////////////////////////////////////////////////////////////|')
    print('|__________________________________________________________________|')
    print('|////| Para selecionar digite o número respectivo ao serviço  |////|')
    print('|__________________________________________________________________|')
    print('|(1)| - CUSTOMER 360                         |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(2)| - VENDAS                               |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(3)| - Atendimento ao Cliente               |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(4)| - Marketing                            |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(5)| - Commerce                             |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(6)| - Data Cloud                           |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(7)| - Tableau                              |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(8)| - Mulesoft                             |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(9)| - Slack                                |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(10)| - Sustentabilidade                    |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(11)| - Pequenas Empresas                   |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(12)| - Especialistas & Apps de parceiros   |/////////////////////|')
    print('|------------------------------------------------------------------|')
    print('|(13)| - Serviços e Planos                   |/////////////////////|')
    print('|__________________________________________________________________|')

    #Input da Escolha (Step-2)
    #select = input('Digite o número do serviço:  ')
    #select = int(select)
    select = validar_numero('Digite o número do serviço: ')

    limpar_tela()

    #Filtro da Escolha (Step-2)
    if 1 <= select <= 13:
        opcoes = [
            "O Customer 360 é a nossa suíte de produtos e serviços que ajuda 98% dos clientes a alcançar ou superar suas metas de ROI.",
            "Eficiência máxima com automação, dados e inteligência melhores. Como? Com automação da força de vendas impulsionada por IA.",
            "Maximize o ROI e impulsione a eficiência, desde a central de contatos ao atendimento externo, tudo em uma única plataforma.",
            "Atraia clientes. Gere mais engajamento. Construa relações duradouras. Tudo isso graças ao marketing digital baseado em dados.",
            "Obtenha valor rapidamente — da descoberta à entrega — na plataforma que já conquistou a confianças das maiores marcas do mercado.",
            "Traga o poder dos dados em tempo real para o Customer 360. Economize tempo e dinheiro enquanto aumenta sua receita com o Data Cloud.",
            "Descubra as conexões entre dados, insights e melhores resultados de negócios com a análise completa.",
            "Com a MuleSoft, integre dados de qualquer sistema e automatize tarefas complexas para fornecer experiências do cliente conectadas mais rapidamente.",
            "Descubra um jeito flexível de conectar pessoas, parceiros de negócios e aplicativos. Integrado ao Salesforce Customer 360, o Slack impulsiona a produtividade e faz funcionar o trabalho colaborativo.",
            "Alcance a emissão zero de carbono de maneira rápida com o Net Zero.",
            "Com o Sales Cloud para Pequenas Empresas, você pode gerir sua operação de forma inteligente e flexível. Inove, conquiste mais leads, aumente as vendas e melhore a experiência dos clientes conforme sua empresa cresce.",
            "https://appexchange.salesforce.com/appxStore?type=App",
            "https://www.salesforce.com/br/services/overview/"
        ]
        print(opcoes[select - 1])
        voltar(dados_usuario)
    else:
        print('Para selecionar as opções, digite apenas o NÚMERO respectivo à opção')
        portal(dados_usuario)

def manuseio_login(dados_usuario):
    dados_usuario = checar_cadastro(dados_usuario)
    if 'E-mail' not in dados_usuario:
        intencao_cadastro(dados_usuario)
    portal(dados_usuario)

manuseio_login({})
