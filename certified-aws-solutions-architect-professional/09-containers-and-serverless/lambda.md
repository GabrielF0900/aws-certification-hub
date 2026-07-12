# AWS Lambda

- Lambda é um produto de Função como Serviço (Function-as-a-Service - FaaS). Nós fornecemos código especializado de curta duração e focado para o Lambda, e ele se encarregará de executá-lo e nos cobrar apenas pelo que consumimos
- Toda função Lambda usa um tempo de execução (runtime) suportado, por exemplo: Python 3.8, Java 8, NodeJS
- Toda função Lambda é carregada e executada em um ambiente de tempo de execução
- Quando criamos uma função, definimos os recursos que ela usará. Definimos a memória diretamente e a alocação de uso da CPU indiretamente (com base na quantidade de memória)
- Somos cobrados apenas pela duração em que a função está em execução, com base no número de invocações e nos recursos especificados
- Lambda é uma parte fundamental das arquiteturas serverless na AWS
- Lambda tem suporte para os seguintes runtimes:
    - Python
    - Ruby
    - Go
    - Java
    - C#
    - Personalizado usando camadas Lambda (Lambda layers), como Rust
- Tamanho do pacote de implantação do Lambda:
    - 50 MB compactado (zipped)
    - 250 MB descompactado (unzipped)
    - Até 10 GB como imagem Docker
- Funções Lambda não mantêm estado (stateless), o que significa que nenhum dado sobra após uma invocação
- Ao criar uma função Lambda, definimos a memória. A memória pode ser entre 128 MB e 10240 MB, em incrementos de 1 MB
- Não definimos diretamente a vCPU alocada para cada função; ela escalará automaticamente com a memória: 1769 MB de memória fornecem 1 vCPU
- O ambiente de execução possui 512 MB (por padrão) de armazenamento disponível como `/tmp`. Podemos dimensionar esse armazenamento para até 10240 MB. Podemos usar esse armazenamento para o que precisarmos, desde que assumamos que ele estará vazio a cada execução da função
- A função Lambda pode rodar por até 15 minutos; após esse tempo, ocorrerá um timeout (tempo limite esgotado)
- A segurança para uma função Lambda é controlada pela função de execução (execution role). Esta é uma função IAM anexada ao Lambda. Ela pode ter permissões para integração com outros serviços da AWS

## Redes Lambda (Lambda Networking)

- As funções Lambda podem ter 2 tipos de modos de rede:
    - Pública (padrão):
        - A Lambda pode acessar serviços públicos da AWS como SQS, DynamoDB, etc. e também serviços baseados na internet
        - A Lambda possui conectividade de rede para serviços públicos rodando na internet
        - Oferece o melhor desempenho para a Lambda, nenhuma rede específica do cliente é necessária
        - No modo de rede pública, a função Lambda não poderá acessar recursos dentro de uma VPC, a menos que os recursos tenham IPs públicos e os controles de segurança permitam acesso externo
    - Rede VPC:
        - As funções Lambda rodarão dentro de uma VPC, portanto acessarão tudo na VPC, assumindo que NACLs e SGs permitam o acesso
        - Elas não conseguirão acessar serviços fora da VPC, a menos que haja configuração de rede na VPC permitindo acesso externo
        - A Lambda precisa da permissão `EC2Networking` para poder criar ENIs na VPC
        - Funções Lambda baseadas em VPC não rodam diretamente na VPC; elas usarão uma ENI compartilhada para acessar recursos na VPC, desde que todas as funções tenham o mesmo Security Group (Grupo de Segurança). Caso novos Security Groups sejam anexados a uma certa Lambda, novas ENIs serão colocadas dentro da VPC
        - Na criação da função, uma certa ENI pode ser criada para acessar a VPC. A configuração inicial levaria até 90 segundos. Essa configuração ocorrerá apenas uma vez, não a cada invocação

## Segurança da Lambda

