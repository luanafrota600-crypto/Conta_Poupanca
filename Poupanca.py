from Conta import Conta

class Poupanca(Conta):
    def __init__(self, titular, agencia, conta):
        super().__init__(titular, agencia, conta)
        self.taxaRendimento = 0.05
        
        
    def mostrarInfomacoesConta(self):
        super().mostrarInfomacoesConta()
        print(f'taxa de rendimento: {self.taxaRendimento}')
        print('-----------------------------------')
        
    def rendimentoJuros(self):
        self.saldo = self.saldo + (self.saldo * self.taxaRendimento)


if __name__ == '__main__':
    contapp1 = Poupanca('Alvaro Lopes Rios', 1234, 4321)
    contapp1.mostrarInfomacoesConta()
    contapp1.depositar(50)
    contapp1.mostrarInfomacoesConta()
    contapp1.rendimentoJuros()
    contapp1.mostrarInfomacoesConta()
    contapp1.rendimentoJuros()
    contapp1.mostrarInfomacoesConta()
