# FSx

## FSx para Windows File Servers

- O FSx para Windows oferece servidores de arquivos/compartilhamentos de arquivos nativos do Windows totalmente gerenciados
- Projetado para integração com ambientes Windows
- Integra-se com o AWS Managed Microsoft AD ou AD autogerenciado (Self-Managed AD)
- Serviço resiliente e altamente disponível. Pode ser implantado em uma única AZ (Single-AZ) ou em múltiplas AZs (Multi-AZ) dentro de uma VPC. Mesmo em uma implantação Single-AZ, o backend do serviço usa replicação para garantir que seja resiliente a falhas de hardware
- Ele pode realizar uma gama completa de diferentes tipos de backups, incluindo recursos do lado do cliente e do lado da AWS. No lado da AWS, pode realizar backups automáticos e sob demanda
- O FSx pode ser acessado através de VPC Peering, VPN e DX
- O FSx suporta eliminação de duplicidade (deduplication), escalonamento através do Distributed File System (DFS), criptografia em repouso com KMS e criptografia obrigatória em trânsito
- Permite cópias de sombra de volume (Volume Shadow Copies), possibilitando restaurar versões anteriores de um arquivo
- É altamente performático: taxa de transferência (throughput) de 8 MB/s até 2 GB/s, centenas de milhares de IOPS e latência <1ms
- Recursos:
    - VSS - restaurações orientadas pelo usuário (visualizar versões anteriores)
    - Sistema de arquivos nativo acessível via SMB
    - Usa o modelo de permissão do Windows
    - Suporta DFS – estrutura de compartilhamento de arquivos com scale-out, agrupando compartilhamentos em uma única estrutura corporativa
    - Gerenciado – sem necessidade de administrador de servidor de arquivos
    - Integra-se com o Amazon Managed DS ou com o nosso próprio diretório

## FSx para Lustre

- Sistema de arquivos projetado para cargas de trabalho de alto desempenho
- É uma implementação gerenciada do sistema de arquivos Lustre, projetada para HPC - clientes Linux (sistema de arquivos compatível com POSIX)
- O Lustre foi projetado para machine learning, big data e modelagem financeira
- Pode escalar para centenas de GB/s de throughput e oferece latência sub-milissegundo
- Pode ser provisionado usando 2 tipos diferentes de implantação:
    - Persistente (Persistent): fornece alta disponibilidade (HA) em apenas uma AZ, possui autocorreção (self-healing) e é recomendado para armazenamento de dados de longo prazo
    - Temporário (Scratch): altamente otimizado para soluções de curto prazo, não fornece replicação
- O FSx está disponível via VPN ou DX para ambientes locais (on-premises)
- Repositório S3: os arquivos são armazenados no S3 e carregados de forma tardia (lazy loading) no sistema de arquivos FSx para Lustre no primeiro uso
- Sincronização de alterações entre o sistema de arquivos e o S3: comando `hsm_archive`. O sistema de arquivos e o bucket do S3 não entram em sincronia automaticamente
- Sistema de arquivos Lustre:
    - MST - Metadados armazenados em Alvos de Metadados (Metadata Targets)
    - OST - Os objetos são armazenados em alvos de armazenamento de objetos (Object Storage Targets), cada um podendo ter até 1,17 TiB
- O desempenho de linha de base (baseline performance) do sistema de arquivos é baseado no tamanho:
    - Tamanho: mínimo de 1,2 TiB e depois podemos usar incrementos de 2,4 TiB
    - Scratch: base de 200 MB/s por TiB de armazenamento
    - Ofertas de desempenho: 50 MB/s, 100 MB/s e 200 MB/s por TiB de armazenamento
    - Para ambos os tipos, podemos fazer burst de até 1300 MB/s por TiB usando créditos
- Tipos de implantação do FSx para Lustre:
    - Scratch:
        - É projetado para desempenho puro, voltado para cargas de trabalho de curto prazo e temporárias
        - Não fornece nenhum tipo de alta disponibilidade (HA) ou replicação; em caso de falha de hardware, todos os dados armazenados naquele hardware são perdidos
        - Sistemas de arquivos maiores significam mais servidores, mais discos => maior chance de falha
    - Persistent:
        - Possui replicação dentro de apenas uma AZ
        - Corrige-se automaticamente (auto-heals) quando ocorre uma falha de hardware
    - Ambas as opções fornecem backups para o S3 (manuais ou automáticos com retenção de 0 a 35 dias)

