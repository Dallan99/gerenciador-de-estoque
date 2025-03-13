import sqlite3

# Conectar ao banco de dados (se não existir, será criado)
conn = sqlite3.connect('motos.db')
cursor = conn.cursor()

# Criar a tabela de Motos (se não existir)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Motos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    marca TEXT,
    modelo TEXT,
    ano INTEGER,
    cor TEXT,
    placa TEXT,
    valor REAL,
    status TEXT
)
''')

# Função para adicionar uma nova moto ao estoque
def adicionar_moto():
    marca = input("Digite a marca da moto: ")
    modelo = input("Digite o modelo da moto: ")
    ano = int(input("Digite o ano da moto: "))
    cor = input("Digite a cor da moto: ")
    placa = input("Digite a placa da moto: ")
    valor = float(input("Digite o valor da moto: "))

    cursor.execute('''
    INSERT INTO Motos (marca, modelo, ano, cor, placa, valor, status) 
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (marca, modelo, ano, cor, placa, valor, 'Disponível'))
    conn.commit()

    print("Moto adicionada com sucesso!")

# Função para listar todas as motos no estoque
def consultar_estoque():
    cursor.execute('''
    SELECT * FROM Motos
    ''')
    motos = cursor.fetchall()
    if motos:
        print("\nEstoque de Motos:")
        for moto in motos:
            status = moto[7] if moto[7] else 'Indefinido'
            print(f"ID: {moto[0]}, Marca: {moto[1]}, Modelo: {moto[2]}, Ano: {moto[3]}, Cor: {moto[4]}, Placa: {moto[5]}, Valor: R$ {moto[6]:.2f}, Status: {status}")
    else:
        print("\nEstoque Vazio. Inclua novas motos.")

# Função para registrar uma venda
def registrar_venda():
    consultar_estoque()
    moto_id = int(input("\nDigite o ID da moto que foi vendida: "))
    cursor.execute('''
    SELECT * FROM Motos WHERE id = ?
    ''', (moto_id,))
    moto = cursor.fetchone()

    if moto:
        status = moto[7]
        if status == 'Vendida':
            print("Esta moto já foi vendida.")
            return

        print(f"\nVocê selecionou a moto: {moto[1]} {moto[2]}, {moto[3]} - {moto[4]}, Placa: {moto[5]}, Valor: R$ {moto[6]:.2f}")
        desistir = input("Deseja desistir da venda? (1 - Sim, 2 - Não): ")

        if desistir == '1':
            print("Venda cancelada. Voltando ao menu principal.")
            return

        # Registrar os dados da venda
        responsavel = input("Digite o responsável pela venda: ")
        comprador = input("Digite o nome do comprador: ")
        valor_atpv = float(input("Digite o valor da ATPV: "))
        custo_moto = float(input("Digite o custo da moto: "))
        valor_total = float(input("Digite o valor total da venda: "))
        lucro_loja = valor_total - custo_moto
        sinal = float(input("Digite o valor do sinal: "))
        primeira = float(input("Digite o valor da primeira parcela: "))
        segunda = float(input("Digite o valor da segunda parcela: "))
        terceira = float(input("Digite o valor da terceira parcela: "))
        quarta = float(input("Digite o valor da quarta parcela: "))
        falta = float(input("Digite o valor da falta: "))
        pagamento_ok = input("Pagamento ok? (Sim/Não): ")
        pagamento_consignante = input("Pagamento ao consignante? (Sim/Não): ")

        cursor.execute('''
        UPDATE Motos
        SET status = 'Vendida'
        WHERE id = ?
        ''', (moto_id,))
        conn.commit()

        print(f"\nVenda registrada com sucesso para {comprador}!")

        # Exibir o resumo da venda
        print(f"\nResumo da Venda:")
        print(f"Responsável pela venda: {responsavel}")
        print(f"Comprador: {comprador}")
        print(f"Valor da ATPV: R$ {valor_atpv:.2f}")
        print(f"Custo da Moto: R$ {custo_moto:.2f}")
        print(f"Valor Total da Venda: R$ {valor_total:.2f}")
        print(f"Lucro da Loja: R$ {lucro_loja:.2f}")
        print(f"Sinal: R$ {sinal:.2f}")
        print(f"Primeira Parcela: R$ {primeira:.2f}")
        print(f"Segunda Parcela: R$ {segunda:.2f}")
        print(f"Terceira Parcela: R$ {terceira:.2f}")
        print(f"Quarta Parcela: R$ {quarta:.2f}")
        print(f"Falta: R$ {falta:.2f}")
        print(f"Pagamento Ok: {pagamento_ok}")
        print(f"Pagamento ao Consignante: {pagamento_consignante}")

# Função para menu principal
def menu():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Adicionar Moto")
        print("2. Consultar Estoque")
        print("3. Registrar Venda")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_moto()
        elif opcao == '2':
            consultar_estoque()
        elif opcao == '3':
            registrar_venda()
        elif opcao == '4':
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chamada para o menu principal
menu()

# Fechar a conexão ao banco de dados
conn.close()
