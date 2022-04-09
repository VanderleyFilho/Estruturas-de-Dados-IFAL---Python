##############################################################
### DISCIPLINA: Estrutura de Dados - IFAL - 2021.2
### PROFESSOR: Ricardo Nunes
### ALUNO: José Vanderley Pereira da Silva Filho
### MATRÍCULA: 2018004380
### DATA: 08/04/2022
##############################################################

# Definindo variável que será utilizada no Menu
opcao = 0

# Definindo Lista
listaVeiculos = []

# Definindo TAD Veiculo
class Veiculo():
    def __init__(self):
        placa = str(input("Digite a Placa do Veículo: "))
        marca = str(input("Digite a marca do Veículo: "))
        modelo = str(input("Digite o modelo do Veículo: "))
        ano = str(input("Digite o ano do Veículo: "))
        cod = int(input("Digite o Código do Proprietário: "))

        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cod = cod

    # Função para capturar apenas a Placa do veículo
    def getPlaca(self):
        return self.placa


    def __str__(self):
        return "Placa: " + self.placa + "\nMarca: " + self.marca + "\nModelo: " + self.modelo + "\nAno: " + self.ano + "\nCód Proprietário: " + self.cod

    # Função que imprime os dados do veículo
    def imprimeVeiculo(self):
        print(self)

    # Função para capturar o último dígito da placa
    def finalPlaca(self):
        return self.placa[-1]



# Função para Cadastrar Veículo
def cadastrarVeiculo(self):
    placa = str(input("Digite a Placa do Veículo: "))
    marca = str(input("Digite a Marca do Veículo: "))
    modelo = str(input("Digite o Modelo do Veículo: "))
    ano = str(input("Digite o Ano do Veículo: "))
    cod = str(input("Digite o Código do Proprietário do Veículo: "))


# Laço onde será executado o menu de opções - Ao finalizar as ações feitas em cada uma das opções, retorna ao Menu para selecionar opções mais uma vez - Exceto se for escolhida a opção para finalizar.
while opcao != 5:
    print('''
    [1] cadastrar veículo
    [2] remover veículo
    [3] consultar por placa
    [4] consultar por número
    [5] finalizar
    ''')

    opcao = int(input("Digite a opção desejada: "))


    if opcao == 1:
        print("CADASTRO DE VEÍCULOS")

        novoVeiculo = Veiculo()
        listaVeiculos.append(novoVeiculo)
        print("\nNovo Veículo ADICIONADO!!!: \n")
        novoVeiculo.imprimeVeiculo()


    elif opcao == 2:
        print("REMOVER VEÍCULOS")

        if len(listaVeiculos) > 0:

            removerplaca = str(input("Digite a Placa: "))

            itemRemovido = False

            for veiculo in listaVeiculos:
                if veiculo.getPlaca() == removerplaca:
                    listaVeiculos.remove(veiculo)
                    itemRemovido = True
                    break

            if itemRemovido:
                print("Remoção de Veículo de Placa " + removerplaca + " Realizada com SUCESSO!!!")
            else:
                print("Remoção não Realizada!!!")

        else:
            print("Lista Vazia")


    elif opcao == 3:
        print("CONSULTA DE VEÍCULOS - POR PLACA")

        consultaplaca = str(input("Digite a Placa: "))

        itemEncontrado = False

        for veiculo in listaVeiculos:
            if consultaplaca == veiculo.getPlaca():
                veiculo.imprimeVeiculo()
                itemEncontrado = True
                break

        if not itemEncontrado:
            print("Veículo não Encontrado!")


    elif opcao == 4:
        print("CONSULTA DE VEÍCULOS - POR NÚMERO")

        consultacod = int(input("Digite o Número: "))

        if consultacod < 0 or consultacod >= 10:
            print("Dígito Inválido. Por Favor, Verifique o Número e Tente Mais uma Vez!!!")

        else:
            codEncontrado = False

            for veiculo in listaVeiculos:
                if consultacod == int(veiculo.finalPlaca()):
                    veiculo.imprimeVeiculo()
                    codEncontrado = True
                    break

            if not codEncontrado:
                print("Veículo não Encontrado!")


    elif opcao > 5:
        print("Opção Inválida. Tente Novamente!!!")


print("********** FIM DO PROGRAMA **********")
