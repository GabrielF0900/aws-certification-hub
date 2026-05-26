# EBS e Instance Store

## Tipos de Volume EBS (EBS Volume Types)

- **SSD de Uso Geral (General Purpose SSD - GP2/GP3)**:
    - O GP2 é o tipo de armazenamento padrão para o EC2; o GP3 é a versão mais recente
    - Um volume GP2 pode ser tão pequeno quanto 1 GB ou tão grande quanto 16 TB
    - Créditos de E/S (IO Credits):
        - Uma operação de E/S (IO) é uma operação de entrada/saída, correspondente a um bloco de dados de 16 KB
        - 1 IOPS é 1 E/S em 1 segundo
        - 1 crédito de E/S = 1 IOPS
    - Se não tivermos créditos para o volume, não poderemos realizar nenhuma operação de E/S
    - O bucket de E/S possui 5,4 milhões de créditos e é reabastecido a uma taxa baseada no desempenho de linha de base (baseline performance) do armazenamento
    - O desempenho de linha de base para o GP2 é baseado no tamanho do volume: recebemos 3 créditos de E/S por segundo por GB de tamanho do volume. Além disso, ele é preenchido com um mínimo de 100 créditos de E/S por segundo, independentemente do tamanho do volume
    - Por padrão, o GP2 pode fazer burst de até 3000 IOPS
    - Se consumirmos mais créditos do que a taxa de reabastecimento do bucket, estaremos esgotando o bucket
    - Devemos garantir que os buckets estejam se reabastecendo e não se esgotando até 0; caso contrário, o armazenamento ficará inutilizável
    - Volumes maiores que 1 TB excederão a taxa de burst de 3000 IOPS; eles sempre alcançarão o desempenho de linha de base por padrão e não utilizarão o sistema de créditos
    - E/S máxima de 16.000 créditos de E/S por segundo; qualquer volume maior que 5,33 TB alcançará essa taxa máxima constantemente
    - O GP2 pode ser usado para volumes de inicialização (boot volumes)
    - O GP3 é semelhante ao GP2, mas remove o sistema de créditos para oferecer uma forma mais simples de trabalho:
        - Cada volume GP3 começa com um padrão de 3000 IOPS e 125 MiB/s, independentemente do tamanho do volume
    - O preço base do GP3 é 20% mais barato que o do GP2
    - Para obter mais desempenho, podemos pagar um custo adicional para alcançar até 16.000 IOPS ou 1000 MiB/s de taxa de transferência (throughput)
- **SSD de IOPS Provisionadas (Provisioned IOPS SSD - IO1/IO2)**:
    - Existem 3 tipos de opções de armazenamento de IOPS provisionadas: IO1, seu sucessor IO2 e o IO2 BlockExpress (atualmente em preview)
    - Para esta categoria de armazenamento, o valor de IOPS pode ser configurado de forma independente do tamanho do armazenamento
    - Os armazenamentos de IOPS provisionadas são recomendados para uso onde são necessárias baixa latência consistente e alta taxa de transferência (throughput)
    - As IOPS máximas por volume são 64.000 IOPS por volume e 1000 MB/s de throughput, enquanto com o BlockExpress podemos alcançar 256.000 IOPS por volume e 4000 MB/s de throughput
    - O tamanho do volume varia de 4 GB até 16 TB para IO2/IO3 e até 64 TB para o BlockExpress
    - Podemos alocar valores de desempenho de IOPS independentemente do tamanho do volume, existindo um valor máximo de IOPS por tamanho:
        - IO1: Máximo de 50 IOPS / GB
        - IO2: Máximo de 500 IOPS / GB
        - BlockExpress: Máximo de 1000 IOPS / GB
    - Desempenho por instância: desempenho máximo entre o serviço EBS e o EC2. Geralmente, isso exige mais de um volume para ser saturado. Valores máximos:
        - IO1: 260.000 IOPS e 7500 MB/s (4 volumes para saturar)
        - IO2: 160.000 IOPS e 4750 MB/s (menos que o IO1)
        - BlockExpress: 260.000 IOPS e 7500 MB/s
    - Casos de uso: volumes menores e altíssimo desempenho
