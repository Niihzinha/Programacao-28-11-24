import os
import time

def carregar_estoque():
    try:
        with open("estoque\\estoque_carros.txt", "r") as arquivo:
            return [linha.strip().split(",") for linha in arquivo]
    except FileNotFoundError:
        return []

def salvar_estoque(estoque):
    with open("estoque\\estoque_carros.txt", "w") as arquivo:
        for carro in estoque:
            arquivo.write(",".join(carro) + "\n")

def menu_interativo():
    estoque = carregar_estoque()

    while True:
        print("\n======= MENU PRINCIPAL =======")
        print("1 - Cadastrar um novo carro")
        print("2 - Pesquisar carros")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()
        time.sleep(0.5)

    
        if opcao == "1":
            cadastrar_carro(estoque)
            salvar_estoque(estoque)
        elif opcao == "2":
            realizar_pesquisa(estoque)
        elif opcao == "0":
            print("OK, até a próxima!"); break
        
        else:
            print("Opção inválida.")
        time.sleep(0.5)



def cadastrar_carro(estoque):
    nome = input("Informe o nome do carro: ").strip()
    preco = input("Informe o preço do carro: ").strip()
    ano = input("Informe o ano de fabricação: ").strip()
    estado = input("Informe o estado do carro (ex.: novo, seminovo, conservado e mal estado): ").strip()
    estoque.append([nome, preco, ano, estado])
    print("Carro cadastrado!")
    time.sleep(0.5)


def realizar_pesquisa(estoque):
    filtro = input("Preço máximo ou estado do carro: ").strip()
    try:
        filtro = float(filtro)
        resultado = [c for c in estoque if float(c[1]) <= filtro]
    except ValueError:
        resultado = [c for c in estoque if c[3].lower() == filtro.lower()]
        time.sleep(0.5)
    if resultado:
        for c in resultado:
            print(f"Nome: {c[0]}, Preço: R${c[1]}, Ano: {c[2]}, Estado: {c[3]}")
    else:
        print("Nenhum carro encontrado.")
        time.sleep(0.5)

menu_interativo()
