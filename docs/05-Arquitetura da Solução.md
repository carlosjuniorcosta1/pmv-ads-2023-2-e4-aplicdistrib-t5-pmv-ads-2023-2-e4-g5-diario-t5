# Arquitetura da Solução



![ArqSoluc](img/ArquiteturaSolução/ProjetoAPi.png)

A base de nossa aplicação, tanto para web quanto para mobile, consiste na manipulação de dois bancos de dados SQL, acessados por meio de APIs diferentes, mas complementares. Vamos denominá-las de API BNCC e API DIARIO e explicitar suas funções a seguir. 

A API BNCC acessa as habilidades e outras informações do banco de dados da BNCC e que devem ser registradas no diário eletrônico. Trata-se de uma api com diversos métodos GET que filtram os vários componentes curriculares, habilidades e conteúdos a serem trabalhados, obrigatoriamente, em sala de aula.

Já a API ALUNOS permite o acessar, editar, inserir e excluir alunos, atividades, notas e frequência dos discentes. Dessa forma, uma atividade avaliativa registrada pelo professor em sala de aula vai utilizar essas duas APIs e fazer o registro em uma tabela SQL com a junção de ambas. 

Isso significa que, quando o professor digitar o nome e nota de uma atividade, vai acessar a API ALUNOS, enquanto que, quando escolher em um menu a habilidade ou conteúdo trabalhados, vai acessar a API BNCC, e salvar os dados gerados em uma tabela só no SQL.
Dessa forma, temos:
1) Usuário acessa APIs hospedadas na nuvem, cada qual com sua função
2) Registros e edições do usuário são salvos pela API e aplicados no banco de dados

## Diagrama de Classes

O diagrama de classes ilustra graficamente como será a estrutura do software, e como cada uma das classes da sua estrutura estarão interligadas. Essas classes servem de modelo para materializar os objetos que executarão na memória.

![DGC](img/ArquiteturaSolução/Diagramas%20de%20Classe%20.png)

## Modelo ER
Abaixo é possivel ver o modelo ER da aplicação

![DGC](img/ArquiteturaSolução/modeloEr.png)


## Esquema Relacional

O Esquema Relacional corresponde à representação dos dados em tabelas juntamente com as restrições de integridade e chave primária.
 
As referências abaixo irão auxiliá-lo na geração do artefato “Esquema Relacional”.

> - [Criando um modelo relacional - Documentação da IBM](https://www.ibm.com/docs/pt-br/cognos-analytics/10.2.2?topic=designer-creating-relational-model)

## Modelo Físico

Entregar um arquivo banco.sql contendo os scripts de criação das tabelas do banco de dados. Este arquivo deverá ser incluído dentro da pasta src\bd.

## Tecnologias Utilizadas

Para sua construção das APIs, tem sido utilizada a linguagem Python, juntamente com a biblioteca Flask e Pandas, além de PyODBC, que integra o SQL no Python. A justificativa para utilizar Python se deve a seu poder de manipulação de dados e demanda extremamente grande de expressões regulares para pesquisa e extração de dados da BNCC, que não tem um banco de dados tal como disponibilizado neste trabalho. No extensivo trabalho para construção do banco de dados da BNCC, por exemplo, foi bastante utilizada a biblioteca re, de expressões regulares do Python, juntamente com filtragens em conjunto com o Pandas, sem os quais esse trabalho não seria possível. 
As linguagens de front end estão sendo analisadas. A princípio, vamos utilizar HTML, CSS, Bootstrap e JavaScript para a versão Web e Flutter ou React Native para a versão mobile. 

## Estilo Arquitetural do Projeto
No projeto utilizaremos um estilo monolitico.

![EstiloArq](img/ArquiteturaSolução/DDD.png)

Neste projeto vamos usar o padrão arquitetural DDD (Domain-Driven-Design) para o consumo da api e o front-end Web.

A escolha de adotar o padrão arquitetural Domain-Driven Design (DDD) em nosso projeto é fundamentada em várias razões essenciais:

1 - **Representação Precisa do Domínio:** DDD nos permite modelar nosso domínio de negócios de forma precisa no software, garantindo que nossas estruturas e lógicas reflitam fielmente as complexidades do nosso campo de atuação.

2 - **Orientação ao Negócio:** Com DDD, nosso foco principal é alinhar o software às necessidades reais do negócio e dos usuários. Isso assegura que nosso projeto seja centrado nas demandas do mercado e nas expectativas dos clientes.

3 - **Arquitetura Flexível e Adaptável:** DDD promove uma arquitetura modular que facilita a expansão e evolução do sistema à medida que nossos requisitos e o domínio de negócios mudam. Isso garante que o software seja duradouro e resiliente.

Portanto, a adoção do padrão arquitetural DDD em nosso projeto visa criar uma solução robusta, orientada ao negócio e adaptável às mudanças futuras.
## Hospedagem

A hospedagem dos bancos de dados e aplicação pode ser feita pelo https://smarterapp.com.br/Login.aspx ou https://planetscale.com/. Estamos estudando as opções disponíveis e fazendo testes. 

## Qualidade de Software

Conceituar qualidade de fato é uma tarefa complexa, mas ela pode ser vista como um método gerencial que através de procedimentos disseminados por toda a organização, busca garantir um produto final que satisfaça às expectativas dos stakeholders.

No contexto de desenvolvimento de software, qualidade pode ser entendida como um conjunto de características a serem satisfeitas, de modo que o produto de software atenda às necessidades de seus usuários. Entretanto, tal nível de satisfação nem sempre é alcançado de forma espontânea, devendo ser continuamente construído. Assim, a qualidade do produto depende fortemente do seu respectivo processo de desenvolvimento.

A norma internacional ISO/IEC 25010, que é uma atualização da ISO/IEC 9126, define oito características e 30 subcaracterísticas de qualidade para produtos de software.
Com base nessas características e nas respectivas sub-características, identifique as sub-características que sua equipe utilizará como base para nortear o desenvolvimento do projeto de software considerando-se alguns aspectos simples de qualidade. Justifique as subcaracterísticas escolhidas pelo time e elenque as métricas que permitirão a equipe avaliar os objetos de interesse.

> **Links Úteis**:
>
> - [ISO/IEC 25010:2011 - Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models](https://www.iso.org/standard/35733.html/)
> - [Análise sobre a ISO 9126 – NBR 13596](https://www.tiespecialistas.com.br/analise-sobre-iso-9126-nbr-13596/)
> - [Qualidade de Software - Engenharia de Software 29](https://www.devmedia.com.br/qualidade-de-software-engenharia-de-software-29/18209/)
