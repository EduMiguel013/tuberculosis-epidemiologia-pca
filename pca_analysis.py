# Importar bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Carregar o dataset
data = pd.read_csv("tuberculosis_2020-2023.csv", delimiter=";", encoding="latin1")

# Exibir informações iniciais do dataset
print("Informações do dataset antes do tratamento:")
print(data.info())

# Substituir espaços em branco ou valores ausentes por NaN e preencher com 0
data = data.replace(' ', np.nan).fillna(0)

# Manter apenas colunas numéricas
data = data.select_dtypes(include=[np.number])

# Exibir a dimensão dos dados após o tratamento
print("\nDimensão do dataset após tratamento:")
print(f"Número de amostras: {data.shape[0]}")
print(f"Número de variáveis: {data.shape[1]}")

# Normalizar os dados usando StandardScaler (centraliza e normaliza)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Calcular a matriz de covariância
cov_matrix = np.cov(scaled_data, rowvar=False)

# Exibir a matriz de covariância
print("\nMatriz de Covariância:")
print(cov_matrix)

# Calcular os autovalores e autovetores da matriz de covariância
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Ordenar os autovalores em ordem decrescente e reorganizar os autovetores
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]
eigenvectors = eigenvectors[:, sorted_indices]

# Exibir autovalores e autovetores
print("\nAutovalores:")
print(eigenvalues)
print("\nAutovetores (primeiros 5 vetores):")
print(eigenvectors[:, :5])

# Selecionar o número de componentes principais (por exemplo, 2 componentes)
n_components = 2
selected_vectors = eigenvectors[:, :n_components]

# Transformar os dados para o novo espaço de componentes principais
transformed_data = np.dot(scaled_data, selected_vectors)

# Exibir os dados transformados
print("\nDados transformados (primeiras 5 amostras):")
print(transformed_data[:5])

# Visualizar os dois primeiros componentes principais em um gráfico
plt.figure(figsize=(10, 7))
plt.scatter(transformed_data[:, 0], transformed_data[:, 1], c='blue', edgecolor='k', alpha=0.7)
plt.title("PCA - Visualização dos Dois Primeiros Componentes Principais")
plt.xlabel("Componente Principal 1")
plt.ylabel("Componente Principal 2")
plt.grid(True)
plt.show()

