# Trabalho Final  

# Cadastra peças novas tanto no arquivo como na lista existente.
def cadastrar_pecas():
    est = []
    id = int(input('Insira o ID da peça: '))
    while id in lista_id: # Validação com os IDs repetidos
        print('IDs utilizados:', lista_id)
        id = int(input('Insira um ID que não esteja sendo utilizado: '))
    f = open('pecas.txt', 'a', encoding='utf-8')
    peca = {}
    peca['Id'] = id # A partir de agora tudo segue o mesmo padrão. Adiconamos ao registro e ao arquivo.
    f.write(str(peca['Id']) + '\n')
    peca['Tipo'] = tratar_entradas(['Calçado', 'Inferior', 'Superior'], 'Insira o tipo da sua roupa. (Calçado, Inferior ou Superior):' )
    f.write(peca['Tipo'] + '\n')
    peca['Tamanho'] = tratar_entradas(['P','M','G'], 'Insira o tamanho da sua roupa. (P, M ou G): ')
    f.write(peca['Tamanho'] + '\n')
    peca['Cor'] = input('Insira a cor pedrominante da sua peça: ')
    f.write(peca['Cor'] + '\n')
    peca['Padrao'] = tratar_entradas(['Masculino', 'Feminino', 'Unissex'], 'Insira o padrão da sua peça (Masculino, Feminino, Unissex): ')
    f.write(peca['Padrao'] + '\n')
    peca['Data'] = tratar_datas('Insira a data de hoje: (dd/mm/aaaa): ')
    f.write(peca['Data'] + '\n')
    peca['Situação'] = tratar_entradas(['Venda', 'Doação', 'Ficar'], 'Insira a situação da peça (Venda, Doação ou Ficar): ')
    f.write(peca['Situação'] + '\n')
    peca['Preço'] = float(input('Insira o preço da peça. (0 caso seja não seja para Venda)'))
    f.write(str(peca['Preço']) + '\n')
    print(estilos) # Aqui delimitamos os estilos disponíveis para o usuário escolher, caso ele queira outro, deverá registrar antes de cadastrar uma peça.
    qtd_estilos = int(input('Em quantos dos estilos acima sua peça se enquadra? '))
    for i in range(qtd_estilos):
        indice = tratar_indice(estilos,'Insira o índice do estilo que você combina com sua roupa: (Primeiro é o de índice 0) ')
        while estilos[indice] in est: # Tratar para que o usuário não possa repetir um estilo na peça
            indice = tratar_indice(estilos, 'Insira o índice de um estilo não repetido!')
        est.append(estilos[indice])
        if i == qtd_estilos - 1:
            f.write(estilos[indice] + '\n')
        else:
            f.write(estilos[indice] + ' ')
    peca['Estilos'] = est
    pecas.append(peca) # Adicionando o registro para uma lista, facilitando o o trabalho posterior.
    lista_id.append(id)
    f.close()
    return f


def tratar_datas(men): # Tratamento para os casos de data inválida (Ano inexistente, dia inexistente...)
    para = 0
    while para==0:
        entrada = input(men)
        errado = 0
        if entrada.find("/")!=2 or entrada.rfind("/")!=5 or len(entrada)!=10 or entrada.count("/")!=2:
            print("Entrada inválida!")
            errado = 1
        else:
            dia = entrada[:2]
            dia = int(dia)
            mes = entrada[3:5]
            mes = int(mes)
            ano = entrada[6:]
            ano = int(ano)
            anobis = 0
            if (ano % 4) == 0:
                if (ano % 100) ==0 and (ano % 400) !=0:
                    anobis = 0 # Não é bissexto
                else:
                    anobis = 1 # É bissexto
            if dia>31 or mes>12:
                print("Entrada inválida!")
            elif dia<1 or mes<1:
                print("Entrada inválida")
            elif dia>30 and (mes==2 or mes==4 or mes==6 or mes==9 or mes==11):
                print("Entrada inválida")
            elif mes==2 and dia>28 and anobis==0 or dia>29 :
                print("Entrada inválida")
            else:
                para=1
    return entrada


def tratar_entradas(lista, mensagem): # Função que, dada uma lista da palavras, repete o input até que o usuário escreva uma dessas palavras
    n = input(mensagem)
    while n not in lista:
        print('Entrada inválida!')
        n = input(mensagem)
        
    else:
        return n 


