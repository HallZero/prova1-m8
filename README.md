# prova1-m8

## Atividade prática
Você está desenvolvendo um sistema de atendimento ao cliente automatizado em Python, que utiliza processamento de linguagem natural e expressões regulares para identificar a intenção dos usuários e fornecer respostas automáticas às suas perguntas. O sistema deve funcionar através do terminal, processando as entradas (comandos) do usuário e exibindo as respostas apropriadas.


Implemente em Python um sistema simples que realiza as seguintes ações:
1. Recebe um comando do usuário por meio do terminal.
2. Identifica a intenção do usuário baseando-se na entrada, utilizando expressões regulares.
3. Exibe uma resposta adequada com base na intenção identificada.

As intenções do usuário para as quais o sistema deve estar preparado são:

- Intenção A: Pergunta sobre como atualizar as informações de pagamento.
  - Perguntas relacionadas: "Como posso atualizar meu cartão de crédito?", "Preciso mudar a forma de pagamento, o que fazer?", "Quero atualizar minhas informações de pagamento", "Método de pagamento desatualizado, como proceder para atualizar?"

- Intenção B: Pergunta sobre como acompanhar o status do pedido.
  - Perguntas relacionadas: "Onde vejo o status do meu pedido?", "Como faço para rastrear meu pedido?", "Quero saber onde está meu pedido, como faço?", "Status de entrega, como consultar?"

Para resolver o desafio, siga os passos:

1. Crie um dicionário de intenções intencoes onde as chaves são expressões regulares e os valores são as intenções correspondentes (por exemplo, "atualizar pagamento" e "acompanhar pedido").

2. Crie um dicionário de ações acoes onde as chaves são as intenções identificadas e os valores são as respostas pré-definidas que o sistema deve exibir.

3. Escreva uma função que recebe o comando do usuário, percorre o dicionário intencoes para encontrar a intenção utilizando expressões regulares, e então busca no dicionário acoes a resposta para exibir ao usuário.

4. Utilize uma entrada de loop infinito que permite ao usuário digitar comandos repetidamente até que digite "sair" para terminar o programa.
