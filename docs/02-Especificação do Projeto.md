# Especificações do Projeto

<span style="color:red">Pré-requisitos: <a href="1-Documentação de Contexto.md"> Documentação de Contexto</a></span>

Definição do problema e ideia de solução a partir da perspectiva do usuário. É composta pela definição do  diagrama de personas, histórias de usuários, requisitos funcionais e não funcionais além das restrições do projeto.

Apresente uma visão geral do que será abordado nesta parte do documento, enumerando as técnicas e/ou ferramentas utilizadas para realizar a especificações do projeto

## Personas

Pedro Paulo tem 26 anos, é arquiteto recém-formado e autônomo. Pensa em se desenvolver profissionalmente através de um mestrado fora do país, pois adora viajar, é solteiro e sempre quis fazer um intercâmbio. Está buscando uma agência que o ajude a encontrar universidades na Europa que aceitem alunos estrangeiros.

Enumere e detalhe as personas da sua solução. Para tanto, baseie-se tanto nos documentos disponibilizados na disciplina e/ou nos seguintes links:

> **Links Úteis**:
> - [Rock Content](https://rockcontent.com/blog/personas/)
> - [Hotmart](https://blog.hotmart.com/pt-br/como-criar-persona-negocio/)
> - [O que é persona?](https://resultadosdigitais.com.br/blog/persona-o-que-e/)
> - [Persona x Público-alvo](https://flammo.com.br/blog/persona-e-publico-alvo-qual-a-diferenca/)
> - [Mapa de Empatia](https://resultadosdigitais.com.br/blog/mapa-da-empatia/)
> - [Mapa de Stalkeholders](https://www.racecomunicacao.com.br/blog/como-fazer-o-mapeamento-de-stakeholders/)
>
Lembre-se que você deve ser enumerar e descrever precisamente e personalizada todos os clientes ideais que sua solução almeja.

## Histórias de Usuários

Com base na análise das personas forma identificadas as seguintes histórias de usuários:

|EU COMO... `PERSONA`| QUERO/PRECISO ... `FUNCIONALIDADE` |PARA ... `MOTIVO/VALOR`                 |
|--------------------|------------------------------------|----------------------------------------|
|Usuário do sistema  | Registrar minhas tarefas           | Não esquecer de fazê-las               |
|Administrador       | Alterar permissões                 | Permitir que possam administrar contas |

Apresente aqui as histórias de usuário que são relevantes para o projeto de sua solução. As Histórias de Usuário consistem em uma ferramenta poderosa para a compreensão e elicitação dos requisitos funcionais e não funcionais da sua aplicação. Se possível, agrupe as histórias de usuário por contexto, para facilitar consultas recorrentes à essa parte do documento.

> **Links Úteis**:
> - [Histórias de usuários com exemplos e template](https://www.atlassian.com/br/agile/project-management/user-stories)
> - [Como escrever boas histórias de usuário (User Stories)](https://medium.com/vertice/como-escrever-boas-users-stories-hist%C3%B3rias-de-usu%C3%A1rios-b29c75043fac)
> - [User Stories: requisitos que humanos entendem](https://www.luiztools.com.br/post/user-stories-descricao-de-requisitos-que-humanos-entendem/)
> - [Histórias de Usuários: mais exemplos](https://www.reqview.com/doc/user-stories-example.html)
> - [9 Common User Story Mistakes](https://airfocus.com/blog/user-story-mistakes/)

## Modelagem do Processo de Negócio 

### Análise da Situação Atual

Os principais pontos da proposta é, em primeiro lugar, o processo de avaliação e frequência se refere às notas obtidas dos alunos durante o bimestre ou ano letivo, além de suas faltas. Nossa aplicação deve facilitar o trabalho do professor nesse sentido e permitir que o trabalho de lançamento de atividades, acompanhamento da nota dos estudantes em determinados períodos e sua presença seja registrada de forma rápida e efetiva. 

Em segundo lugar, os professores têm nos relatado dificuldades no que concerne ao registro das habilidades e conteúdos temáticos a serem trabalhados segundo à Base Nacional Curricular Comum (BRASIL, 2017). Trata-se de um documento norteador para a estrutura curricular que é adotada por todas as escolas do país, quer sejam públicas, quer particulares. Como a BNCC é um documento bastante extenso, de aproximadamente 600 páginas, os docentes têm a penosa tarefa de memorizar nomes para centenas de habilidades diferentes, pois o registro nos diários escolares é obrigatório desde a promulgação desse documento. Por essa razão, seria bastante bem-vindo um diário que permitisse o acesso automático à BNCC, de forma que as habilidades possam ser facilmente filtradas por bancos de dados e selecionadas em vez de buscadas exaustivamente em livros físicos.

### Descrição Geral da Proposta

Nossa proposta de aplicação visa a facilitar a vida dos docentes da Educação Básica no registro diário de suas atividades por meio de um novo diário eletrônico com acesso a documentos norteadores da educação do Ministério da Educação, como a BNCC. 

### Processo - Fluxo do App

O processo apresentado consiste no fluxo da aplicação e a estrutura usada

![Processo 1](img/Especificacão/DiagramaProcesso.jpeg)

---

## Indicadores de Desempenho

Apresente aqui os principais indicadores de desempenho e algumas metas para o processo. Atenção: as informações necessárias para gerar os indicadores devem estar contempladas no diagrama de classe. Colocar no mínimo 5 indicadores. 

Usar o seguinte modelo: 

![Indicadores de Desempenho](img/02-indic-desemp.png)
Obs.: todas as informações para gerar os indicadores devem estar no diagrama de classe a ser apresentado a posteriori. 

## Requisitos

As tabelas que se seguem apresentam os requisitos funcionais e não funcionais que detalham o escopo do projeto. Para determinar a prioridade de requisitos, aplicar uma técnica de priorização de requisitos e detalhar como a técnica foi aplicada.

### Requisitos Funcionais

|ID    | Descrição do Requisito  | Prioridade |
|------|-----------------------------------------|----|
|RF-001| A aplicação deve ter uma tela de login | BAIXA |
|RF-002| Permitir aos professores registrar informações sobre as aulas lecionadas, como data, disciplina, conteúdo abordado e materiais utilizados. | ALTA |
|RF-003| Possibilitar o cadastro de informações dos alunos, como nome, matrícula, contato, turma e outras informações relevantes. | ALTA |
|RF-004| Permitir que os professores registrem avaliações, tarefas e atividades de avaliação com datas, tipo de avaliação e notas atribuídas. | ALTA |
|RF-005| Calcular automaticamente as médias e notas finais com base nas avaliações registradas.   | BAIXA |
|RF-006| Permitir que os professores registrem a presença ou falta de alunos em cada aula   | MÉDIA |
|RF-007| Gerar relatórios de frequência para pais, responsáveis e gestores   | BAIXA |
|RF-008| Fornecer visualizações gráficas de médias de alunos, desempenho geral da turma e outras estatísticas relevantes   | BAIXA |
|RF-009| Garantir que o aplicativo seja acessível em diferentes dispositivos, como smartphones, tablets e computadores.   | MÉDIA |
|RF-010| O layout deve ser intuitivo, tornando fácil para os usuários navegar e encontrar as funcionalidades desejadas   | BAIXA |

### Requisitos não Funcionais


|ID    | Descrição do Requisito  | Prioridade |
|------|-----------------------------------------|----|
|RNF-001| O banco de dados deve ser hospedado na nuvem para acesso da aplicação | ALTA |
|RNF-002| Tempo de resposta aceitável para as ações do usuário, como carregamento de páginas e processamento de dados. | ALTA |
|RNF-003| A aplicação deve ter um tempo de resposta baixo para as requisições | MÉDIA |
|RNF-004| A aplicação deve possuir uma interface limpa e intuitiva para o usuário | BAIXA |
|RNF-005| A aplicação deve criptografar a senha do usuário   | ALTA |


## Restrições

O projeto está restrito pelos itens apresentados na tabela a seguir.

|ID| Restrição                                             |
|--|-------------------------------------------------------|
|01| O projeto deverá ser entregue até o final do semestre |



## Diagrama de Casos de Uso

Na imagem abaixo é apresentado o diagrama de casos de uso do projeto.

![Gerenciamento de Tempo](img/Especificacão/CasosDeUso.jpeg)

---
# Matriz de Rastreabilidade

A matriz de rastreabilidade é uma ferramenta usada para facilitar a visualização dos relacionamento entre requisitos e outros artefatos ou objetos, permitindo a rastreabilidade entre os requisitos e os objetivos de negócio. 

A matriz deve contemplar todos os elementos relevantes que fazem parte do sistema, conforme a figura meramente ilustrativa apresentada a seguir.

![Exemplo de matriz de rastreabilidade](img/02-matriz-rastreabilidade.png)

> **Links Úteis**:
> - [Artigo Engenharia de Software 13 - Rastreabilidade](https://www.devmedia.com.br/artigo-engenharia-de-software-13-rastreabilidade/12822/)
> - [Verificação da rastreabilidade de requisitos usando a integração do IBM Rational RequisitePro e do IBM ClearQuest Test Manager](https://developer.ibm.com/br/tutorials/requirementstraceabilityverificationusingrrpandcctm/)
> - [IBM Engineering Lifecycle Optimization – Publishing](https://www.ibm.com/br-pt/products/engineering-lifecycle-optimization/publishing/)


# Gerenciamento de Projeto

De acordo com o PMBoK v6 as dez áreas que constituem os pilares para gerenciar projetos, e que caracterizam a multidisciplinaridade envolvida, são: Integração, Escopo, Cronograma (Tempo), Custos, Qualidade, Recursos, Comunicações, Riscos, Aquisições e Partes Interessadas. Para desenvolver projetos um profissional deve se preocupar em gerenciar todas essas dez áreas. Elas se complementam e se relacionam, de tal forma que não se deve apenas examinar uma área de forma estanque. É preciso considerar, por exemplo, que as áreas de Escopo, Cronograma e Custos estão muito relacionadas. Assim, se eu amplio o escopo de um projeto eu posso afetar seu cronograma e seus custos.

### Gerenciamento de Tempo
O gráfico de Gantt é uma ferramenta visual para gerenciar o cronograma de atividades de um projeto. Ele lista as atividades necessárias, as divide em etapas e estima o tempo necessário para executá-las. A seguir, há uma imagem da utilização do gráfico de Gantt para este projeto.

![Gerenciamento de Tempo](img/Especificacão/Diagrama%20de%20grantt.png)

O gráfico de Gantt ou diagrama de Gantt também é uma ferramenta visual utilizada para controlar e gerenciar o cronograma de atividades de um projeto. Com ele, é possível listar tudo que precisa ser feito para colocar o projeto em prática, dividir em atividades e estimar o tempo necessário para executá-las.

### Gerenciamento de Equipe
O gerenciamento adequado de tarefas contribuirá para que o projeto alcance altos níveis de produtividade. Por isso, é fundamental que ocorra a gestão de tarefas e de pessoas, de modo que os times envolvidos no projeto possam ser facilmente gerenciados. 


|                  | Agosto           | Setembro         | Outubro          | Novembro         |
|------------------|------------------|------------------|------------------|------------------|------------------|
| **Data de Entrega**  | <span style="color:black;">01/08/23 a 03/09/23</span> | <span style="color:black;">04/09/23 a 01/10/23</span>   | <span style="color:black;">02/10/23 a 29/10/23</span>    | <span style="color:black;">30/10/23 a 26/11/23</span> | 
| **Equipe de Gestão** | <span style="color:red;">**`Documento de Contexto...`**</span> |||||
|**Equipe Back**      || <span style="color:green;">**`Implementação da API`**</span> ||||
| **Equipe Front**    ||| <span style="color:blue;">**`Projeto e implementação da interface Web`**</span> | <span style="color:blue;">**`Projeto e implementação da interface Mobile`**</span>|


## Gestão de Orçamento

O processo de determinar o orçamento do projeto é uma tarefa que depende, além dos produtos (saídas) dos processos anteriores do gerenciamento de custos, também de produtos oferecidos por outros processos de gerenciamento, como o escopo e o tempo.

![Orçamento](img/02-orcamento.png)