- Existem 2 partes principais do modelo de segurança:
    - As Funções Lambda assumirão uma role de execução (execution role) para acessar outros recursos da AWS
    - Políticas de recursos (Resource policies): similares às políticas de recursos do S3. Permitem que contas externas invoquem funções Lambda ou que certos serviços usem funções Lambda. As políticas de recursos podem ser modificadas usando CLI/API (atualmente não podem ser alteradas no console)

## Logs da Lambda

- A Lambda usa CloudWatch Logs e X-Ray
- Os logs das execuções da Lambda são armazenados no CloudWatch Logs
- Detalhes sobre métricas da Lambda são armazenados no CloudWatch Metrics
- A Lambda pode ser integrada ao X-Ray para rastreamento distribuído (distributed tracing)
- Para que a Lambda consiga gerar logs, precisamos dar permissões via execution role (role de execução)

## Invocações da Lambda

- Existem 3 formas de invocar funções Lambda:
    - **Invocação síncrona (Synchronous invocation)**:
        - Linha de comando ou API invocando a função diretamente
        - O CLI ou API esperará até a função retornar
        - O API Gateway também invocará Lambdas sincronicamente, um caso de uso para muitas aplicações serverless
        - Quaisquer erros ou tentativas (retries) devem ser tratados no lado do cliente
    - **Invocação assíncrona (Asynchronous invocation)**:
        - Utilizado tipicamente quando serviços AWS invocam a função (exemplo: eventos S3)
        - O serviço não espera pela resposta (dispare e esqueça / fire and forget)
        - A Lambda é responsável por qualquer falha. O reprocessamento acontecerá entre 0 e 2 vezes
        - A função deve ser idempotente para ser executada novamente
        - A Lambda pode ser configurada para enviar eventos a uma DLQ (Dead Letter Queue) caso o processamento não tenha sucesso após o número de tentativas
        - Destinos: eventos processados por Lambdas podem ser entregues a destinos como SQS, SNS, outra Lambda ou EventBridge. Eventos de sucesso e falha podem ser enviados a destinos diferentes
    - **Mapeamento de Fonte de Eventos (Event Source mapping)**:
        - Utilizado tipicamente em streams ou filas que não geram eventos sozinhas (Kinesis, DynamoDB streams, SQS)
        - Mapeadores de fonte de eventos (Event Source mappers) consultam (poll) esses streams e recuperam lotes (batches). Esses lotes podem ser quebrados em pedaços e enviados a várias invocações Lambda para processamento
        - Não podemos ter um lote parcialmente bem-sucedido; ou tudo funciona, ou nada funciona
- No caso do processamento de eventos em invocação assíncrona, para processar o evento não precisamos explicitamente de permissão para ler de quem enviou (sender)
- No caso do mapeamento de fonte de eventos, o mapeador está lendo da fonte. O mapeamento usa permissões da role de execução da Lambda para acessar o serviço de origem
- Mesmo que a função não leia dados diretamente do stream, a role de execução precisa de direitos de leitura para lidar com o lote de eventos
- Qualquer lote que falhe consistentemente ao ser processado pode ser enviado para uma fila SQS ou tópico SNS para processamento posterior

## Versões da Lambda

- Podemos definir diferentes versões para uma determinada função
- Uma versão de uma função é o código + a configuração da função
- Quando publicamos uma versão, ela se torna imutável, não podendo mais ser alterada. Ela até ganha um ARN (Amazon Resource Name) próprio
- `$Latest` (A mais recente) aponta para a última versão não publicada da Lambda (não é imutável)
- Podemos também definir aliases (DEV, STAGE, PROD) que apontam para uma versão da função. Aliases podem ser alterados para apontar para outras versões

## Tempos de Inicialização da Lambda (Start-up Times)

