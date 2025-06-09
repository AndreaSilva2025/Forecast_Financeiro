# Forecast Financeiro com Python

Este projeto tem como objetivo demonstrar a aplicação de Python para realização de previsão financeira com base em séries temporais de receita mensal. Utilizamos bibliotecas como `pandas`, `matplotlib` e `statsmodels` para processar dados, gerar gráficos e prever valores futuros de maneira automatizada.

## Objetivos do Projeto

* Automatizar a previsão financeira de receita mensal
* Aplicar métodos de série temporal (Holt-Winters com tendência)
* Criar um gráfico visual para tomada de decisão
* Fornecer uma base para aplicações em FP\&A e controle financeiro

## Funcionalidades

* Leitura de dados históricos a partir de um arquivo CSV (`dados_receita.csv`)
* Ajuste de modelo de previsão com `ExponentialSmoothing` (sem sazonalidade)
* Geração de gráfico com receita histórica e prevista
* Exportação automática do gráfico em PNG

## Como Usar

1. Clone este repositório
2. Instale as dependências:

```bash
pip install pandas matplotlib statsmodels
```

3. Execute o script principal:

```bash
python forecast.py
```

4. O arquivo `dados_receita.csv` contém os dados de entrada e pode ser atualizado conforme sua necessidade.

## Formato do CSV esperado

```csv
Mes,Receita
2023-01,15000
2023-02,16000
...
```

## Exemplo de Gráfico Gerado

O gráfico exibe a curva histórica de receitas e a projeção para os próximos meses, permitindo tomada de decisão rápida e baseada em dados.

![grafico_forecast](https://github.com/user-attachments/assets/b1fc5baf-0ce5-4e61-98a1-f33a3a735939)


## Autor

Andrea Jocelina Silva
Especialista em FP\&A, Análise de Dados Financeiros, Riscos e Produtos
[LinkedIn](https://www.linkedin.com/in/andrea-jocelina-cea-/)
[GitHub](https://github.com/AndreaSilva2025A)

---

Este é apenas o primeiro projeto da minha série de aplicações em finanas, BI e automação com dados. Acompanhe o repositório para novas publicações!

