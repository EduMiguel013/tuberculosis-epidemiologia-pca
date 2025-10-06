# 🧭 tuberculosis-epidemiologia-pca

**🔬 Análise de Componentes Principais (PCA)** aplicada a dados de tuberculose (2020–2023).  
Repositório pensado para portfólio de Cientista de Dados: contém dados, relatório e código reprodutível para executar a análise PCA e visualizar insights epidemiológicos.

---

## 📂 Estrutura do repositório

tuberculosis-pca-epidemiologia/
├─ data/
│ └─ tuberculosis_2020-2023.csv
├─ docs/
│ └─ PCA_report_TB_2020-2023.pdf
├─ src/
│ └─ pca_analysis.py
├─ notebooks/
│ └─ 01-explore-pca.ipynb (opcional)
├─ figures/
│ └─ pca_scatter.png (gerado pelo script)
├─ requirements.txt
├─ .gitignore
└─ README.md

---

## ❓ Sobre o projeto

Este projeto aplica **PCA** para reduzir a dimensionalidade e explorar padrões em uma base de dados de tuberculose (ex.: DataSUS — 2020 a 2023). O objetivo é identificar variáveis que explicam maior parte da variação, visualizar agrupamentos e gerar insights para análise epidemiológica.

---

## 🚀 Objetivos principais

- Demonstrar aplicação prática de PCA em dados de saúde pública.  
- Visualizar agrupamentos entre observações/anos.  
- Gerar outputs reprodutíveis (figuras e relatórios) para portfólio.

---

## 🛠️ Como rodar (passo a passo)

1. Criar e ativar um ambiente virtual (recomendado):
```bash
python -m venv .venv
# Linux / macOS
source .venv/bin/activate
# Windows
.venv\Scripts\activate
```
2. Instalar dependências:
``
pip install -r requirements.txt
``
3. Estruturar os arquivos conforme a pasta data/, src/, docs/ (veja estrutura acima).

4. Rodar o script principal:
```
python src/pca_analysis.py --input data/tuberculosis_2020-2023.csv --output figures/pca_scatter.png
```
O script deve:

- carregar e pré-processar os dados,

- padronizar variáveis (StandardScaler),

- calcular PCA (autovalores/autovetores),

- salvar figura dos 2 primeiros componentes em figures/.

### 📦 Dependências sugeridas (requirements.txt)
```
pandas
numpy
scikit-learn
matplotlib
seaborn        # opcional para notebooks
```

## ✅ Boas práticas / Sugestões para o portfólio

🧩 Transforme src/pca_analysis.py em um script com argparse para facilitar parametrização.

📝 Adicione um notebooks/01-explore-pca.ipynb com EDA, correlações e interpretação de loadings.

📊 Inclua um scree plot (variância explicada) e salve figuras em figures/.

🔍 Documente decisões de tratamento de dados (por que preencher NAs com X, normalização, seleção de features).

🧾 Adicione LICENSE (MIT sugerida) e CONTRIBUTING.md se quiser colaboração pública.

⚙️ Crie requirements.txt e .gitignore (ignorar __pycache__/, .venv/, arquivos grandes).

## ✍️ Autor / Créditos

Eduardo Miguel Ribeiro Cordeiro - script base do projeto.
Waleska Mayara Reis da Silva - relatório

## 📄 Licença

MIT 
