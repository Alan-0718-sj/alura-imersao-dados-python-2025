import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- Configuração da Página ---
# Define o título da página, o ícone e o layout para ocupar a largura inteira.
st.set_page_config(
    page_title="Dashboard Neon | Salários na Área de Dados",
    page_icon="💸",
    layout="wide",
)

# --- Estilo Neon e Tema dos Gráficos ---

# 1. CSS para efeito "glow" (neon) nos textos
def load_css():
    st.markdown("""
        <style>
            /* Cor primária para o efeito neon */
            :root {
                --neon-glow-color: #00f9e0; /* Ciano vibrante */
            }

            /* Títulos com efeito neon */
            h1, h2, h3 {
                color: #ffffff;
                text-shadow: 
                    0 0 5px var(--neon-glow-color),
                    0 0 10px var(--neon-glow-color),
                    0 0 15px #fff,
                    0 0 20px #000;
            }

            /* Métricas (KPIs) com estilo neon */
            .stMetric {
                background-color: #1a1a2e;
                border: 1px solid var(--neon-glow-color);
                border-radius: 10px;
                padding: 15px;
                box-shadow: 0 0 10px var(--neon-glow-color);
            }
            .stMetric .st-ax { /* Cor do valor da métrica */
                color: var(--neon-glow-color);
                font-size: 2.5rem;
            }
        </style>
    """, unsafe_allow_html=True)

load_css()

# 2. Tema "Dark Neon" para o Plotly
NEON_COLORS = ['#00f9e0', "#1ab4e3", '#aeff00', '#ff6600', '#f8f8f8'] # Ciano, Magenta, Verde-limão, Laranja, Branco
dark_neon_template = go.layout.Template()

dark_neon_template.layout = go.Layout(
    paper_bgcolor='#0E1117',  # Cor de fundo do Streamlit Dark
    plot_bgcolor='#1a1a2e',   # Cor de fundo do gráfico
    font=dict(color='#f8f8f8'),
    title_font=dict(size=20, family='Arial, sans-serif'),
    colorway=NEON_COLORS,
    xaxis=dict(gridcolor='rgba(255, 255, 255, 0.1)', linecolor='rgba(255, 255, 255, 0.5)'),
    yaxis=dict(gridcolor='rgba(255, 255, 255, 0.1)', linecolor='rgba(255, 255, 255, 0.5)'),
    legend=dict(bgcolor='rgba(0,0,0,0.3)', bordercolor='rgba(255, 255, 255, 0.5)'),
)
# Define o tema como padrão para todos os gráficos do Plotly
px.defaults.template = dark_neon_template


# --- Carregamento dos dados ---
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")
        return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return None

df = load_data()

if df is None:
    st.stop() # Interrompe a execução se os dados não puderem ser carregados

# --- Barra Lateral (Filtros) ---
# st.sidebar.image("https://i.imgur.com/u1mPefy.png", width=100) # Exemplo de logo
st.sidebar.header("🔍 Filtros")

# Filtro de Ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

# Filtro de Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

# Filtro por Tipo de Contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

# Filtro por Tamanho da Empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

# --- Filtragem do DataFrame ---
# O dataframe principal é filtrado com base nas seleções feitas na barra lateral.
df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) &
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# --- Conteúdo Principal ---
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os salários na área de dados. Use os filtros à esquerda para uma análise personalizada.")