def tratar_indice(lista, mensagem): # Impede que, dada uma lista, o usuário digite um índice que supera o da lista
    indices = []
    for i in range(len(lista)):
        indices.append(i)
    n = int(input(mensagem))
    while n not in indices:
        print('Entrada Inválida')
        n = int(input(mensagem))
    return n


def remover_pecas_arquivo(linha):
    linha = linha - 1 # Como vamos tratar de um índice de uma lista, a linha terá índice -1. # Mudando o tipo da referência para string para concatenar depois.
    documento = open("pecas.txt", "r", encoding="utf-8") # Abrimos o arquivo, passamos para uma lista, escrevemos novamente o arquivo com a alteração.
    lines = documento.readlines()
    documento.close()
    for i in range(9):    
        lines.pop(linha)
    documento = open("pecas.txt", "w", encoding="utf-8")
    documento.writelines(lines)
    documento.close()


def remover_estilo():
    print(estilos)  
    estilos_usados = [] # Tratamento para não deixar que o usuário remova um estilo que está cadastrado em uma peça
    x = tratar_indice(estilos,"Digite o número do índice do estilo que você quer remover: ") 
    for i in pecas:
        for j in i['Estilos']:
            if j not in estilos_usados:
                estilos_usados.append(j)
    while estilos[x] in estilos_usados:
        print('Esse são os estilos que estão sendo utilizados:\n%s' %estilos_usados)
        print(estilos)
        x = tratar_indice(estilos,"Digite o número do índice de um estilo que não esteja sendo utilizado! : ") 



    line = x + 1
    estilos.pop(x) # Tira da lista de estilos
    linha = line - 1 # Como vamos tratar de um índice de uma lista, a linha terá índice -1. 
    documento = open("estilos.txt", "r", encoding="utf-8")
    lines_arquivo_estilo = documento.readlines()
    documento.close()
    lines_arquivo_estilo.pop(linha) # Remove o estilo da lista que corresponde ao arquivo
    documento = open("estilos.txt", "w", encoding="utf-8")
    documento.writelines(lines_arquivo_estilo)  # Escreve novamente no arquivo
    documento.close()


def alterar_estilo():
    print(estilos)
    estilos_usados = [] # Tratamento para não deixar que ele altere um estilo que esteja cadastrado em uma peça
    n = tratar_indice(estilos, 'Insira o índice do estilo que você quer alterar: ')
    for i in pecas:
        for j in i['Estilos']:
            if j not in estilos_usados:
                estilos_usados.append(j)
    while estilos[n] in estilos_usados:
        print('Esse são os estilos que estão sendo utilizados:\n%s' %estilos_usados)
        print(estilos)
        n = tratar_indice(estilos,"Digite o número do índice de um estilo que não esteja sendo utilizado! : ")    
    

    novo_nome = input('Insira o novo nome: ')
    while novo_nome in estilos: # Verifica se o nome já está cadastrado
        novo_nome = input('Insira o nome de um estilo que não esteja cadastrado: ')
    estilos[n] = novo_nome  # Modificamos na lista de estilos
    doc = open("estilos.txt", "r", encoding="utf-8")
    lines = doc.readlines()
    doc.close()
    lines[n] = novo_nome + '\n' # Modificamos no arquivo
    doc = open("estilos.txt", "w", encoding="utf-8")
    doc.writelines(lines)
    doc.close()
    

def mudar_linha(linha, conteudo):
    linha = linha - 1 # Como vamos tratar de um índice de uma lista, a linha terá índice -1.
    conteudo = str(conteudo) # Mudando o tipo da referência para string para concatenar depois.
    documento = open("pecas.txt", "r", encoding="utf-8")
    lines = documento.readlines()
    documento.close() # Abrimos o arquivo, passamos para uma lista, escrevemos novamente o arquivo com a alteração na linha.
    lines[linha] = conteudo + '\n'
    documento = open("pecas.txt", "w", encoding="utf-8")
    documento.writelines(lines)
    documento.close()


def selecionar_estilo_por_nome():
  print(estilos)
  x = tratar_indice(estilos,"Digite o índice do estilo que você quer selecionar(o primeiro estilo tem índice 0): ")
  estilo = estilos[x]
  print(estilo)
  for i in pecas: # Mostra as peças que possuem o estilo selecionado
    if i["Estilos"].count(estilo) == 1:
      print(i)
  resposta = int(input("Digite: \n1 Se você escolheu o estilo que queria. \n2 Se deseja mudar o estilo."))
  if resposta == 1: # Quando o usuário confirmar o estilo que quer, o contador dele aumenta em um
    contador[x] = contador[x] + 1
  elif resposta != 1: # Se ele não tiver confirmado, a função repete
    selecionar_estilo_por_nome() 


