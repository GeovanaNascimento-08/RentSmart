def calcular_valor_quarto(tipo, quartos):
    if quartos == 2:
        if tipo == 'Apartamento':
            return 200
        elif tipo == 'Casa':
            return 250
    return 0


def calcular_valor_vaga(vagas, tipo):
    if tipo == 'Apartamento' or tipo == 'Casa':
        return vagas * 300
    elif tipo == 'Estúdio':
        if vagas == 0:
            return 0
        elif vagas <= 2:
            return 250
        else:
            return 250 + (vagas - 2) * 60
    return 0


def calcular_desconto_criancas(tipo, aluguel, valor_quarto, criancas):
    if tipo == 'Apartamento' and criancas == 'n':
        return (aluguel + valor_quarto) * 0.05
    return 0


def calcular_total(aluguel, valor_quarto, valor_vaga, desconto):
    return aluguel + valor_quarto + valor_vaga - desconto