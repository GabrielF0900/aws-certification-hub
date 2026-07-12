# Amazon Athena

- É um serviço de consulta interativa sem servidor
- Podemos pegar dados armazenados no S3 e realizar consultas ad-hoc nos dados pagando apenas pelos dados consumidos
- O Athena usa um processo chamado **Schema-on-read** - tradução semelhante a tabela
- Os dados originais no S3 nunca são alterados; permanecem na forma original. São traduzidos para o esquema predefinido quando lidos para processamento
- Formatos suportados pelo Athena: XML, JSON, CSV/TSV, AVRO, PARQUET, ORC, Apache, CloudTrail, VPC Flowlogs, etc. Suporta formatos padrão de dados estruturados, semiestruturados e não estruturados
- "Tabelas" são definidas antecipadamente em um catálogo de dados e os dados são projetados quando lidos. Permite consultas semelhantes a SQL nos dados sem transformar os dados de origem
- O Athena não tem infraestrutura. Não precisamos configurar nada antecipadamente
- O Athena é ideal para situações onde carregar/transformar dados não é desejado
- É preferido para consultar logs da AWS: VPC Flow Logs, CloudTrail, logs ELB, relatórios de custo, etc.
- Pode consultar dados do Glue Data Catalog e Web Server Logs
- Athena Federated Query: o Athena agora suporta consultas de outras fontes de dados além do S3. Requer um conector de fonte de dados (AWS Lambda)

---

# Amazon Athena

- It is a serverless interactive querying service
- We can take data stored in S3 and perform ad-hoc queries on the data paying only for the data consumed
- Athena uses a process named **Schema-on-read** - table-like translation
- Original data in S3 is never changed, it remains in its original form. It is translated to the predefined schema when it is read for processing
- Supported formats by Athena: XML, JSON, CSV/TSV, AVRO, PARQUET, ORC, Apache, CloudTrail, VPC Flowlogs, etc. Supports standard formats of structured data, semi-structured and unstructured data
- "Tables" are defined in advance in a data catalog and data is projected through when read. It allows SQL-like queries on data without transforming source data
- Athena has no infrastructure. We don't need set up anything in advance
- Athena is ideal for situations where loading/transforming data isn't desired
- It is preferred for querying AWS logs: VPC Flow Logs, CloudTrail, ELB logs, cost reports, etc.
- Can query data form Glue Data Catalog and Web Server Logs
- Athena Federated Query: Athena now supports querying other data sources than S3. Requires a data source connector (AWS Lambda)