def listar_estilos():
  # Colocar os contadores na ordem crescente
  contador_crescente = contador[:]
  contador_crescente.sort()
  # Pegar os index dos contadores já colocados em ordem crescente
  index_dos_contadores_crescente = []
  for i in range(len(contador)):
    for j in range(len(contador)):
      # Se esse contador tiver nessa peça, e essa peça não tiver no index, adiciona ela a lista.
      if contador_crescente[i]==contador[j] and j not in index_dos_contadores_crescente:
        index_dos_contadores_crescente.append(j)
        break
  for i in index_dos_contadores_crescente:
    print(estilos[i], end=" ")


def alterar_pecas():
    for i in range(len(pecas)):
        print(pecas[i])
    print("Assuma a primeira linha como 0, a segunda como 1, e assim por diante.")
    x = tratar_indice(pecas,"Digite o número da linha da peça que você quer alterar: ") 
    line = x*9 # Como as peças no arquivo seguem o mesmo padrão, o primeiro ID sempre estará na linha (x * 9) + 1.

    print("\nId da peça: ", pecas[x]["Id"])
    resposta = int(input("Digite: \n1 - se quiser alterar o ID\n2 - se não quiser alterar o ID\n"))
    if resposta == 1:
        id = int(input('Insira o novo ID da peça: '))
        while id in lista_id:
            print('IDs utilizados:', lista_id)
            id = int(input('Insira um ID que não esteja sendo utilizado: '))
        mudar_linha(line + 1, id)
        lista_id[lista_id.index(pecas[x]["Id"])] = id
        pecas[x]["Id"] = id

    # Os elementos são alterado tanto na lista IDs, como na lista peças como no arquivo.
    # A partir daqui será dada a opção de trocar cada informação da peça, alterando tanto na lista pecas quanto no arquivo.
    print("\nTipo da peça: ", pecas[x]["Tipo"])
    print("Caso não queira alterar, digite o mesmo tipo que estava antes.")
    pecas[x]['Tipo'] = tratar_entradas(['Calçado', 'Inferior', 'Superior'], 'Insira o tipo da sua roupa. (Calçado, Inferior ou Superior):' )
    mudar_linha(line + 2, pecas[x]['Tipo']) # Função mudar linha usada novamente.

    print("\nTamanho da peça: ", pecas[x]["Tamanho"])
    print("Caso não queira alterar, digite o mesmo tamanho que estava antes.")
    pecas[x]['Tamanho'] = tratar_entradas(['P','M','G'], 'Insira o tamanho da sua roupa. (P, M ou G): ')
    mudar_linha(line + 3, pecas[x]['Tamanho'])

    print("\nCor da peça: ", pecas[x]["Cor"])
    print("Caso não queira alterar, digite a mesma cor que estava antes.")
    pecas[x]['Cor'] = input('Insira a cor pedrominante da sua peça: ')
    mudar_linha(line + 4, pecas[x]['Cor'])

    print("\nPadrão da peça: ", pecas[x]["Padrao"])
    print("Caso não queira alterar, digite o mesmo padrão que estava antes.")
    pecas[x]['Padrao'] = tratar_entradas(['Masculino', 'Feminino', 'Unissex'], 'Insira o padrão da sua peça (Masculino, Feminino, Unissex): ')
    mudar_linha(line + 5, pecas[x]['Padrao'])

    print("\nData da peça: ", pecas[x]["Data"])
    print("Caso não queira alterar, digite a mesma data que estava antes.")
    pecas[x]['Data'] = tratar_datas('Insira a nova data: (dd/mm/aaaa): ')
    mudar_linha(line + 6, pecas[x]['Data'])

    print("\nSituação da peça: ", pecas[x]["Situação"])
    print("Caso não queira alterar, digite a mesma situação que estava antes.")
    pecas[x]['Situação'] = tratar_entradas(['Venda', 'Doação', 'Ficar'], 'Insira a situação da peça (Venda, Doação ou Ficar): ')
    mudar_linha(line + 7, pecas[x]['Situação'])

    print("\nPreço da peça: ", pecas[x]["Preço"])
    print("Caso não queira alterar, digite o mesmo preço que estava antes.")
    pecas[x]['Preço'] = float(input('Insira o preço da peça (0 caso não seja para Venda): '))
    mudar_linha(line + 8, pecas[x]['Preço'])

    # Na hora de alterar o estilo, será dada a opção de adicionar ou remover um estilo à peça.
    print("\nEstilo(s) da peça: ",pecas[x]["Estilos"])
    resposta2 = 0
    while resposta2 != 3:
      resposta2 = int(input("Digite:\n1 - se quiser adicionar um estilo à peça \n2 - se quiser remover um estilo da peça \n3 - se não quiser alterar os estilos\n"))
      if resposta2 == 1:
        print(estilos)
        ind = tratar_indice(estilos, 'Insira o índice do estilo que você quer adicionar: (Primeiro é o de índice 0) ')
        if estilos[ind] not in pecas[x]["Estilos"]: # Evitar estilos repetidos na mesma peça
          pecas[x]["Estilos"].append(estilos[ind])
      elif resposta2 == 2:
        print(pecas[x]["Estilos"])
        ind = tratar_indice(pecas[x]["Estilos"], 'Insira o índice do estilo que você quer remover: (Primeiro é o de índice 0) ')
        pecas[x]["Estilos"].pop(ind)
    aux = ''
    for i in range(len(pecas[x]["Estilos"])):
        if i < (len(pecas[x]["Estilos"]) - 1):
            aux += pecas[x]["Estilos"][i] + ' '
        else:
            aux += pecas[x]["Estilos"][i]
    mudar_linha(line + 9, aux)


