# Define a lista de candidatos com seus resultados no processo seletivo
candidatos = [
    ('João', 8, 6, 7, 9),
    ('Maria', 8, 7, 9, 8),
    ('José', 4, 6, 8, 7),
    ('Ana', 7, 9, 6, 9),
    ('Carlos', 6, 8, 8, 7)
]

# Define a função que busca candidatos de acordo com critérios de nota
def buscar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s):
    candidatos_selecionados = []
    for candidato in candidatos:
        nome = candidato[0]
        nota_e_candidato = candidato[1]
        nota_t_candidato = candidato[2]
        nota_p_candidato = candidato[3]
        nota_s_candidato = candidato[4]
        if nota_e_candidato >= nota_e and nota_t_candidato >= nota_t and nota_p_candidato >= nota_p and nota_s_candidato >= nota_s:
            candidatos_selecionados.append(nome)
    return candidatos_selecionados

# Adiciona uma função auxiliar para verificar se uma nota é maior ou igual a 10
def nota_valida(nota):
    return isinstance(nota, int) and nota >= 0 and nota <= 10

# Pede ao usuário para informar as notas de corte desejadas e executa a pesquisa
while True:
    nota_e = int(input("Informe a nota mínima desejada em entrevista: "))
    nota_t = int(input("Informe a nota mínima desejada em teste teórico: "))
    nota_p = int(input("Informe a nota mínima desejada em teste prático: "))
    nota_s = int(input("Informe a nota mínima desejada em avaliação de soft skills: "))
    
    if nota_valida(nota_e) and nota_valida(nota_t) and nota_valida(nota_p) and nota_valida(nota_s):
        candidatos_selecionados = buscar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s)
        print("Candidatos selecionados: ", ", ".join(candidatos_selecionados))
        
        continuar = input("Deseja realizar outra pesquisa? (s/n) ")
        if continuar.lower() == "n":
            break
    else:
        print("Por favor, informe apenas notas válidas entre 0 e 10.")
