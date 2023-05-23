#lista de dicionários
candidatos = [
    {'nome': 'João', 'resultado': 'e6_t10_p7_s9'},
    {'nome': 'Maria', 'resultado': 'e8_t7_p9_s8'},
    {'nome': 'José', 'resultado': 'e4_t6_p8_s7'},
    {'nome': 'Ana', 'resultado': 'e7_t9_p6_s9'},
    {'nome': 'Carlos', 'resultado': 'e6_t8_p8_s7'}
]

def verificar_criterio(candidato, criterio, nota):
    # Extrai as notas do resultado do candidato
    notas = candidato['resultado'].split('_')[1:]
    notas = [int(nota[1:]) for nota in notas]
    # Verifica se todas as notas do critério são maiores ou iguais à nota mínima
    return all(nota >= criterio for nota in notas)

def buscar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s):
    candidatos_selecionados = []
    for candidato in candidatos:
        # Verifica se o candidato atende a todos os critérios
        if (
            verificar_criterio(candidato, 'e', nota_e) and
            verificar_criterio(candidato, 't', nota_t) and
            verificar_criterio(candidato, 'p', nota_p) and
            verificar_criterio(candidato, 's', nota_s)
        ):
            # Adiciona o nome do candidato à lista de candidatos selecionados
            candidatos_selecionados.append(candidato['nome'])
    return candidatos_selecionados

def obter_nota_minima(mensagem):
    while True:
        try:
            nota = int(input(mensagem))
            # Verifica se a nota está no intervalo válido (0 a 10)
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

# Solicita ao usuário as notas mínimas desejadas
nota_e = obter_nota_minima("Informe a nota mínima desejada em entrevista: ")
nota_t = obter_nota_minima("Informe a nota mínima desejada em teste teórico: ")
nota_p = obter_nota_minima("Informe a nota mínima desejada em teste prático: ")
nota_s = obter_nota_minima("Informe a nota mínima desejada em avaliação de soft skills: ")

# Busca os candidatos que atendem aos critérios e armazena em uma lista
candidatos_selecionados = buscar_candidatos(candidatos, nota_e, nota_t, nota_p, nota_s)

# Imprime os candidatos selecionados
print("Candidatos selecionados:", candidatos_selecionados)
