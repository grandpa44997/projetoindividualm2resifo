candidatos = [
    ('João', 8, 6, 7, 9),
    ('Maria', 8, 7, 9, 8),
    ('José', 4, 6, 8, 7),
    ('Ana', 7, 9, 6, 9),
    ('Carlos', 6, 8, 8, 7)
]

def buscar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s):
    # Lista para armazenar os candidatos selecionados
    candidatos_selecionados = []
    
    for candidato in candidatos:
        # Extrai as informações do candidato
        nome = candidato[0]
        nota_e_candidato = candidato[1]
        nota_t_candidato = candidato[2]
        nota_p_candidato = candidato[3]
        nota_s_candidato = candidato[4]
        
        # Verifica se o candidato atende aos critérios de nota mínima
        if (nota_e_candidato >= nota_e and
            nota_t_candidato >= nota_t and
            nota_p_candidato >= nota_p and
            nota_s_candidato >= nota_s):
            # Adiciona o nome do candidato à lista de selecionados
            candidatos_selecionados.append(nome)
    
    # Retorna a lista de candidatos selecionados
    return candidatos_selecionados

def nota_valida(nota):
    # Verifica se a nota é um número inteiro válido entre 0 e 10
    return isinstance(nota, int) and 0 <= nota <= 10

while True:
    # Solicita ao usuário as notas mínimas desejadas para cada categoria
    nota_e = int(input("Informe a nota mínima desejada em entrevista: "))
    nota_t = int(input("Informe a nota mínima desejada em teste teórico: "))
    nota_p = int(input("Informe a nota mínima desejada em teste prático: "))
    nota_s = int(input("Informe a nota mínima desejada em avaliação de soft skills: "))

    # Verifica se todas as notas informadas são válidas
    if (nota_valida(nota_e) and nota_valida(nota_t) and
        nota_valida(nota_p) and nota_valida(nota_s)):
        
        # Chama a função para buscar os candidatos que atendem aos critérios de nota
        candidatos_selecionados = buscar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s)
        
        # Imprime a lista de candidatos selecionados
        print("Candidatos selecionados: ", ", ".join(candidatos_selecionados))
        
        # Pergunta ao usuário se deseja realizar outra pesquisa
        continuar = input("Deseja realizar outra pesquisa? (s/n) ")
        
        if continuar.lower() == "n":
            break
    else:
        # Informa ao usuário que as notas informadas são inválidas
        print("Por favor, informe apenas notas válidas entre 0 e 10.")
