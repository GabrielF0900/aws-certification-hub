# Elastic Beanstalk - EB

- É um produto de plataforma como serviço (PaaS - Platform as a Service) na AWS, o que significa que o fornecedor lida com toda a infraestrutura e nós fornecemos apenas o código
- O EB é um produto focado no desenvolvedor, fornecendo ambientes de aplicativos gerenciados
- Em alto nível, os desenvolvedores fornecem código e o EB cuida da infraestrutura
- O EB é totalmente personalizável - usa produtos da AWS nos bastidores, provisionados com o CloudFormation
- O uso do EB requer suporte a aplicativos, há coisas a fazer como desenvolvedor. Isso não é gratuito e não é algo que um usuário final não técnico poderia fazer

## Plataformas (Platforms)

- O EB é capaz de aceitar código em muitas linguagens conhecidas como plataformas
- O EB tem suporte para linguagens integradas (built-in), Docker e plataformas personalizadas
- Linguagens integradas suportadas: Go, Java SE, Java Tomcat, .NET Core (Linux) e .NET (Windows), Node.JS, PHP, Python, Ruby
- Opções de Docker: docker de contêiner único (single container) e docker multicontêiner (multi container - ECS)
- Docker pré-configurado: maneira de fornecer runtimes que ainda não são suportados nativamente, exemplo: Java com Glassfish
- Podemos criar nossa própria plataforma personalizada usando o packer, que pode ser usada com o Beanstalk

## Terminologia do EB

- **Aplicativo Elastic Beanstalk (Elastic Beanstalk Application)**: é uma coleção de coisas relacionadas a um aplicativo - um contêiner/pasta
- **Versão do Aplicativo (Application Version)**: versão com rótulo (labeled) específico de código implantável (deployable) para um aplicativo. O pacote fonte (source bundle) é armazenado no S3
- **Ambientes (Environments)**: são contêineres de infraestrutura e configuração para uma versão específica
- Cada ambiente é uma **camada de servidor da web (web server tier)** ou uma **camada de trabalho (worker tier)**. A camada do servidor da web foi projetada para se comunicar com os usuários finais. A camada de trabalho foi projetada para processar o trabalho das camadas da web. A camada do servidor da web e a camada de trabalho se comunicam usando filas SQS
- Cada ambiente está rodando uma versão específica em qualquer momento
- Cada ambiente tem seu próprio CNAME, uma troca (SWAP) de CNAME pode ser feita para trocar o DNS do ambiente

## Políticas de Implantação (Deployment Policies)

- **Tudo de uma vez (All at once)**:
    - Implanta em todas as instâncias de uma só vez
    - É rápido e simples, mas causará uma breve interrupção (outage)
    - Recomendado para ambientes de teste e desenvolvimento
- **Contínuo (Rolling)**:
    - O código do aplicativo é implantado em lotes contínuos (rolling batches)
    - É mais seguro, já que a implantação continuará apenas se o lote anterior estiver saudável (healthy)
    - O aplicativo encontrará perda de capacidade com base no tamanho do lote (batch size) que você selecionou.
    - Precisamos selecionar o tamanho do lote com base na decisão de quantas instâncias você pode tolerar fora de serviço a qualquer momento.
- **Contínuo com lote adicional (Rolling with additional batch)**:
    - Mesmo que a implantação contínua (rolling deployment), com o acréscimo de ter um novo lote para manter a capacidade durante o processo de implantação
    - Recomendado para ambiente de produção com carga (load) real
    - Essa implantação leva mais tempo, mas é mais segura e boa para prod (produção) porque não perdemos nenhuma capacidade.
- **Imutável (Immutable)**:
    - Um novo ASG temporário é criado com a versão mais recente do aplicativo
    - Assim que a validação estiver concluída, a stack antiga é removida
    - É mais fácil reverter (roll back), pois se algo der errado, as instâncias originais estarão disponíveis em seu estado original.
    - Tem o custo mais alto, pois usa o dobro de instâncias.
- **Divisão de tráfego (Traffic Splitting)**:
    - Instâncias novas (fresh instances) são criadas de maneira semelhante à implantação imutável
    - O tráfego será dividido entre a versão mais antiga e a mais recente
    - Permite realizar testes A/B na aplicação
    - Não tem quedas de capacidade, mas virá com um custo adicional
- **Azul/Verde (Blue/Green)**:
    - Não suportado automaticamente pelo EB
    - Requer troca manual (manual swap) de CNAME entre 2 ambientes
    - Fornece controle total em termos de quando queremos mudar (switch) para o novo ambiente

## EB e RDS

- Para acessar uma instância RDS a partir do EB, podemos criar uma instância RDS num ambiente EB
- Se fizermos isso, o RDS fica vinculado (linked) ao ambiente
- Se excluirmos o ambiente, o banco de dados também será excluído
- Se vincularmos um banco de dados a um ambiente, temos acesso às seguintes propriedades do ambiente:
    - `RDS_HOSTNAME`
    - `RDS_PORT`
    - `RDS_DB_NAME`
    - `RDS_USERNAME`
    - `RDS_PASSWORD`
