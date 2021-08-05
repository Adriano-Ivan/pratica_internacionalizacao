import locale
locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
valor_em_dolar_formatado = locale.currency(15000.0567, grouping=True, symbol=True, international=True)
print(valor_em_dolar_formatado)

locale.setlocale(locale.LC_MONETARY, 'pt_PT.UTF-8')

def converte_real_para_euro(valor_em_real):
    valor_em_euro = valor_em_real / 6.16
    return locale.currency(valor_em_euro, grouping=True, symbol=True, international=True)
    pass

valor_inicial_em_real = 50.0
valor_convertido_em_euro = converte_real_para_euro(valor_inicial_em_real)
print(valor_convertido_em_euro)
# valor_em_euro_texto = str(valor_convertido_em_euro).replace('.',',')
# valor_em_euro_formatado = f'{valor_em_euro_texto} €'
# print(valor_em_euro_formatado)