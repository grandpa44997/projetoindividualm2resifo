# Isso é uma lista de dicionários de candidatos com seus resultados no processo seletivo
candidatos = [
    {'nome': 'João', 'resultado': 'e10_t10_p10_s10'},
    {'nome': 'Maria', 'resultado': 'e8_t7_p9_s8'},
    {'nome': 'José', 'resultado': 'e4_t6_p8_s7'},
    {'nome': 'Ana', 'resultado': 'e7_t9_p6_s9'},
    {'nome': 'Carlos', 'resultado': 'e6_t8_p8_s7'}
]

def verificar_criterio(candidato, etapa, criterio):
    # Obtém o resultado do candidato atual na forma de uma string
    resultado = candidato['resultado']
    # Extrai as notas de cada etapa do resultado do candidato atual e as converte em inteiros
    notas = [int(nota[1:]) for nota in resultado.split('_') if nota.startswith(etapa)]
    # Verifica se todas as notas do critério atual são maiores ou iguais ao critério desejado
    return all(nota >= criterio for nota in notas)

def buscar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s):
    # Cria uma lista vazia para armazenar os candidatos selecionados
    candidatos_selecionados = []
    # Itera sobre cada candidato na lista de candidatos fornecida
    for candidato in candidatos:
        # Verifica se o candidato atual atende a todos os critérios
        if (verificar_criterio(candidato, 'e', nota_e) and
            verificar_criterio(candidato, 't', nota_t) and
            verificar_criterio(candidato, 'p', nota_p) and
            verificar_criterio(candidato, 's', nota_s)):
            # Adiciona o nome do candidato atual à lista de candidatos selecionados
            candidatos_selecionados.append(candidato['nome'])
    # Retorna a lista de candidatos selecionados
    return candidatos_selecionados

# Pede ao usuário para informar as notas de corte desejadas
nota_e = int(input("Informe a nota mínima desejada em entrevista: "))
nota_t = int(input("Informe a nota mínima desejada em teste teórico: "))
nota_p = int(input("Informe a nota mínima desejada em teste prático: "))
nota_s = int(input("Informe a nota mínima desejada em avaliação de soft skills: "))

# Chama a função com as notas de corte informadas pelo usuário e imprime o resultado
candidatos_selecionados = buscar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s)
print("Candidatos selecionados:", candidatos_selecionados)