- Outra alternativa é criar a instância RDS fora do EB
- As propriedades de ambiente acima não são fornecidas automaticamente neste caso, podemos criá-las manualmente
- Com este método o ciclo de vida do RDS não está vinculado ao ambiente EB
- Desacoplando (Decoupling) um RDS existente de um ambiente EB:
    1. Crie um Snapshot
    2. Habilite a Proteção Contra Exclusão (Delete Protection)
    3. Crie um novo ambiente EB com a mesma versão do aplicativo
    4. Certifique-se de que o novo ambiente pode se conectar ao BD
    5. Troque o ambiente (Swap environment - CNAME ou DNS)
    6. Encerre (Terminate) o ambiente antigo - isso tentará encerrar a instância RDS
    7. Localize a stack em estado de falha `DELETE_FAILED` na console do CloudFormation, exclua a stack manualmente e escolha reter os recursos presos (retain stuck resources)

## Personalizando via `.ebextensions`

- Podemos incluir diretivas para personalizar ambientes EB usando a pasta `.ebextensions`
- Qualquer coisa adicionada nesta pasta como YAML ou JSON e que termine em `.config` é considerada um arquivo de configuração de extensão EB. Esses arquivos de configuração são definições do CloudFormation e são usados para influenciar o próprio ambiente EB para alterar sua configuração ou provisionar novos recursos
- O EB usará o CFN para criar recursos adicionais no ambiente especificado nos arquivos `.config`
- Estes arquivos podem ter as seguintes seções:
    - `option_settings`: permite-nos definir opções de recursos (exemplo: usar NLB em vez de ALB para o ambiente EB)
    - `Resources`: permite-nos criar novos recursos usando o CFN (exemplo: configurar cluster OpenSearch para nosso ambiente)
    - Seções adicionais: packages, sources, files, users, groups, commands, container_commands e services

## EB com HTTPS

- Para usar o HTTPS com o EB precisamos aplicar um certificado SSL ao balanceador de carga (load balancer)
- Podemos fazer isso usando a console do EB ou podemos usar o recurso `.ebextensions/securelistener-[alb|nlb].config`
- Também podemos configurar o grupo de segurança (security group) para permitir conexões SSL

## Clonagem de Ambiente (Environment Cloning)

- A clonagem permite criar um novo ambiente EB clonando ambientes existentes
- Ao clonar um ambiente, não precisamos configurar manualmente opções, variáveis de ambiente, recursos e outras configurações
- Um clone copia qualquer instância RDS definida, mas os dados não são copiados por padrão
- A clonagem de EB não inclui nenhuma alteração não gerenciada (un-managed changes) em recursos do ambiente. Alterações em recursos da AWS que fazemos usando ferramentas que não sejam a console/CLI/API do EB são consideradas alterações não gerenciadas
- Para clonar um ambiente da linha de comando eb, podemos usar o comando `eb clone <ENV>`

## EB e Docker

### Modo de Contêiner Único (Single Container Mode)

- Só podemos rodar um contêiner num host Docker
- Este modo usa EC2 com Docker, não o ECS
- Para usar este modo temos que fornecer algumas configurações:
    - `Dockerfile`: usado para criar uma nova imagem de contêiner a partir deste arquivo
    - `Dockerrun.aws.json` (versão 1): para usar uma imagem docker existente. Podemos configurar portas, volumes e outros atributos do Docker
    - `Docker-compose.yml`: se quisermos usar o Docker compose

### Modo Multicontêiner (Multi-Container Mode)

- O Elastic Beanstalk usa o ECS para criar um cluster
- O ECS usa instâncias EC2 provisionadas no cluster e um ELB para HA
- O EB cuida das tarefas do ECS, criação do cluster, definição da tarefa (task definition) e execução da tarefa
- Precisamos fornecer um arquivo `Dockerrun.aws.json` (~~versão 2~~ versão 3) no pacote de origem do aplicativo (source bundle) no nível da raiz (root)
- Quaisquer imagens precisam ser armazenadas num registro de contêiner (container registry), como o ECR

---

# Elastic Beanstalk - EB

- It is a platform as a service (PaaS) product in AWS, meaning the vendors handles all the infrastructure, we provide the code only
- EB is a developer focused product, providing managed application environments
- At a high level, developers provide code and EB handles infrastructure
- EB is fully customizable - uses AWS products under the covers provisioned with CloudFormation
- Using EB requires application support, there are things to do as a developer. This does not come for free, and it not something a non-technical end-user could do

## Platforms

- EB is capable of accepting code in many languages known as platforms
- EB has support for built-in languages, Docker and custom platforms
- Built-in supported languages: Go, Java SE, Java Tomcat, .NET Core (Linux) and .NET (Windows), Node.JS, PHP, Python, Ruby
- Docker options: single container docker and multi container docker (ECS)
- Pre-configured Docker: way to provide runtimes which are not yet natively supported, example Java with Glassfish
- We can create our own custom platform using packer which can be used with Beanstalk

## EB Terminology

