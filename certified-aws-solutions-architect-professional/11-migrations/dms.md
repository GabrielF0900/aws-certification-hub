# DMS - Database Migration Service (Serviço de Migração de Banco de Dados)

- As migrações de banco de dados são ações complexas de se executar
- O DMS é um serviço de migração de banco de dados gerenciado
- Começa usando uma instância de replicação rodando em EC2
- Essa instância executa uma ou mais tarefas de replicação (replication task)
- Para essas tarefas, precisamos especificar os endpoints de origem (source) e destino (target) nos bancos de dados de origem e alvo. **Um endpoint deve estar na AWS!** Não podemos usar o produto entre migrações exclusivamente on-premises
- Os bancos de dados de origem suportados são: MySQL, Aurora, Microsoft SQL, MariaDB, MongoDB, PostgreSQL, Oracle, Azure SQL, etc.
- O DMS usa trabalhos (jobs) para lidar com as migrações. Os trabalhos podem ser de 3 tipos:
    - Migrações de carga total (Full load migrations): usadas para migrar dados existentes, simplesmente migra os dados da origem para o destino. Ótimo se pudermos suportar uma interrupção (outage) para o BD de origem
    - Carga total + CDC (Change data capture - Captura de dados de alteração): migra os dados existentes e replica quaisquer alterações contínuas (ongoing changes)
    - Somente CDC: projetado para replicar apenas alterações de dados. Em algumas situações, pode ser mais eficiente usar outras ferramentas para a migração completa e usar o CDC apenas para mudanças contínuas depois
- O DMS não suporta nenhuma forma de conversão de esquema (schema conversions), para isso devemos usar o Schema Conversion Tool (SCT) fornecido pela AWS

## SCT - Schema Conversion Tool (Ferramenta de Conversão de Esquema)

- SCT é um aplicativo independente (standalone app) usado para converter uma engine de banco de dados em outra, incluindo a conversão de esquema de um BD para o S3
- SCT não é usado quando se migra entre BDs do mesmo tipo
- O SCT funciona com bancos de dados OLTP (MySQL, Oracle, Aurora, etc.) e bancos de dados OLAP (Teradata, Oracle, Vertica, Greenplum, etc.)
- Exemplo de quando o SCT deve ser usado: MSSQL on-premises -> RDS MySQL (a engine muda de MSSQL para MySQL) ou de Oracle -> Aurora

## DMS e Snowball

- Migrações maiores podem implicar em mover bancos de dados com tamanhos de vários TB
- Mover dados pelas redes leva tempo e consome capacidade
- O DMS é capaz de utilizar produtos Snowball para migrar bancos de dados
- Passos da migração:
    1. Use o SCT para extrair dados localmente e mova os dados para um Snowball
    2. Envie o dispositivo de volta para a AWS. Eles carregarão os dados num bucket S3
    3. O DMS migra do S3 para a fonte de destino (target source)
    4. O Change Data Capture (CDC) pode capturar alterações e, via S3 como intermediário, elas também são gravadas no banco de dados de destino

---

# DMS - Database Migration Service

- Database migrations are complex actions to perform
- DMS it is a managed database migration service
- It starts with using a replication instance running on EC2
- This instance runs one or more replication task
- For these tasks we have to specify the source and destination endpoints at source and target databases. **One endpoint must be on AWS!** We can't use the product between on-premises migrations
- Source databases supported are: MySQL, Aurora, Microsoft SQL, MariaDB, MongoDB, PostgreSQL, Oracle, Azure SQL, etc.
- DMS uses jobs to handle migrations. Jobs can be one of 3 types:
    - Full load migrations: used to migrate existing data, simply migrates the data from source to target. Great if we can afford an outage for the source DB
    - Full load + CDC (Change data capture): migrates the existing data and replicates any ongoing changes
    - CDC only: designed to replicate only data changes. In some situations might be more efficient to use other tools for full migration and use CDC only for ongoing changes afterwards
- DMS does not support any form of schema conversions, for this we should use Schema Conversion Tool (SCT) provided by AWS

## SCT - Schema Conversion Tool

- SCT is a standalone app used for converting one database engine to another including conversion of schema from a DB to S3
- SCT is not used when migrating between DBs of the same type
- SCT works with OLTP DBS (MySQL, Oracle, Aurora, etc.) and OLAP databases (Teradata, Oracle, Vertica, Greenplum, etc.)
- Example when SCT should be used: on-premises MSSQL -> RDS MySQL (the engine changes from MSSQL to MySQL) or from Oracle -> Aurora

## DMS and Snowball

- Larger migrations might imply moving databases with sizes of multi-TB
- Moving data over networks takes time and consumes capacity
- DMS is able to utilize Snowball products to migrate databases
- Migration steps:
    1. Use SCT to extract data locally and move the data to a Snowball
    2. Ship the device back to AWS. They will load the data into an S3 bucket
    3. DMS migrates from S3 into a target source
    4. Change Data Capture (CDC) can capture changes and via S3 intermediary they are also written to the target database