- O código Lambda roda dentro de um ambiente de execução (contexto de execução)
- Na primeira invocação, esse contexto de execução precisa ser criado e isso leva tempo
- Esse processo é conhecido como cold start (partida a frio) e pode levar 100ms ou mais
- Se a função for invocada novamente sem muito intervalo, pode usar o mesmo contexto de execução. Isso é chamado de warm start (partida a quente)
- Cada invocação de função roda num ambiente de execução por vez. Se múltiplas instâncias paralelas forem necessárias, os contextos exigirão cold starts
- **Concorrência provisionada (Provisioned concurrency)**: podemos provisionar um ou mais contextos de execução com antecedência para invocações da Lambda
- Para melhorar a performance, podemos usar a pasta `/tmp` para baixar dados previamente. Se outra invocação usar o mesmo contexto de execução, ela conseguirá acessar os dados já baixados
- Podemos criar conexões de banco de dados fora do manipulador da Lambda (Lambda handler). Elas também estarão disponíveis para outras invocações depois

## Manipulador de Função Lambda (Lambda Function Handler)

- Execuções de funções Lambda têm ciclos de vida
- O código da função roda dentro de um ambiente de execução
- Fases do ciclo de vida:
    - `INIT`: cria ou "descongela" o ambiente de execução
        - Possui os seguintes subcomponentes:
            - `EXTENSION INIT` (Inicialização de Extensão)
            - `RUNTIME INIT` (Inicialização de Tempo de Execução)
            - `FUNCTION INIT` (Inicialização de Função)
        - A fase Init roda apenas em cold-starts (partidas a frio)
    - `INVOKE`: executa o manipulador de função (cold start)
    - `NEXT INVOKE`(s) (PRÓXIMAS INVOCAÇÕES): warm start usando o mesmo ambiente
    - `SHUTDOWN`: o ambiente de execução é terminado após um período de inatividade
        - Possui os seguintes subcomponentes:
            - `RUNTIME SHUTDOWN`
            - `EXTENSION SHUTDOWN`
        - Podemos usar a Concorrência Provisionada para evitar um cold-start no caso de a Lambda ser terminada

## Versões e Aliases da Lambda

- Funções não publicadas podem ser alteradas e implantadas
- A versão `$LATEST` do código da Lambda pode ser editada e implantada
- Podemos pegar o estado atual da função e publicá-lo, o que criará uma versão imutável
- Se a função for publicada, o código, as dependências, as configurações de runtime e variáveis de ambiente na versão criada não poderão ser editados
- Cada versão ganha um ARN único (ARN Qualificado)
- ARN não qualificado (Unqualified ARN) aponta para a função sem uma versão específica (`$LATEST`)
- Um alias é um ponteiro para a versão de uma função
- Exemplo: PROD => function:1, BETA => function:2
- Cada alias tem um ARN único
- Aliases podem ser atualizados, mudando a versão a que fazem referência
- Úteis para deployments PROD/DEV, BLUE/GREEN, testes A/B
- Também podemos usar roteamento por alias (alias routing): enviar uma certa porcentagem de requisições para a v1 e outra porcentagem para a v2. Ambas as versões precisam da mesma role, a mesma DLQ (ou nenhuma DLQ) será usada e ambas precisam estar publicadas

## Variáveis de Ambiente da Lambda

- Pares de chave e valor associados às funções Lambda
- Por padrão, são associadas ao `$LATEST` - podem ser editadas
- Se forem publicadas, não poderão ser editadas
- Elas podem ser acessadas de dentro do ambiente de execução
- As variáveis de ambiente podem ser criptografadas com o KMS
- Permitem que a execução do código seja ajustada com base em variáveis

## Camadas Lambda (Lambda Layers)

- Usadas para separar bibliotecas e dependências das funções Lambda
- Reduz o tamanho do pacote de implantação
- Camadas podem ser reutilizadas por múltiplas funções Lambda
- Bibliotecas nas camadas são extraídas na pasta `/opt`
- Camadas permitem novos runtimes que não são suportados explicitamente pela AWS

