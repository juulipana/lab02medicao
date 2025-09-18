# Qualidade de Software em Repositórios Java - Laboratório 02
Estudo sobre métricas de qualidade em repositórios open-source Java, analisando popularidade, maturidade, atividade e tamanho com base na ferramenta CK.

# Alunos
* Juliana Parreiras Guimarães da Cunha
* Pedro Henrique Marques de Oliveira

# Professor
* Danilo de Quadros Maia Filho

# Índice

- [Objetivo](#objetivo)
- [Metodologia](#metodologia)
  - [Seleção dos Repositórios](#seleção-dos-repositórios)
  - [Questões de Pesquisa](#questões-de-pesquisa)
  - [Definição das Métricas](#definição-das-métricas)
  - [Coleta de Dados](#coleta-de-dados)
- [Hipóteses](#hipóteses)
- [Análise dos Resultados](#análise-dos-resultados)
  - [RQ01 - Popularidade x Qualidade](#rq01---popularidade-x-qualidade)
  - [RQ02 - Maturidade x Qualidade](#rq02---maturidade-x-qualidade)
  - [RQ03 - Atividade x Qualidade](#rq03---atividade-x-qualidade)
  - [RQ04 - Tamanho x Qualidade](#rq04---tamanho-x-qualidade)
- [Relações de maturidade](#relações-de-maturidade)
  - [Repositórios mais velhos possuem maior contribuição?](#repositórios-mais-velhos-possuem-maior-contribuição)
  - [Repositórios mais velhos são maiores?](#repositórios-mais-velhos-são-maiores)
- [Conclusão](#conclusão)
- [Trabalhos Relacionados](#trabalhos-relacionados)
- [Referências](#referências)

# Objetivo
Este projeto tem como objetivo estudar as qualidades de sistemas open-source. O foco principal é analisar aspectos da qualidade de repositórios desenvolvidos em Java, correlacionando-os com características de seu processo de desenvolvimento, sob a perspectiva de métricas de produtividade calculadas por meio da ferramenta CK. A CK é uma ferramenta que analisa códigos Java e mostra, de forma simples, quão complexo, acoplado ou organizado ele está.

# Metodologia

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
   * **Dados dos repositórios:**
     * Popularidade: número de **estrelas** no GitHub.
     * Tamanho: número de **linhas de código** e **comentários**.
     * Atividade: número de **releases**.
     * Maturidade: **idade** do repositório (em anos).
       
   * **Métricas de qualidade do código (usando CK):**
     * **CBO**: Coupling Between Objects (CBO), ou Acoplamento entre Objeto, mede o acoplamento entre classes, valores altos indicam forte acoplamento, o que pode dificultar manutenção e reutilização.
     * **DIT**: O Depth of Inheritance Tree (DIT) ou Profundidade da Árvore de Herança mede a  profundidade da árvore de herança. Ou seja, mede a quantidade de níveis que uma classe está abaixo da raiz na herança e valores maiores indicam maior complexidade e maior dependência.
     * **LCOM**: O Lack of Cohesion of Methods (LCOM) ou Falta de Coesão dos Métodos mede a falta de coesão entre os métodos. Valores altos indicam que a classe possui métodos pouco relacionados entre si, sugerindo baixa coesão e potencial fragilidade na organização do código.
     * **WMC**: O Weighted Methods per Class (WMC) ou ou Métodos Ponderados por Classe mede a complexidade de uma classe somando a complexidade de seus métodos, indicando quão difícil ela é de entender e manter.
     
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

# Análise dos Resultados

## RQ01 - Popularidade x  Qualidade

Para responder a esta pergunta, utilizamos o padrão MCK para medir a qualidade dos sistemas e relacioná-la à popularidade dos repositórios. O MCK (Maintainability, Complexity, Knowledge) é um indicador que avalia a qualidade do código com base em sua manutenibilidade, complexidade e legibilidade, fornecendo uma medida objetiva de quão fácil é compreender, modificar e evoluir o software.

Ao analisar a relação entre a qualidade do código (MCK) e o número de estrelas dos repositórios, observou-se que há pouca correlação entre eles. Em outras palavras, repositórios com muitas estrelas não apresentam necessariamente maior qualidade segundo o padrão MCK.

O gráfico abaixo ilustra essa relação:

<img src="https://github.com/user-attachments/assets/eac7981e-b019-48a2-b309-b2424af673f1" style="height:500px; width:auto;" />

## RQ02 - Maturidade x Qualidade

Após analisar os dados obtidos, pudemos concluir o seguinte acerca dos repositórios de acordo com sua maturidade:

1. Embora a distribuição não seja completamente homogênea, observa-se que os valores mais altos de WMC estão concentrados na metade dos repositórios mais maduros, com idades entre 12 e 14 anos. Por outro lado, poucos repositórios mais novos apresentam alta complexidade, com exceção de três casos destacados.
2. Observa-se também uma relativa homogeneidade de LCOM entre os repositórios, independentemente da idade. Isso indica que, para a maioria dos repositórios, há boa coesão entre os métodos, mesmo nos projetos mais recentes.
3. Nos repositórios mais maduros, verifica-se um alto CBO, especialmente nos que têm mais de 10 anos, enquanto repositórios mais novos apresentam valores menores, com poucas exceções. Um CBO elevado pode indicar que uma classe depende de muitas outras, o que pode aumentar a complexidade do sistema e dificultar testes e manutenção e aumentar o WMC geral.

**Sendo assim, repositórios maduros possuem maior qualidade?**

**Não necessariamente.**

Repositórios mais velhos tendem a apresentar maior complexidade e acoplamento, ainda que mantenham boa coesão entre os métodos. Em outras palavras: o fator maturidade não é suficiente por si só para garantir maior qualidade de um repositório.

<img width="1600" height="500" alt="image" src="https://github.com/user-attachments/assets/b572888d-78d8-4b0b-9ccf-c35e8128b1b2" />

## RQ03 - Atividade x Qualidade

Para responder essa questão, definimos a relação entre WMC, LCOM, CBO e atividade de repositórios populares. Com isso, pudemos ver que:

1. **WMC x Atividade**: Repositórios ativos apresentam uma variação maior no WMC, com alguns outliers bem altos. Repositórios não ativos têm WMC geralmente menor, mas também possuem alguns outliers. Ou seja, repositórios ativos tendem a ter classes mais complexas, possivelmente porque continuam evoluindo e acumulando funcionalidades. Porém, os outliers sugerem que alguns projetos ativos estão muito complexos, o que pode indicar necessidade de refatoração.
2. **LCOM x Atividade**: O LCOM é baixo para ambos os grupos, mas há outliers extremos, especialmente em repositórios não ativos. Os outliers podem indicar projetos com classes muito desorganizadas ou que não foram mantidos, reforçando que projetos não ativos podem acumular problemas de qualidade estrutural.
3. O CBO é maior e mais disperso em repositórios ativos. Não ativos tendem a ter valores mais baixos, mas ainda existem alguns outliers. Repositórios ativos apresentam mais acoplamento entre classes, provavelmente devido à adição contínua de funcionalidades e integrações. Já os não ativos têm acoplamento menor, possivelmente por estarem congelados ou menos complexos.

**Sendo assim, repositórios ativos tem maior qualidade?**

**Não necessariamente.**

Projetos ativos tendem a ser mais complexos, enquanto projetos não ativos podem estar menos acoplados, mas não necessariamente mais bem organizados. Portanto, atividade recente não garante melhor qualidade, mas pode indicar mais evolução funcional e manutenção contínua.

<img width="1600" height="500" alt="image" src="https://github.com/user-attachments/assets/6a4e41ac-72a4-4793-b53e-b2eb340ebf25" />

## RQ04 - Tamanho x Qualidade

Para investigar essa questão, utilizamos o LOC (Lines of Code) como métrica de tamanho e analisamos sua relação com indicadores de qualidade, como WMC (Weighted Methods per Class) e LCOM (Lack of Cohesion of Methods):

1. O gráfico que relaciona LOC e WMC mostra uma tendência linear e crescente: repositórios maiores tendem a ter classes com mais métodos, indicando maior complexidade à medida que o tamanho aumenta.

2. Já a análise de LCOM mostra que repositórios populares, independentemente do tamanho, apresentam baixa coesão. Isso sugere que mesmo projetos grandes e complexos podem manter módulos relativamente coesos, o que é um indicativo de boa organização.

**O que isso quer dizer?**

**O aumento do tamanho de um repositório está diretamente associado a um crescimento da complexidade das classes.** Em outras palavras, quanto maior o software, mais difícil pode ser mantê-lo e compreendê-lo. No entanto, a baixa LCOM em repositórios populares indica que equipes bem estruturadas conseguem preservar a coesão e a qualidade do código, mesmo em projetos grandes.

<img width="1600" height="685" alt="image" src="https://github.com/user-attachments/assets/a49c6062-4109-4bb6-94c0-e4e3d25a52ac" />

# Relações de maturidade

## Repositórios mais velhos possuem maior contribuição?

// TO-DO

## Repositórios mais velhos são maiores?

// TO-DO

# Conclusão

De modo geral, nosso estudo mostrou que não existe uma receita única para garantir boa qualidade de software. Fatores como popularidade, maturidade, atividade ou mesmo tamanho não nos dizem, sozinhos, se um repositório é de qualidade. Ainda assim, podemos observar que, à medida que os repositórios crescem em idade ou tamanho, eles tendem a se tornar mais complexos. Isso acontece porque, com o tempo, eles recebem mais contribuições, aumentam em linhas de código e, consequentemente, sua complexidade cresce junto.

| Questão de Pesquisa (RQ) | Resposta |
|---------------------------|----------------|
| **RQ01: Popularidade x Qualidade** | Pouca correlação; repositórios populares não necessariamente têm maior qualidade de código. |
| **RQ02: Maturidade x Qualidade** | Não necessariamente; repositórios mais velhos tendem a ser mais complexos e acoplados, mas mantêm boa coesão. |
| **RQ03: Atividade x Qualidade** | Não necessariamente; projetos ativos têm maior complexidade e acoplamento, mas isso não garante melhor qualidade estrutural. |
| **RQ04: Tamanho x Qualidade** | Repositórios maiores tendem a ter maior complexidade (WMC), mas podem manter boa coesão (LCOM), especialmente os populares. |

# Trabalhos Relacionados

Para complementar esta pesquisa, consideramos o estudo Evaluating Test Quality in GitHub Repositories: A Comparative Analysis of CI/CD Practices Using GitHub Actions, que avaliou a qualidade de testes em 940 repositórios Java com e sem GitHub Actions. O estudo analisou test smells, bugs e tempo de correção, mostrando que repositórios com CI/CD apresentaram menos test smells, mas sem diferença estatisticamente significativa na resolução de bugs. Assim, CI/CD não garante melhoria automática na qualidade dos testes, mas ajuda a controlar problemas. Nosso estudo indica que maturidade, tamanho e atividade aumentam a complexidade dos repositórios, e o artigo complementa ao evidenciar que práticas de CI/CD podem mitigar impactos negativos da complexidade, mantendo a qualidade dos testes mesmo em projetos grandes e ativos.

# Referências

SILVA, Edson Campolina; RODRIGUES, Rodolfo; OLIVEIRA, Johnatan; BOECHAT, Danilo; TAVARES, Cleiton. Evaluating Test Quality in GitHub Repositories: A Comparative Analysis of CI/CD Practices Using GitHub Actions. Anais do 12º Workshop de Visualização, Evolução e Manutenção de Software (VEM 2024). Sociedade Brasileira de Computação, 2024. Disponível em: https://sol.sbc.org.br/index.php/vem/article/view/30281
.

