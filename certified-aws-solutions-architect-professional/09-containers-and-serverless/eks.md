# EKS - Elastic Kubernetes Service

## Kubernetes 101

- É um sistema de orquestração de contêineres de código aberto
- Nós o usamos para automatizar a implantação, escalonamento e gerenciamento de aplicativos em contêineres
- É um produto independente de nuvem (cloud-agnostic), pode ser usado localmente (on-premises) também
- Estrutura do Cluster:
    - Um cluster Kubernetes é um cluster HA (Altamente Disponível) de recursos de computação organizados para funcionar como uma unidade
    - O cluster começa com o Plano de Controle do Cluster (Cluster Control Plane): gerencia o cluster, o agendamento, as aplicações, o escalonamento e a implantação
    - A computação no Kubernetes é fornecida por meio dos Nós do Cluster (Cluster Nodes): VM ou servidores físicos que funcionam como trabalhadores (workers) no cluster. Estes executam as aplicações em contêineres
    - Software que será executado em cada nó:
        - Em cada um dos nós é executado um tempo de execução de contêiner (container runtime): `containerd` ou outro software usado para lidar com operações de contêiner
        - `kubelet`: o agente que interage com o plano de controle. Este usa a API do Kubernetes para se comunicar com o plano de controle
- Detalhes do Cluster:
    - Pods: 
        - As menores unidades de computação no Kubernetes
        - Pods podem ter vários contêineres e fornecem armazenamento e rede compartilhados para eles
        - É comum ter um contêiner por pod, embora possamos ter vários contêineres em um pod
        - Pods não são permanentes: eles podem ser excluídos ao terminar um trabalho, evictados devido à falta de recursos ou quando um nó falha
    - O plano de controle executa o seguinte software:
        - `kube-apiserver`: 
            - O front-end para o controle do Kubernetes 
            - É com ele que os nós e outros elementos do cluster interagem
            - Pode ser escalonado horizontalmente para HA e desempenho
        - `etcd`:
            - Armazenamento de chave/valor HA
            - Armazenamento de apoio (Backing store) para o cluster
        - `kube-scheduler`:
            - Identifica quaisquer pods dentro de um cluster que não tenham um nó atribuído
            - Atribui pods com base em recursos, prazos, afinidade, localidade de dados e quaisquer outras restrições
        - `cloud-controller-manager`:
            - Componente opcional
            - Fornece lógica de controle específica da nuvem
            - Permite-nos vincular o Kubernetes a APIs de provedores de nuvem, como a AWS
        - `kube-controller-manager`:
            - É uma coleção de processos:
                - Node Controller (Controlador de Nó): monitoramento e resposta a interrupções de nó
                - Job Controller (Controlador de Trabalho): tarefas únicas (jobs)
                - Endpoint Controller (Controlador de Endpoint): preenche endpoints 
                - Service Account and Token Controllers (Controladores de Conta de Serviço e Token): contas/tokens de API
    - kube-proxy:
        - Todo nó o executa
        - É um proxy de rede
        - Coordena a rede com o plano de controle
        - Ajuda a implementar "serviços" e configura regras que permitem comunicações com pods de dentro ou fora do cluster
- Ingress: expõe um caminho para um serviço de fora para dentro do cluster
- Ingress Controller: um software que organiza o hardware subjacente para permitir o ingress (exemplo: AWS LB Controller que usa ALB/NLB)
- Armazenamento Persistente (Persistent Storage - PV): são volumes cujo ciclo de vida vai além de qualquer pod único que os esteja utilizando. Armazenamento "normal" de longa duração

## Elastic Kubernetes Service 101

- É uma implementação gerenciada pela AWS do Kubernetes como serviço
- O EKS pode ser executado de diferentes maneiras:
    - Na própria AWS como um produto
    - No Outposts: racks e servidores operando em locais on-premises, mas controlados e gerenciados pela AWS
    - EKS Anywhere: clusters EKS rodando on-premises ou em qualquer outro lugar
    - EKS Distro: produto EKS como código aberto
- O plano de controle EKS é gerenciado pela AWS e é escalonado com base na carga. Ele é executado em várias AZs
- Integra-se com outros serviços da AWS, como ECR, ELB, IAM, VPC
- EKS Cluster = EKS Control Plane + EKS Nodes
- O etcd também é gerenciado pela AWS e distribuído em várias AZs
- Os nós podem ser dos seguintes tipos:
    - Autogerenciados (Self managed): instâncias EC2 gerenciadas por nós
    - Grupos de nós gerenciados (Managed node groups): ainda são instâncias EC2, mas o EKS gerencia o provisionamento e o gerenciamento do ciclo de vida
    - Fargate: nós são gerenciados pelo EKS, não precisamos nos preocupar em escalonar e otimizar clusters (semelhante ao ECS Fargate)
