import random

print("==================================================")
print("GURGEL")
print("Sistema Inteligente para Eletropostos")
print("==================================================")

# Energia solar simulada

energia = random.randint(50, 120)

print("\nEnergia solar disponível:", energia, "kW")

# Veículos conectados

carros = [
    {"nome": "Carro A", "bateria": random.randint(10, 100)},
    {"nome": "Carro B", "bateria": random.randint(10, 100)},
    {"nome": "Carro C", "bateria": random.randint(10, 100)},
    {"nome": "Carro D", "bateria": random.randint(10, 100)}
]

print("\nVeículos conectados:")

for carro in carros:
    print(carro["nome"], "-", carro["bateria"], "%")

# Encontrar o carro com menor bateria

menor = carros[0]

for carro in carros:
    if carro["bateria"] < menor["bateria"]:
        menor = carro

print("\nAnálise da IA:")

print(
    "O veículo com maior prioridade é",
    menor["nome"],
    "pois possui apenas",
    menor["bateria"],
    "% de bateria."
)

# Distribuição de energia

print("\nDistribuição de potência:")

energia_restante = energia

for carro in carros:

    if carro["bateria"] < 30:
        carga = 35

    elif carro["bateria"] < 60:
        carga = 25

    else:
        carga = 15

    if carga > energia_restante:
        carga = energia_restante

    energia_restante = energia_restante - carga

    print(carro["nome"], "recebeu", carga, "kW")

# Tarifação dinâmica

print("\nTarifação dinâmica:")

if energia < 70:
    preco = 2.00
    situacao = "Alta demanda"

else:
    preco = 1.20
    situacao = "Demanda normal"

print("Situação:", situacao)
print("Preço:", "R$", preco, "/kWh")

# Relatório

print("\nRELATÓRIO FINAL")

print("Energia solar gerada:", energia, "kW")
print("Energia restante:", energia_restante, "kW")
print("Preço atual:", "R$", preco, "/kWh")

print("\nProjeto desenvolvido como prova de conceito da Gurgel.")
print("Automação + Inteligência Artificial + Energia Renovável")


print("\nSIMULAÇÃO DO DIA")

periodos = ["Manhã", "Tarde", "Noite"]

for periodo in periodos:

    print("\nPeríodo:", periodo)

    if periodo == "Manhã":
        energia = 60

    elif periodo == "Tarde":
        energia = 120

    else:
        energia = 30

    print("Energia solar:", energia, "kW")

    if energia < 50:
        print("Atenção: baixa geração de energia.")
        print("Tarifa dinâmica ativada.")

    else:
        print("Energia suficiente para operação normal.")


economia = energia * 0.4

print("\nImpacto Sustentável")
print("Energia renovável utilizada:", energia, "kW")
print("Economia estimada:", economia, "kg de CO2")