- **Elastic Beanstalk Application**: is a collection of things relating to an application - a container/folder
- **Application Version**: specific labeled version of deployable code for an application. The source bundle is stored in S3
- **Environments**: are containers of infrastructure and configuration for a specific version
- Each environment is either a **web server tier** or a **worker tier**. The web server tier is designed to communicate with the end-users. The worker tier is designed to process work from the web tiers. Web server tier and worker tier communicate using SQS queues
- Each environment is running a specific version at any given time
- Each environment has its own CNAME, a CNAME SWAP can be done to exchange to environment DNS

## Deployment Policies

- **All at once**: 
    - Deploy to all instances at once
    - It is quick and simple, but it will cause a brief outage
    - Recommended for testing and development environments
- **Rolling**:
    - Application code is deployed in rolling batches
    - It is safer, since the deployment will continue only if the previous batch is healthy
    - The application will encounter loss in capacity based on size of batch you selected.
    - We need to select the batch size based on decision how many instances you can tolerate out of service at any one time. 
- **Rolling with additional batch**:
    - Same as rolling deployment, with the addition of having a new batch in order to maintain capacity during the deployment process
    - Recommended for production environment with real load
    - This deployment takes longer time but is asfer and good for prod because we don't drop any capacity.
- **Immutable**:
    - New temporary ASG is created with the newer version of the application
    - Once the validation is complete, the older stack is removed
    - It is easier to roll back as if anything goes wrong the original instances are available in their original state.
    - It has the highest cost as it uses the double of instances.
- **Traffic Splitting**:
    - Fresh instances are created in a similar way as in case of immutable deployment
    - Traffic will be split between the older and the newer version
    - Allows to perform A/B testing on the application
    - It does not have capacity drops, but it will come with an additional cost
- **Blue/Green**:
    - Not automatically supported by EB
    - Requires manual CNAME swap between 2 environments
    - Provides full control in terms of when we would want to switch to the new environment

## EB and RDS

- In order to access an RDS instance from EB we can create an RDS instance within an EB environment
- If we do this, the RDS is linked to the environment
- If we delete the environment, the database will also be deleted
- If we link a database to an environment, we get access to the following environment properties:
    - `RDS_HOSTNAME`
    - `RDS_PORT`
    - `RDS_DB_NAME`
    - `RDS_USERNAME`
    - `RDS_PASSWORD`
- Other alternative is to create the RDS instance outside of the EB
- The environment properties above are not automatically provided in this case, we can create them manually
- With this method the RDS lifecycle is not tied to the EB environment
- Decoupling an existing RDS from an EB environment:
    1. Create a Snapshot
    2. Enable Delete Protection
    3. Create a new EB environment with the same app version
    4. Ensure new environment can connect to the DB
    5. Swap environment (CNAME or DNS)
    6. Terminate the old environment - this will try to terminate the RDS instance
    7. Locate the `DELETE_FAILED` stack in CloudFormation console, manually delete the stack and pick to retain stuck resources

## Customizing via `.ebextensions`

- We can include directive to customize EB environments using `.ebextensions` folder
- Anything added in this folder as YAML or JSON and it ends in `.config` is regarded to be an EB extension configuration file. These configurations files are CloudFormation definitions, and they are used to influence the EB environment itself to change its configuration or provision new resources
- EB will use CFN to create additional resources within the environment specified in the `.config` files
- These files can have the following sections:
    - `option_settings`: allows us to set options of resources (example: use NLB instead of ALB for the EB environment)
    - `Resources`: allows us to create new resources using CFN (example: configure OpenSearch cluster for our environment)
    - Additional sections: packages, sources, files, users, groups, commands, container_commands and services

## EB with HTTPS

- To use HTTPS with EB we need to apply an SSL certificate to the load balancer
- We can do this using the EB console or we can use the `.ebextensions/securelistener-[alb|nlb].config` feature
- We can configure the security group as well to allow SSL connections

## Environment Cloning

- Cloning allows to create new EB environment by cloning existing environments
- By cloning an environment we don't have to manually configure options, environment variables, resources and other settings
- A clone does copy any RDS instance defined, but the data is not copied by default
- EB cloning does not include any un-managed changes to resources from the environment. Changes to AWS resources we make using tools other than the EB console/CLI/API are considered un-managed changes
- To clone an environment from the eb command line we can use `eb clone <ENV>` command

## EB and Docker

### Single Container Mode

- We can only run one container in one Docker host
- This mode uses EC2 with Docker, not ECS
- In order to use this mode we have to provide a few configurations:
    - `Dockerfile`: used to create a new container image from this file
    - `Dockerrun.aws.json` (version 1): to use an existing docker image. We can configure ports, volumes and other Docker attributes
    - `Docker-compose.yml`: if we want to use Docker compose

### Multi-Container Mode

- Elastic Beanstalk uses ECS to create a cluster
- ECS uses EC2 instances provisioned in the cluster and an ELB for HA
- EB takes care of ECS tasks, cluster creation, task definition and task execution
- We need to provide an `Dockerrun.aws.json` (~~version 2~~ version 3) file in the application source bundle (root level)
- Any images need to be stored in a container registry such as ECR