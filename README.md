# 🎮 Dashboard de Análise de Vendas de Videogames 🕹️

Um dashboard interativo construído com Streamlit para explorar e visualizar dados do mercado global de videogames, baseado no popular dataset do Kaggle.

-----

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como um exercício prático de análise de dados e visualização. O objetivo é transformar um dataset estático (`.csv`) em uma ferramenta de exploração dinâmica, permitindo que usuários filtrem e descubram insights sobre as vendas de jogos por gênero, plataforma e ano de lançamento.

-----

## ✨ Funcionalidades

  - **📊 Métricas Dinâmicas:** Cards que exibem o total de jogos, receita global, número de publishers e o gênero dominante, tudo atualizado em tempo real com base nos filtros.
  - **🚩 Filtros Interativos:** Filtre todo o dashboard por Gênero e Ano de Lançamento através de uma barra lateral intuitiva.
  - **📈 Visualizações Interativas:**
      - Gráfico de Pizza com a distribuição de vendas por gênero.
      - Gráfico de Linha mostrando a evolução das vendas globais ao longo dos anos.
  - **🏆 Ranking de Jogos:** Lista dos jogos mais vendidos que se atualiza de acordo com a seleção de filtros.

-----

## 💾 Fonte dos Dados

Os dados utilizados neste projeto são do dataset **"Video Game Sales"**, disponível publicamente no Kaggle.

  * **Link para o Dataset:** [Kaggle: Video Game Sales](https://www.kaggle.com/datasets/gregorut/videogamesales)

-----

## 🛠️ Tecnologias Utilizadas

O projeto foi construído utilizando as seguintes tecnologias e bibliotecas:

-----

## 🚀 Como Executar o Projeto

### Pré-requisitos

  - Python 3.8 ou superior
  - Gerenciador de pacotes `pip`

### Passos

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Instale as dependências:**
    Crie um arquivo `requirements.txt` com o seguinte conteúdo:

    ```txt
    streamlit
    pandas
    plotly
    ```

    E então, instale-o com o comando:

    ```bash
    pip install -r requirements.txt
    ```

3.  **Execute o Dashboard:**
    Certifique-se de que o arquivo `vgsales.csv` está na mesma pasta.

    ```bash
    streamlit run app.py
    ```

4.  Abra seu navegador no endereço `http://localhost:8501`.

-----

## 📂 Estrutura do Projeto

```
seu-projeto/
├── 📄 app.py      # Script principal do Streamlit
├── 📊 vgsales.csv         # Dataset
├── 📝 requirements.txt    # Dependências do projeto
└── README.md             # Este arquivo
```

-----

## 👨‍💻 Autor

Feito com ❤️ por **Matheus Marques de Lima**.

[](https://www.google.com/search?q=https://www.linkedin.com/in/matheusmarqlima/)
[](https://www.google.com/search?q=https://github.com/matheusmarqlima/)