- Tipos de volumes baseados em HDD:
    - Existem 2 tipos de armazenamentos baseados em HDD: ST1 Otimizado para Throughput (Throughput Optimized) e SC1 HDD Frio (Cold HDD)
    - **ST1**:
        - Mais barato que os volumes baseados em SSD, ideal para grandes volumes de dados
        - Recomendado para dados sequenciais, aplicações onde a taxa de transferência (throughput) é mais importante que as IOPS
        - O tamanho do volume pode variar entre 125 GB e 16 TB
        - Oferece no máximo 500 IOPS, as operações de E/S de dados são medidas em blocos de 1 MB => throughput máximo de 500 MB/s
        - Funciona de forma semelhante ao GP2, com um sistema de créditos
        - Oferece um desempenho de linha de base de 40 MB/s por TB de tamanho do volume, com burst de até 250 MB/s por TB
        - Projetado para dados sequenciais acessados com frequência a um custo menor
    - **SC1**:
        - O SC1 é mais barato que o ST1 e possui compensações (trade-offs) significativas
        - Voltado para a máxima economia quando queremos armazenar/compartilhar muitos dados sem nos preocupar com o desempenho
        - Oferece um máximo de 250 IOPS e 250 MB/s de throughput
        - Oferece um desempenho de linha de base de 12 MB/s por TB de tamanho do volume, com burst de até 80 MB/s por TB
        - O tamanho do volume pode variar entre 125 GB e 16 TB
        - É o armazenamento EBS de menor custo disponível

## Volumes de Instance Store (Instance Store Volumes)

- Fornece dispositivos de armazenamento em bloco, volumes brutos (raw volumes) que podem ser montados em um sistema
- Eles são semelhantes ao EBS, mas são unidades locais em vez de serem apresentadas através da rede
- Esses volumes estão fisicamente conectados ao host do EC2, e as instâncias no host podem acessar esses volumes
- Fornece o mais alto desempenho de armazenamento na AWS
- Os armazenamentos de instância (instance stores) já estão incluídos no preço das instâncias EC2 com as quais eles vêm
- **Os armazenamentos de instância devem ser anexados no momento do lançamento; eles não podem ser adicionados posteriormente!**
- Se uma instância EC2 for movida entre hosts, o volume de instance store perderá todos os seus dados
- As instâncias podem se mover entre hosts por vários motivos: instâncias são interrompidas e reiniciadas, motivos de manutenção, falha de hardware, etc.
- **Os volumes de instance store são volumes efêmeros!**
- Um dos principais benefícios do instance store é o desempenho. Ex: uma instância D3 fornece 4,6 GB/s de throughput, e volumes I3 fornecem 16 GB/s de throughput sequencial com SSD NVMe
- Considerações sobre o Instance Store:
    - Os volumes de instance store são locais para os hosts EC2
    - O instance store só pode ser adicionado no lançamento
    - Os dados são perdidos em um instance store caso a instância seja movida, redimensionada ou ocorra uma falha de hardware
    - Os armazenamentos de instância fornecem alto desempenho
    - Para os volumes de instance store, pagamos por eles junto com a instância EC2
    - Os volumes de instance store são temporários!

## Escolhendo entre Instance Store e EBS

- Para armazenamento persistente, devemos usar o EBS por padrão
- Para armazenamento resiliente, devemos evitar o instance store e usar o EBS por padrão
- Se o armazenamento deve ser isolado do ciclo de vida da instância EC2, devemos usar o EBS
- Resiliência com replicação integrada - podemos usar ambos, depende da situação
- Para necessidades de alto desempenho - também podemos usar ambos, depende da situação
- Para um desempenho super alto, devemos usar o instance store
- Se o custo for a principal preocupação, podemos usar o instance store se ele já vier com a instância EC2
- Consideração de custo (volumes mais baratos): ST1 ou SC1
- Taxa de transferência (throughput) ou streaming: ST1
- Volumes de inicialização (boot volumes): volumes baseados em HDD não são suportados (sem ST1 ou SC1)
- GP2/GP3 - desempenho máximo de até 16.000 IOPS
- IO1/IO2 - até 64.000 IOPS (BlockExpress: 256.000)
- RAID 0 + EBS: até 260.000 IOPS (máximo de IOPS possível por instância EC2)
- Para mais de 260.000 IOPS - use instance store

---

# EBS and Instance Store

## EBS Volume Types

- **General Purpose SSD (GP2/GP3)**:
    - GP2 is the default storage type for EC2, GP3 is the newer version
    - A GP2 volume can be as small as 1GB or as large as 16TB
    - IO Credit:
        - An IO is one input/output operations, one 16 KB chunk of data
        - 1 IOPS is 1 IO in 1 second
        - 1 IO credit = 1 IOPS
    - If we have no credits for the volume, we can not perform any IO
    - The IO bucket has 5.4 million of credits, it refills based at rate based on the baseline performance of the storage
    - The baseline performance for GP2 is based on the volume size, we get 3 IO credits per second, per GB of volume size. Also, it fills with a min of 100 IO credit per second regardless of the volume size
    - By default GP2 can burst up to 3000 IOPS
    - If we consume more credits than the bucket is refilling, than we are depleting the bucket
    - We have to ensure the buckets are replenishing and not depleting down to 0, otherwise the storage will be unusable
    - Volume larger than 1TB will exceed the burst rate of 3000 IOPS, they will always achieve the baseline performance as standard, they wont use the credit system
    - Max IO 16000 IO credits per second, any volume larger than 5.33 TB will achieve this maximum rate constantly
    - GP2 can be used for boot volumes
    - GP3 is similar to GP2, but it removes the credit system for a simpler way of working:
        - Every GP3 volume starts at a standard 3000 IOPS and 125 MiB/s regardless of volume size
    - Base price for GP3 is 20% cheaper than GP2
    - For more performance we can pay extra cost for up to 16000 IOPS or 1000 MiB/s throughput
