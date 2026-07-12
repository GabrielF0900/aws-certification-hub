# ECS - Elastic Container Service

- É um serviço que aceita contêineres e orquestra onde e como executá-los
- É um serviço de computação baseado em contêiner gerenciado
- Ele é executado em dois modos: EC2 e Fargate
- Cluster: é o local onde os contêineres são executados com base em como queremos que eles sejam executados
- Os contêineres estão localizados em registros de contêineres (ECR, DockerHub)
- O ECS usa **definições de contêiner (container definitions)** para localizar imagens nos registros de contêineres, qual porta a imagem deve usar, etc., fornecendo informações sobre o contêiner que queremos executar
- **Definição de tarefa (Task definition)**: representa um aplicativo independente, pode ter um ou vários contêineres definidos nela. Uma tarefa no ECS define o aplicativo como um todo
- As definições de tarefas armazenam os recursos a serem usados (CPU, memória), configuração de rede, compatibilidade (modo EC2 ou Fargate) e também armazenam a função da tarefa (função IAM ou IAM role)
- **Função da tarefa (Task role)** é a função IAM que a tarefa pode assumir. Ela dá permissão aos contêineres ECS para acessar serviços da AWS
- **Função de Execução de Tarefa (Task Execution Role)**: para configurar o próprio contêiner e mantê-lo, algumas tarefas são executadas. O Agente de Contêiner (Container Agent) executa essas tarefas para o contêiner. Portanto, a função exigida e assumida pelo Agente de Contêiner para configurar o contêiner é a Função de Execução de Tarefa
- Uma tarefa não é dimensionada sozinha (doesn't scale by its own) e não é HA (Altamente Disponível)
- **Serviço ECS (ECS service)**: é configurado por uma **definição de serviço (service definition)**. Em um serviço, definimos como queremos que uma tarefa seja dimensionada, quantas cópias gostaríamos de executar
- Os serviços ECS definem a escalabilidade e HA para tarefas

## Modos de Cluster ECS

- O modo de cluster define quanto da sobrecarga administrativa é necessária para executar contêineres no ECS (quais partes gerenciamos e quais partes a AWS gerencia)
- Os modos de cluster são:
    - Modo EC2
    - Modo Fargate

### Modo EC2

- Usa instâncias EC2 que estão em execução dentro de uma VPC
- Como estamos dentro de uma VPC, podemos nos beneficiar do uso de várias zonas de disponibilidade (AZs)
- Quando criamos o cluster, especificamos o tamanho inicial dos contêineres
- O escalonamento horizontal para instâncias EC2 e para tarefas ECS é controlado por ASGs (Auto Scaling Groups)
- Com o modo de cluster EC2, pagamos por instâncias EC2 independentemente de quais contêineres e quantos contêineres estão sendo executados nelas

### Modo Fargate

- Não precisamos gerenciar instâncias EC2 para usar como host de contêiner
- Com o Fargate não há servidores para gerenciar
- A AWS mantém uma plataforma de infraestrutura Fargate compartilhada oferecida a todos os usuários
- Temos acesso a recursos de um pool compartilhado, não temos visibilidade de outros clientes
- Uma implantação do Fargate ainda usa um cluster com uma VPC que opera em AZs
- As tarefas do ECS são injetadas na VPC com uma ENI e são executadas na plataforma compartilhada do Fargate
- Com o modo Fargate, pagamos apenas pelos contêineres que estamos usando com base nos recursos que eles consomem

## EC2 vs ECS (EC2) vs Fargate

- Se já estamos usando contêineres, devemos usar o ECS
- Os contêineres fazem sentido se quisermos isolar aplicativos
- Geralmente escolhemos o modo EC2 se tivermos uma grande carga de trabalho e o negócio for sensível a preços
- Historicamente, o modo EC2 oferecia mais valor pelo preço se usássemos saving plans (planos de economia). Hoje em dia, podemos ter saving plans para Fargate e Lambda, então devemos usar o Fargate como padrão em vez do modo EC2
- Se estivermos preocupados com a sobrecarga de gerenciamento (overhead conscious), devemos usar o Fargate
- Para cargas de trabalho pequenas/com picos (burst), também devemos usar o Fargate. O mesmo é recomendado para cargas de trabalho em lote (batch) / periódicas

---

# ECS - Elastic Container Service

- It is a service that accepts containers and orchestrates where and how to run those containers
- It is a managed container based compute service
- It runs on two modes: EC2 and Fargate
- Cluster: is the place where container run based on how we want them to run
- Containers are located in container registries (ECR, DockerHub)
- ECS uses **container definitions** to locate images in the container registries, which port should the image use, etc. providing information about the container we want to run
- **Task definition**: represents a self-contained application, can have one or many containers defined in it. A task in ECS defines the application as a whole
- Task definitions store the resources to be used (CPU, memory), networking configuration, compatibility (EC2 mode or Fargate) and also they store the task role (IAM role)
- **Task role** is IAM role that the task can assume. It gives permission to ECS containers to access AWS services
- **Task Execution Role**: to set up the container itself and maintain that, some tasks are performed. Container Agent performs those tasks for the container. So, the role required & assumed by Container Agent to set up the container is Task Execution Role
- A task does not scale by its own and it is not HA
- **ECS service**: it is configured by a **service definition**. In a service we define how we want a task to scale, how many copies we like to run
- ECS services define scalability and HA for tasks

## ECS Cluster Modes

- Cluster mode define how much of the admin overhead is required for running containers in ECS (what parts do we manage and what parts does AWS manage)
- Cluster modes are:
    - EC2 Mode
    - Fargate Mode

### EC2 Mode

- Uses EC2 instances which are running inside of a VPC
- Since we are inside of a VPC, we can benefit from using multiple AZs
- When we create the cluster, we specify the initial size of containers
- Horizontal scaling for EC2 instances and for ECS tasks is controlled by ASGs
- With EC2 cluster mode we are paying for EC2 instances independently of what containers and how many of containers are running on them

### Fargate Mode

- We don't have to manage EC2 instances for use as container host
- With Fargate there are no servers to manage
- AWS maintains a shared Fargate infrastructure platform offered to all users
- We gain access to resources from a shared pool, we don't have visibility for other customers
- A Fargate deployment still uses a cluster with a VPC which operates in AZs
- ECS tasks are injected into the VPC with an ENI, they are running on the Fargate shared platform
- With Fargate mode we only pay for the containers we using based on the resources they consume

## EC2 vs ECS (EC2) vs Fargate

- If we are already using containers, we should use ECS
- Containers make sense if we want to isolate applications
- We generally pick EC2 mode if we have a large workload and the business is price conscious
- Historically EC2 mode was giving the most value for the price if we were using saving plans. Nowadays we can have savings plan for Fargate and Lambda, so we should default to Fargate instead of EC2 mode
- If we are overhead conscious, we should use Fargate
- For small/burst workloads we should use Fargate as well. Same is recommended for batch/periodic workloads