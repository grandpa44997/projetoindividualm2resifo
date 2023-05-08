# Define a lista de candidatos com seus resultados no processo seletivo
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
