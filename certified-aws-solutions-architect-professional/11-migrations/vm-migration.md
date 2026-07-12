# Migrações de VM (VM Migrations) AWS <=> On-Premises

## Application Discovery Service (AMS - Serviço de Descoberta de Aplicativos)

- Permite-nos descobrir a infraestrutura on-premises:
    - Quais VMs temos
    - Quanta CPU e memória estão alocadas a elas
    - Endereços MAC
    - Utilização de recursos
    - etc.
- Ele também acompanha (tracks) essas propriedades ao longo do tempo para uma migração mais eficiente
- O AMS roda em 2 modos:
    - Sem agente (Agentless - Application Discovery Agentless Connector):
        - É um virtual appliance baseado em OVA que se integra com VMWare
        - Ele consegue medir performance e uso de recursos, informações que podem ser obtidas do lado de fora de uma VM
    - Modo Baseado em Agente (Agent Based mode - com o CloudWatch Agent): oferece informações adicionais de dentro de uma VM
        - Oferece coleta de dados de rede, processos, desempenho
        - Podemos ver aplicativos rodando numa VM
        - Podemos até ver dependências entre VMs com base na atividade de rede
- O AMS não migra nada, ele nos ajuda a descobrir instâncias de VM e os relacionamentos entre elas com a finalidade de serem migradas
- Essa informação é valiosa se tivermos milhares de instâncias que queremos migrar
- O AMS se integra com o AWS Migration Hub e Athena
- **AWS Migration Hub**: acompanha migrações de diferentes tipos na AWS. Migrações como as de VM e de banco de dados

## Server Migration Service (SMS - Serviço de Migração de Servidor)

- Usado para migrar VMs inteiras para a AWS (incluindo SO, Dados, Apps, etc.)
- Essa é a ferramenta que realmente executa a migração
- Ele roda em modo agentless usando um conector. O conector é uma VM que roda on-premises dentro do nosso ambiente de VM existente
- O conector se integra com VMware, Hyper-V e AzureVM
- O SMS faz a replicação incremental de volumes ao vivo (live volumes)
- Oferece orquestração de migrações multisservidores (multi-servers)
- Cria AMIs que podem ser usadas para criar instâncias EC2
- Pode ser usado com outras ferramentas como CloudFormation para automatizar a implantação repetida de instâncias
- Ele também se integra com o AWS Migration Hub

## AWS Application Migration Service (MGN)

- É usado para migrar servidores on-premises para a AWS
- Permite que as empresas façam um lift-and-shift de um grande número de servidores físicos, virtuais ou em nuvem sem problemas de compatibilidade, interrupção de desempenho ou longas janelas de cutover (virada)
- A AWS recomenda a replicação baseada em agente quando possível, pois suporta a proteção contínua de dados (CDP)
- O AWS MGN fornece esse agente. O MGN cria um Modelo de Lançamento (Launch Template) que é usado então para lançar instâncias EC2
- O AWS MGN fornece uma maneira de descobrir que tipo de dependências temos entre bancos de dados, servidores de aplicativos, servidores web, etc. Podemos agrupar esses servidores e migrá-los juntos
- Ele também pode fornecer modelos do CloudFormation para implantação (deployment)
- Diferença entre o SMS e o MGN:
    - O Server Migration Service utiliza replicação incremental baseada em snapshots (instantâneos) e permite janelas de cutover em horas
    - O Application Migration Service utiliza replicação contínua em nível de bloco (block-level) e permite curtas janelas de cutover medidas em minutos
- A AWS recomenda o uso do MGN em vez do SMS
- Também podemos migrar servidores virtuais e físicos

---

# VM Migrations AWS <=> On-Premises

## Application Discovery Service (AMS)

- Allows us to discover on-premises infrastructure:
    - What VM we have
    - What CPU and memory they are allocated
    - MAC addresses
    - Resource utilization
    - etc.
- It also tracks these properties over time for more effective migration
- AMS runs in 2 modes:
    - Agentless (Application Discovery Agentless Connector): 
        - It is an OVA based virtual appliance that integrates with VMWare
        - It can measure performance and resource usage, information which can be obtained from the outside of a VM
    - Agent Based mode (with CloudWatch Agent): offers additional information from inside of a VM
        - Offers data gathering for network, processes, performance
        - We can see applications running on a VM
        - We can even see dependencies between VM based on network activity
- AMS does not migrate anything, it helps us discover VM instances and relationships between them in order to be migrated
- This information is valuable if we have thousands of instances we want to migrate
- AMS integrates with AWS Migration Hub and Athena
- **AWS Migration Hub**: tracks migrations of different types in AWS. Migrations such as VM migrations and database migrations

## Server Migration Service (SMS)

- Used to migrate whole VMs into AWS (including OS, Data, Apps, etc.)
- This is the tool which actually performs the migration
- It runs in agentless mode using a connector. The connector is VM which runs on on-premises within our existing VM environment
- The connector integrates with VMware, Hyper-V and AzureVM
- SMS does incremental replication of live volumes
- Offers orchestration of multi-servers migrations
- Creates AMIs which can be used to create EC2 instances
- It can be used with other tooling such as CloudFormations to automate repeated deployment of instances
- It too integrates with AWS Migration Hub

## AWS Application Migration Service (MGN)

- Is used to migrate servers from on-prem to AWS
-  It allows companies to lift-and-shift a large number of physical, virtual, or cloud servers without compatibility issues, performance disruption, or long cutover windows
- AWS recommends agent-based replication when possible as it supports continuous data protection (CDP)
- AWS MGN provides this agent. MGN creates a Launch Template which is then used to launch EC2 instances
- AWS MGN provides a way to work out what kind of dependencies do we have between databases, app servers, web servers, etc. We can group these servers and migrate them together
- It can also provide CloudFormation templates for deployment
- Difference between SMS and MGN:
    - Server Migration Service utilizes incremental, snapshot-based replication and enables cutover windows in hours
    - Application Migration Service utilizes continuous, block-level replication and enables short cutover windows measured in minutes
- AWS recommends to use MGN instead of SMS
- We can migrate virtual and physical servers as well