import pyfiglet as pfig

# Dicionários

adm ={
    "adm":"12345",
    "adm2": "senhaAdm2"
}

usuarios = {
    "" : "",
    "user1" : "123",
    "user2": "12345"
}

nfts = {
    #nome da equipe : [pos_antiga, valor]
    'equipe1': [1, 20],
    'equipe2': [2, 10],
    'equipe3': [3, 210],
    'equipe4': [4, 30],
    'equipe5': [5, 40],
    'equipe6': [6, 50],
    'equipe7': [7, 80],
    'equipe8': [8, 10],
    'equipe9': [11, 5],
    'equipe10': [9, 40],
    'equipe11': [10, 20]
}

carrinho = {
    'nft' : {},
    'valor_total' : 0,
}

carteira_usuario = {
    "nft": {}
}

# Funções

def calculo_ntf(equipe):
    percentuais = [0.15, 0.12, 0.09, 0.06, 0.03, 0.0, -0.03, -0.06, -0.09, -0.12, -0.15]
    index = nfts[equipe][0] - 1
    preco = nfts[equipe][1] + (nfts[equipe][1] * percentuais[index])
    return preco


def forca_escolha(lista, msg, msg_erro='Inválido'):
    print("Opções disponíveis:", ", ".join(lista))
    while True:
        escolha = input(msg)
        if escolha in lista:
            return escolha
        else:
            print("---------------------")
            print(msg_erro)


def sair_continuar(msg, lista):
    sair = forca_escolha(lista, msg)
    if sair == "sair":
        return False
    else:
        return True


# verifica a posicao que o usuario colocou em cada equipe para nao se repitir e ficar entre 1 e 11
def posicao(piloto, i, posicoes_usadas):
    while True:
        position = input(f"Digite a posição do piloto {piloto[i]} \n --> ")
        if position.isnumeric():
            position = int(position)
            if 1 <= position <= 11:
                if position not in posicoes_usadas:
                    posicoes_usadas.append(position)
                    return position
                else:
                    print("Esta posição já foi usada. Por favor, digite uma posição diferente.")
            else:
                print("Digite um valor entre 1 e 11.")
        else:
            print("Entrada inválida. Digite um número.")


# Verificação do User
def login(msg, msg_pwd, dic):
    while True:
        user_login = input(msg + "\n -->")
        user_Pwd = input(msg_pwd + "\n -->")
        if user_login in dic.keys():
            if user_Pwd == dic[user_login]:
                print('Suceeso')
                break
            else:
                print('Senha inválida')
                continue
        else:
            print('Usuário inválido')
    return True


# printa o dicionario
def print_dic(dic, index_value, valor=False):
    if valor:
        for key in dic.keys():
            print(f"{key} = Valor:R${dic[key][1]:.2f} ")
    else:
        for key in dic.keys():
            print(f"{key} = {dic[key][index_value]}")


# forca o usuario a digitar um numero
def numeric(msg, msg_erro="invalido!!"):
    while True:
        numero = input(msg)
        if numero == "":
            print(msg_erro)
            continue
        if numero.isnumeric():
            return int(numero)
        else:
            print(msg_erro)


# limpa o carrinho de compras
def limpar_carrinho():
    carrinho['nft'].clear()
    carrinho['valor_total'] = 0


# realiza o cadastro
def cadastro():
    newUser = input("Digite o nome de usuario que deseja cadastrar: \n -->")
    newPwd = input(f"Digite a senha de login do usuario {newUser}\n --> ")
    usuarios[newUser] = newPwd
    print("Voce voltara ao inicio, digite 1 para realizar o login \n Obrigado por se cadastrar no TechAdvanced!")


# adiciona as nfts que o usuario quis ao carrinho
def adicionar_carrinho():
    while True:
        comprar = forca_escolha(["sim", "nao"], "Deseja comprar alguma nft? \n -->")
        if comprar == "nao":
            break
        print_dic(nfts, 1, True)
        nft_Buy = forca_escolha(nfts.keys(), "De qual equipe voce deseja comprar a nft? \n -->")
        qtd = numeric("Digite a quandidade que deseja comprar \n --> ")

        if qtd <= 0:
            print('A quantidade deve ser maior que 0')
            continue

        carrinho['nft'][nft_Buy] = qtd
        carrinho['valor_total'] += carrinho['nft'][nft_Buy] * nfts[nft_Buy][1]
        print(f"valor: {carrinho['nft'][nft_Buy] * nfts[nft_Buy][1]:.2f}")

        if sair_continuar("Digite [sair] para sair e [continuar] para continuar comprando \n -->",
                          ["sair", "continuar"]):
            continue
        else:
            return


