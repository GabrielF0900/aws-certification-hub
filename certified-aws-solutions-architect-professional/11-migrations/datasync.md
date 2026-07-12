# AWS DataSync

- É um serviço de transferência de dados que permite que dados sejam transferidos para dentro ou fora da AWS
- Pode ser usado para fluxos de trabalho (workflows) como migrações, transferências de processamento de dados, arquivamento, armazenamento econômico e DR/BC (Recuperação de Desastres / Continuidade de Negócios)
- Cada agente (agent) pode lidar com velocidades de transferência de 10 Gbps, e cada trabalho (job) pode lidar com 15 milhões de arquivos
- Ele também lida com a transferência de metadados (permissões, carimbos de data e hora)
- Ele fornece validação de dados integrada (built in)

## Principais Recursos (Key Features)

- Escalável: 10 Gbps por agente (~100 TB de dados por dia)
- Limitadores de Largura de Banda (Bandwidth Limiters): usados para evitar a saturação do link
- Opções de transferência incremental e agendada
- Compressões e criptografia
- Recuperação automática de erros de trânsito
- Integração de serviço: S3, EFS, FSx, transferência serviço-a-serviço
- Serviço "Pague conforme usa" (Pay as you go): por GB de dados transferidos
- O agente (agent) do DataSync roda numa plataforma de virtualização como o VMWare

## Componentes do DataSync

- Task (Tarefa): um trabalho (job) no DataSync, define o que está sendo sincronizado, com que rapidez, de onde e para onde
- Agent (Agente): software usado para ler ou gravar em armazenamentos de dados on-premises (locais) usando NFS ou SMB
- Location (Local): toda tarefa tem dois locais de origem e destino, exemplos: Network File System (NFS), Server Message Block (SMB), Amazon EFS, Amazon FSx e Amazon S3

---

# AWS DataSync

- It is a data transfer service which allows data to be transferred into or out of AWS
- Can be used for workflows such as migrations, data processing transfers, archival, cost effective storage, DR/BC
- Each agent can handle 10 Gbps transfer speed, each job can handle 15 million files
- It also handles the transfer of metadata (permissions, timestamps)
- It provides built in data validation

## Key Features

- Scalable: 10 Gbps per agent (~100 TB of data per day)
- Bandwidth Limiters: used to avoid link saturation
- Incremental and scheduled transfer options
- Compressions and encryption
- Automatic recovery from transit errors
- Service integration: S3, EFS, FSx, service-to-service transfer
- Pay as you use service: per GB of data transferred
- The DataSync agent runs on a virtualization platform such as VMWare

## DataSync Components

- Task: a job within DataSync, defines what is being synced, how quickly, from where and to where
- Agent: software used to read or write to on-premises data stores using NFS or SMB
- Location: every task has two locations from and to, examples: Network File System (NFS), Server Message Block (SMB), Amazon EFS, Amazon FSx and Amazon S3