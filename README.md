![Image](https://github.com/user-attachments/assets/84f8a6a0-c37e-47ac-bed4-a8d6e3a586f5)

---

# Imersão Dados com Python - Alura


## 📖 Sobre o Projeto

Este projeto foi desenvolvido durante a **Imersão de Dados com Python** promovida pela [Alura](https://www.alura.com.br/), com foco em análise e visualização de dados.

Este projeto consiste em um dashboard interativo construído com **Streamlit** para a análise de salários de profissionais da área de dados. A aplicação permite que os usuários explorem dados salariais de diferentes cargos, senioridades e locais, utilizando filtros dinâmicos para personalizar a visualização.

O grande diferencial deste dashboard é sua **estética Neon**, com textos e gráficos que brilham sobre um fundo escuro, proporcionando uma experiência de usuário moderna e visualmente impactante.

---

## ✨ Features Principais

*   🎨 **Tema Neon Customizado**: Estilo único com CSS para criar um efeito "glow" em títulos e métricas, além de um tema Plotly customizado para gráficos vibrantes.
*   🔍 **Filtros Interativos**: Filtre os dados por ano, nível de senioridade, tipo de contrato e tamanho da empresa.
*   📈 **Métricas Chave (KPIs)**: Visualize rapidamente o salário médio, salário máximo, total de registros e o cargo mais frequente com base nos filtros aplicados.
*   📊 **Visualizações Detalhadas com Plotly**:
    *   **Gráfico de Linha**: Acompanhe a evolução do salário médio ao longo dos anos.
    *   **Gráfico de Barras**: Compare o salário médio dos 10 cargos mais bem pagos.
    *   **Histograma**: Entenda a distribuição das faixas salariais.
    *   **Gráfico de Grupos**: Analise o salário por senioridade, segmentado por tipo de contrato.
    *   **Box Plot**: Observe a dispersão salarial com base no tamanho da empresa.
    *   **Mapa Interativo (Choropleth)**: Explore o salário médio por país para um cargo específico.
*   📄 **Tabela de Dados**: Expanda uma seção para visualizar e inspecionar os dados brutos filtrados.

---

## 🚀 Como Executar o Projeto

Para executar este dashboard em sua máquina local, siga os passos abaixo.

### Pré-requisitos

*   Python 3.8 ou superior
*   Pip (gerenciador de pacotes do Python)

### Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Alan-0718-sj/alura-imersao-dados-python-2025.git
    cd alura-imersao-dados-python-2025
    ```

2.  **Crie um ambiente virtual (recomendado):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # No Windows, use: .venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    Crie um arquivo chamado `requirements.txt` na raiz do projeto com o seguinte conteúdo:
    ```txt
    pandas==2.2.3
    streamlit==1.44.1
    plotly==5.24.1
    ```
    Em seguida, instale as bibliotecas com o comando:
    ```bash
    pip install -r requirements.txt
    ```

### Execução

1.  Com o ambiente virtual ativado e as dependências instaladas, execute o seguinte comando no terminal:

    ```bash
    streamlit run app.py 
    ```
    > **Nota**: Substitua `seu_script.py` pelo nome do seu arquivo Python.

2.  O Streamlit abrirá automaticamente uma nova aba no seu navegador com o dashboard em execução.

---

## 🛠️ Tecnologias Utilizadas

*   **[Python](https://www.python.org/)**: Linguagem de programação principal.
*   **[Streamlit](https://streamlit.io/)**: Framework para a criação da aplicação web interativa.
*   **[Pandas](https://pandas.pydata.org/)**: Biblioteca para manipulação e análise dos dados.
*   **[Plotly](https://plotly.com/python/)**: Biblioteca para a criação de gráficos interativos e de alta qualidade.
*   **[HTML/CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)**: Utilizado para a estilização customizada do tema Neon.

---

## 📂 Estrutura do Código

O código está organizado nas seguintes seções lógicas:

1.  **Configuração da Página**: Define o título, ícone e layout da aplicação usando `st.set_page_config`.
2.  **Estilo Neon e Tema**:
    *   Uma função `load_css` injeta CSS customizado para o efeito "glow".
    *   Um template do Plotly (`dark_neon_template`) é criado e definido como padrão para garantir que todos os gráficos sigam a mesma identidade visual.
3.  **Carregamento de Dados**: Uma função `load_data` com cache (`@st.cache_data`) lê o CSV de um repositório no GitHub, garantindo performance e eficiência.
4.  **Barra Lateral (Filtros)**: Contém todos os widgets `st.sidebar.multiselect` que permitem ao usuário interagir e filtrar os dados.
5.  **Conteúdo Principal**:
    *   **Métricas (KPIs)**: Apresenta os principais indicadores em colunas.
    *   **Análises Visuais**: Seção onde os gráficos do Plotly são gerados e exibidos.
    *   **Análise Geográfica**: Contém o mapa interativo com um seletor de cargo.
    *   **Dados Detalhados**: Um `st.expander` que revela a tabela de dados (DataFrame) quando clicado.

---

## 📊 Fonte dos Dados

Os dados utilizados neste dashboard foram obtidos a partir do seguinte arquivo CSV público, disponível no GitHub:

*   **URL**: `https://raw.githubusercontent.com/Alan-0718-sj/alura-imersao-dados-python-2025/refs/heads/main/dados-imers%C3%A3o-final.csv`

---

### 🔗 Link do Dashboard:

- https://alura-imersao-dados-python-2025-nan-silva.streamlit.app/

---

### 📫 Contato

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Perfil%20Profissional-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/alan-silva-5933771b6/) 

[![YouTube](https://img.shields.io/badge/YouTube-Canal%20Oficial-red?style=flat-square&logo=youtube)](https://www.youtube.com/@AlanSilva-zg6ui)

[![GitHub](https://img.shields.io/badge/GitHub-Repositórios%20Públicos-black?style=flat-square&logo=github)](https://github.com/Alan-0718-sj)
 

---
<p align="center">Feito com 💙 e muito código por Alan Silva</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=052D6E&height=120&section=footer" alt="Capa animada inferior" width="1000" />
</p>