- A escolha entre os tipos de nós depende para que queremos usar o cluster. Se quisermos nós Windows, GPU, Inferentia, Bottlerocket, Outposts, Local zones, etc., precisamos verificar quais tipos de nós suportam o recurso de que precisamos
- Armazenamento persistente no EKS: pode usar EBS, EFS, FSx for Lustre, FSx for NetApp ONTAP como provedores de armazenamento

---

# EKS - Elastic Kubernetes Service

## Kubernetes 101

- It is an open source container orchestration system
- We used to automate the deployment, scaling and management of containerized applications
- It is a cloud-agnostic product, can be used on-premises as well
- Cluster Structure:
    - A Kubernetes cluster is a HA cluster of compute resources organized to work as one unit
    - Cluster starts with the Cluster Control Plane: manages the cluster, scheduling, applications, scaling and deploying
    - Compute in Kubernetes is provided via Cluster Nodes: VM or physical servers which function as a worker in the cluster. These run the containerized applications
    - Software that will run on each node:
        - On each of the nodes runs a container runtime: `containerd` or other software used to handle container operations
        - `kubelet`: the agent which interacts with the control plane is. This uses the Kubernetes API to communicate with the control plane
- Cluster details:
    - Pods: 
        - The smallest units of computing in Kubernetes
        - Pods can have multiple containers and provide shared storage and networking for them
        - It is common to have one container per pod, although we can have multiple container in a pod
        - Pods are not permanent: they can be deleted when finished with a job, evicted because of lack of resources or when a node fails
    - Control plane runs the following software:
        - `kube-apiserver`: 
            - The front-end for the Kubernetes control 
            - It is what nodes and other cluster elements interact with
            - Can be horizontally scaled for HA and performance
        - `etcd`:
            - HA key/value store
            - Backing store for the cluster
        - `kube-scheduler`:
            - Identifies any pods within a cluster that does not have a node assigned
            - Assigned pods based on resources, deadlines, affinity, data locality and any other constraints
        - `cloud-controller-manager`:
            - Optional component
            - Provides cloud-specific control logic
            - It allows us to link Kubernetes with cloud providers APIs such as AWS
        - `kube-controller-manager`:
            - It is a collection of processes:
                - Node Controller: monitoring and responding to node outages
                - Job Controller: one-of tasks (jobs)
                - Endpoint Controller: populates endpoints 
                - Service Account and Token Controllers: accounts/API tokens
    - kube-proxy:
        - Every node runs it
        - It is a networking proxy
        - It coordinates networking with the control plane
        - It helps implement "services" and configures rules allowing communications with pods from inside or outside of the cluster
- Ingress: exposes a way into a service from outside to the cluster
- Ingress Controller: a piece of software with arranges the underlying hardware to allow ingres (example: AWS LB Controller which use ALB/NLB)
- Persistent Storage (PV): they are volumes whose lifecycle lives beyond any one single pod that is using it. "Normal" long running storage

## Elastic Kubernetes Service 101

- It is an AWS managed implementation of Kubernetes as a service
- EKS can be run in different ways:
    - On AWS itself as a product
    - On Outposts: racks and servers operating in on-premises locations, but controlled and managed by AWS
    - EKS Anywhere: EKS clusters running on on-premises or anywhere else
    - EKS Distro: EKS product as open-source
- The EKS control plane is managed by AWS and scales based on load. It runs across multiple AZs
- Integrates with other AWS services such as ECR, ELB, IAM, VPC
- EKS Cluster = EKS Control Plane and EKS Notes
- etcd is also managed by AWS and distributed across multiple AZs
- Nodes can be the following types:
    - Self managed: EC2 instances managed by us
    - Managed node groups: still EC2 instances, but EKS manages the provisioning and lifecycle managing
    - Fargate: nodes are managed by EKS, we don't have to worry about scaling and optimizing clusters (similar to ECS Fargate)
- Choosing between node types depends on for what we want to use the cluster. If we want Windows nodes, GPU, Inferentia, Bottlerocket, Outposts, Local zones, etc. we need to check which types of nodes support the feature we require
- Persistent storage on EKS: it can use EBS, EFS, FSx for Lustre, FSx for NetApp ONTAP as storage providers