- **Provisioned IOPS SSD (IO1/2)**:
    - There are 3 types of provisioned IOPS storage options: IO1 and its successor IO2 and IO2 BlockExpress (currently in preview)
    - For this storage category the IOPS value can be configured independently of the storage size
    - Provisioned IOPS storages are recommended for usage where consistent low latency and high throughput is required
    - Max IOPS per volume is 64_000 IOPS per volume and 1000 MB/s throughput, while with BlockExpress we can achieve 256_000 IOPS per volume and 4000 MB/s throughput
    - Volume size ranges from 4 GB up to 16 TB for IO2/IO3 and up to 64 TB for BlockExpress
    - We can allocate IOPS performance values independently of the size of the volume, there is a maximum IOPS value per size:
        - IO1 50 IOPS / GB MAX
        - IO2 500 IOPS / GB MAX
        - BlockExpress 1000 IOPS / GB MAX
    - Per instance performance: maximum performance between EBS service and EC2. Usually this implies more than one volume in order to be saturated. Max values:
        - IO1 260_000 IOPS and 7500 MB/s (4 volumes to saturate)
        - IO2 160_000 IOPS and 4750 MB/s (less than IO1)
        - BlockExpress 260_000 IOPS and 7500 MB/s
    - Use cases: smaller volumes and super high performance
- HDD based volume types:
    - There are 2 types of HDD based storages: ST1 Throughput Optimized, SC1 Cold HDD
    - **ST1**:
        - Cheaper than SSD based volumes, ideal for larger volumes of data
        - Recommended for sequential data, applications when throughput is more important than IOPS
        - Volume size can be between 125 GB and 16 TB
        - Offers maximum 500 IOPS, data IO is measured in blocks of 1 MB => max throughput of 500 MB/s
        - Works similar as GP2 with a credit system
        - Offer a base performance of 40 MB/s per TB of volume size with bursting to 250 MB/s per TB
        - Designed for frequently accessed sequential data at lower cost
    - **SC1**:
        - SC1 is cheaper than ST1, has significant trade-offs
        - Geared towards maximum economy when we want to share a lot of data without caring about performance
        - Offers a maximum of 250 IOPS, 250 MB/S throughput
        - Offer a base performance of 12 MB/s per TB of volume size with bursting to 80 MB/s per TB
        - Volume size can be between 125 GB and 16 TB
        - It is the lower cost EBS storage available

## Instance Store Volumes

- Provides block storage devices, raw volumes which can be mounted to a system
- They are similar to EBS, but they are local drives instead of being presented over the network
- These volumes are physically connected to the EC2 host, instances on the host can access these volumes
- Provides the highest storage performance in AWS
- Instance stores are included in the price of EC2 instances with which they come with
- **Instance stores have to be attached at launch time, they can not be added afterwards!**
- If an EC2 instance moves between hosts the instance store volume loses all its data
- Instances can move between hosts for many reasons: instance are stopped and restarted, maintenance reasons, hardware failure, etc.
- **Instance store volumes are ephemeral volumes!**
- One of the primary benefit of instance stores is performance, ex: D3 instance provides 4.6 GB/s throughput, I3 volumes provide 16 GB/s of sequential throughput with NVMe SSD
- Instance store considerations:
    - Instance store volumes are local to EC2 hosts
    - Instance store can be added only at launch
    - Data is lost on an instance stores in case the instance is moved, resized or there is a hardware failure
    - Instance stores provide high performance
    - For instance store volumes we pay for it with the EC2 instance
    - Instance store volumes are temporary!

## Choosing between Instance Store and EBS

- Fer persistence storage we should default to EBS
- For resilience storage we should avoid instance store an default to EBS
- If the storage should be isolated from EC2 instance lifecycle we should use EBS
- Resilience with in-built replication - we can use both, it depends on the situation
- For high performance needs -  we can also use both, it depends on the situation
- Fos super high performance we should use instance store
- If cost is a primary concern we can use instance store if it comes with the EC2 instance
- Cost consideration: cheaper volumes: ST1 or SC1
- Throughput or streaming: ST1
- Boot volumes: HDD based volumes are not supported (no ST1 or SC1)
- GP2/3 - max performance up to 16000 IOPS
- IO1/2 - up to 64000 IOPS (BlockExpress: 256000)
- RAID0 + EBS: up to 260000 IOPS (maximum possible IOPS per EC2 instance)
- For more than 260000 IOPS - use instance store