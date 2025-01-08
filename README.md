Análise de Dados Prouni com Python
Este repositório contém um projeto de análise de dados sobre o Programa Universidade para Todos (Prouni), utilizando Python. O objetivo principal é explorar e analisar os dados do Prouni para identificar padrões e tendências, como a distribuição das bolsas, o perfil dos estudantes e a evolução do programa ao longo dos anos.

Objetivo
A análise foca em:

Distribuição geográfica das bolsas (por estado e município).
Perfil dos candidatos (idade, renda, etnia, etc.).
Comparação entre bolsas integrais e parciais.
Evolução do número de bolsas ao longo dos anos.
Identificação de tendências nas bolsas oferecidas por curso e instituição.
Tecnologias Utilizadas
Python 3.x: Linguagem principal para análise de dados.
Pandas: Manipulação e análise de dados.
Matplotlib e Seaborn: Visualização de dados.
NumPy: Para cálculos numéricos e operações com arrays.
CSV: Leitura e escrita de arquivos CSV com dados do Prouni.
Estrutura do Repositório
bash
Copiar código
prouni-analysis/
│
├── data/                  # Dados brutos (CSV)
│   ├── prouni_2020.csv    # Dados de 2020
│  
│
├── scripts/               # Scripts Python para análise
│   ├── data_cleaning.py   # Script para limpar e preparar os dados
│   └── data_analysis.py   # Script principal de análise
│
├── requirements.txt       # Dependências do projeto
├── README.md              # Este arquivo
└── LICENSE                # Licença do projeto
Como Rodar o Projeto
Pré-requisitos
Certifique-se de ter o Python 3.x instalado em seu sistema. Você pode verificar isso com:

bash
Copiar código
python --version
Instalando Dependências
Este projeto depende das bibliotecas listadas no arquivo requirements.txt. Para instalá-las, basta executar o seguinte comando:

bash
Copiar código
pip install -r requirements.txt
O arquivo requirements.txt contém as seguintes dependências:

Copiar código
pandas
matplotlib
seaborn
numpy
Executando o Projeto
O projeto é composto por dois scripts principais:

data_cleaning.py: Realiza a limpeza e o pré-processamento dos dados.
data_analysis.py: Realiza a análise e gera os gráficos.
Passos para executar os scripts:
Clone o repositório:
bash
Acesse a pasta do projeto:
bash
cd prouni-analysis
Execute o script de limpeza de dados:
bash
python scripts/data_cleaning.py
Este script vai carregar os dados de entrada, fazer a limpeza necessária (como tratar valores ausentes, formatar colunas, etc.) e gerar um novo arquivo CSV com os dados limpos.

Execute o script de análise de dados:
bash
python scripts/data_analysis.py
Este script irá carregar os dados limpos e gerar gráficos e análises, como a distribuição das bolsas por estado, tipo de bolsa (integral vs. parcial), perfil dos alunos e a evolução do número de bolsas ao longo dos anos.

Exemplo de Análise
Dentro do script data_analysis.py, você encontrará os seguintes tipos de análise:

Distribuição das bolsas por estado: Um gráfico de barras mostrando quantas bolsas foram concedidas por estado.
Comparação entre bolsas integrais e parciais: Gráficos de pizza ou barras para comparar o número de bolsas integrais e parciais.
Perfil demográfico dos alunos: Análise sobre a idade, renda e etnia dos alunos contemplados pelo Prouni.
