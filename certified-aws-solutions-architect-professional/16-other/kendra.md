# Amazon Kendra

- É um serviço de pesquisa inteligente
- Seu objetivo principal é ser projetado para imitar a interação com um especialista humano
- Suporta uma ampla gama de tipos de perguntas, como:
    - Factuais (Factoid): Quem (Who), O que (What), Onde (Where)
    - Descritivas: Como faço para meu gato parar de ser um idiota? (How do I get my cat to spot being a jek?)
    - Palavras-chave (Keyword): A que horas é o discurso de abertura (address pode ter múltiplos significados) - o Kendra ajuda a determinar a intenção (intent)

## Conceitos Principais (Key Concepts)

- **Index (Índice)**: dados pesquisáveis organizados de forma eficiente
- **Data Source (Fonte de Dados)**: onde os dados vivem, o Kendra se conecta e os indexa a partir deste local. Exemplos de locais são: S3, Confluence, Google Workspaces, RDS, OneDrive, Salesforce, Kendra Web Crawler, Workdocs, FSX, etc.
- Nós configuramos o Kendra para sincronizar uma fonte de dados com um índice com base num **cronograma (schedule)**. Isso deve manter o índice atualizado
- **Documents (Documentos)**: podem ser estruturados (FAQs) e não estruturados (HTML, PDF, etc.)

## Outros (Others)

- O Kendra integra-se com outros serviços da AWS: IAM, Identity Center (SSO) e outros

---

# Amazon Kendra

- Is an intelligent search service
- It's primary aim is to be designed to mimic interacting with a human expert
- Supports wide range if question types such as:
    - Factoid: Who, What, Where
    - Descriptive: How do I get my cat to spot being a jek?
    - Keyword: What time is the keynote address (address can have multiple meaning) - Kendra helps determine intent

## Key Concepts

- **Index**: searchable data organized in an efficient way
- **Data Source**: where the data lives, Kendra connects and indexes from this location. Example of locations are: S3, Confluence, Google Workspaces, RDS, OneDrive, Salesforce, Kendra Web Crawler, Workdocs, FSX, etc.
- We configure Kendra to synchronize a data source with an index based on a **schedule**. This should keep the index current
- **Documents**: can be structured (FAQs) and unstructured (HTML, PDF, etc.)

## Others

- Kendra integrates with other AWS services: IAM, Identity Center (SSO) and others