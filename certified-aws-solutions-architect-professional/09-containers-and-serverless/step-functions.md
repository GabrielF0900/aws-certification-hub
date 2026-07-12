# AWS Step Functions

- As Step Functions abordam as limitações do produto Lambda
- Uma função Lambda tem um tempo de execução máximo de 15 minutos
- Funções Lambda podem ser encadeadas (chained together), mas isso é considerado um antipadrão e pode ficar bagunçado. Ambientes de execução Lambda não mantêm estado (stateless)
- Step Functions é um serviço que nos permite criar máquinas de estado (state machines)
- Estados podem fazer coisas, decidir coisas, receber dados, modificar dados e gerar dados de saída
- A duração máxima para execução de uma máquina de estado é de 1 ano
- Step Functions podem representar 2 tipos diferentes de fluxos de trabalho (workflow):
    - Fluxo de trabalho padrão (Standard workflow): é o padrão e tem um limite de execução de 1 ano
    - Fluxo de trabalho expresso (Express workflow): projetado para processamento de eventos de alto volume (IoT, processamento de dados de streaming e transformações), que pode ser executado por até 5 minutos
- Step Functions podem ser iniciadas com API Gateway, Regras IoT (IoT Rules), EventBridge, Lambda ou mesmo manualmente
- Máquinas de estado para Step Functions podem ser criadas com modelos JSON na Amazon State Language (ASL)

## Estados (States)

- Tipos de estados disponíveis:
    - `SUCCEED` (SUCESSO) e `FAIL` (FALHA)
    - `WAIT` (ESPERA): esperará por um determinado período de tempo ou até uma data
    - `CHOICE` (ESCOLHA): permite que uma máquina de estado siga um caminho diferente dependendo de uma entrada
    - `PARALLEL` (PARALELO): permite criar ramificações paralelas (parallel branches) em uma máquina de estado
    - `MAP` (MAPEAMENTO): espera uma lista de coisas, para cada uma ela executará um determinado conjunto de coisas
    - `TASK` (TAREFA): representa uma única unidade de trabalho executada por uma máquina de estado. Ela pode ser integrada com: Lambda, Batch, DynamoDB, ECS, SNS, SQS, Glue, SageMaker, EMR, outras Step Functions, etc.

---

# AWS Step Functions

- Step Functions address limitations of Lambda product
- A Lambda function has an execution time of maximum 15 minutes
- Lambda functions can be chained together, but it is considered to be an anti-patterns and it can get messy. Lambda runtime environments are stateless
- Step Functions is service which lets us create state machines
- States can do things, can decide things, can take in data, modify data and output data
- Maximum duration for state machine execution is 1 year
- Step Functions can represent 2 different type of workflow:
    - Standard workflow: is the default and it has 1 year execution limit
    - Express workflow: designed for high volume event processing (IoT, streaming data processing and transformations), which can run up to 5 minutes
- Step Functions can be initiated with API Gateway, IoT Rules, EventBridge, Lambda or even manually
- State machines for Step Functions can be created with Amazon State Language (ASL) JSON templates

## States

- Type of states available:
    - `SUCCEED` and `FAIL`
    - `WAIT`: will wait for a certain period or time or until a date
    - `CHOICE`: allows a state machine to take a different path depending on an input
    - `PARALLEL`: allows to create parallel branches in a state machine
    - `MAP`: expects a list of things, for each it will perform a certain set of things
    - `TASK`: represents a single unit of work performed by a state machine. It can be integrated with: Lambda, Batch, DynamoDB, ECS, SNS, SQS, Glue, SageMaker, EMR, other Step Functions, etc.