def mostrar_roupa_para_venda():
    pecas_para_venda_id = []
    precos = []
    pecas_para_venda_dados = []
    for i in pecas: 
        if i["Situação"] == "Venda": # Se a situação for de venda, adicionamos o preço em uma lista de preços.
            precos.append(i["Preço"])
    precos.sort() # Lista de preços ordenada de forma crescente
    for i in precos: # Comparamos cada preço com os preços das peças em situação de venda, como a lista está crescente, a lista de roupas para venda também estará.
        for j in pecas:
            if i == j["Preço"] and j["Situação"] == "Venda" and j["Id"] not in pecas_para_venda_id:
                pecas_para_venda_id.append(j["Id"])
                break # Transferimos o ID exibir todos os dados das peças.
    for x in pecas_para_venda_id:  # Transferimos o ID exibir todos os dados das peças.
        for j in range(len(pecas)):
            if pecas[j]["Id"] == x:
                pecas_para_venda_dados.append(pecas[j])
    for i in pecas_para_venda_dados:
        print(i)
    return(pecas_para_venda_dados)


def listar_roupa_para_doacao():
    pecas_para_doacao_id = []
    datas = []

    for i in pecas: # Se a situação for de doação, adicionamos o preço em uma lista de datas
        if i["Situação"] == "Doação":
            datas.append(i["Data"])

    for i in range(len(datas)): # O ano é o bit mais significativo seguido do mês eo dia . Então vamos transformar a data em um número aaaammdd. (amd = ano, mês e dia)
        amd = datas[i][6:]
        amd = str(amd)
        ta = len(amd)
        amd = amd+datas[i][3:5]
        amd = amd+datas[i][0:2]
        amd = int(amd)
        datas[i] = amd

    datas.sort(reverse=True) # Lista de datas ordenada de forma decrescente

    for i in range(len(datas)): # Retornar a lista a sua forma de data original (dd/mm/aaaa)
        datas[i] = str(datas[i])
        dma = datas[i][6:8]+"/"
        dma = dma+datas[i][4:6]+"/"
        dma = dma+datas[i][:ta]
        datas[i] = dma


    for i in datas: # Comparamos cada preço com os preços das peças em situação de doação, como a lista está decrescente, a lista de roupas para data também estará.
        for j in pecas:
            if i == j["Data"] and j["Situação"] == "Doação" and j['Id'] not in pecas_para_doacao_id:
                pecas_para_doacao_id.append(j["Id"])
                break # Transferimos o ID para exibir todos os dados da peça
  
    pecas_para_doacao_dados = []
    for x in pecas_para_doacao_id: # Pegando os dados das peças a partir do ID
        for j in range(len(pecas)):
            if pecas[j]["Id"] == x:
                pecas_para_doacao_dados.append(pecas[j])
    for i in pecas_para_doacao_dados:
        print(i)
    return pecas_para_doacao_dados


