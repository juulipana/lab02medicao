# Um estudo das caracteristicas de qualidade de sistemas Java
Laboratório 02 de Medição de Software

# Alunos
* Juliana Parreiras Guimarães da Cunha
* Pedro Henrique Marques de Oliveira

# Professor
* Danilo de Quadros Maia Filho

# Objetivo
Este projeto tem como objetivo estudar as qualidades de sistemas open-source. O foco principal é analisar aspectos da qualidade de repositórios desenvolvidos em Java, correlacionando-os com características de seu processo de desenvolvimento, sob a perspectiva de métricas de produtividade calculadas por meio da ferramenta CK. A CK é uma ferramenta que analisa códigos Java e mostra, de forma simples, quão complexo, acoplado ou organizado ele está.

### Metodologia

1. **Seleção dos Repositórios**
   * Serão coletados os **1.000 repositórios Java mais populares** do GitHub.
   * A popularidade será medida pelo **número de estrelas**.

2. **Questões de Pesquisa**
   * O projeto busca responder às seguintes perguntas:

     * RQ1: Qual a relação entre **popularidade** e **qualidade** do código?
     * RQ2: Qual a relação entre **maturidade** (idade) e **qualidade**?
     * RQ3: Qual a relação entre **atividade** (número de releases) e **qualidade**?
     * RQ4: Qual a relação entre **tamanho** do projeto e **qualidade**?

3. **Definição das Métricas**
   * **Métricas do processo de desenvolvimento:**
     * Popularidade: número de **estrelas** no GitHub.
     * Tamanho: número de **linhas de código** e **comentários**.
     * Atividade: número de **releases**.
     * Maturidade: **idade** do repositório (em anos).
   * **Métricas de qualidade do código (usando CK):**
     * **CBO**: acoplamento entre classes.
     * **DIT**: profundidade da árvore de herança.
     * **LCOM**: falta de coesão entre os métodos.
       
4. **Coleta de Dados**
   * Os dados dos repositórios serão coletados usando a **API do GitHub (REST ou GraphQL)**.
   * A ferramenta **CK** será usada para analisar o código e gerar arquivos `.csv` com as métricas de qualidade.
   * Por fim, será feita uma **análise comparativa** entre os dados coletados e as métricas, para responder às perguntas de pesquisa.

# Hipóteses
RQ01 – Qual a relação entre a popularidade dos repositórios e as suas características de
qualidade?
H1: Repositórios com mais estrelas (mais populares) costumam apresentar código mais atualizado e documentação mais completa.

RQ02 – Qual a relação entre a maturidade do repositórios e as suas características de
qualidade?
H2: Projetos mais antigos são mais prováveis de ter uma maior confirmidade com práticas CI/CD. Além disso, possuem quantidade menor de dívidas técnicas não pagas.

RQ03 – Qual a relação entre a atividade dos repositórios e as suas características de
qualidade?
H3: Maior cobertura de testes, redução da dívida técnica e resolução mais rápida de bugs costumam aparecer em repositórios que recebem commits com frequência.

RQ04 – Qual a relação entre o tamanho dos repositórios e as suas características de
qualidade?
H4: Repositórios muito grandes, em linhas de código ou número de arquivos, tendem a ter maior complexidade e menor cobertura de testes.
