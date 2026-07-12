# AWS Glue

- É um produto de ETL (Extração, Transformação, Carga) serverless (sem servidor)
- Semelhante ao AWS Datapipeline (que pode fazer ETL), mas que usa servidores (clusters EMR)
- O Glue é usado para mover e transformar dados entre a origem e o destino
- O Glue também rastreia (crawls) as fontes de dados e gera o AWS Glue Data catalog (catálogo de dados)
- Suporta uma gama de coleta de dados como fontes de dados: S3, RDS, fontes de dados compatíveis com JDBC e DynamoDB
- Suporta fluxos (streams) de dados como fontes de dados, como Kinesis Data Streams e Apache Kafka
- Destinos (targets) de dados suportados: S3, RDS, fontes de dados JDBC

## Data Catalog (Catálogo de Dados)

- Coleção de metadados persistentes sobre fontes de dados em uma região
- Fornece um catálogo de dados único (uniq data catalog) em cada região por conta
- Ajuda a evitar silos de dados: torna visíveis e navegáveis os dados que não seriam visíveis numa organização
- O Data Catalog pode ser usado pelo Amazon Athena, Redshift Spectrum, EMR e AWS Lake Formation
- Os dados são descobertos pela configuração de crawlers (rastreadores) e fornecendo credenciais a eles para acessar as fontes de dados

## Glue Job (Trabalho do Glue)

- Trabalhos (jobs) de Extração, Transformação e Carga (Extract, Transform and Load)
- Os Jobs podem fazer a transformação usando scripts criados por nós
- Os Jobs são serverless (sem servidor), a AWS mantém um pool (reserva) de recursos
- Somos cobrados apenas pelos recursos que consumimos

---

# AWS Glue

- Is a serverless ETL (Extract, Transform, Load) product
- Similar to AWS Datapipeline (which can do ETL) but it uses servers (EMR clusters)
- Glue is used to move data and transform data between source and destination
- Glue also crawls data sources and generates the AWS Glue Data catalog
- Supports a range of data collection as data sources: S3, RDS, JDBC compatible data sources and DynamoDB
- Supports data streams as data sources such as Kinesis Data Streams and Apache Kafka
- Data targets supported: S3, RDS, JDBC data sources

## Data Catalog

- Collection of persistent metadata about data sources in a region
- Provides one uniq data catalog in every region per account
- It helps avoid data silos: makes data not visible in an organization be visible a able to be browsed
- Data Catalog can be used by Amazon Athena, Redshift Spectrum, EMR and AWS Lake Formation
- Data is discovered by configuring crawlers and givin it credentials to access data sources

## Glue Job

- Extract, Transform an Load jobs
- Jobs can do transformation by using scripts created by us
- Jobs are serverless, AWS maintains a pool of resources
- We are only billed by resources we consume