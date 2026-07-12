## Amazon Aurora

## Arquitetura do Aurora

- A arquitetura do Aurora é muito diferente do RDS
- Usa a entidade base de um cluster, algo que outras instâncias de banco de dados RDS não têm
- O Aurora não usa armazenamento local para as instâncias de computação; em vez disso, um cluster Aurora tem um volume personalizado compartilhado
- Um cluster é composto por várias coisas importantes:
    - Uma instância primária única + 0 ou mais réplicas
    - As réplicas podem ser usadas para leitura durante operações normais
- O Aurora usa um *Cluster*:
    - Composto por uma instância primária única e 0 ou mais réplicas
    - As réplicas podem ser usadas para leituras (diferente da réplica de espera no RDS)
    - Armazenamento: o cluster usa um volume de cluster compartilhado (baseado em SSD por padrão). Fornece provisionamento mais rápido, disponibilidade melhorada e melhor desempenho. O tamanho pode chegar a 128 TiB
    - O armazenamento tem 6 réplicas entre AZs. Os dados são replicados sincronamente. A replicação acontece no nível de armazenamento; nenhum recurso extra é consumido para replicação
    - Por padrão, apenas a instância primária pode gravar no armazenamento; as réplicas e o primário podem realizar operações de leitura
    - Auto-reparo: o Aurora pode reparar seus dados se uma réplica ou parte da réplica tiver uma falha de disco
    - O Aurora usa o cluster para reparar os dados sem corrupção. Como resultado, o Aurora evita perda de dados e reduz a necessidade de restaurações pontuais ou restaurações de snapshots
    - Com o Aurora, podemos ter até 15 réplicas; qualquer uma das réplicas pode ser utilizada em um failover
    - Faturamento para armazenamento do Aurora:
        - O armazenamento é cobrado pelo que consumimos até o limite de 128 TiB
        - Marca d'água alta: somos cobrados pelo máximo de dados usados em um determinado momento; em caso de liberação de espaço, seremos cobrados pelo uso máximo consumido
        - Caso precisemos reduzir dados significativamente, precisaremos migrar o banco de dados para outro cluster para evitar pagar pelo armazenamento
        - Recentemente, o Aurora introduziu o redimensionamento dinâmico, onde temos que pagar apenas pelo que usamos. É recomendado atualizar nosso banco de dados para uma versão do Aurora que suporte redimensionamento dinâmico
    - Os clusters Aurora usam endpoints, fornecendo múltiplos endpoints:
        - **Endpoint do Cluster**: sempre aponta para a instância primária; pode ser usado para leituras e gravações
        - **Endpoint do Leitor**: aponta para a instância primária e também para as réplicas de leitura. O Aurora realiza balanceamento de carga ao usar este endpoint
        - **Endpoint Personalizado**: pode ser criado por nós
        - **Endpoint de Instância**: cada instância tem seu próprio endpoint

## Custos do Aurora

- Sem opção de nível gratuito; o Aurora não suporta instâncias micro
- Além do RDS singleAZ (micro), o Aurora oferece melhor valor em comparação com outras opções RDS
- Computação: cobrança por hora, por segundo, mínimo de 10 minutos
- Armazenamento: GB/mês consumido, custo de IO por requisição feita ao armazenamento compartilhado do cluster
- Backups: 100% do tamanho do banco de dados em backups estão incluídos

## Restauração, Clone e Backtrack do Aurora

- Os backups no Aurora funcionam da mesma forma que em outros RDS
- As restaurações criam um novo cluster
- O Backtrack pode ser habilitado por cluster. Permitem reversões no local para um ponto anterior no tempo
- Clone rápido: cria um novo banco de dados muito mais rápido do que copiar todos os dados. O Aurora faz referência ao armazenamento original; armazena apenas as diferenças entre os dados antigos e os novos

## Aurora Serverless

- Fornece uma versão do Aurora sem a necessidade de provisionar estaticamente a instância do banco de dados
- Remove a sobrecarga de administração para gerenciar instâncias de banco de dados
- O Aurora Serverless usa o conceito de ACU - Unidades de Capacidade Aurora: representam uma certa quantidade de computação e uma quantidade correspondente de memória
- Podemos definir valores mínimos e máximos de ACU por cluster; pode chegar a 0
- O faturamento por consumo é por segundo
- O Aurora Serverless fornece a mesma resiliência que o Aurora provisionado (6 cópias entre AZs)
- A arquitetura de cluster Aurora ainda existe, mas em forma de cluster serverless. Em vez de usar instâncias provisionadas, temos unidades de capacidade
- As unidades de capacidade são alocadas de um pool quente de instâncias Aurora gerenciado pela AWS
- As ACUs são sem estado, compartilhadas entre vários clientes AWS
- Se a carga aumentar além do limite de ACU e o pool permitir, mais ACUs serão alocadas à instância
- No Aurora Serverless, temos um Proxy Fleet compartilhado para gerenciamento de conexões:
    - É usado para distribuir conexões de nós, usuários Aurora, para as unidades de capacidade Aurora
    - Nunca nos conectamos diretamente ao Aurora; isso torna o scaling do Aurora transparente
- Casos de uso do Aurora:
    - Aplicações usadas com pouca frequência
    - Novos aplicativos onde não temos certeza sobre os níveis de carga que serão colocados na aplicação
    - Cargas de trabalho variáveis e/ou imprevisíveis
    - Bancos de dados de desenvolvimento e teste: o Aurora pode ser configurado para se desligar
    - Aplicações multi-tenant onde o scaling está alinhado com o tamanho da infraestrutura e a receita

