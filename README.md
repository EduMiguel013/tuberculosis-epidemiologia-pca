# 🔬 Análise Epidemiológica da Tuberculose Utilizando Componentes Principais (PCA)

Este repositório contém a base de dados, relatório e código reprodutível para executar PCA, visualizar componentes principais e interpretar loadings em um contexto epidemiológico.

---

## 📌 Visão geral do projeto
Este projeto aplica PCA para reduzir dimensionalidade e identificar padrões em uma base de dados epidemiológica de tuberculose (ex.: registros agregados por município/ano ou similar). O objetivo é:
- identificar quais variáveis explicam a maior parte da variação dos dados;
- gerar visualizações que ajudem a detectar agrupamentos e outliers;
- entregar um relatório técnico com interpretações dos componentes principais.

---

## ✨ Funcionalidades
- 📥 Carregamento e pré-processamento dos dados (tratamento de valores faltantes, codificação e normalização).  
- 🔢 Padronização das features (StandardScaler) antes do PCA.  
- 🧮 Cálculo de PCA (autovalores, autovetores, scores).  
- 📊 Geração de gráficos: scatter dos primeiros componentes, scree plot (variância explicada), loadings barplot e histogramas de resíduos.  
- 📈 Cálculo da variância explicada cumulativa e interpretação dos principais loadings.  
- 📓 Relatório em PDF com metodologia, resultados e interpretações (em `docs/`).  
- 🧪 Notebook interativo para exploração adicional (opcional).

---

## 🗂️ Estrutura do repositório
```
tuberculosis-pca-epidemiologia/
├─ data/
│  └─ tuberculosis_2020-2023.csv            # dataset original (sugestão de nome)
├─ docs/
│  └─ PCA_report_TB_2020-2023.pdf           # relatório técnico (PDF)
├─ src/
│  └─ pca_analysis.py                       # script principal (rodável)
├─ notebooks/
│  └─ 01-explore-pca.ipynb                  # notebook interativo (opcional)
├─ figures/
│  ├─ pca_scatter.png
│  ├─ scree_plot.png
│  └─ loadings_barplot.png
├─ requirements.txt
├─ .gitignore
└─ README.md
```

---

## 🛠️ Tecnologias utilizadas
- Python 3.8+ (recomendado 3.11+)  
- `pandas` — manipulação de dados  
- `numpy` — álgebra linear e operações vetoriais  
- `scikit-learn` (opcional para verificação) — `StandardScaler`, `PCA` (comparação)  
- `matplotlib` / `seaborn` — visualizações  
- LaTeX (opcional) — para geração de relatório técnico

---

## 🚀 Como executar (passo a passo)

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/tuberculosis-pca-epidemiologia.git
cd tuberculosis-pca-epidemiologia
```

### 2. Criar e ativar ambiente virtual (recomendado)
```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

### 4. Rodar o script principal
```bash
python src/pca_analysis.py --input data/tuberculosis_2020-2023.csv --output figures/
```
O script realiza:
- pré-processamento,
- padronização,
- cálculo da matriz de covariância / autovalores e autovetores,
- projeção dos dados nos K primeiros componentes,
- salvamento das figuras em `figures/` e resumo das métricas no terminal / arquivo.

---

## 📊 Saída esperada (exemplo de formato)
Ao rodar o script você verá algo como:

```
====================================================================
🧾 RESUMO PCA - tuberculosis_2020-2023.csv
====================================================================
- Variância explicada (PC1): 42.7%
- Variância explicada (PC2): 18.3%
- Variância explicada acumulada (PC1+PC2): 61.0%

--- TOP LOADINGS (PC1) ---
1. taxa_incidencia : +0.62
2. mortalidade     : +0.51
3. cobertura_vac   : -0.34

--- ARQUIVOS GERADOS ---
figures/pca_scatter.png
figures/scree_plot.png
figures/loadings_barplot.png
```

> Obs.: os números acima são um exemplo ilustrativo — os valores reais dependem dos dados.

---

## 🧮 Metodologia matemática (resumo)

**Dados:** matriz \(X \in \mathbb{R}^{m 	imes n}\) (m observações, n variáveis).  
**Padronização:** \(Z = \dfrac{X - \mu}{\sigma}\) (média zero, desvio padrão 1).

**Matriz de covariância:**  
\[
C = rac{1}{m-1} Z^	op Z
\]

**Autovalores e autovetores:**  
Resolver \(C v = \lambda v\) para obter autovalores \(\lambda_i\) e autovetores \(v_i\).

**Projeção nos PCs:**  
\[
	ext{scores} = Z \cdot [v_1, v_2, \dots, v_k]
\]

**Variância explicada:**  
\[
	ext{variância explicada de } PC_i = rac{\lambda_i}{\sum_j \lambda_j}
\]

O projeto inclui um `scree plot` e a tabela de loadings (coeficientes dos vetores próprios) para interpretação.

---

## ✅ Boas práticas e recomendações
- 🧾 Documente as decisões de pré-processamento (por que remover/ preencher NAs, transformar variáveis, etc.).  
- 🔁 Compare PCA manual com `sklearn.decomposition.PCA` para validar resultados.  
- 📌 Salve as transformações (mean, std, autovetores) para uso futuro / reprodutibilidade.  
- 🧪 Realize análise de sensibilidade (ex.: rodar PCA sem outliers, com variáveis selecionadas).  
- 🧑‍💻 Transforme `src/pca_analysis.py` em CLI com `argparse` (já sugerido).  
- 📂 Versione dados grandes com cuidado (ou use amostras para o repositório público).

---

## 📚 Relatório técnico
O relatório completo (metodologia, resultados e interpretações) está em `docs/PCA_report_TB_2020-2023.pdf`. Recomenda-se incluir no relatório:
- descrição do dataset (variáveis, origem, período),
- critérios de limpeza e tratamento,
- interpretação dos principais componentes,
- implicações epidemiológicas e limitações.

---

## 🧾 requirements.txt (sugestão)
```
pandas
numpy
scikit-learn
matplotlib
seaborn
```

---

## 📁 .gitignore (sugestão)
```
__pycache__/
.venv/
*.pyc
data/*.csv        # opcional: se os dados não forem públicos
figures/
.ipynb_checkpoints/
```

---

## 📝 Licença
MIT (sugerida). Ajuste conforme sua preferência.

---

## 👨‍💻 Autor
Eduardo Miguel Ribeiro Cordeiro  
E-mail: edumiguelcordeiro@gmail.com

---
