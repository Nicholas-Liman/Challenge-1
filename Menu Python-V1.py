import sys
import subprocess
import json
import re

#Funções Globais
def limpar_tela(): #Funçao limpar tela universal
    subprocess.run(['cls' if sys.platform == 'win32' else 'clear'], shell=True)

def voltar(dados_usuario): #Função voltar
    print('\n|------------------------------------------------------|')
    print('|                                                      |')
    print('| Caso deseje ir ao PORTAL.                 Digite [1] |')
    print('|                                                      |')
    print('| Caso deseje fazer o LOGOUT.               Digite [2] |')
    print('|                                                      |')
    print('| Caso deseje Sair.                         Digite [3] |')
    print('|                                                      |')
    print('|------------------------------------------------------|')
    voltar = validar_numero('\nO que deseja fazer: ')
        
    if voltar == 1:
        limpar_tela()
        portal(dados_usuario)
    
    elif voltar == 2:
        limpar_tela()
        checar_cadastro(dados_usuario)
        
    elif voltar == 3:
        sair()
        
    else:
        limpar_tela()
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|     | Você não digitou uma das opções válidas |      |')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        voltar(dados_usuario)

def sair(): #Função para fechar o programa
    print('\n|------------------------------------------------------|')
    print('|                                                      |')
    print('| Sem problemas, quando quiser estaremos a disposição  |')
    print('|                                                      |')
    print('|                 Fechando o programa                  |')
    print('|                                                      |')
    print('|------------------------------------------------------|')
    exit()

def deletar_registro(nome_arquivo, email): #Função que apagar o registro do user
    try:
        with open(nome_arquivo, 'r') as arquivo_existente:
            dados_existente = json.load(arquivo_existente)
    except FileNotFoundError:
        dados_existente = {}

    if email in dados_existente:
        del dados_existente[email]
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados_existente, arquivo, indent=2)
            print('\n|------------------------------------------------------|')
            print('|                                                      |')
            print(f'|    |O registro do e-mail {email} foi deletado.|    ')
            print('|                                                      |')
            print('|------------------------------------------------------|')
    else:
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print(f'|    |O e-mail {email} não foi encontrado no registro.|')
        print('|                                                      |')
        print('|------------------------------------------------------|')

def deletar_conta(dados_usuario): #Status de apagar registro
    if 'E-mail' in dados_usuario:
        email = dados_usuario['E-mail']
        deletar_registro('cadastro_usuario.json', email)
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|      |Sua conta foi deletada com sucesso.|            ')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        sair()
    else:
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|  |Você precisa estar logado para deletar a conta.|   |')
        print('|                                                      |')
        print('|------------------------------------------------------|')

def validar_numero(mensagem): #Confirma que so existam numeros em inputs numerais
    while True:
        try:
            entrada = int(input(mensagem))
            return entrada

        except ValueError:
            print('\n|------------------------------------------------------|')
            print('|                                                      |')
            print('|     | Você não digitou uma das opções válidas |      |')
            print('|                                                      |')
            print('|------------------------------------------------------|')

def validar_email(email): #Valida se o e-mail é valido
    # Expressão regular para validar o formato do e-mail
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(regex, email):
        return True
    else:
        return False