## Imagens de Contêiner Lambda

- Até pouco tempo, o Lambda era considerado um produto Function as a Service (FaaS), o que significava a criação de uma função, envio de código e execução
- Muitas organizações usam contêineres e processos CI/CD criados para contêineres
- O Lambda agora é capaz de usar imagens de contêiner
- É uma forma alternativa de empacotar o código da função e usá-lo com o produto Lambda
- Lambda Runtime API - tem que ser incluída nas imagens de contêiner, é um pacote que permite a interação entre o contêiner e a Lambda
- AWS Lambda Runtime Interface Emulator (RIE): usado para testes locais do Lambda

## Lambda e ALB (Application Load Balancer)

- Funções Lambda podem ser registradas em grupos de destino (target groups) de um ALB
- A comunicação entre o usuário e o ALB é via HTTP/HTTPS, não havendo diferença em relação a se conectar a um servidor clássico (EC2) da perspectiva do usuário
- Quando o ALB recebe uma requisição do cliente, ele invoca de forma síncrona a função Lambda
- O LB passa uma estrutura JSON para a função Lambda, dentro da estrutura `Event`. Isso tem que ser interpretado pela Lambda. O que acontece na prática é que o LB traduz o request HTTP(S) para um evento compatível com a Lambda, ao qual a Lambda responde com um objeto JSON que é traduzido de volta para resposta HTTP/HTTPS
- Cabeçalhos de múltiplos valores (Multi-Value headers):
    - Por exemplo, vamos usar esta URL para a Lambda: http://catagram.io?&search=roffle&search=winkie
    - Sem cabeçalhos multi-valor, a Lambda recebe o seguinte:
        ```
        "queryStringParameters": {
            "search": "winkie"
        }
        ```
    - Se os cabeçalhos multi-valor forem habilitados, a Lambda recebe isso:
        ```
        "multiValueQueryStringParameters": {
            "search": ["roffle", "winkie"]
        }
        ```

---

# AWS Lambda

- Lambda is a Function-as-a-Service (FaaS) product. We provide specialized short running focused code for Lambda and it will take care running it and billing us for only what we consume
- Every Lambda function uses a supported runtime, example: Python 3.8, Java 8, NodeJS
- Every Lambda function is loaded into an executed in a runtime environment
- When we create a function we define the resources the function will use. We define the memory directly and CPU usage allocation indirectly (based on the amount of memory)
- We are only billed for the duration the function is running based on the number of invocations and the resources specified
- Lambda is a key part of serverless architectures in AWS
- Lambda has support for the following runtimes:
    - Python
    - Ruby
    - Go
    - Java
    - C#
    - Custom using Lambda layers (such as Rust)
- Lambda deployment package size:
    - 50 MB zipped
    - 250 MB unzipped
    - Up to 10 GB as a Docker image
- Lambda functions are stateless, meaning there is no data left over after an invocation
- When creating a Lambda function we define the memory. The memory can be between 128 MB and 10240 MB in 1 MB steps
- We do not directly define the vCPU allocated to each function, it will automatically scale with the memory: 1769 MB of memory gives 1 vCPU
- The runtime env. has a 512 MB (by default) storage available as `/tmp`. We can scale this storage up to 10240 MB. We can use this storage for whatever we need as long as we assume that it is blank at each execution of the function
- Lambda function can run up to 15 minutes, after this a timeout will occur
- The security for a Lambda function is controlled by the execution role. This is an IAM role attached to the function. This can have permissions for integration with other AWS services

## Lambda Networking