## FSx para NetApp ONTAP

- Armazenamento totalmente gerenciado construído sobre o NetApp ONTAP
- Oferece um conjunto rico de recursos disponíveis com o software de gerenciamento de dados da NetApp:
    - Eficiências de armazenamento: compressão, eliminação de duplicidade (deduplication), compactação, thin provisioning
    - Definição de camadas (tiering) de pool de capacidade de baixo custo e totalmente elástica
    - Proteção de dados: snapshots, SnapVault e backups nativos do Amazon FSx
    - Recuperação de desastres (DR) usando SnapMirror e Amazon FSx Backups
    - Cache: FlexCache, Global File Cache
    - Acesso multiprotocolo a partir do Linux, Windows
    - Outros recursos: varredura de antivírus
- Movimentação inteligente de dados entre camadas (tiers) baseada em políticas:
    - O sistema de arquivos Amazon FSx para NetApp ONTAP possui duas camadas de armazenamento: armazenamento primário (primary storage) e armazenamento de pool de capacidade (capacity pool storage)
        - O armazenamento primário é um armazenamento SSD provisionado, escalável e de alto desempenho (até 192 TB), construído especificamente para a parte ativa do nosso conjunto de dados
        - O armazenamento de pool de capacidade é uma camada de armazenamento totalmente elástica que pode escalar para o tamanho de petabytes e é otimizada para custos para dados acessados com pouca frequência
    - Habilitar o tiering permite a movimentação inteligente de dados entre as camadas com base no acesso
- Casos de uso para o NetApp ONTAP:
    - Backup e arquivamento usando SnapVaults
    - Cópia de recuperação de desastres (DR) entre regiões dos dados de arquivos do FSx usando SnapMirror
    - FlexCache para armazenar dados em cache e aproximar os dados entre regiões e o acesso local (on-premises)
    - Pode ser usado com o Amazon WorkSpaces para fornecer armazenamento anexado à rede (NAS) compartilhado ou para armazenar perfis móveis (roaming profiles) para contas do Amazon WorkSpaces

## FSx para OpenZFS

- Serviço de armazenamento de arquivos totalmente gerenciado construído sobre o sistema de arquivos de código aberto OpenZFS
- Pode ser acessado através do protocolo Network File System (NFS), padrão da indústria
- Alimentado por processadores AWS Graviton, juntamente com as mais recentes tecnologias de disco e rede da AWS
- Casos de uso:
    - Migração de dados locais (on-premises) armazenados em ZFS ou outros servidores de arquivos baseados em Linux para a AWS
    - Uma ampla variedade de cargas de trabalho Linux, Windows e macOS, incluindo big data e analytics, repositórios de código e artefatos, soluções de DevOps, gerenciamento de conteúdo web, automação de design eletrônico (EDA) front-end, pesquisa genômica e processamento de mídia
- Segurança dos dados:
    - A criptografia de dados em repouso é habilitada automaticamente quando criamos um sistema de arquivos Amazon FSx para OpenZFS através da AWS
    - O Amazon FSx para OpenZFS usa o algoritmo de criptografia AES-256 padrão da indústria para criptografar os dados do sistema de arquivos em repouso
    - Os sistemas de arquivos Amazon FSx para OpenZFS criptografam dados em trânsito automaticamente quando são acessados a partir de instâncias Amazon EC2 que suportam criptografia em trânsito

---

# FSx

## FSx For Windows File Servers

- FSx for Windows are fully managed native Windows file servers/file shares
- Designed for integration with Windows environments
- Integrates with AWS managed Directory Service or Self-Managed AD
- Resilient and highly available service. Can be deployed in single or multi-AZ within a VPC. Even in a single-AZ deployment the backend of the service uses replications to ensure that is resilient to hardware failure
- It can perform a full range of different kind of backups, including client-side and AWS-side features. On the AWS-side, it can perform automatic and on-demand backups
- FSx can be accessed over VPC peering, VPN and DX
- FSx supports de-duplication, scaling through Distributed File System (DFS), KMS at rest encryption and enforced encryption in transit
- Allows for volumes shadow copies, we can initiate previous versions for a file
- It is highly performant: 8 MB/s up to 2 GB/s throughput, 100k's IOPS, <1ms latency
- Features:
    - VSS - user-driven restores (view previous versions)
    - Native file system accessible over SMB
    - Uses Windows permission model
    - Supports DFS - scale-out file share structure, group file shares together in one enterprise-wise structure
    - Managed - no file server admin
    - Integrates with Amazon managed DS or our own directory

