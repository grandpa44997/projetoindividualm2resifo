# projetoindividualm2resifo
projeto individual de busca de candidatos por nota de corte de varias habilidades
problema: Uma startup está desenvolvendo um aplicativo que verifica a compatibilidade
de um candidato com uma vaga de acordo com seu resultado nas etapas do
processo seletivo.
Para isso foi criado um teste que devolve uma string no seguinte formato:
eX_tX_pX_sX (sendo que cada X é substituído pela avaliação da pessoa em
uma das etapas do processo - entrevista, teste teórico, teste prático e
avaliação de soft skills)

o que fazer:
Criar com Python uma lista para armazenar esses resultados
(e outros resultados que quiser no mesmo formato, o código
precisa funcionar para qualquer lista que seja inserida nesse
formato) e depois uma função que busca o candidato de
acordo com os critérios digitados pelo usuário.
Entrega: deverá ser realizada em um único arquivo .py (que
será entregue em um repositório do Github).

como fazer:
Temos uma lista de candidatos como exemplo e os resultados: por favor gere exemplos
Você deve criar com Python uma lista para armazenar esses resultados
(e outros resultados que quiser no mesmo formato, o código precisa
funcionar para qualquer lista que seja inserida nesse formato) e depois
uma função que busca o candidato de acordo com os critérios
digitados pelo usuário. O usuário vai informar qual a nota mínima de e,
t, p e s que ele deseja buscar, nossa aplicação deve listar quem são os
candidatos disponíveis com nota maior ou igual a essas informadas
pelo usuário.
⇨ Ao buscar por alguém com resultados 4,4,8,8 por exemplo vamos
receber que os candidatos 1 e 5 atendem esse critério, foram bem no
teste prático e apresentaram um ótimo nível de soft skills!

Sistema de Seleção de Candidatos

Este é um sistema simples de seleção de candidatos com base em critérios de notas mínimas em diferentes etapas de um processo seletivo. Ele permite que você informe as notas mínimas desejadas em cada critério e retorna os candidatos que atendem a esses critérios.
Como usar

    Certifique-se de ter o Python instalado em sua máquina.

    Faça o download ou clone este repositório.

    Abra um terminal ou prompt de comando e navegue até o diretório do projeto.

    Execute o arquivo main.py com o comando:

    css

    python main.py

    Siga as instruções apresentadas no terminal para informar as notas mínimas desejadas em cada critério (entrevista, teste teórico, teste prático e avaliação de soft skills).

    Após inserir todas as notas, o sistema irá mostrar os candidatos que atendem aos critérios informados.

Observações

    Certifique-se de que o arquivo main.py e o arquivo de dados candidatos estejam no mesmo diretório.

    As notas mínimas devem estar no intervalo de 0 a 10.

    O arquivo de dados candidatos contém uma lista de dicionários, onde cada dicionário representa um candidato com seu nome e resultados nas diferentes etapas do processo seletivo. Caso queira adicionar novos candidatos ou modificar os resultados existentes, edite o arquivo candidatos diretamente.

    Lembre-se de seguir as instruções exibidas no terminal para inserir as notas mínimas corretamente.

    Os resultados serão exibidos no terminal após inserir todas as notas mínimas.

    Caso queira executar o sistema novamente, basta executar novamente o arquivo main.py e seguir as instruções.

Melhorias Futuras

    Possibilitar a leitura dos dados dos candidatos a partir de um arquivo externo, como um arquivo CSV, para facilitar a inclusão e modificação dos candidatos.

    Implementar tratamento de erros mais robusto para lidar com entradas inválidas do usuário, como letras em vez de números.

    Adicionar recursos de ordenação ou classificação dos candidatos selecionados com base em outros critérios, como ordem alfabética.

    Aprimorar a interface do usuário, por exemplo, usando uma interface gráfica em vez de apenas o terminal.

    Implementar testes automatizados para garantir o funcionamento correto do sistema.

    Contribuições e sugestões são bem-vindas!
