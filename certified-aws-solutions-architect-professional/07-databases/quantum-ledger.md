# Amazon Quantum Ledger Database - QLDB

- Parte da linha de produtos de Blockchain da AWS
- É um banco de dados somente de registro imutável e somente de acréscimo
- Fornece um log de transações verificável criptograficamente
- É transparente: o histórico completo sempre está acessível
- É um produto serverless; fornece Ledgers e Tabelas. Não temos servidores para gerenciar
- É resiliente em 3 AZs; replica dados dentro de cada uma dessas AZs
- Pode transmitir dados para o Amazon Kinesis; pode transmitir quaisquer alterações de dados para o Kinesis em tempo real
- É um modelo de banco de dados de documentos, armazenando documentos JSON (pares de chave-valor com uma estrutura aninhada)
- Fornece transações ACID
- Casos de uso para QLDB:
    - Qualquer coisa relacionada a finanças: saldos de contas e transações
    - Aplicações médicas: o histórico completo das alterações de dados importa
    - Logística: rastrear o movimento de objetos
    - Jurídico: rastrear o uso e a alteração de dados (custódia)

---

# Amazon Quantum Ledger Database - QLDB

- Part of AWS Blockchain part of products
- It as an immutable append-only ledger-only database
- It provides a cryptographically verifiable transaction log
- It is transparent: full history is always accessible
- It is a serverless product, it provides Ledgers and Tables. We have no servers to manage
- It is resilient through 3 AZs, replicates data within each of those AZs
- It can stream data to Amazon Kinesis, it can stream any changes to data into Kinesis in real-time
- It is a document database model, storing JSON documents (key-value pairs with a nested structure)
- Provides ACID transactions
- Use cases for QLDB:
    - Anything related to finance: account balances and transactions
    - Medical application: full history of data changes matters
    - Logistics: track movement of objects
    - Legal: track the usage and change of data (custody)