## FSx for Lustre

- File system designed for high performance workloads
- Is a managed implementation of the Lustre file system, designed for HPC - Linux clients (POSIX file system)
- Lustre is designed for machine learning, big data, financial modelling
- Can scale to 100's GB/s throughput and offers sub millisecond latency
- Can be provisioned using 2 different deployment types:
    - Persistent: provides HA in one AZ only, provides self-healing, recommended for long term data storage
    - Scratch: highly optimized for short term solutions, no replication is provided
- FSx is available over VPN or DX for on-premises
- S3 repository: files are stored in S3 and they are lazily loaded into FSx for Lustre file system at first usage
- Sync changes between the file system and S3: `hsm_archive` command. The file system and the S3 bucket are not automatically in sync
- Lustre file system:
    - MST - Metadata stored on Metadata Targets
    - OST - Objects are stored on object storage targets, each can be up to 1.17 TiB
- Baseline performance of the file system is based on the size:
    - Size: min 1.2 TiB  and then we can use increments of 2.4 TiB
    - Scratch: base 200 MB/s per TiB of storage
    - Performance offers: 50 MB/s, 100 MB/s and 200 MB/s per TiB storage
    - For both types we can burst up to 1300 MB/s per TiB using credits
- FSx for Luster deployment types:
    - Scratch:
        - Is designed for pure performance, for short term and temporary workloads
        - Does not provide any type of HA or replication, in case of a HW failure all the data stored on that hardware is lost
        - Larger file systems mean more servers, more disks => more chance of failure
    - Persistent:
        - Has replication within one AZ only
        - Auto-heals when hardware failure occurs
    - Both of these options provide backups to S3 (manual or automatic with a retention of 0-35 days)

## FSx for NetApp ONTAP

- Fully managed storage built on NetAPP ONTAP
- Provides reach set of features available with NetApp's data management software:
    - Storage efficiencies: compression, deduplication, compaction, thin provisioning
    - Low-cost, fully elastic capacity pool tiering
    - Data protection: snapshots, SnapVault and native Amazon FSx backups
    - Disaster recovery using SnapMirror and Amazon FSx Backups
    - Caching: FlexCache, Global File Cache
    - Multiprotocol access from Linux, Windows
    - Other features: antivirus scanning
- Intelligent policy-based data movement between tier:
    - Amazon FSx for NetApp ONTAP file system has two storage tiers: primary storage and capacity pool storage
        - Primary storage is provisioned, scalable, high-performance SSD storage (up to 192 TB) that’s purpose-built for the active portion of our data set
        - Capacity pool storage is a fully elastic storage tier that can scale to petabytes in size and is cost-optimized for infrequently accessed data
    - Enabling tiering allows intelligent data movement between tiers based on the access
- Use case for NetApp ONTAP:
    - Backup and archive using SnapVaults
    - Cross region DR copy of FSx file data using SnapMirror
    - FlexCache for caching data and bringing data closer between regions and on-prem access
    - Can be used with Amazon WorkSpaces to provide shared network-attached storage (NAS) or to store roaming profiles for Amazon WorkSpaces accounts

## FSx for OpenZFS

- Fully managed file storage service built on the open-source OpenZFS file system
- Can be accessed over the industry-standard Network File System (NFS) protocol
- Powered by AWS Graviton processors, along with the latest AWS disk and networking technologies
- Use cases:
    - Migration of on-premises data stored in ZFS or other Linux-based file servers to AWS
    - Wide range of Linux, Windows, and macOS workloads, including big data and analytics, code and artifact repositories, DevOps solutions, web content management, front-end electronic design automation (EDA), genomics research, and media processing
- Data security:
    - Encryption of data at rest is automatically enabled when we create an Amazon FSx for OpenZFS file system through the AWS
    - Amazon FSx for OpenZFS uses industry-standard AES-256 encryption algorithm to encrypt file system data at rest
    - Amazon FSx for OpenZFS file systems automatically encrypt data in transit when they are accessed from Amazon EC2 instances that support encryption in transit