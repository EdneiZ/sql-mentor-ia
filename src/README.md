# 🤖 SQL Mentor IA

## Sobre o Projeto

O SQL Mentor IA é um assistente virtual desenvolvido para auxiliar estudantes e profissionais iniciantes na aprendizagem de SQL.

O sistema utiliza uma base de conhecimento estruturada em JSON para responder dúvidas sobre comandos e conceitos fundamentais de banco de dados.

## Funcionalidades

- Consulta de conceitos SQL
- Base de conhecimento em JSON
- Respostas automáticas
- Múltiplas perguntas na mesma execução
- Encerramento da conversa por comando

## Tecnologias Utilizadas

- Python
- JSON
- Git
- GitHub

## Estrutura do Projeto

```text
SQL-MENTOR-IA
│
├── data
│   └── conhecimento.json
│
├── docs
│   ├── documentacao.md
│   ├── metricas.md
│   └── prompt.md
│
├── src
│   └── app.py
│
└── README.md
```

## Como Executar

```bash
cd src
python app.py
```

## Exemplo de Uso

Pergunta:

```text
o que é inner join?
```

Resposta:

```text
INNER JOIN retorna apenas registros com correspondência entre as tabelas.
```

## Autor

Projeto desenvolvido para o Lab da DIO - Construindo um Assistente Virtual com Inteligência Artificial.