# --- Métricas Principais (KPIs) ---
st.subheader("Métricas Gerais (Salário Anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, "N/A"

col1, col2, col3, col4 = st.columns(4)
col1.metric("Salário Médio", f"${salario_medio:,.0f}")
col2.metric("Salário Máximo", f"${salario_maximo:,.0f}")
col3.metric("Total de Registros", f"{total_registros:,}")
col4.metric("Cargo Mais Frequente", cargo_mais_frequente)

st.markdown("<hr/>", unsafe_allow_html=True)

# --- Análises Visuais com Plotly ---
st.subheader("Análises Visuais")

# GRÁFICO NOVO: Evolução do Salário ao Longo do Tempo
if not df_filtrado.empty:
    salario_por_ano = df_filtrado.groupby('ano')['usd'].mean().reset_index()
    grafico_evolucao = px.line(
        salario_por_ano,
        x='ano',
        y='usd',
        title="Evolução do Salário Médio Anual",
        labels={'usd': 'Média Salarial (USD)', 'ano': 'Ano'},
        markers=True
    )
    grafico_evolucao.update_traces(line=dict(width=3))
    st.plotly_chart(grafico_evolucao, use_container_width=True)
else:
    st.warning("Nenhum dado para exibir no gráfico de evolução.")


col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 Cargos por Salário Médio",
            labels={'usd': 'Média Salarial Anual (USD)', 'cargo': ''},
            text='usd'
        )
        grafico_cargos.update_traces(texttemplate='$%{text:,.0f}', textposition='outside')
        grafico_cargos.update_layout(yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=40,
            title="Distribuição de Salários Anuais",
            labels={'usd': 'Faixa Salarial (USD)', 'count': 'Quantidade'}
        )
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

st.markdown("<hr/>", unsafe_allow_html=True)
st.subheader("Análises Adicionais")

col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    # GRÁFICO NOVO: Salário por Senioridade e Tipo de Contrato
    if not df_filtrado.empty:
        salario_senioridade_contrato = df_filtrado.groupby(['senioridade', 'contrato'])['usd'].mean().reset_index()
        grafico_senioridade = px.bar(
            salario_senioridade_contrato,
            x='senioridade',
            y='usd',
            color='contrato',
            barmode='group',
            title="Salário Médio por Senioridade e Contrato",
            labels={'usd': 'Média Salarial (USD)', 'senioridade': 'Senioridade', 'contrato': 'Contrato'},
            category_orders={"senioridade": ["Júnior", "Pleno", "Sênior", "Liderança"]}
        )
        st.plotly_chart(grafico_senioridade, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir na análise por senioridade.")

with col_graf4:
    # GRÁFICO NOVO: Distribuição de Salários por Tamanho da Empresa (Box Plot)
    if not df_filtrado.empty:
        grafico_tamanho_empresa = px.box(
            df_filtrado,
            x='tamanho_empresa',
            y='usd',
            color='tamanho_empresa',
            title="Distribuição Salarial por Tamanho da Empresa",
            labels={'usd': 'Salário Anual (USD)', 'tamanho_empresa': 'Tamanho da Empresa'},
            category_orders={"tamanho_empresa": ["Pequena", "Média", "Grande"]}
        )
        st.plotly_chart(grafico_tamanho_empresa, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir na análise por tamanho da empresa.")

st.markdown("<hr/>", unsafe_allow_html=True)
st.subheader("Análise Geográfica")

# GRÁFICO MELHORADO: Mapa Interativo por Cargo
if not df_filtrado.empty:
    cargos_disponiveis_mapa = sorted(df_filtrado['cargo'].unique())
    cargo_selecionado_mapa = st.selectbox("Selecione um Cargo para visualizar no mapa:", cargos_disponiveis_mapa, index=cargos_disponiveis_mapa.index("Data Scientist") if "Data Scientist" in cargos_disponiveis_mapa else 0)

    df_mapa = df_filtrado[df_filtrado['cargo'] == cargo_selecionado_mapa]
    media_cargo_pais = df_mapa.groupby('residencia_iso3')['usd'].mean().reset_index()

    if not media_cargo_pais.empty:
        grafico_paises = px.choropleth(
            media_cargo_pais,
            locations='residencia_iso3',
            color='usd',
            hover_name='residencia_iso3',
            color_continuous_scale='Viridis', # Uma escala de cor vibrante
            title=f'Salário Médio de {cargo_selecionado_mapa} por País',
            labels={'usd': 'Salário Médio (USD)', 'residencia_iso3': 'País'}
        )
        grafico_paises.update_layout(geo=dict(bgcolor='rgba(0,0,0,0)'))
        st.plotly_chart(grafico_paises, use_container_width=True)
    else:
        st.warning(f"Não há dados suficientes para o cargo '{cargo_selecionado_mapa}' nos filtros selecionados.")
else:
    st.warning("Nenhum dado para exibir no mapa.")

# --- Tabela de Dados Detalhados ---
with st.expander("Ver dados detalhados da seleção atual"):
    st.dataframe(df_filtrado)