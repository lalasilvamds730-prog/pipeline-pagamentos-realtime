# Pipeline de Pagamentos em Tempo Real

## Projeto DIO — Dados em Tempo Real para Agentes de IA

### Sobre o projeto

Este projeto tem como objetivo desenvolver uma simulação de um pipeline de pagamentos em tempo real, utilizando Python e PostgreSQL para processar, armazenar e analisar transações financeiras.

A solução permite identificar pagamentos com valores elevados, consultar transações e gerar informações para apoiar a análise de possíveis operações suspeitas.

A implementação foi realizada localmente, sem necessidade de cadastro ou contratação de serviços em nuvem.

### Tecnologias utilizadas

- Python 3.14
- PostgreSQL 18
- SQL
- Visual Studio Code
- CSV

### Estrutura do projeto

```text
pipeline-pagamentos-realtime/
│
├── generate_data.py
├── pagamentos_teste.csv
├── processar_pagamentos.py
├── analise_pagamentos.sql
└── README.md
```

### Funcionamento

**1. Geração de dados**

Utilização de Python para gerar dados fictícios de pagamentos armazenados em arquivo CSV.

**2. Armazenamento**

Utilização do PostgreSQL para armazenar as transações na tabela `transactions`.

**3. Processamento**

O Python realiza a leitura dos pagamentos e identifica transações com valores iguais ou superiores a R$ 1.000,00.

**4. Análise SQL**

Consultas SQL permitem visualizar:
- Total de pagamentos.
- Pagamentos com valores elevados.
- Valor total das transações.
- Quantidade de pagamentos por status.
- Volume financeiro por cartão.

**5. Resultados**

Os resultados são apresentados no terminal e nas consultas do PostgreSQL.

### Resultados obtidos

No teste realizado com 20 pagamentos:

- Total de transações analisadas: 20.
- Pagamentos sinalizados por valor elevado: 6.
- Valor total processado: R$ 13.179,22.

Os alertas representam transações que precisam de análise adicional e não uma confirmação de fraude.

### Sobre as cinco camadas do desafio

O projeto contempla uma implementação local das etapas de geração de dados, armazenamento, processamento e análise.

A integração com PostgreSQL CDC, Confluent Cloud, Flink SQL e consumidores Kafka não foi implementada. Essas etapas permanecem como evolução futura da solução.

### Aprendizados

Durante o desenvolvimento, pratiquei:

- Geração e manipulação de dados com Python.
- Leitura de arquivos CSV.
- Criação e consulta de tabelas PostgreSQL.
- Utilização de comandos SQL.
- Identificação de transações com valores elevados.
- Organização e documentação de projetos.

### Autora

Larissa Martins

Projeto desenvolvido como atividade prática de aprendizagem na DIO.