def remover_pecas():
    for i in range(len(pecas)):
        print(pecas[i])
    print("Assuma a primeira linha como 0, a segunda como 1, e assim por diante.")
    x = tratar_indice(pecas, "Digite o número da linha da peça que você quer remover: ") 
    line = x*9 # A linha é o número da peça vezes 9, já que cada peça ocupa 9 linhas no arquivo
    id = pecas[x]["Id"]
    lista_id.remove(id)
    pecas.pop(x)
    remover_pecas_arquivo(line+1)


def mostrar_roupas_interesse():
    tam = input('Insira o tamanho da sua roupa. (P, M ou G): ')
    padr = input('Insira o padrão da sua peça (Masculino, Feminino, Unissex): ')
    for i in pecas:
        if i['Tamanho'] == tam and i['Padrao'] == padr: # Mostramos quais possuem a mesma das informações indicadas.
            print(i)


def cadastrar_estilo():
    nome = input('Insira o nome do estilo que você quer cadastrar: ')
    while nome in estilos: # Tratamento caso o estilo já exista.
        nome = input('Insira o nome de um estilo que não esteja cadastrado: ')
    estilos.append(nome) # Escrevemos o estilo na lista de estilos
    estilos_arq = open("estilos.txt", "a", encoding="utf-8")
    estilos_arq.write(nome + '\n') # Escrevemos o estilo no arquivo
    arq_estilos.close()
    contador.append(0)


def vender_peca():
    print('Assuma a primeira como 0, a segunda por 1 e assim em diante.')
    peca_venda = mostrar_roupa_para_venda()
    indice_venda = tratar_indice(peca_venda, 'Qual dessas peças você deseja vender?')
    # Remove da lista pecas
    index_na_lista_pecas = pecas.index(peca_venda[indice_venda])
    pecas.pop(index_na_lista_pecas)
    lista_id.remove(peca_venda[indice_venda]['Id'])
    peca_venda[indice_venda]['Data Entregue'] = tratar_datas('Que dia a peça está sendo vendida? ')
    peca_venda[indice_venda]['Destino'] = input('Para quem a roupa está sendo entregue? ')
    peca_venda[indice_venda]['Preço Venda'] = input('Qual o valor a peça está sendo transferia?')
    pecas_vendidas.append(peca_venda[indice_venda]) # Adiciona a lista de peças vendidas
    remover_pecas_arquivo(index_na_lista_pecas + 1) # Remove do arquivo geral
    # Adicionando ao arquivo de peças vendidas
    arq = open("vendidos.txt", "a", encoding="utf-8")
    arq.write(str(peca_venda[indice_venda]['Id']) + '\n') 
    arq.write(peca_venda[indice_venda]['Tipo'] + '\n')
    arq.write(peca_venda[indice_venda]['Tamanho'] + '\n')
    arq.write(peca_venda[indice_venda]['Cor'] + '\n')
    arq.write(peca_venda[indice_venda]['Data Entregue'] + '\n')
    arq.write(peca_venda[indice_venda]['Preço Venda'] + '\n')
    arq.write(peca_venda[indice_venda]['Destino'] + '\n')
    arq.close()

  
def doar_peca():
    print('Assuma a primeira como 0, a segunda por 1 e assim em diante.')
    peca_doada = listar_roupa_para_doacao()
    indice_doar = tratar_indice(peca_doada, 'Qual dessas peças você deseja doar? ')
    # Remove da lista pecas
    index_na_lista_pecas = pecas.index(peca_doada[indice_doar])
    pecas.pop(index_na_lista_pecas)
    lista_id.remove(peca_doada[indice_doar]['Id'])
    
    # Recebe novas informações para um registro de peças doadas
    peca_doada[indice_doar]['Data Entregue'] = tratar_datas('Que dia a peça está sendo doada? ')
    peca_doada[indice_doar]['Destino'] = input('Para quem a roupa está sendo entregue? ')
    dic_peca_doada = {}
    dic_peca_doada['Tipo'] = peca_doada[indice_doar]['Tipo'] 
    dic_peca_doada['Tamanho'] = peca_doada[indice_doar]['Tamanho'] 
    dic_peca_doada['Cor'] = peca_doada[indice_doar]['Cor']  
    dic_peca_doada['Data Entregue'] = peca_doada[indice_doar]['Data Entregue']
    dic_peca_doada['Destino'] = peca_doada[indice_doar]['Destino']


    pecas_doadas.append(dic_peca_doada) # Adiciona a lista de peças doadas
    remover_pecas_arquivo(index_na_lista_pecas + 1) # Remove do arquivo geral
    # Adicionando ao arquivo de peças doadas
    arq = open("doados.txt", "a", encoding="utf-8")
    arq.write(str(peca_doada[indice_doar]['Id']) + '\n')
    arq.write(peca_doada[indice_doar]['Tipo'] + '\n')
    arq.write(peca_doada[indice_doar]['Tamanho'] + '\n')
    arq.write(peca_doada[indice_doar]['Cor'] + '\n')
    arq.write(peca_doada[indice_doar]['Data Entregue'] + '\n')
    arq.write(peca_doada[indice_doar]['Destino'] + '\n')
    arq.close()


