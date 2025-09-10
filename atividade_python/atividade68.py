import re
from datetime import datetime


alunos = {}
contador_matricula = 1000


def validar_nome(nome):
    return bool(nome.strip())

def validar_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def gerar_matricula():
    global contador_matricula
    contador_matricula += 1
    return f"A{contador_matricula}"

def cadastrar_aluno():
    nome = input("Nome: ").strip()
    email = input("E-mail: ").strip()
    data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()

    if not validar_nome(nome):
        print(" Nome inválido.")
        return
    if not validar_email(email):
        print(" E-mail inválido.")
        return
    if not validar_data(data_nasc):
        print(" Data de nascimento inválida.")
        return

    matricula = gerar_matricula()
    alunos[matricula] = {
        "nome": nome,
        "email": email,
        "data_nasc": data_nasc,
        "matricula": matricula
    }
    print(f" Aluno cadastrado com matrícula: {matricula}")


def atualizar_aluno():
    matricula = input("Digite a matrícula do aluno a ser atualizado: ").strip()
    if matricula not in alunos:
        print(" Matrícula não encontrada.")
        return

    print("Deixe em branco para manter o valor atual.")
    nome = input("Novo nome: ").strip()
    email = input("Novo e-mail: ").strip()
    data_nasc = input("Nova data de nascimento (DD/MM/AAAA): ").strip()

    if nome and validar_nome(nome):
        alunos[matricula]["nome"] = nome
    if email and validar_email(email):
        alunos[matricula]["email"] = email
    if data_nasc and validar_data(data_nasc):
        alunos[matricula]["data_nasc"] = data_nasc

    print(f" Dados do aluno {matricula} atualizados.")

def remover_aluno():
    matricula = input("Digite a matrícula do aluno a ser removido: ").strip()
    if matricula in alunos:
        del alunos[matricula]
        print(f" Aluno {matricula} removido.")
    else:
        print(" Matrícula não encontrada.")

def listar_alunos():
    if not alunos:
        print(" Nenhum aluno cadastrado.")
        return
    print("\n Lista de alunos:")
    for aluno in alunos.values():
        print("-" * 30)
        print(f"Nome: {aluno['nome']}")
        print(f"E-mail: {aluno['email']}")
        print(f"Data de nascimento: {aluno['data_nasc']}")
        print(f"Matrícula: {aluno['matricula']}")
    print("-" * 30)


def mostrar_aluno_por_matricula():
    matricula = input("Digite a matrícula do aluno: ").strip()
    aluno = alunos.get(matricula)
    if aluno:
        print("\n📌 Dados do aluno:")
        print(f"Nome: {aluno['nome']}")
        print(f"E-mail: {aluno['email']}")
        print(f"Data de nascimento: {aluno['data_nasc']}")
        print(f"Matrícula: {aluno['matricula']}")
    else:
        print(" Matrícula não encontrada.")

# Menu principal
def menu():
    while True:
        print("\n Sistema de Cadastro de Alunos")
        print("1 - Cadastrar aluno")
        print("2 - Atualizar aluno")
        print("3 - Remover aluno")
        print("4 - Listar todos os alunos")
        print("5 - Mostrar dados de um aluno por matrícula")
        print("Outro - Encerrar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_aluno()
        elif opcao == "2":
            atualizar_aluno()
        elif opcao == "3":
            remover_aluno()
        elif opcao == "4":
            listar_alunos()
        elif opcao == "5":
            mostrar_aluno_por_matricula()
        else:
            print(" Encerrando o sistema.")
            break


menu()