def validar_senha(senha): #valida se a senha segue as regras
    # Expressão regular para validar a senha
    regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    if re.match(regex, senha):
        return True
    else:
        return False

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
            print('\n|------------------------------------------------------|')
            print('|                                                      |')
            print(f'|      |O e-mail {email} já possui um cadastro.|      ')
            print('|                                                      |')
            print('|------------------------------------------------------|')
        else:
            dados_existente[email] = dados
            with open(nome_arquivo, 'w') as arquivo:
                json.dump(dados_existente, arquivo, indent=2)
                print('\n|------------------------------------------------------|')
                print('|                                                      |')
                print(f'|    |O e-mail {email} foi cadastrado com sucesso.|    ')
                print('|                                                      |')
                print('|------------------------------------------------------|')

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
def checar_cadastro(dados_usuario): #Verifica se o usuário é cadastrado
    print('\n|------------------------------------------------------|')
    print('|                  |  SALESFORCE  |                    |')
    print('|                                                      |')
    print('|        |  Você já é um usuário Salesforce?  |        |')
    print('|                                                      |')
    print('| Caso já seja cadastrado.                  Digite [1] |')
    print('|                                                      |')
    print('| Caso não seja.                            Digite [2] |')
    print('|                                                      |')
    print('|------------------------------------------------------|')
    
    possui_cadastro = validar_numero('\nÉ cadastrado? ')

    if possui_cadastro == 1:
        limpar_tela()
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|   | Seja bem-vindo. Por favor, indique seu e-mail |  |')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        email = input('\nE-mail:  ')
        email = str(email)
        
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|   | Seja bem-vindo. Por favor, indique sua senha |   |')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        senha = input('\nSenha:  ')
        senha = str(senha)

        dados_armazenados = ler_dados('cadastro_usuario.json')

        if dados_armazenados and email in dados_armazenados:
            if senha == dados_armazenados[email]['Senha']:
                limpar_tela()
                print('\n|-------------------------------------------------------|')
                print('|                                                       |')
                print('|             | Login efetuado com sucesso |            |')
                print('|                                                       |')
                print('|-------------------------------------------------------|')
                return dados_armazenados[email]
            else:
                limpar_tela()
                print('\n|------------------------------------------------------|')
                print('|                                                      |')
                print('|   | E-mail ou senha incorretos. Tente novamente. |   |')
                print('|                                                      |')
                print('|------------------------------------------------------|')
                return checar_cadastro(dados_usuario)
        else:
            limpar_tela()
            print('\n|------------------------------------------------------|')
            print('|                                                      |')
            print(f'|   | Não há cadastro com o e-mail {email}. |   ')
            print('|                                                      |')
            print('|------------------------------------------------------|')
            return checar_cadastro(dados_usuario)

    elif possui_cadastro == 2:
        limpar_tela()
        return {}

    else:
        limpar_tela()
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|     | Você não digitou uma das opções válidas |      |')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        return checar_cadastro(dados_usuario)

def intencao_cadastro(dados_usuario): #Verifica se o usuario quer se cadastrar
    limpar_tela()
    print('\n|------------------------------------------------------|')
    print('|                                                      |')
    print('|            |  Gostaria de se cadastrar?  |           |')
    print('|                                                      |')
    print('| Caso SIM.                                 Digite [1] |')
    print('|                                                      |')
    print('| Caso NÃO.                                 Digite [2] |')
    print('|                                                      |')
    print('|------------------------------------------------------|')
    
    intencao = validar_numero('\nCadastrar? ')

    limpar_tela()

    if intencao == 1:
        limpar_tela()
        reg_email(dados_usuario)

    elif intencao == 2:
       sair()

    else:
        limpar_tela()
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|     | Você não digitou uma das opções válidas |      |')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        intencao_cadastro()

def reg_email(dados_usuario): #Recebe e verifica email
    print('\n|------------------------------------------------------|')
    print('|                                                      |')
    print('|     |Digite o e-mail que gostaria de registrar|      |')
    print('|                                                      |')
    print('|------------------------------------------------------|')
    email = input('\nPor favor, indique seu e-mail: ')

    if validar_email(email):
            limpar_tela()
            print('\n|------------------------------------------------------|')
            print('|                                                      |')
            print('|         |Agora é só repetir o mesmo e-mail|          |')
            print('|                                                      |')
            print('|------------------------------------------------------|')
            email2 = input('\nConfirme seu e-mail:  ')
            
        
            if email == email2:
                limpar_tela()
                print('\n|------------------------------------------------------|')
                print('|                                                      |')
                print('|       |Maravilha, seu e-mail foi registrado|         |')
                print('|                                                      |')
                print('|------------------------------------------------------|')
                guardar_dados('E-mail', email, dados_usuario)
                reg_senha(dados_usuario)
            else:
                limpar_tela()
                print('\n|------------------------------------------------------|')
                print('|                                                      |')
                print('|     |Ops, parece que os e-mais eram diferentes|      |')
                print('|                                                      |')
                print('|------------------------------------------------------|')
                reg_email(dados_usuario)
    else:
        limpar_tela()
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|     |Eita, o e-mail que você digitou é inválido|     |')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        reg_email(dados_usuario)

