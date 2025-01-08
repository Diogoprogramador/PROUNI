import pandas as pd

# Caminho para o arquivo CSV
file_path = "ProuniRelatorioDadosAbertos2020.csv"

# Lista de codificações comuns
encodings_to_try = ["utf-8", "latin1", "iso-8859-1"]

# Ajustar as configurações do pandas para exibir todas as linhas e colunas
pd.set_option('display.max_rows', None)  # Exibe todas as linhas
pd.set_option('display.max_columns', None)  # Exibe todas as colunas
pd.set_option('display.width', None)  # Evita truncamento das colunas
pd.set_option('display.max_colwidth', None)  # Exibe todo o conteúdo das colunas

for encoding in encodings_to_try:
    try:
        # Carrega o arquivo sem o parâmetro 'errors'
        data = pd.read_csv(file_path, delimiter=';', encoding=encoding)
        print(f"Dados carregados com sucesso usando a codificação: {encoding}")
        print(f"Colunas disponíveis: {data.columns.tolist()}")

        # Excluir a coluna 'CPF_BENEFICIARIO' (caso exista)
        if 'CPF_BENEFICIARIO' in data.columns:
            data = data.drop(columns=['CPF_BENEFICIARIO'])
            print("\nColuna 'CPF_BENEFICIARIO' excluída com sucesso!")
        else:
            print("\nA coluna 'CPF_BENEFICIARIO' não foi encontrada.")

        # Exibe a contagem e porcentagem de cada valor para cada coluna restante
        for col in data.columns:
            print(f"\nDistribuição da coluna: {col}")
            value_counts = data[col].value_counts()  # Contagem de valores
            value_percentages = data[col].value_counts(normalize=True) * 100  # Porcentagem de valores
            result = pd.DataFrame({'Contagem': value_counts, 'Porcentagem': value_percentages})
            print(result)  # Exibe a contagem e porcentagem para cada valor na coluna

        break  # Sai do loop se a leitura for bem-sucedida
    except UnicodeDecodeError as e:
        print(f"Erro de decodificação com a codificação {encoding}: {e}")
    except Exception as e:
        print(f"Erro ao carregar com a codificação {encoding}: {e}")

import plotly.express as px

# Gerar os gráficos de barras para cada coluna
for col in data.columns:
    # Obter a distribuição de contagem e porcentagem
    value_counts = data[col].value_counts()
    value_percentages = data[col].value_counts(normalize=True) * 100
    result = pd.DataFrame({'Contagem': value_counts, 'Porcentagem': value_percentages})

    # Criar o gráfico de barras para contagem
    fig = px.bar(result,
                 x=result.index,
                 y='Contagem',
                 text='Porcentagem',
                 labels={'index': col, 'Contagem': 'Contagem', 'Porcentagem': 'Porcentagem (%)'},
                 title=f'Distribuição de {col}')

    # Exibir a porcentagem nas barras
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

    # Exibir o gráfico
    fig.show()



