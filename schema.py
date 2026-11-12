import csv


class Imovel:
    def __init__(self, tipo, quartos, vagas, criancas,
                 aluguel, valor_quarto, valor_vaga, desconto):
        self.tipo = tipo
        self.quartos = quartos
        self.vagas = vagas
        self.criancas = criancas
        self.aluguel = aluguel
        self.valor_quarto = valor_quarto
        self.valor_vaga = valor_vaga
        self.desconto = desconto

    def apresentar_imovel(self, total):
        print('\n===== Resumo do orçamento =====')
        print('Tipo de imóvel:', self.tipo)
        print('Quantidade de quartos:', self.quartos)
        print('Quantidade de vagas:', self.vagas)
        print('Possui crianças:', 'Sim' if self.criancas == 's' else 'Não')
        print(f'Aluguel-base: R$ {self.aluguel:.2f}')
        print(f'Adicional de quartos: R$ {self.valor_quarto:.2f}')
        print(f'Vagas de garagem: R$ {self.valor_vaga:.2f}')
        print(f'Desconto: - R$ {self.desconto:.2f}')
        print(f'Total mensal: R$ {total:.2f}')


class Contrato:
    TAXA = 2000

    def __init__(self, parcelas):
        self.parcelas = parcelas

    def calcular_parcela(self):
        return self.TAXA / self.parcelas

    def apresentar_contrato(self):
        print('\n===== Taxa contratual =====')
        print(f'Taxa contratual: R$ {self.TAXA:.2f}')
        print(f'Parcelas: {self.parcelas}x de R$ {self.calcular_parcela():.2f}')

    def gerar_csv(self, total_mensal, arquivo='projecao_12_meses.csv'):
        valor_parcela = self.calcular_parcela()
        with open(arquivo, 'w', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f, delimiter=';')
            escritor.writerow(['Mês', 'Aluguel mensal',
                               'Parcela da taxa', 'Total do mês'])
            for mes in range(1, 13):
                if mes <= self.parcelas:
                    parcela = valor_parcela
                else:
                    parcela = 0
                escritor.writerow([mes, f'{total_mensal:.2f}',
                                   f'{parcela:.2f}',
                                   f'{total_mensal + parcela:.2f}'])
        return arquivo