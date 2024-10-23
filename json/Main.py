import pyodbc
import pandas as pd

try:
    server = 'localhost'
    database = 'petshop'
    username = 'sa'
    password = '*123456HAS*'
    conn = pyodbc.connect('DRIVER={SQL Server}; SERVER=;DATABASE='+database+';UID='+username+';PWD='+password)
    inst_cadastro = conn.cursor()
    inst_consulta= conn.cursor()
except Exception as e:
    print("Erro", e)
    conexao = False
else:
    conexao = True
    print("Conexão efetuada com sucesso! ")
while conexao:
    print("""
    0 => sair
    1 => cadastrar pets 
    2 => listar
    """)

    escolha = int(input("Escolha: "))
    match escolha:
        case 0:
            conexao = False
        case 1:
            try:
                tipo = input("Tipo.........!")
                nome = input("Nome.........!")
                idade = int(input("idade........!"))

                cadastro = f"""
                            INSERT INTO petshop (tipo_pet, nome_pet, idade)
                            VALUES('{tipo}', '{nome}', '{idade}')
                            """
                inst_cadastro.execute(cadastro)
                conn.commit()
            except ValueError:
                print("Digite uma idade numerica")
            except:
                print("Erro em alguma coisa que eu não sei ")
            else:
                print("Dados gravados com sucesso! ")
        case 2:
            lista_dados = []
            inst_consulta.execute("SELECT * FROM petshop")
            data = inst_consulta.fetchall()

            for dt in data:
                lista_dados.append(dt)

            dados_df = pd.DataFrame.from_records(lista_dados, columns=['Id', 'Tipo', 'Nome', 'Idade'], index='Id')
            if dados_df.empty:
                print("Nao ha pets cadastrados")
            else:
                print(dados_df)
            input("Pressione algo para continuar...........")