def mostrar_doadas_por_ong():
    ong = []
    # Criando uma lista de ONGs 
    for i in pecas_doadas:
        if i['Destino'] not in ong:
            ong.append(i['Destino'])
    print(ong)
    # Escolhendo uma das ONGs
    indice = int(input('Insira o índice de uma das instituições/pessoas acima: '))
    # Mostra as peças da ONG
    for i in pecas_doadas:
        if i['Destino'] == ong[indice]:
            print(i)


# Programa Principal

# Tratamento para caso os arquivos não existam, criando cada um deles e adicionando os estilos pré-salvos no arquivo.
try:
     a = open('pecas.txt', 'r')
     a.close()
except:
    a = open('pecas.txt', 'w')
    a.close()
try:
     a = open('doados.txt', 'r')
     a.close()
except:
    a = open('doados.txt', 'w')
    a.close()
try:
     a = open('estilos.txt', 'r')
     a.close()
except:
    a = open('estilos.txt', 'w', encoding='utf-8')
    a.write('Clássico\nVintage\nRetro\nStreet\nCasual\nGlam\nComfy\nHipster\nEsportivo\nIndie\nMinimalista\nRomântico\nSexy\nUrbano\nRocker\nEmo\n')
    a.close()
try:
     a = open('vendidos.txt', 'r')
     a.close()
except:
    a = open('vendidos.txt', 'w')
    a.close()



# Salvando a quantidade de linhas do texto de estilos
arq_estilos = open("estilos.txt", "r", encoding="utf-8")
linhas_estilos = len(arq_estilos.readlines())
arq_estilos.close()
arq_estilos = open("estilos.txt", "r", encoding="utf-8")
estilos = []
pecas_vendidas = []
pecas_doadas = []


# Adicionando os estilos do arquivo à lista de estilos
for i in range(linhas_estilos):
    estilos.append(arq_estilos.readline().strip('\n'))
    
arq_estilos.close()

contador = [0]*len(estilos)
ref_arquivo = open("pecas.txt", "r", encoding='utf-8')
linhas = len(ref_arquivo.readlines())
ref_arquivo.close()
lista_id = []
qtd_pecas = int(linhas / 9) # Como cada peça é divida em 9 linhas, a quantidade de peças será a quantidade de linhas dividia por 9
pecas = []
ref_arquivo = open("pecas.txt", "r", encoding='utf-8')

# Adicionando as peças à lista de peças
for i in range(qtd_pecas):
    peca = {}
    id = int(ref_arquivo.readline().strip('\n'))
    lista_id.append(id)
    peca['Id'] = id
    peca['Tipo'] = ref_arquivo.readline().strip('\n')
    peca['Tamanho'] = ref_arquivo.readline().strip('\n')
    peca['Cor'] = ref_arquivo.readline().strip('\n')
    peca['Padrao'] = ref_arquivo.readline().strip('\n')
    peca['Data'] = ref_arquivo.readline().strip('\n')
    peca['Situação'] = ref_arquivo.readline().strip('\n')
    peca['Preço'] = float(ref_arquivo.readline().strip('\n'))
    peca['Estilos'] = ref_arquivo.readline().strip('\n').split()
    pecas.append(peca)
ref_arquivo.close()