# o usuario compra as nft e vai para sua carteira
def comprar_carrinho():
    print("Você esta comprando: ")
    for key in carrinho['nft'].keys():
        print(f"{key} = R${carrinho['nft'][key] * nfts[key][1]:.2f}")
    print(f"Valor Total = R${carrinho['valor_total']:.2f}")
    if sair_continuar("Digite 'sair' para sair do carrinho \n -Digite 'comprar' para comprar\n -->",
                      ["sair", "comprar"]):
        for key in carrinho['nft'].keys():
            if key in carteira_usuario['nft']:
                carteira_usuario['nft'][key] += carrinho['nft'][key]
            else:
                carteira_usuario['nft'][key] = carrinho['nft'][key]
        limpar_carrinho()
        print("Compra efetuada com sucesso, seu carrinho foi esvaziado!")


# funcao de administrador para trocar as posicoes das equipes
def adm_trocar_posicao():
    alterar = forca_escolha(['sim', 'nao'], "Você deseja trocar as posições das equipes? sim ou nao\n --> ")
    if alterar == 'sim':
        posicoes_usadas = []
        for key in nfts:
            while True:
                posicao = numeric(f"Digite a posição da equipe {key} (1 a 11): \n -->")

                if posicao in range(1, 12):
                    if posicao not in posicoes_usadas:
                        posicao_antiga = nfts[key][0]
                        posicoes_usadas.append(posicao)
                        nfts[key][0] = posicao
                        nova_preco = calculo_ntf(key)
                        nfts[key][1] = nova_preco
                        print(
                            f"A posição da {key} foi alterada de {posicao_antiga}º para {nfts[key][0]}º e o novo valor é R${nfts[key][1]} ")

                        break
                    else:
                        print("Essa posição já está ocupada. Tente outra.")
                else:
                    print("Entrada inválida. Por favor, digite um número entre 1 e 11.")
        print_dic(nfts, '', True)
        print("Novos valores após a alteração!")


# visualizar carteira
def visualizar_carteira():
    while True:
        for key in carteira_usuario['nft']:
            print(f"{key} = {carteira_usuario['nft'][key]} unidades")
        if sair_continuar("Digite 'voltar' para voltar ao Menu\n --> ", ['voltar']):
            return


opcoes_Inicio = ["1","2","3","4"]
user = False
admin = False
print(pfig.figlet_format('TechAdvanced'))
while True:
    while True:
        print("Seja bem vindo a TechAdvanced: ") 
        escolha_inicio = forca_escolha(opcoes_Inicio,"Voce deseja fazer \n -->(1)Login \n -->(2)Cadastrar \n -->(3)Login como administrador \n -->(4)Sair \n -->")
        match escolha_inicio:
            case "1":
                user = login('Digite seu Usuário', 'Digite sua senha', usuarios)
                break
            case '2':
               cadastro()
            case '3':
                admin = login('Digite seu Usuário', 'Digite sua senha', adm)
                break
            #is_adm = True
            case '4':
                print('Obrigado por utilizar TechAdvanced!')
                exit()

        
    if user:
        admin = False
        user = False
        while True:
            print(f"Bem vindo ao portal do Usuário")
            escolha = forca_escolha(['1','2','3','4','5','6'], "Digite:\n [1] para ver os preços de nft de cada Equipe \n [2] Para visualizar a posição das equipes na ultima corrida \n [3] Para comprar nft \n [4] Exibir carrinho \n [5] Para exibir suas NFTs\n [6] Para sair\n -->")
            match escolha:
                case '1':
                    while True:
                        print_dic(nfts,1, True)
                        if sair_continuar("Digite 'voltar' para voltar ao Menu\n --> ",['voltar']):
                            break

                case '2':
                    while True:
                        print_dic(nfts,0)
                        if sair_continuar("Digite 'voltar' para voltar ao Menu\n --> ",['voltar']):
                                break

                case '3':
                    adicionar_carrinho()
                case '4':
                    comprar_carrinho()
                        
                
                case '5': 
                    while True:
                        for key in carteira_usuario['nft']:
                            print(f"{key} = {carteira_usuario['nft'][key]} unidades")
                        if sair_continuar("Digite 'voltar' para voltar ao Menu\n --> ",['voltar']):
                            break
                case '6':
                    break 

    if admin:
        admin = False
        user = False
        while True:
            print(f"Bem-vindo ao portal da Administração")
            escolha = forca_escolha(['1', '2'], "Digite:\n [1] Alterar posição das equipes na última corrida (Muda automaticamente os preços das NFT)\n [2] Para sair\n --> ")
            
            match escolha:
                case '1':
                    adm_trocar_posicao()
                case '2':
                    break