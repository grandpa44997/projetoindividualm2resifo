# Isso é uma lista de dicionários de candidatos com seus resultados no processo seletivo
candidatos = [
    {'nome': 'João', 'resultado': 'e6_t8_p7_s9'},
    {'nome': 'Maria', 'resultado': 'e8_t7_p9_s8'},
    {'nome': 'José', 'resultado': 'e4_t6_p8_s7'},
    {'nome': 'Ana', 'resultado': 'e7_t9_p6_s9'},
    {'nome': 'Carlos', 'resultado': 'e6_t8_p8_s7'}
]
def buscar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s):
    # cria uma lista vazia para armazenar os candidatos selecionados
    candidatos_selecionados = []
    # itera sobre cada candidato na lista de candidatos fornecida
    for candidato in candidatos:
        # obtém o resultado do candidato atual na forma de uma string
        resultado = candidato['resultado']
        # extrai as notas de cada etapa do resultado do candidato atual e as converte em inteiros
        nota_e_candidato = int(resultado[1])
        nota_t_candidato = int(resultado[4])
        nota_p_candidato = int(resultado[7])
        nota_s_candidato = int(resultado[10])
        # verifica se as notas de cada etapa do candidato atual são maiores ou iguais às notas de corte fornecidas
        if nota_e_candidato >= nota_e and nota_t_candidato >= nota_t and nota_p_candidato >= nota_p and nota_s_candidato >= nota_s:
            # adiciona o nome do candidato atual à lista de candidatos selecionados
            candidatos_selecionados.append(candidato['nome'])
    # retorna a lista de candidatos selecionados
    return candidatos_selecionados

# Pede ao usuário para informar as notas de corte desejadas
nota_e = int(input("Informe a nota mínima desejada em entrevista: "))
nota_t = int(input("Informe a nota mínima desejada em teste teórico: "))
nota_p = int(input("Informe a nota mínima desejada em teste prático: "))
nota_s = int(input("Informe a nota mínima desejada em avaliação de soft skills: "))

# Chama a função com as notas de corte informadas pelo usuário e imprime o resultado
candidatos_selecionados = buscar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s)
print("Candidatos selecionados:", candidatos_selecionados)
