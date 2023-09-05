class Cliente:

    _total = 0

    def __init__(self, CPF, nome, Email):
        self._cpf = CPF
        self._nome = nome
        self._email = Email
        Cliente._total += 1

    def get_cpf(self):
        return self._cpf

    def set_cpf(self, CPF):
        self._cpf = CPF

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_email(self):
        return self._email

    def set_email(self, Email):
        self._email = Email

    def imprimir_cliente(self):
        print(f"""===============
              CPF: {self.get_cpf()}
              Nome: {self.get_nome()}
              E-mail: {self.get_email()}
              ==============""")

    @staticmethod
    def total_clientes():
        return Cliente._total


class Conta:

    _total = 0

    def __init__(self, agencia, numero, saldo, titular):
        self._agencia = agencia
        self._numero = numero
        self._saldo = saldo
        self._titular = titular
        Conta._total += 1

    def get_agencia(self):
        return self._agencia

    def set_agencia(self, agencia):
        self._agencia = agencia

    def get_numero(self):
        return self._numero

    def set_numero(self, numero):
        self._numero = numero

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, saldo):
        self._saldo = saldo

    def get_titular(self):
        return self._titular

    def set_titular(self, titular):
        self._titular = titular

    def imprimir_conta(self):
        print(f"""===============
              Agência: {self.get_agencia()}
              Número: {self.get_numero()}
              Saldo: {self.get_saldo()}
              Titular: {self.get_titular().get_nome()}
              ==============""")

    @staticmethod
    def total_contas():
        return Conta._total


clientes = []
contas = []


def menu():
    print("""===============
[1] - Cadastrar Cliente
[2] - Cadastrar Conta
[3] - Buscar Contas por CPF ou Nome
[4] - Listar Clientes por Ordem de Saldo
[5] - Sair
==============""")


def cadastrar_cliente():
    cpf = int(input("Informe os dígitos do CPF: "))
    nome = input("Informe o nome: ")
    email = input("Informe o E-mail: ")
    clientes.append(Cliente(cpf, nome, email))
    print("Cliente cadastrado com sucesso!")

def cadastrar_conta():
    agencia = input("Informe a agência: ")
    numero = int(input("Informe o número da conta: "))
    saldo = float(input("Informe o saldo: "))
    titular = ""
    verificacao = int(input("Informe os dígitos do CPF: "))
    tem_cliente = False

    for i in clientes:
        if i.get_cpf() == verificacao:
            titular = i
            tem_cliente = True
        if tem_cliente:
            contas.append(Conta(agencia, numero, saldo, titular))
            print("Conta cadastrada com sucesso!")
        else:
            print("O cliente não está cadastrado! Conta não cadastrada.")

def busca_contas_por_cpf_ou_nome():

    print("""===============
[1] - Buscar por CPF
[2] - Buscar por Nome""")
    
    
    escolha = int(input("Escolha uma opção: "))
    cont_total_buscadas = 0
    cont_sequencial = 1

    if escolha == 1:
        cpf = int(input("Informe os dígitos do CPF: "))
        for i in contas:
            if i.get_titular().get_cpf() == cpf:
                print(f"Conta {cont_sequencial})")
                i.imprimir_conta()
                cont_sequencial += 1
                cont_total_buscadas += 1
        print(f"Total de contas: {cont_total_buscadas}")
        if cont_total_buscadas == 0:
            print("Nenhuma conta encontrada!")
    elif escolha == 2:
        nome = int(input("Informe o nome: "))
        for i in contas:
            if i.get_titular().get_nome() == nome:
                print(f"Conta {cont_sequencial})")
                i.imprimir_conta()
                cont_sequencial += 1
                cont_total_buscadas += 1
        print(f"Total de contas: {cont_total_buscadas}")
        if cont_total_buscadas == 0:
            print("Nenhuma conta encontrada!")

def listar_clientes_por_ordem_saldo():
    cont_sequencial = 1
    contas_ordenadas_por_saldo = sorted(contas, key=Conta.get_saldo)
    
    for i in contas_ordenadas_por_saldo:
        print(f"Cliente {cont_sequencial})")
        i.get_titular().imprimir_cliente()
        cont_sequencial += 1
    print(f"Total de clientes: {Cliente.total_clientes()}")
    if Cliente.total_clientes() == 0:
        print("Não há clientes!")

busca_contas_por_cpf_ou_nome()