def reg_senha(dados_usuario): #Recebe e verifica senha
    print('|------------------------------------------------------|')
    print('|                                                      |')
    print('|         |Agora só falta escolher uma senha|          |')
    print('|                                                      |')
    print('|  |Tenha em mente que a senha precisa ter pelo menos| |')
    print('|                                                      |')
    print('|  |* Uma letra maiúscula. |                           |')
    print('|  |* Uma letra minúscula. |                           |')
    print('|  |* Um carácter especial.|                           |')
    print('|  |* Um número.           |                           |')
    print('|                                                      |')
    print('|------------------------------------------------------|')
    senha = input('\nSenha: ')
    senha = str(senha)
    
    limpar_tela()
    print('\n|------------------------------------------------------|')
    print('|                                                      |')
    print('|         |Agora é só repetir a mesma senha|           |')
    print('|                                                      |')
    print('|------------------------------------------------------|')
    senha2 = input('\nRepita sua senha: ')
    senha2 = str(senha2)
    
    if validar_senha(senha):
        if senha == senha2:
            limpar_tela()
            print('\n|------------------------------------------------------|')
            print('|                                                      |')
            print('|       |Perfeito senha registrada com sucesso|        |')
            print('|                                                      |')
            print('|------------------------------------------------------|')
            guardar_dados('Senha', senha, dados_usuario)
            salvar_dados_arquivo('cadastro_usuario.json', dados_usuario)
            logar(dados_usuario)
        else:
            limpar_tela()
            print('\n|------------------------------------------------------|')
            print('|                                                      |')
            print('|          |Ops, as senhas eram diferentes|            |')
            print('|                                                      |')
            print('|------------------------------------------------------|')
            reg_senha(dados_usuario)
    else:
        limpar_tela()
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|    |A senha não atende aos critérios mínimos.|       |')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        reg_senha(dados_usuario)

def logar(dados_usuario): #Valida se o user quer logar após se registrar
    limpar_tela()
    print('\n|------------------------------------------------------|')
    print('|                                                      |')
    print('| Caso deseje fazer LOGIN.                  Digite [1] |')
    print('|                                                      |')
    print('| Caso deseje SAIR.                         Digite [2] |')
    print('|                                                      |')
    print('|------------------------------------------------------|')
    login = validar_numero('\nO que deseja fazer: ')
    limpar_tela()
    
    if login == 1:
        manuseio_login(dados_usuario)
        
    elif login == 2:
        sair()
    else:
        limpar_tela()
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|     | Você não digitou uma das opções válidas |      |')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        logar(dados_usuario)              
#Fim do Cadastro

#Funções de menu
def portal(dados_usuario): #Função Portal
    print('\n|-------------------------------------------------------|')
    print('|                                                       |')
    print('|                     | SALESFORCE |                    |')
    print('|                                                       |')
    print('|           |Bem vindo ao portal de serviços|           |')
    print('|                                                       |')
    print('|              |Qual você deseja acessar?|              |')
    print('|                                                       |')
    print('| Para selecionar digite o número respectivo ao serviço |')
    print('|_______________________________________________________|')
    print('|(1)| - CUSTOMER 360                         |//////////|')
    print('|                                                       |')
    print('|(2)| - VENDAS                               |//////////|')
    print('|                                                       |')
    print('|(3)| - Atendimento ao Cliente               |//////////|')
    print('|                                                       |')
    print('|(4)| - Marketing                            |//////////|')
    print('|                                                       |')
    print('|(5)| - Commerce                             |//////////|')
    print('|                                                       |')
    print('|(6)| - Data Cloud                           |//////////|')
    print('|                                                       |')
    print('|(7)| - Tableau                              |//////////|')
    print('|                                                       |')
    print('|(8)| - Mulesoft                             |//////////|')
    print('|                                                       |')
    print('|(9)| - Slack                                |//////////|')
    print('|                                                       |')
    print('|(10)| - Sustentabilidade                    |//////////|')
    print('|                                                       |')
    print('|(11)| - Pequenas Empresas                   |//////////|')
    print('|                                                       |')
    print('|(12)| - Especialistas & Apps de parceiros   |//////////|')
    print('|                                                       |')
    print('|(13)| - Serviços e Planos                   |//////////|')
    print('|                                                       |')
    print('|(14)| - Excluir conta                       |//////////|')
    print('|-------------------------------------------------------|')
    

    #Input da Escolha (Step-2)
    #select = input('Digite o número do serviço:  ')
    #select = int(select)
    select = validar_numero('\nServiço desejado: ')

    limpar_tela()

    #Filtro da Escolha (Step-2)
    if 1 <= select <= 14:
        if select == 14:
            deletar_conta(dados_usuario)
            
        else:
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
        limpar_tela()
        print('\n|------------------------------------------------------|')
        print('|                                                      |')
        print('|     | Você não digitou uma das opções válidas |      |')
        print('|                                                      |')
        print('|------------------------------------------------------|')
        portal(dados_usuario)

def manuseio_login(dados_usuario): #Função Main
    dados_usuario = checar_cadastro(dados_usuario)
    if 'E-mail' not in dados_usuario:
        intencao_cadastro(dados_usuario)
    portal(dados_usuario)

manuseio_login({})
