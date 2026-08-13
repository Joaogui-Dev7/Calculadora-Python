def calc():
    while True:
        print()
        print("Calculadora Simples")
        print()
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("S. Sair")
        print()

        opcao = input("Escolha uma operação ou S para sair: ")

        if opcao == 's' or opcao == 'S':
            break

        if opcao in ['1', '2', '3', '4']:

            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if opcao == '1':
                result = num1 + num2
                print("A soma é:", result)

            elif opcao == '2':
                result = num1 - num2
                print("A subtração é:", result)

            elif opcao == '3':
                result = num1 * num2
                print("A multiplicação é:", result)

            elif opcao == '4':
                if num2 != 0:
                    result = num1 / num2
                    print("A divisão é:", result)
                else:
                    print("Divisão por 0 é inválida!")

        else:
            print("Opção inválida!")

calc()