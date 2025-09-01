# Desafio de Análise de Dados: Explorando o Mercado Global de Videogames

## 📝 Cenário

Você é um analista de dados recém-contratado por um estúdio de desenvolvimento de jogos. Sua primeira tarefa é analisar o mercado de videogames das últimas décadas para identificar tendências e oportunidades que possam guiar o desenvolvimento do próximo grande sucesso da empresa.

---

## 💾 1. O Dataset

Para este desafio, utilizaremos o dataset **"Video Game Sales"**, um clássico do Kaggle que contém informações sobre as vendas de mais de 16.500 jogos.

* **Fonte:** [Kaggle: Video Game Sales Dataset](https://www.kaggle.com/datasets/gregorut/videogamesales)
* **Arquivo:** `vgsales.csv`

### Colunas Principais

* `Rank`: Ranking geral de vendas.
* `Name`: Nome do jogo.
* `Platform`: Console/Plataforma (ex: PS4, X360, Wii).
* `Year`: Ano de lançamento.
* `Genre`: Gênero do jogo (ex: Action, Sports, Role-Playing).
* `Publisher`: Empresa que publicou o jogo.
* `NA_Sales`: Vendas na América do Norte (em milhões).
* `EU_Sales`: Vendas na Europa (em milhões).
* `JP_Sales`: Vendas no Japão (em milhões).
* `Other_Sales`: Vendas em outras regiões (em milhões).
* `Global_Sales`: Vendas totais no mundo (em milhões).

---

## 🛠️ 2. Ferramentas Sugeridas

* **Linguagem:** Python
* **Bibliotecas Principais:**
    * `Pandas`: Para carregar, manipular e limpar os dados.
    * `Matplotlib` & `Seaborn`: Para criar visualizações e gráficos.
* **Ambiente:** Jupyter Notebook ou Google Colab.

---

## 🚀 3. O Desafio: Passo a Passo

### Fase 1: Preparação e Limpeza dos Dados (Data Cleaning)

O primeiro passo em qualquer projeto de análise é garantir que os dados estejam limpos e prontos para uso.

1.  **Carregar o Dataset:** Importe o arquivo `vgsales.csv` para um DataFrame do Pandas.
2.  **Exploração Inicial:**
    * Visualize as primeiras e últimas linhas com `.head()` e `.tail()`.
    * Verifique os tipos de dados e valores não-nulos com `.info()`.
    * Obtenha estatísticas descritivas com `.describe()`.
3.  **Tratamento de Dados Faltantes:**
    * Identifique as colunas com valores nulos (`.isnull().sum()`).
    * Decida uma estratégia para lidar com eles (para este desafio, remover as linhas com `.dropna()` é uma abordagem aceitável).
4.  **Correção de Tipos de Dados:**
    * A coluna `Year` está como `float`. Converta-a para `int` para uma representação mais adequada.

### Fase 2: Análise Exploratória de Dados (EDA)

Com os dados limpos, comece a fazer perguntas para extrair os primeiros insights.

1.  **Quais são os 10 jogos mais vendidos de todos os tempos?**
    * *Dica:* Ordene o DataFrame pela coluna `Global_Sales`.
2.  **Quais plataformas (consoles) tiveram mais jogos lançados?**
    * *Dica:* Use `.value_counts()` na coluna `Platform` e visualize com um gráfico de barras.
3.  **Quais são os gêneros de jogos mais comuns?**
    * *Dica:* Use `.value_counts()` na coluna `Genre`.
4.  **Quais são as 10 publishers que mais publicaram jogos? E as 10 que mais venderam (Global_Sales)?**
    * *Dica:* Para a segunda pergunta, use `.groupby('Publisher')['Global_Sales'].sum()`.
5.  **Como o número de jogos lançados por ano evoluiu ao longo do tempo?**
    * *Dica:* Agrupe os dados por `Year` e crie um gráfico de linhas.

### Fase 3: Análise Aprofundada

Cruze informações para encontrar insights mais valiosos e responder a perguntas de negócio.

1.  **Análise de Vendas por Região:**
    * **Pergunta:** Qual gênero vende mais em cada região (América do Norte, Europa e Japão)? Existem diferenças culturais claras?
    * *Dica:* Agrupe por `Genre` e some as vendas de `NA_Sales`, `EU_Sales` e `JP_Sales`.
2.  **Ciclo de Vida das Plataformas:**
    * **Pergunta:** Qual foi o "auge" e o "declínio" de vendas de plataformas famosas como 'Wii', 'PS2' e 'X360'?
    * *Dica:* Filtre o DataFrame para uma plataforma e plote as vendas anuais em um gráfico de linhas.
3.  **Performance Cruzada (Gênero vs. Plataforma):**
    * **Pergunta:** Onde está a "mina de ouro"? Qual gênero vendeu melhor em qual plataforma?
    * *Dica:* Crie um *heatmap* (mapa de calor) com os 5 gêneros mais vendidos nas 5 plataformas mais vendidas. Pode ser necessário usar `pd.pivot_table()`.

### Fase 4: Conclusão e Recomendações

Com base em toda a sua análise, prepare um resumo com **3 a 5 recomendações acionáveis** para o estúdio de jogos.
