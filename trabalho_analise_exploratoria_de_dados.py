import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Criação dos DataFrames para cada indicador econômico
dados = {

    Mes: ['Maio 2023','Junho 2023','Julho 2023','Agosto 2023','Setembro 2023','Outubro 2023','Novembro 2023','Dezembro 2023','Janeiro 2024','Fevereiro 2024','Março 2024','Abril 2024'],
    'Mes2':['Abril 2023','Maio 2023','Junho 2023','Julho 2023','Agosto 2023','Setembro 2023','Outubro 2023','Novembro 2023','Dezembro 2023','Janeiro 2024','Fevereiro 2024','Março 2024'],
    'tri':['1º trimestre 2021','2º trimestre 2021','3º trimestre 2021','4º trimestre 2021','1º trimestre 2022','2º trimestre 2022','3º trimestre 2022','4º trimestre 2022','1º trimestre 2023','2º trimestre 2023','3º trimestre 2023','4º trimestre 2023'],
    'Ano':['2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
    'IPCA': [0.23, -0.08, 0.12, 0.23, 0.26, 0.24, 0.28, 0.56, 0.42, 0.83, 0.16, 0.38],
    'INPC': [0.36, -0.10, -0.09, 0.20, 0.11, 0.12, 0.10, 0.55, 0.57, 0.81, 0.19, 0.37],
    'IPCA-15': [0.51, 0.04, -0.07, 0.28, 0.35, 0.21, 0.33, 0.40, 0.31, 0.78, 0.36, 0.21],
    'IPP': [-0.35, -2.88, -2.72, -0.76, 0.75, 1.06, 1.07, -0.34, -0.20, -0.24, 0.14, 0.35],
    'SINAPI': [0.36, 0.39, 0.23, 0.18, 0.02, 0.14, 0.08, 0.26, 0.19, 0.15, 0.07, 0.41],
    'PIM-PF': [-0.50, 0.40, 0.00, 0.40, 0.50, 0.20, 0.10, 0.70, 1.20, -1.10, 0.10, 0.90],
    'PMC': [0.30, -0.70, 0.00, 0.90, -0.20, 0.80, -0.30, 0.20, -1.50, 2.70, 1.00, 0.00],
    'PMS': [-1.90, 1.60, 0.40, 0.90, -1.40, -0.10, -0.30, 0.50, 0.50, 0.50, -0.90, 0.40]
}

df = pd.DataFrame(dados)

# Calculo de medidas centrais e de dispersão
medidas_centrais = df.describe()
print(medidas_centrais)

#Histograma
plt.figure(figsize=(10, 6))
sns.histplot(df['IPCA'], bins=10, kde=True)
plt.title('Distribuição do IPCA')
plt.xlabel('Mes')
plt.ylabel('Frequência')
plt.show()

#inflação e o comportamento dos preços no Brasil. 
plt.figure(figsize=(12, 8))
plt.plot(df['Mes'], df['IPCA'], label='IPCA', marker='o')
plt.plot(df['Mes'], df['INPC'], label='INPC', marker='o')
plt.plot(df['Mes'], df['IPCA-15'], label='IPCA-15', marker='o')
plt.xticks(rotation=45)
plt.title('Evolução dos Índices de Preços ao Consumidor')
plt.xlabel('Mês')
plt.ylabel('Variação (%)')
plt.legend()
plt.show()

#Regressão Linear
import statsmodels.api as sm

# Preparando os dados para a regressão linear
X = df['IPCA']
y = df['INPC']
X = sm.add_constant(X)  # Adiciona constante (intercepto)

# Ajustando o modelo
model = sm.OLS(y, X).fit()

# Resumo do modelo
print(model.summary())

# Plotando a regressão linear
plt.figure(figsize=(10, 6))
sns.regplot(x='IPCA', y='INPC', data=df)
plt.title('Regressão Linear entre IPCA e INPC')
plt.xlabel('IPCA (%)')
plt.ylabel('INPC (%)')
plt.show()

# Calculando a matriz de correlação
correlation_matrix = df[['IPCA', 'INPC', 'IPCA-15', 'IPP', 'SINAPI', 'PIM-PF', 'PMC', 'PMS']].corr()

# Configurando o estilo dos gráficos
plt.figure(figsize=(12, 8))

# Criando o heatmap para a matriz de correlação
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, linewidths=.5, linecolor='black')
plt.title('Matriz de Correlação entre Índices Econômicos')
plt.show()