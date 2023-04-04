Marco Túlio Souto Maior Duarte - Desafio Final Backend da Fábrica de Software - UBTECH

Esta é uma API em Django Rest Framework para uma Barbearia fictícia. O objetivo é que o usuário possa registrar, consultar, atualizar e deletar tanto Serviços quanto Funcionários.
Utilizo, portanto, quatro operações: GET, POST, PUT e DELETE.

O app foi testado com Insomnia, e o banco de dados utilizado foi o PostgreSQL.

Para rodar o programa, utilize o "requirements.txt" para instalar tanto o Django Rest Framework quanto o PostgreSQL.

A classe Servico possui os seguintes atributos: "nome", "preco" e "barbeiro" (se relaciona com a outra classe).
A classe Funcionario possui os seguintes atributos: "nome_funcionario" e "telefone_funcionario". Também possui uma id, que é criada automaticamente pelo PostgreSQL.

Listo, abaixo, as operações que o app pode realizar:

GET /servicos/ - lista todos os serviços
GET /servicos/{id}/ - recupera um serviço por ID
POST /servicos/ - cria um novo serviço
PUT /servicos/{id}/ - atualiza um serviço existente
DELETE /servicos/{id}/ - deleta um serviço existente
GET /funcionarios/ - lista todos os funcionários
GET /funcionarios/{id}/ - recupera um funcionário por ID
POST /funcionarios/ - cria um novo funcionário
PUT /funcionarios/{id}/ - atualiza um funcionário existente
DELETE /funcionarios/{id}/ - deleta um funcionário existente

Obrigado pela atenção!