- Lambda functions can have 2 types of networking modes:
    - Public (default):
        - Lambda can access public AWS services such as SQS, DynamoDB, etc. and also internet based services
        - Lambda has network connectivity to public services running on the internet
        - Offers the best performance for Lambda, no customer specific networking is required
        - With public networking mode Lambda function wont be able to access resources in a VPC unless the resources do have public IPs and security controls allow external access
    - VPC Networking:
        - Lambda functions will run inside a VPC, so they will access everything in a VPC, assuming NACLs and SGs allow access
        - They wont be able to access services outside of the VPC, unless networking configuration exists in the VPC to allow external access
        - The Lambda needs `EC2Networking` permissions in order ot be able to create ENIs in the VPC
        - VPC based Lambda functions do not directly in the VPC, they will use a shared ENI to access resources in the VPC as long as all the functions have the same Security Group. In case new Security Groups are attached to a certain Lambda, new ENIs are placed inside the VPC
        - At the creation of the function, a certain ENI might be created for accessing the VPC. The initial setup would take up to 90 seconds. This setup will take place only once, not at every invocation

## Lambda Security

- There are 2 key parts of the security model
    - Lambda Functions will assume an execution role in order to access other AWS resources
    - Resource policies: similar to resource policies for S3. Allows external accounts to invoke a Lambda functions, or certain services to use Lambda functions. Resources polices can be modified using the CLI/API (currently cannot be changed with the console)

## Lambda Logging

- Lambda uses CloudWatch Logs and X-Ray
- Logs from Lambda executions are stored in CloudWatch Logs
- Details about Lambda metrics are stored in CloudWatch Metrics
- Lambda can be integrated with X-Ray for distributed tracing
- For Lambda to be able to log we need to give permissions via the execution role

## Lambda Invocations

- There are 3 ways Lambda functions can be invoked:
    - **Synchronous invocation**:
        - Command line or API directly invoking the function
        - The CLI or API will wait until the function returns
        - API Gateway will also invoke Lambdas synchronously, use case for many serverless applications
        - Any errors or retries have to be handled on the client side
    - **Asynchronous invocation**:
        - Used typically when AWS services invoke the function (example: S3 events)
        - The service will not wait for the response (fire and forget)
        - Lambda is responsible for any failure. Reprocessing will happen between 0 and 2 times
        - The function should be idempotent in order to be rerun
        - Lambda can be configured to send events to a DLQ in case of the processing did not succeed after the number of retries
        - Destination: events processed by Lambdas can be delivered to destinations like SQS, SNS, other Lambda, EventBride. Success and failure events can be sent to different destinations
    - **Event Source mapping**:
        - Typically used on streams or queues which don't generate events (Kinesis, DynamoDB streams, SQS)
        - Event Source mappers polls these streams and retrieves batches. These batches can be broken in pieces and sent to multiple Lambda invocations for processing
        - We can not have a partially successful batch, either everything works or nothing works
- In case of event processing in async invocation, in order to process the event we don't explicitly need rights to read from the sender
- In case of event source mapping the event source mapper is reading from the source. The event source mapping uses permissions from the Lambda execution role to access the source service
- Even if the function does not read data directly from the stream, the execution role needs read rights in order to handle the event batch
- Any batch that consistently fails to be processed, it can be sent to an SQS queue or SNS topic for further processing

## Lambda Versions

- We can define different versions for given functions
- A version of a function is the code + configuration of the function
- When we publish a version, it becomes immutable, it no longer can be changed. It event gets its own ARN (Amazon Resource Name)
- `$Latest` points to the latest version of Lambda version (it is not immutable)
- We can also define aliases (DEV, STAGE, PROD) which point to a version of the function. Aliases can be changed to point to other versions

## Lambda Start-up Times

- Lambda code runs inside of a runtime environment (execution context)
- At first invocation this execution context needs to be created and this will take time
- This process is known as cold start and it can take 100ms or more
- If the function is invoked again without too much of a gap, it might use the same execution context. This is called warm start
- One function invocation runs in an execution environment at a time. If multiple parallel instances are needed, the contexts will require cold starts
- **Provisioned concurrency**: we can provision one or more execution contexts in advance for Lambda invocations
- The improve performance we can use the `/tmp` folder to pre-download data to it. If another invocations uses the same execution context, it will be able to access the previously downloaded data
- We can create database connections outside of the Lambda handler. These will also be available for other invocations afterwards

