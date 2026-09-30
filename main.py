from Conta import Conta
from Poupanca import Poupanca


def main():
    print('===== EXEMPLO: CONTA POUPANÇA =====\n')

    # Abrindo uma conta poupança
    poupanca = Poupanca('Alvaro Lopes Rios', 1234, 4321)
    poupanca.mostrarInfomacoesConta()

    # Depósito e saque
    poupanca.depositar(1000)
    poupanca.sacar(200)
    poupanca.mostrarInfomacoesConta()

    # Rendimento mensal (5%)
    print('\n>>> Aplicando rendimento do mês 1')
    poupanca.rendimentoJuros()
    poupanca.mostrarInfomacoesConta()

    print('\n>>> Aplicando rendimento do mês 2')
    poupanca.rendimentoJuros()
    poupanca.mostrarInfomacoesConta()

    # Transferência da poupança para uma conta comum
    print('\n>>> Transferindo R$ 300 para a conta de John Wick')
    conta = Conta('John Wick', 1234, 7777)
    poupanca.transferir(300, conta)
    conta.mostrarInfomacoesConta()
    poupanca.mostrarInfomacoesConta()

    # Tentativas inválidas
    print('\n>>> Testando operações inválidas')
    poupanca.sacar(99999)
    poupanca.depositar(-10)


if __name__ == '__main__':
    main()