## Aurora Multi-Master

- O modo padrão do Aurora é single-master: um endpoint de leitura/escrita e 0 ou mais réplicas de leitura
- Em contraste com o modo padrão do Aurora, o multi-master oferece múltiplos endpoints que podem ser usados para leituras e gravações
- Não há endpoint de cluster para usar; a aplicação é responsável pela conexão com as instâncias no cluster
- Benefícios:
    - Múltiplos endpoints de gravação; se tivermos uma aplicação que pode fazer failover entre endpoints, o tempo de failover pode ser significativamente reduzido
    - A tolerância a falhas pode ser implementada no nível da aplicação, mas a aplicação precisa balancear a carga manualmente entre as instâncias

---

## Amazon Aurora

## Aurora Architecture

- Aurora architecture is very different from RDS
- It uses the base entity of a cluster, which something that other instances of RDS database do not have
- Aurora does not use local storage for the compute instances, instead an Aurora cluster has a shared custom volume
- A cluster is made up from a number of important things:
    - A single primary instance + 0 or more replicas
    - The replicas can be used for read during normal operations
- Aurora uses a *Cluster*:
    - Made up of a single primary instance and 0 or more replicas
    - The replicas can be used for reads (not like the standby replica in RDS)
    - Storage: the cluster uses a shared cluster volume (SSD based by default). Provides faster provisioning, improved availability and better performance. Size can go up to 128 TiB
    - The storage has 6 replicas across AZs. The data is replicated synchronously. Replication happens at the storage level, no extra resources are consumed for replication
    - By default only the primary instance are able to write to the storage, replicas and the primary can perform read operation
    - Self-healing: Aurora can repair its data if a replica or part of the replica if there is a disk failure
    - Aurora uses the cluster to repair the data with no corruption. As a result, Aurora avoids data loss and reduces needs for point-in-time restores or snapshot restores
    - With Aurora can have up to 15 replicas, any of the replicas can be failed over to
    - Billing for Aurora storage:
        - Storage is billed to what we consume up to 128 TiB limit
        - High water mark: we get billed for the most used data at a time, in case of free-up we will be billed for the max usage consumed
        - In case we have to reduce data significantly, we will need to migrate the database to another cluster to avoid paying for the storage
        - Recently Aurora introduced dynamic resizing, where we have to pay for only what we use. It is recommended to upgrade our database to an Aurora version which supports dynamic resizing
    - Aurora clusters use endpoints, providing multiple endpoints:
        - **Cluster endpoint**: always point to the primary instance, can be used for reads and writes
        - **Reader endpoint**: points to the primary instance and also to the read-replicas. Aurora does load balancing we using this endpoint
        - **Custom endpoint**: can be created by us
        - **Instance endpoint**: each instance has its own endpoint

## Aurora Costs

- No free-tier option, Aurora does not support micro instances
- Beyond RDS singleAZ (micro) Aurora offers better value compared to other RDS options
- Compute: hourly charge, per second, 10 minute minimum
- Storage: GB/month consumed, IO cost per request made to the cluster's shared storage
- Backups: 100% DB size in backups are included

## Aurora Restore, Clone and Backtrack

- Backups in Aurora work the same way as other RDS
- Restores create a new cluster
- Backtrack can be enabled per cluster. They allow in-place rewinds to a previous point-in-time
- Fast clone: makes a new database much faster than copying all the data. Aurora references the original storage, only stores any differences between the old data and the new one

## Aurora Serverless

- It provides a version of Aurora without the need to statically provision the database instance
- Removes admin overhead for managing db instances
- Aurora Serverless uses the concept of ACU - Aurora Capacity Units: represent a certain amount of compute and a corresponding amount of memory
- We can set minimum and maximum ACU values per cluster, can go down to 0
- Consumption billing is per-second basis
- Aurora Serverless provides the same resilience as Aurora provisioned (6 copies across AZs)
- Aurora cluster architecture still exists, but in a for of serverless cluster. Instead of using provisioned instances we have capacity units
- Capacity units are allocated from a warm pool of Aurora instances managed by AWS
- ACUs are stateless, shared across multiple AWS customers
- If the load increases beyond the ACU limit and the pool allows it, than more ACU will be allocated to the instance
- In Aurora Serverless we have shared Proxy Fleet for connection management:
    - It is used to distribute connections from us, Aurora users, to Aurora capacity units
    - We never directly connect to Aurora, this makes Aurora scaling seamless
- Aurora use cases:
    - Infrequently used applications
    - New applications where we are unsure about the levels of load that will be places on the application
    - Variable and/or unpredictable workloads
    - Development and test databases: Aurora can be configured to stop itself
    - Multi-tenant applications where the scaling is aligned with infrastructure size and revenue

## Aurora Multi-Master

- Default Aurora mode is single-master: one read/write endpoint and 0 or more read replicas
- In contrast with default mode for Aurora, multi-master offers multiple endpoints which can be used for reads and writes
- There is no cluster endpoint to use, the application is responsible for connection to instances in the cluster
- Benefits:
    - Multiple writer endpoints, if we have an application which can failover between endpoints, the failover time can be significantly reduced
    - Fault tolerance can be implemented at the application level, but the application needs to manually load balance between the instances