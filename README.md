# 💼 Finanlytics — Controle Financeiro Interativo com Streamlit

O **Finanlytics** é um painel interativo desenvolvido em Python com Streamlit e Plotly, que permite visualizar, filtrar e analisar suas finanças pessoais com base em arquivos `.csv` ou `.xlsx`. Ideal para quem quer acompanhar receitas, despesas e saldo ao longo do tempo de forma simples e visual.

---

## 🚀 Funcionalidades

- 📤 Upload de arquivos financeiros (`.csv` ou `.xlsx`)
- 📅 Filtros por intervalo de datas
- 💰 Cálculo automático de:
  - Total geral
  - Total de despesas
  - Total de receitas
- 📊 Visualizações interativas com Plotly:
  - Pizza de despesas por categoria
  - Barras de saldo mensal
  - Linha de evolução diária do saldo
  - Barras de receitas vs despesas
- 📥 Exportação dos dados filtrados em CSV

---

## 📁 Estrutura dos Dados Esperados

A aplicação espera arquivos com a seguinte estrutura:

```csv
Data,Categoria,Descrição,Valor
2025-05-01,Alimentação,Cachorro Quente,-65.00
2025-05-01,Salário,Pagamentos,3000.00
2025-05-02,Transporte,Gasolina,-25.00
```

### 📌 Regras:

- `Data`: formato `YYYY-MM-DD`
- `Categoria`: nome da categoria (ex: Alimentação)
- `Descrição`: descrição da transação
- `Valor`: número positivo para receitas e negativo para despesas

---

## ▶️ Como Executar

1. **Clone o repositório**:

```bash
git clone https://github.com/seu-usuario/finanlytics.git
cd finanlytics
```

2. **(Opcional) Crie e ative um ambiente virtual**:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

4. **Execute a aplicação**:

```bash
streamlit run app.py
```

5. **Acesse no navegador**:

```
http://localhost:8501
```

---

## ✅ Requisitos

- Python 3.8+
- Bibliotecas:
  - pandas
  - streamlit
  - plotly
  - openpyxl (para arquivos .xlsx)

Tudo está listado no arquivo `requirements.txt`.

---

## 📂 Uploads e Persistência

Todos os arquivos enviados são armazenados localmente na pasta `dates/`.  
Você pode excluir os arquivos manualmente para resetar os dados.

---

## 📦 Estrutura do Projeto

```
finanlytics/
├── app.py                 # Código principal da aplicação
├── dates/                 # Pasta onde os arquivos são salvos
├── requirements.txt       # Dependências da aplicação
└── README.md              # Este arquivo
```

---

## 🧠 Tecnologias Usadas

- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)
- [Plotly](https://plotly.com/python/)
- [Openpyxl](https://openpyxl.readthedocs.io/)

---

## 💡 Ideias Futuras

- 🔮 Previsão de gastos futuros com Machine Learning
- 🧠 Classificação automática de categorias
- 🔗 Integração com APIs bancárias
- 👥 Suporte multiusuário com autenticação
- 🧾 Exportação de relatórios em PDF

---

## 👨‍💻 Autor

Desenvolvido por **Pedro Augusto Alexandre**  
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

---

## 📜 Licença

Este projeto está licenciado sob a licença **MIT**.  
Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
