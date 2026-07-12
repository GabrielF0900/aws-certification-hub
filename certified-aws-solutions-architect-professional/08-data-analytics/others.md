# Outros Produtos Relacionados à Análise de Dados

## AWS Data Exchange

- O AWS Data Exchange é um serviço que ajuda a AWS a compartilhar e gerenciar facilmente direitos de dados de outras organizações em escala
- Como receptor de dados, podemos rastrear e gerenciar todas as nossas concessões de dados e assinaturas de dados do AWS Marketplace em um só lugar
- Para remetentes de dados, o AWS Data Exchange elimina a necessidade de criar e manter qualquer infraestrutura de entrega e direitos de dados

## AWS Data Pipeline

- O AWS Data Pipeline é um serviço web que podemos usar para automatizar o movimento e a transformação de dados
- Podemos definir fluxos de trabalho orientados a dados, de modo que as tarefas possam depender da conclusão bem-sucedida de tarefas anteriores
- Componentes de um pipeline de dados:
    - Definição do Pipeline: especifica a lógica de negócios do nosso gerenciamento de dados
    - Pipeline: agenda e executa tarefas criando instâncias Amazon EC2 para realizar as atividades de trabalho definidas
    - Executores de Tarefas (Task Runners): pesquisam tarefas e as executam. Por exemplo, o Task Runner pode copiar arquivos de log para o Amazon S3 e iniciar clusters Amazon EMR. O Task Runner é instalado e executado automaticamente nos recursos criados pelas definições de pipeline
- Exemplos de casos de uso:
    - Podemos usar o AWS Data Pipeline para arquivar os logs do servidor web no Amazon Simple Storage Service (Amazon S3) todos os dias e, em seguida, executar um cluster Amazon EMR semanalmente sobre esses logs para gerar relatórios de tráfego

## AWS Lake Formation

- O AWS Lake Formation é um serviço que facilita a configuração de um data lake seguro em dias
- Criar um data lake com o Lake Formation é tão simples quanto definir fontes de dados e quais políticas de acesso e segurança de dados queremos aplicar
- Ajuda a coletar e catalogar dados de bancos de dados e armazenamento de objetos, mover os dados para um novo data lake Amazon S3, limpar e classificar dados usando algoritmos de aprendizado de máquina e proteger o acesso a dados sensíveis

---

# Other Data Analytics Related Products

## AWS Data Exchange

- AWS Data Exchange is a service that helps AWS easily share and manage data entitlements from other organizations at scale
- As a data receiver, we can track and manage all of our data grants and AWS Marketplace data subscriptions in one place
- For data senders, AWS Data Exchange eliminates the need to build and maintain any data delivery and entitlement infrastructure

## AWS Data Pipeline

- AWS Data Pipeline is a web service that we can use to automate the movement and transformation of data
- We you can define data-driven workflows, so that tasks can be dependent on the successful completion of previous tasks
- Components of a data pipeline:
    - Pipeline definition:  specifies the business logic of our data management
    - Pipeline: schedules and runs tasks by creating Amazon EC2 instances to perform the defined work activities
    - Task Runners: polls for tasks and then performs those tasks. For example, Task Runner could copy log files to Amazon S3 and launch Amazon EMR clusters. Task Runner is installed and runs automatically on resources created by your pipeline definitions
- Use case examples:
    - We can use AWS Data Pipeline to archive your web server's logs to Amazon Simple Storage Service (Amazon S3) each day and then run a weekly Amazon EMR (Amazon EMR) cluster over those logs to generate traffic reports

## AWS Lake Formation

- AWS Lake Formation is a service that makes it easy to set up a secure data lake in days
- Creating a data lake with Lake Formation is as simple as defining data sources and what data access and security policies we want to apply
- Helps us collect and catalog data from databases and object storage, move the data into new Amazon S3 data lake, clean and classify data using machine learning algorithms, and secure access to sensitive data