arquivo_doadas = open("doados.txt", "r", encoding="utf-8")
qtd_pecas_doadas = int(len(arquivo_doadas.readlines()) / 6)
arquivo_doadas.close()
arquivo_doadas = open("doados.txt", "r", encoding="utf-8")
# Adicionando as roupas doadas do arquivo à lista de roupas doadas
for i in range(qtd_pecas_doadas):
    dic_doada = {}
    dic_doada['Id'] = arquivo_doadas.readline().strip('\n')
    dic_doada['Tipo'] = arquivo_doadas.readline().strip('\n')
    dic_doada['Tamanho'] = arquivo_doadas.readline().strip('\n')
    dic_doada['Cor'] = arquivo_doadas.readline().strip('\n')
    dic_doada['Data Entregue'] = arquivo_doadas.readline().strip('\n')
    dic_doada['Destino'] = arquivo_doadas.readline().strip('\n')
    pecas_doadas.append(dic_doada)
arquivo_doadas.close()
arquivo_vendidas = open("vendidos.txt", "r", encoding="utf-8")
qtd_pecas_vendidas = int(len(arquivo_vendidas.readlines()) /7)
arquivo_vendidas.close()
arquivo_vendidas = open("vendidos.txt", "r", encoding="utf-8")
# Adicionando as roupas vendidas do arquivo à lista de roupas vendidas.
for i in range(qtd_pecas_vendidas):
    dic_vendidas = {}
    dic_vendidas['Id'] = arquivo_vendidas.readline().strip('\n')
    dic_vendidas['Tipo'] = arquivo_vendidas.readline().strip('\n')
    dic_vendidas['Tamanho'] = arquivo_vendidas.readline().strip('\n')
    dic_vendidas['Cor'] = arquivo_vendidas.readline().strip('\n')
    dic_vendidas['Data Entregue'] = arquivo_vendidas.readline().strip('\n')
    dic_vendidas['Preço Venda'] = arquivo_vendidas.readline().strip('\n')
    dic_vendidas['Destino'] = arquivo_vendidas.readline().strip('\n')
    pecas_vendidas.append(dic_vendidas)
arquivo_vendidas.close()


# Loop Principal
grupo = [['Trio do Armarinho', 0, 0],['Gustavo Fernandez', 'Guilherme Sousa', 'João Italo']]
funcionando = True
while funcionando:
    n = input(('\nDigite: \n0 - Parar o programa\n1 - Alterar algo no guarda-roupa\n2 - Visualizar algo no guarda-roupa\n3 - Vender / Doar alguma peça\n'))
    if n == '0':
        funcionando = False
    elif n == '1':
        n1 = input('Digite: \n0 - Voltar para o menu principal\n1 - Cadastrar uma peça\n2 - Alterar uma peça\n3 - Remover uma peça\n4 - Remover estilo\n5 - Alterar estilo\n6 - Cadastrar estilo\n')
        if n1 == '1':
            cadastrar_pecas()
        elif n1 == '2':
            if len(pecas) != 0:
                alterar_pecas()
            else:
                print('Não há peças para alterar!')
        elif n1 == '3':
            if len(pecas) != 0:
                remover_pecas()
            else:
                print('Não há peças para remover!')
        elif n1 == '4':
            remover_estilo()
        elif n1 == '5':
            alterar_estilo()
        elif n1 == '6':
            cadastrar_estilo()
    elif n == '2':
        n2 = input('Digite: \n0 - Voltar para o menu principal\n1 - Listar roupas para doação\n2 - Listar roupas para venda \n3 - Listar roupas do seu interesse\n4 - Listar roupas doadas\n5 - Listar estilos\n6 - Selecionar estilos por nome\n')
        if n2 == '1':
            listar_roupa_para_doacao()
        elif n2 == '2':
            mostrar_roupa_para_venda()
        elif n2 == '3':
            mostrar_roupas_interesse()
        elif n2 == '4':
            mostrar_doadas_por_ong()
        elif n2 == '5':
            listar_estilos()
        elif n2 =='6':
            selecionar_estilo_por_nome()
    elif n =='3':
        n3 = input('Digite: \n 0 - Voltar para o menu principal\n 1 - Vender uma peça\n 2 - Doar uma peça\n')
        if n3 == '1':
            vender_peca()
        elif n3 == '2':
            doar_peca()



print('Obrigado por usar o programa! :)')
print('Programa feito por: ')
print(grupo[0][0])
for i in range(len(grupo[1])):
    print(grupo[1][i])