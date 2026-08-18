# DGT2823 — Data Cleaning with Python

[English](#english) | [Português](#português)

## English

Practical project for **DGT2823 — Technologies for Big Data Solution Development**. It contains data manipulation and cleaning exercises built with Python and pandas.

### Project contents

- `data.csv` — dataset provided for the assignment;
- `microatividades.py` — activities covering data reading, subsets, display options, `head`, `tail` and `info`;
- `pratica_pandas.py` — practical data cleaning and conversion of the `Date` column.

### Result

The cleaning pipeline fills missing calorie values with zero, normalizes inconsistent dates and removes records without a valid date. The included dataset produces 31 valid rows from 32 source records.

| Validation | Result |
| --- | --- |
| Missing calories after cleaning | 0 |
| Invalid dates after cleaning | 0 |
| Automated tests | 3 passing |

### Technologies

- Python
- pandas
- CSV data

### How to run

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python microatividades.py
python pratica_pandas.py
```

### Validation

```bash
python -m unittest discover -s tests -v
```

---

## Português

Projeto prático da disciplina **DGT2823 — Tecnologias para Desenvolvimento de Soluções de Big Data**. Reúne exercícios de manipulação e limpeza de dados desenvolvidos com Python e pandas.

### Conteúdo do projeto

- `data.csv` — conjunto de dados fornecido para a atividade;
- `microatividades.py` — atividades de leitura, subconjuntos, opções de exibição, `head`, `tail` e `info`;
- `pratica_pandas.py` — prática de limpeza de dados e conversão da coluna `Date`.

### Resultado

O processo preenche calorias ausentes com zero, normaliza datas inconsistentes e remove registros sem data válida. O conjunto incluído produz 31 linhas válidas a partir de 32 registros originais.

| Validação | Resultado |
| --- | --- |
| Calorias ausentes após a limpeza | 0 |
| Datas inválidas após a limpeza | 0 |
| Testes automatizados | 3 aprovados |

### Tecnologias

- Python
- pandas
- Dados em CSV

### Como executar

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python microatividades.py
python pratica_pandas.py
```

### Validação

```bash
python -m unittest discover -s tests -v
```

## Author / Autora

**Morgana Petterle da Cunha**  
[LinkedIn](https://linkedin.com/in/morgana-petterle) · [GitHub](https://github.com/Morgana-Fstack)
