import datetime
from src.Estacionamento import Estacionamento

print("Bem vind& ao Trabalho Prático 1 - Test-Driven Development")
choice = -1

estacionamentos = [
    Estacionamento(
        valorFracao=30,
        valorHoraCheia=15,
        valorDiariaNoturna=45,
        valorDiariaDiurna=120,
        mensalidade=600,
        valorEvento=50,
        horarios=["06:00", "22:00", "19:00", "08:00", "19:00", "08:00"],
        capacidade=300,
        retorno=50,
    ),
    Estacionamento(
        valorFracao=20,
        valorHoraCheia=10,
        valorDiariaNoturna=30,
        valorDiariaDiurna=70,
        mensalidade=455,
        valorEvento=60,
        horarios=[
            "00:00",
            "00:00",
            "21:00",
            "07:00",
            "21:00",
            "07:00",
        ],
        capacidade=120,
        retorno=60,
    ),
    Estacionamento(
        valorFracao=10,
        valorHoraCheia=0,
        valorDiariaNoturna=40,
        valorDiariaDiurna=50,
        mensalidade=350,
        valorEvento=40,
        horarios=["06:00", "22:00", "20:00", "08:00", "20:00", "08:00"],
        capacidade=600,
        retorno=70,
    ),
]

while int(choice) != 0:
    print("1 - Adicionar estacionamento")
    print("2 - Adicionar acesso")
    print("3 - Valor apurado pelo contratante")
    print("0 - Sair")
    print("Selecione a opção desejado: ")
    choice = int(input())

    if choice == 0:
        break

    elif choice == 1:
        valorFracao = input("Insira o valor do acesso por fração de hora: ")
        valorHoraCheia = input(
            "Insira o percentual de desconto para acessos de hora cheia (Ex: 15): "
        )
        valorDiariaDiurna = input("Insira o valor do acesso para diária diurna: ")
        valorDiariaNoturna = input(
            "Insira o valor percentual do acesso para diária noturna (Ex: 15): "
        )
        mensalidade = input("Insira o valor do acesso por mensalidade: ")
        valorEvento = input("Insira o valor do acesso por evento: ")
        capacidade = input("Insira a capacidade de carros do estacionamento: ")
        retorno = input(
            "Insira o valor percentual de retorno ao contratante (Ex: 15): "
        )

        horarios = []
        horario = input("Insira o horário de abertura do estacionamento (hh:mm): ")
        horarios.append(horario)
        horario = input("Insira o horário de fechamento do estacionamento (hh:mm): ")
        horarios.append(horario)

        horario = input("Insira o horário que inicia o período noturno (hh:mm): ")
        horarios.append(horario)
        horario = input("Insira o horário que termina o período noturno (hh:mm): ")
        horarios.append(horario)

        horarios.append(horarios[2])
        horarios.append(horarios[3])

        novoEstacionamento = Estacionamento(
            valorFracao=valorFracao,
            valorHoraCheia=valorHoraCheia,
            valorDiariaNoturna=valorDiariaNoturna,
            valorDiariaDiurna=valorDiariaDiurna,
            retorno=retorno,
            capacidade=capacidade,
            valorEvento=valorEvento,
            mensalidade=mensalidade,
            horarios=horarios,
        )
        estacionamentos.append(novoEstacionamento)

    elif choice == 2:
        print("Selecione para qual estacionamento será adicionado o acesso: ")
        for index, item in enumerate(estacionamentos):
            print(index + 1, f" - Estacionamento {item.retorno}")

        estacionamentoEscolhido = int(input()) - 1

        placa = input("Insira a placa do veículo: ")
        horaInicio = input("Insira a hora do inicio: ")
        horaFinal = input("Insira a hora do final: ")
        estacionamentos[estacionamentoEscolhido].AddAcesso(placa, horaInicio, horaFinal)
        print("\n")
        print(
            f"O tempo de permanência para a {placa} foi {estacionamentos[estacionamentoEscolhido].FindTipoAcesso(placa)}"
        )
        print(
            f"O valor desse acesso foi: {estacionamentos[estacionamentoEscolhido].GetValorAcesso(placa)}\n"
        )

    elif choice == 3:
        print("Selecione para qual estacionamento você deseja ver o valor apurado: ")
        for index, item in enumerate(estacionamentos):
            print(index + 1, f" - Estacionamento {item.retorno}")

        estacionamentoEscolhido = int(input()) - 1
        print("\n")
        print(
            f"O valor apurado foi: {estacionamentos[estacionamentoEscolhido].GetTotalApurado()}\n"
        )
