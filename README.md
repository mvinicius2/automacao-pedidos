# Automação de Pedidos e Faturamento em Python

## Sobre o projeto

Projeto desenvolvido para automatizar a leitura e o processamento de pedidos armazenados em arquivos CSV.

A aplicação calcula o valor de cada pedido, valida os dados de entrada e gera relatórios com os resultados do processamento.

## Funcionalidades

- Leitura de pedidos utilizando arquivos CSV.
- Conversão de preços e quantidades para valores numéricos.
- Validação de dados inválidos e valores negativos.
- Cálculo do total de cada pedido e do faturamento.
- Contabilização de pedidos processados e rejeitados.
- Geração automática de relatórios CSV.

## Tecnologias utilizadas

- Python 3
- Módulo `csv` da biblioteca padrão do Python.

## Como executar

1. Instale o Python 3.
2. Baixe ou clone este repositório.
3. Abra o terminal na pasta do projeto.
4. Execute:

   `python main.py`

## Arquivos do projeto

- `main.py`: código principal da aplicação.
- `pedidos.csv`: arquivo com os pedidos de entrada.
- `relatorio.csv`: relatório com os pedidos válidos e seus respectivos totais.
- `resumo.csv`: resumo com a quantidade de pedidos processados, rejeitados e o faturamento total.

## Validações implementadas

A aplicação rejeita pedidos com preços ou quantidades que não podem ser convertidos para números, além de rejeitar valores negativos.

Os pedidos rejeitados não são incluídos no faturamento nem no relatório de pedidos válidos.

## Aprendizados

O projeto foi desenvolvido para praticar leitura e escrita de arquivos CSV, dicionários, listas, estruturas condicionais, laços de repetição, funções de conversão, tratamento de exceções e validação de dados.
