class Maquina:
    def __init__(self, preco_do_ticket):
        self.preco_do_ticket = int(preco_do_ticket)
        self.dinheiro_inserido = 0
        self.dinheiro_dentro = 0

    def inserir_dinheiro(self, dinheiro_inserido):
        self.dinheiro_inserido += dinheiro_inserido

    def imprimir_ticket(self):
        if self.dinheiro_inserido < self.preco_do_ticket:
            print(f"O dinheiro inserido na máquina ({self.dinheiro_inserido}) é insuficiente. Preço do Ticket: {self.preco_do_ticket} centavos")
        elif self.dinheiro_inserido == self.preco_do_ticket:
            print(f"""
####################
       TICKET
    {self.preco_do_ticket} centavos
####################
            """)
            # Atualizando quantidade de dinheiro inserido na máquina
            self.dinheiro_dentro += self.dinheiro_inserido
            # Zerando valor inserido
            self.dinheiro_inserido = 0

        elif self.dinheiro_inserido > self.preco_do_ticket:
            troco = self.dinheiro_inserido - self.preco_do_ticket
            print(f"""
            ####################
                   TICKET
                {self.preco_do_ticket} centavos
            Troco: {troco} centavos
            ####################
                        """)

            # Atualizando quantidade de dinheiro inserido na máquina
            self.dinheiro_dentro += (self.dinheiro_inserido - troco)
            # Zerando valor inserido
            self.dinheiro_inserido = 0

    # Getter de dinheiro_inserido
    def get_dinheiro_inserido(self):
        return self.dinheiro_inserido

    def dinheiro_arrecadado(self):
        return self.dinheiro_dentro
