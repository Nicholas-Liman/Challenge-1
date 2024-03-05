import sys, subprocess

def voltar(): #Função voltar
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
        subprocess.run('cls', shell=True)
        portal()
    
    elif voltar.lower() == "logout":
        subprocess.run('cls', shell=True)
        menu()
        
    elif voltar.lower() == "sair":
        subprocess.run('cls', shell=True)
        print('Você saiu do programa')
        print()
        exit()
        
    else:
        print('Você não digitou uma das opções validas')
        voltar()

def validação(numero): #Função validar número inteiro
    while True:
        try:
            entrada = int(input(numero))
            return entrada
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

def portal(): #Função Portal
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
    select = validação('Digite o número do serviço: ')

    subprocess.run('cls', shell=True)

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
        voltar()
    else:
        print('Para selecionar as opções, digite apenas o NÚMERO respectivo à opção')
        portal()

def registro(): #Função Regsitrar
    print()
    email = input("Por favor indique seu e-mail:  ")
    email2 = input("Agora confirme seu e-mail:  ")

    email = str(email)
    email2 = str(email2)
    
    subprocess.run('cls', shell=True)

    if email2 == email:
        print('Seu e-mail foi cadastrado com sucesso!')
    
        #Registro Senha (Step-1)
        chave = input("Certo, agora digite sua senha:  ")
        chave2 = input("Certo, agora confirme sua senha:  ")
    
        chave = str(chave)
        chave2 = str(chave2)
        
        subprocess.run('cls', shell=True)

        #Usuário termina de se Registrar
        if chave2 == chave:
            print('|/////////| Sucesso, você esta cadastrado na Salesforce! |/////////|')
            print('|------------------------------------------------------------------|')
            portal()
            
        else:
            print('As senhas digitadas são diferentes!')
            registro()

    else:
        print('Os e-mails digitados são diferentes!')
        registro()
        
def menu(): #Função Menu  
    print('|/////////////////////////|  SALESFORCE  |/////////////////////////|')
    print('|/////////////|  Você já é um usuário Salesforce?  |///////////////|')

    possui_cadastro = input("Sim, Nao:   ")
    possui_cadastro = str(possui_cadastro)
    
    subprocess.run('cls', shell=True)
    
    if possui_cadastro.lower() == "sim":  #Usuário Cadastrado (Step-1)
        user = input("Seja bem vindo. Por favor indique seu e-mail:  ")
        senha = input("Certo, agora digite sua senha:  ")
        user = str(user)
        senha = str(senha)
        
        subprocess.run('cls', shell=True)
    
        portal()

    elif possui_cadastro.lower() == "nao":  #Usuário não Cadastrado (Step-1)
        print("Será necessário fazer seu cadastro, você concorda em se cadastrar?")
        intenção = input("Sim, Nao?   ")
        intenção = str(intenção)
        
        subprocess.run('cls', shell=True)
        
        if intenção.lower() == "sim":
            registro()
        
        elif intenção.lower() == "nao":
            subprocess.run('cls', shell=True)
            print('Sem problemas, quando quiser, estaremos a disposição!')
            print()
            print('Você saiu do programa')
            print()
            exit()
            
        else:
            print("Para selecionar as opções digite Sim ou Nao")
            menu()

    else: #Usuário digitou errado (Step-1)
        subprocess.run('cls', shell=True)
        print("Para selecionar as opções digite Sim ou Nao")
        menu()

menu()