## Lambda Function Handler

- Lambda function executions have life cycles
- The function code runs inside an execution environment
- Lifecycle phases:
    - `INIT`: creates or unfreezes the execution environment
        - It has the following sub-components:
            - `EXTENSION INIT`
            - `RUNTIME INIT`
            - `FUNCTION INIT`
        - Init phase runs only at cold-starts
    - `INVOKE`: runs the function handler (cold start)
    - `NEXT INVOKE`(s): warm start using the same environment
    - `SHUTDOWN`: execution environment is terminated after a period of inactivity
        - It has the following sub-components:
            - `RUNTIME SHUTDOWN`
            - `EXTENSION SHUTDOWN`
        - We can use Provisioned Concurrency to avoid having a cold-start in case the Lambda should be terminated

## Lambda Versions and Aliases

- Unpublished functions can be changed and deployed
- `$LATEST` version of the Lambda code can be edited and deployed
- We can take the current state of the function and publish it which will create an immutable version
- If the function is published, the code, dependencies, runtime settings and env. variables in the version created can not be edited
- Each version gets an uniq ARN (Qualified ARN)
- Unqualified ARN points at the function without a specific version (`$LATEST`)
- An alias is a pointer to a function version
- Example: PROD => function:1, BETA => function:2
- Each alias has an unique ARN
- Aliases can be updated, changing which version they reference
- Useful for PROD/DEV, BLUE/GREEN deployments, A/B testing
- We can also use alias routing: sending a certain percentage of request to v1 and other percentage to v2. Both versions need the same role, same DLQ (or no DLQ) will be used and both versions need to be published

## Lambda Environment Variables

- Key and value pairs for associated with Lambda functions
- By default they are associated with `$LATEST` - can be edited
- If they are publishes, they can not be edited
- They can be accessed within the execution environment
- The environment variables can be encrypted with KMS
- They allow code execution to be adjusted based on variables

## Lambda Layers

- Used to split off libraries and dependencies from Lambda functions
- Reduces the size of the deployment package
- Layers can be reused by multiple Lambda functions
- Libraries in layers are extracted in the `/opt` folder
- Layers allow new runtimes which are not explicitly supported by AWS

## Lambda Container Images

- Until recently Lambda was considered to be a Function as a Service (FaaS) product, which means creation of a function, uploading code and executing it
- Many organizations use containers and CI/CD processes built for containers
- Lambda is now capable to use containers images
- It is an alternative way of packaging the function code and using it with the Lambda product
- Lambda Runtime API - has to be included with the container images, it is a package which allows interaction between a container and the Lambda
- AWS Lambda Runtime Interface Emulator (RIE): used for local Lambda testing

## Lambda and ALB

- Lambda functions can be registered to ALB target groups
- Communication between the user and the ALB is via HTTP/HTTPS, there is no difference than connecting to a classic server (EC2) from the user's perspective
- When the ALB receives a request from the client it synchronously invokes the Lambda function
- The LB passes in a JSON structure to the Lambda function, inside the `Event` structure. This has to be interpreted by the Lambda. What actually happens is that the LB translates the HTTP(S) request to a Lambda compatible event, to which the Lambda answers with a JSON object that gets translated back to HTTP/HTTPS response
- Multi-Value headers:
    - For an example lets us this URL for the Lambda: http://catagram.io?&search=roffle&search=winkie
    - Without multi-value headers the Lambda receives the following:
        ```
        "queryStringParameters": {
            "search": "winkie"
        }
        ```
    - If the multi-value headers are enabled, we get this delivered to Lambda:
        ```
        "multiValueQueryStringParameters": {
            "search": ["roffle", "winkie"]
        }
        ```