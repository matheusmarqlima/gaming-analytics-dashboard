import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA E CSS (Seu código original, mantido)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Gaming Analytics Dashboard",
    page_icon="🎮",
    layout="wide"
)

# CSS customizado para tema gaming
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 100%);
    }
    .stMetric {
        background-color: #16213e;
        border: 1px solid #00d4ff;
        border-radius: 10px;
        padding: 15px;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.2);
    }
    .stMetric > div {
        background-color: transparent;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# ### MUDANÇA 1: CARREGAR OS DADOS REAIS DO CSV ###
# -----------------------------------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv('vgsales.csv')
    # Limpeza básica dos dados
    df = df.dropna(subset=['Year', 'Publisher'])
    df['Year'] = df['Year'].astype(int)
    return df

# Carregar dados
df_original = load_data()

# -----------------------------------------------------------------------------
# ### MUDANÇA 2: FILTROS NA SIDEBAR QUE REALMENTE FUNCIONAM ###
# -----------------------------------------------------------------------------
st.sidebar.header("🎛️ Filtros")

# Filtro por Gênero
all_genres = df_original['Genre'].unique()
selected_genre = st.sidebar.selectbox(
    "Filtrar por Gênero:",
    options=['Todos'] + list(all_genres)
)

# Filtro por Ano (Slider)
min_year, max_year = int(df_original['Year'].min()), int(df_original['Year'].max())
selected_year_range = st.sidebar.slider(
    "Filtrar por Ano de Lançamento:",
    min_value=min_year,
    max_value=max_year,
    value=(min_year, max_year)
)

# Aplicar os filtros ao DataFrame
df_filtrado = df_original[
    (df_original['Year'] >= selected_year_range[0]) &
    (df_original['Year'] <= selected_year_range[1])
]
if selected_genre != "Todos":
    df_filtrado = df_filtrado[df_filtrado['Genre'] == selected_genre]

# -----------------------------------------------------------------------------
# HEADER
# -----------------------------------------------------------------------------
st.markdown("# 🎮 Dashboard com os jogos mais vendidos")
st.markdown("### Este conjunto de dados contém uma lista de videogames com vendas superiores a 100.000 cópias. ")

# -----------------------------------------------------------------------------
# ### MUDANÇA 3: MÉTRICAS DINÂMICAS BASEADAS NOS DADOS FILTRADOS ###
# -----------------------------------------------------------------------------
col1, col2, col3, col4 = st.columns(4)

total_jogos = df_filtrado.shape[0]
receita_total = df_filtrado['Global_Sales'].sum()
publishers_unicas = df_filtrado['Publisher'].nunique()
genero_dominante = df_filtrado['Genre'].mode()[0]

with col1:
    st.metric(label="📊 Total de Jogos Filtrados", value=f"{total_jogos:,}")

with col2:
    st.metric(label="💰 Receita Global (Milhões)", value=f"${receita_total:,.2f}M")

with col3:
    st.metric(label="🏢 Publishers Únicas", value=publishers_unicas)

with col4:
    st.metric(label="⭐ Gênero Dominante", value=genero_dominante)

st.markdown("---")

# -----------------------------------------------------------------------------
# ### MUDANÇA 4: GRÁFICOS DINÂMICOS ###
# -----------------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Distribuição de Vendas por Gênero")
    vendas_por_genero = df_filtrado.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False).reset_index()
    
    fig_pie = px.pie(
        vendas_por_genero,
        values='Global_Sales',
        names='Genre',
        color_discrete_sequence=px.colors.qualitative.Vivid
    )
    fig_pie.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', legend_title_text='Gênero')
    st.plotly_chart(fig_pie, use_container_width=True)

with col2:
    st.subheader("⚡ Vendas Globais por Ano")
    vendas_por_ano = df_filtrado.groupby('Year')['Global_Sales'].sum().reset_index()

    fig_line = px.line(
        vendas_por_ano,
        x='Year',
        y='Global_Sales',
        markers=True,
        color_discrete_sequence=['#00d4ff']
    )
    fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', xaxis_title='Ano', yaxis_title='Vendas Globais (Milhões)')
    fig_line.update_traces(line=dict(width=3))
    st.plotly_chart(fig_line, use_container_width=True)

# -----------------------------------------------------------------------------
# ### MUDANÇA 5: LISTA DE TOP JOGOS DINÂMICA ###
# -----------------------------------------------------------------------------
st.subheader("🥇 Top Jogos (Seleção Atual)")

# Ordena os jogos filtrados e pega os 10 melhores
top_jogos = df_filtrado.sort_values(by='Global_Sales', ascending=False).head(10)

for idx, game in top_jogos.iterrows():
    col1, col2, col3, col4 = st.columns([4, 2, 2, 2])
    with col1:
        st.write(f"**{game['Name']}** ({game['Platform']})")
    with col2:
        st.write(f"Gênero: {game['Genre']}")
    with col3:
        st.write(f"Ano: {game['Year']}")
    with col4:
        st.write(f"📈 **${game['Global_Sales']:.2f}M**")
    st.markdown("<hr style='margin-top: 5px; margin-bottom: 5px;'>", unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.markdown("*Feito com ❤️ por Matheus Marques de Lima*")
st.markdown("*Dashboard criado com Python + Streamlit 🐍*")