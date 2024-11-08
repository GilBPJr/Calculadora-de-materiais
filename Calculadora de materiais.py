# Calculadora de Materiais
from math import ceil

def calcular_tijolos():
    print("\n===== CALCULAR A QUANTIDADE DE TIJOLOS =====\n")
    area_parede = float(input("Digite a area da parede(m²): "))
    comprimento_tijolo = 0.29 #metros
    altura_tijolo = 0.19 #metros
    area_tijolo = comprimento_tijolo * altura_tijolo
    qtd_tijolos_por_parede = (area_parede / area_tijolo)

    return print(f'Quantidade de tijolos necessária: {ceil(qtd_tijolos_por_parede)}',
                 f'\nQuantidade de tijolos considerando um deperdicio de 10%: {ceil(qtd_tijolos_por_parede + (qtd_tijolos_por_parede * 0.1))}')

def calcular_contrapiso():
    print("\n===== CALCULAR A QUANTIDADE DE CIMENTO PARA CONTRAPISO =====\n")
    area = float(input("Digite a area(m²): "))
    espessura = float(input("Digite a espessura do contrapiso(cm): "))
    proporção = 1 + 3 + 3 # 1 parte de cimento, 3 parte de areia e 3 parte de brita
    volume_contrapiso = area * (espessura/100) # Dividir por 100, pois a espessura será pedida em cm
    volume_cimento = volume_contrapiso * (1/proporção)
    desperdicio = volume_cimento + (volume_cimento * 0.1)
    volume_areia = ceil(volume_contrapiso * (3/proporção))
    volume_brita = volume_areia
    peso_por_m3 = 1400 # Considerando que 1m³ de cimento possui cerca de 1400 kg. (1400kg/m³)
    peso_saco_cimento = 50 # Um saco de cimento pesa 50 kg.
    qtd_sacos_cimento = ceil((volume_cimento * peso_por_m3) / peso_saco_cimento)
    qtd_cimento_deperdicio = ((desperdicio * peso_por_m3) / peso_saco_cimento)

    return print(f'Quantidade de sacos de cimento necessária: {qtd_sacos_cimento}',
                 f'\nQuantidade de areia: {ceil(volume_areia)} m³' ,
                 f'\nQuantidade de brita: {ceil(volume_brita)} m³',
                 f'\nQuantidade de sacos de cimento para um desperdicio de 10%: {ceil(qtd_cimento_deperdicio)}',
                 f'\nQuantida de areia com desperdicio de 10%: {ceil(volume_areia + (volume_areia * 0.1))} m³',
                 f'\nQuantida de areia com desperdicio de 10%: {ceil(volume_brita + (volume_brita * 0.1))} m³')

def calcular_reboco():
    print("\n===== CALCULAR A QUANTIDADE DE CIMENTO PARA REBOCO =====\n")
    area_parede = float(input("Digite a area da parede(m²): "))
    espessura = float(input("Digite a espessura do reboco(cm): "))
    proporção = 1 + 4 # 1 parte de cimento, 4 partes de areia
    volume_reboco = area_parede * (espessura / 100)
    volume_cimento = volume_reboco * (1/proporção)
    desperdicio = volume_cimento + (volume_cimento * 0.1)
    volume_areia = volume_reboco * (4/proporção)
    peso_por_m3 = 1400 # Considerando que 1m³ de cimento possui cerca de 1400 kg. (1400kg/m³)
    peso_saco_cimento = 50 # Um saco de cimento pesa 50 kg
    qtd_saco_cimento = (volume_cimento * peso_por_m3) / peso_saco_cimento
    qtd_cimento_deperdicio = ((desperdicio * peso_por_m3) / peso_saco_cimento)

    return print(f'Quantidade de sacos de cimento: {ceil(qtd_saco_cimento)}',
            f'\nQuantidade de areia: {ceil(volume_areia)} m³',
            f'\nQuantidade de sacos de cimento para um desperdicio de 10%: {ceil(qtd_cimento_deperdicio)}',
            f'\nQuantidade de areia com desperdicio de 10%: {ceil(volume_areia + (volume_areia * 0.1))} m³' )

def calcular_tinta():
    print("\n===== CALCULAR A QUANTIDADE DE TINTA =====\n")
    area = float(input("Digite a area a ser pintada(m²): "))
    rendimento = float(input("Digite o redimento da tinta: "))
    qtd_tinta = area * rendimento # Rendimento da tinta por litro
    return print(f'Quantidade de tinta necessária(m²/l): {qtd_tinta} litros')

def info():
    print("\n===== INFORMAÇÕES IMPORTANTES =====\n",
          "\n1) Dimensões do tijolo utilizado como padrão (largura × altura × comprimento): 9 cm × 19 cm × 29 cm",
          "\n2) Proporção utlizada para o cálculo do contrapiso: 1:3:3 ",
          "\n3) Proporção utilizada para o cálculo do reboco: 1:4",
          "\n4) Para o cálculo da quantidade de sacos de cimento considera-se que",
          "1 m³ de cimento possui 1400kg e que um saco de cimento possui 50kg",
          "\n5) Todos os valores são estimados acima do cálculo real")

def menu():
    print("  \n===== CALCULADORA DE MATERIAIS =====")
    print("\nDigite [1] Quantidade de tijolos",
          "\nDigite [2] Quantidade de cimento para contrapiso",
          "\nDigite [3] Quantidade de cimento para reboco",
          "\nDigite [4] Quantidade de tinta.",
          "\nDigite [5] Informações sobre a calculadora",
          "\nDigite [0] para sair.")

    while True:
      try:
        i = int(input("Escolha o tipo de cálculo:  "))

        if i == 1:
          return calcular_tijolos()
        elif i == 2:
          return calcular_contrapiso()
        elif i == 3:
          return calcular_reboco()
        elif i == 4:
          return calcular_tinta()
        elif i == 5:
          return info()
        elif i == 0:
          break
        else:
          print("Número inválido. Por favor tente novamente.")
          continue
        break

      except ValueError:
        print("Valor inválido. Por favor tente novamente.")

# Corpo principal do programa

menu()
while True:
    i = input("\nDeseja continuar [s/n]? ").strip().lower()

    if i not in ('s', 'n'):
        print("Entrada inválida. Por favor, digite 's' para continuar ou 'n' para sair.")
        continue
    elif i == 'n':
        print("\nFim do programa")
        break

    menu()