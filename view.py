from controller import (
    calcular_desconto_criancas,
    calcular_valor_vaga,
    calcular_valor_quarto,
    calcular_total
)
from schema import Imovel, Contrato


def ler_inteiro(mensagem):
    try:
        return int(input(mensagem))
    except ValueError:
        print('Digite apenas números!')
        exit()


print('=== RENTSMART - R.M. IMÓVEIS ===')
print('1 - Apartamento (R$ 700,00)')
print('2 - Casa (R$ 900,00)')
print('3 - Estúdio (R$ 1.200,00)')

opcao = input('Escolha o tipo de imóvel: ')

if opcao == '1':
    tipo = 'Apartamento'
    aluguel = 700
elif opcao == '2':
    tipo = 'Casa'
    aluguel = 900
elif opcao == '3':
    tipo = 'Estúdio'
    aluguel = 1200
else:
    print('Opção inválida!')
    exit()

quartos = 1
if tipo == 'Apartamento' or tipo == 'Casa':
    quartos = ler_inteiro('Informe a quantidade de quartos (1 ou 2): ')
    if quartos < 1 or quartos > 2:
        print('Quantidade indisponível')
        exit()

criancas = input('Possui crianças? (s/n): ').lower()
if criancas != 's' and criancas != 'n':
    print('Opção inválida')
    exit()

vagas = ler_inteiro('Informe a quantidade de vagas: ')
if vagas < 0:
    print('Quantidade inválida')
    exit()
if tipo != 'Estúdio' and vagas > 2:
    print('Casas e apartamentos aceitam no máximo 2 vagas')
    exit()

parcelas = ler_inteiro('Parcelas da taxa contratual (1 a 5): ')
if parcelas < 1 or parcelas > 5:
    print('Quantidade de parcelas inválida!')
    exit()

valor_quarto = calcular_valor_quarto(tipo, quartos)
valor_vaga = calcular_valor_vaga(vagas, tipo)
desconto = calcular_desconto_criancas(tipo, aluguel, valor_quarto, criancas)
total = calcular_total(aluguel, valor_quarto, valor_vaga, desconto)

imovel = Imovel(tipo, quartos, vagas, criancas,
                aluguel, valor_quarto, valor_vaga, desconto)
contrato = Contrato(parcelas)

imovel.apresentar_imovel(total)
contrato.apresentar_contrato()

arquivo = contrato.gerar_csv(total)
print('\nArquivo gerado:', arquivo)

