# DynamoDB

- Produto NoSQL, de coluna larga, DBaaS (Database as a Service)
- O DynamoDB pode lidar com dados de chave/valor ou dados de documento
- Não requer servidores autogerenciados nem infraestrutura para gerenciar
- Suporta uma variedade de opções de scaling:
    - Desempenho provisionado manual/automático entrada/saída
    - Modo Sob Demanda
- O DynamoDB é altamente resiliente entre AZs e, opcionalmente, globalmente
- O DynamoDB é muito rápido; fornece recuperação de dados em milissegundos de um dígito
- Fornece backups automáticos, recuperação pontual e criptografia em repouso
- Suporta integração orientada a eventos; fornece ações quando os dados são modificados dentro de uma tabela

## Tabelas DynamoDB

- Uma tabela no DynamoDB é um agrupamento de itens com a mesma chave primária
- A chave primária pode ser uma chave primária simples (Chave de Partição - PK) ou chave primária composta (Chave de Partição + Chave de Classificação - SK)
- Em uma tabela não há limites para o número de itens
- No caso de chaves compostas, a combinação de PK e SK deve ser única
- Os itens podem ter, além da chave primária, outros dados chamados atributos
- Cada item pode ser diferente, desde que tenha a mesma chave primária
- Um item pode ter no máximo 400 KB
- O DynamoDB pode ser configurado com capacidade provisionada e sob demanda (capacidade = velocidade)
- Para capacidade sob demanda, devemos definir:
    - Unidades de Capacidade de Escrita (WCU): 1 WCU = 1 KB por segundo
    - Unidades de Capacidade de Leitura (RCU): 1 RCU = 4 KB por segundo

## Backups do DynamoDB

- Backups sob demanda:
    - Uma cópia completa da tabela é retida até que o backup seja removido
    - Os backups sob demanda podem ser usados para restaurar dados e configurações para a mesma região ou entre regiões
    - Se restaurarmos um backup, podemos reter ou remover índices
    - Da mesma forma, podemos ajustar as configurações de criptografia
- Recuperação Pontual:
    - Não habilitada por padrão; deve ser habilitada
    - É um registro contínuo de alterações
    - Permite repetição em qualquer ponto na janela (janela de recuperação de 35 dias)
    - Desta janela de 35 dias, podemos restaurar para outra tabela com granularidade de 1 segundo

## Considerações sobre o DynamoDB

- É um banco de dados NoSQL; NÃO é relacional; não é adequado para dados relacionais
- É um banco de dados de Chave/Valor
- O acesso às tabelas do DynamoDB é via console, CLI ou API (SDK)
- A linguagem de consulta SQL verdadeira não é suportada; o DynamoDB oferece suporte para PartiQL (linguagem semelhante a SQL)
- Faturamento: baseado em RCU/WCU, armazenamento e recursos adicionais habilitados. A alocação reservada pode ser comprada para compromissos mais longos

## Operação, Consistência e Desempenho do DynamoDB

- Podemos escolher entre dois modos de capacidade diferentes na criação da tabela: sob demanda e provisionado
- Podemos ser capazes de alternar entre esses modos de capacidade posteriormente
- Modo de capacidade sob demanda:
    - Projetado para carga desconhecida e imprevisível
    - Requer baixa administração
    - Não precisamos definir explicitamente as configurações de capacidade; tudo é gerenciado pelo DynamoDB
    - Pagamos um preço por milhão de unidades de leitura ou escrita
- Modo de capacidade provisionada:
    - Definimos o RCU/WCU por tabela
- Cada operação consome pelo menos 1 RCU/WCU
- 1 RCU é `1 * 4 KB` de operação de leitura por segundo para leituras fortemente consistentes; `2 * 4 KB` de operações de leitura por segundo para leituras eventualmente consistentes
- 1 WCU é `1 * 1 KB` de operação de escrita por segundo
- Cada tabela tem um pool de burst de RCU e WCU (300 segundos)
- Operações do DynamoDB:
    - **Consulta (Query)**:
        - Quando uma consulta é realizada, precisamos fornecer uma chave de partição. Opcionalmente, podemos fornecer uma chave de classificação ou um intervalo
        - A consulta pode retornar 0 ou mais itens, mas precisamos especificar a chave de partição sempre
        - Podemos especificar atributos específicos que gostaríamos que fossem retornados; seremos cobrados por consultar o item inteiro de qualquer forma
    - **Varredura (Scan)**:
        - Operação menos eficiente, mas a mais flexível
        - A varredura percorre uma tabela consumindo a capacidade de cada item
        - Qualquer atributo pode ser usado e qualquer filtro pode ser aplicado, mas a varredura consumirá a capacidade de cada item varrido

## Modelo de Consistência do DynamoDB

- O DynamoDB pode operar usando dois modos de consistência diferentes:
    - Eventualmente consistente
    - Fortemente (imediatamente) consistente
- O DynamoDB replica dados entre AZs usando nós de armazenamento. Os nós de armazenamento têm um nó líder, que é eleito a partir dos nós existentes
- O DynamoDB tem um conjunto de entidades que redirecionam conexões para os nós de armazenamento apropriados. As gravações são sempre direcionadas ao nó líder
- O nó líder replica dados para outros nós, geralmente concluindo em alguns milissegundos
- Existem 2 tipos de leituras possíveis no DynamoDB:
    - Leituras eventualmente consistentes:
        - Pode acontecer que tentemos ler dados que estão desatualizados (stale) / totalmente ausentes
        - Podemos ler o dobro de dados com o mesmo número de RCUs
    - Leituras fortemente consistentes:
        - Essas operações de leitura sempre usam o nó líder
        - Nem todo aplicativo pode tolerar leituras eventualmente consistentes
        - Leituras fortemente consistentes custam duas vezes mais do que as eventualmente consistentes

## Cálculo de WCU/RCU

- Exemplo: precisamos armazenar 10 itens por segundo, tamanho médio de 2,5 KB por item
    - WCU necessário:
        ```
        ARREDONDAR PARA CIMA(TAMANHO DO ITEM / 1 KB) => 3
        MULT pela média (30) => WCU necessário = 30
        ```
- Exemplo: precisamos recuperar 10 itens por segundo, tamanho médio de 2,5 KB por item
    - RCU necessário:
        ```
        ARREDONDAR PARA CIMA (TAMANHO DO ITEM / 4 KB) => 1
        MULT pela média de operações de leitura por segundo (10) => Leituras fortemente consistentes = 10, Leituras eventualmente consistentes => 5
        ```

## Índices do DynamoDB

- São formas de melhorar a eficiência da recuperação de dados do DynamoDB
- Os índices são visões alternativas dos dados da tabela, permitindo que a operação de consulta funcione de formas que não seria possível de outra forma
- Índices Secundários Locais permitem criar uma visão usando uma chave de classificação diferente; Índices Secundários Globais permitem criar uma chave de partição e classificação diferentes

### Índices Secundários Locais (LSI)

- **Devem ser criados com a tabela base!**
- Podemos ter no máximo 5 LSIs por tabela base
- Os LSIs permitem uma chave de classificação alternativa, mas com a mesma chave de partição
- Compartilham o mesmo RCU e WCU com a tabela principal
- Atributos que podem ser projetados nos LSIs: `ALL`, `KEYS_ONLY`, `INCLUDE` (podemos escolher especificamente quais atributos incluir)
- Os Índices Secundários Locais são esparsos: apenas itens que têm um valor na chave de classificação alternativa do índice são adicionados ao índice

### Índices Secundários Globais (GSI)

- Podem ser criados a qualquer momento
- É um limite padrão de 20 GSIs por tabela base
- Podemos definir diferentes chaves de partição e classificação
- Os GSIs têm suas próprias alocações de RCU e WCU caso estejamos usando capacidade provisionada
- Atributos que podem ser projetados em um índice: `ALL`, `KEYS_ONLY`, `INCLUDE`
- Os GSIs também são esparsos; apenas itens que têm valores na nova PK e SK opcional são adicionados ao índice
- Os GSIs são sempre eventualmente consistentes; os dados são replicados da tabela principal

### Considerações sobre LSI e GSI

- Devemos ter cuidado com as projeções; mais capacidade é consumida se projetarmos atributos desnecessários
- Se não projetarmos um atributo específico e o exigirmos ao consultar o índice, ele buscará os dados da tabela principal, tornando a consulta ineficiente
- A AWS recomenda usar GSIs como padrão; LSI somente quando a consistência forte é necessária

## Streams e Gatilhos do DynamoDB

- Um stream do DynamoDB é uma lista ordenada por tempo de alterações de itens em uma tabela DynamoDB
- Um stream do DynamoDB é uma janela deslizante de 24 horas dessas alterações. Nos bastidores, usa o Kinesis Streams
- Os streams devem ser habilitados por tabela
- Os streams registram inserções, atualizações e exclusões
- Podemos criar diferentes tipos de visão que influenciam o que está no stream
- Tipos de visão disponíveis:
    - `KEYS_ONLY`: o stream registrará apenas a chave de partição e as chaves de classificação disponíveis para itens que foram alterados
    - `NEW_IMAGE`: armazena o item inteiro com o novo estado após a alteração
    - `OLD_IMAGE`: armazena o estado inteiro do item antes da alteração
    - `NEW_AND_OLD_IMAGE`: armazena os estados antes/depois dos itens em caso de alteração
- Em alguns casos, os novos/antigos estados registrados podem estar vazios; exemplo: no caso de uma exclusão, o novo estado de um item fica em branco
- Os streams são a base dos gatilhos de banco de dados
- Uma alteração de item dentro de uma tabela gera um evento, que contém os dados que foram alterados
- Uma ação é tomada usando esses dados no caso de evento
- Podemos usar streams e Lambda no caso de alterações e eventos
- Streams e gatilhos são úteis para agregação de dados, mensagens, notificações, etc.

## DynamoDB Accelerator (DAX)

- É um cache em memória diretamente integrado ao DynamoDB
- O DAX opera dentro de uma VPC; projetado para ser implantado em múltiplas AZs em uma VPC
- O DAX é um serviço de cluster; os nós são colocados em diferentes AZs. Há nós primários a partir dos quais os dados são replicados para nós de réplica
- O DAX mantém 2 caches diferentes:
    - Cache de itens: mantém os resultados das chamadas (`Batch`)`GetItem`
    - Cache de consulta: mantém a coleção de itens com base nos parâmetros de consulta/varredura
- O DAX é acessado por meio de um endpoint. Este endpoint balanceia a carga entre os nós
- Os nós são altamente disponíveis (HA); se o nó primário falhar, outro nó é eleito
- O DAX pode escalar verticalmente (UP) ou horizontalmente (OUT)
- Ao gravar dados no DynamoDB, o DAX usa cache de gravação direta (write-through); os dados são gravados ao mesmo tempo no cache e no banco de dados
- O DAX é implantado em uma VPC! Qualquer aplicação que queira usar o DAX também deve estar em uma VPC
- Cache hits são retornados em microssegundos; cache misses em milissegundos
- O DAX não é adequado para aplicações que exigem leituras fortemente consistentes

## Tabelas Globais do DynamoDB

- As tabelas globais fornecem replicação multi-master entre regiões
- Para implementar tabelas globais, precisamos criar tabelas em múltiplas regiões e adicioná-las à mesma tabela global (tornando-se tabelas de réplica)
- O DynamoDB utiliza **last writer wins** (último escritor vence) na resolução de conflitos
- Podemos ler e gravar em qualquer região; as atualizações geralmente são replicadas em menos de um segundo
- Leituras fortemente consistentes são suportadas apenas na mesma região que as gravações
- As tabelas globais fornecem HA global e DR/BC global

## TTL do DynamoDB

- TTL = Time-to-Live (Tempo de Vida)
- Para usar o TTL, precisamos habilitá-lo em uma tabela e selecionar um atributo específico para o TTL
- O atributo deve conter um número representando uma época (número de segundos)
- Um processo por partição verifica periodicamente o tempo atual em relação ao valor no atributo TTL
- Itens onde o atributo TTL é mais antigo que o tempo atual são definidos como expirados
- Outro processo em segundo plano por partição verifica itens expirados e os remove das tabelas e índices, adicionando um evento de exclusão aos streams, se habilitados
- Esses processos são executados em segundo plano sem afetar o desempenho da tabela e sem nenhuma cobrança adicional
- Podemos configurar um stream dedicado vinculado aos processos TTL, com uma janela deslizante de 24 horas para quaisquer exclusões causadas pelos processos TTL. Útil se quisermos ter qualquer manutenção onde rastreamos os eventos TTL que ocorrem nas tabelas (por exemplo, podemos implementar um processo de desfazer exclusão)

---

# DynamoDB

- NoSQL, wide column, DB-as-service product
- DynamoDB can handle key/value data or document data
- It requires no self-managed servers of infrastructure to be managed
- Supports a range of scaling options:
    - Manual/automatic provisioned performance IN/OUT
    - On-Demand mode
- DynamoDB is highly resilient across AZs and optionally globally
- DynamoDB is really fast, provides single-digit millisecond data retrieval
- Provides automatic backups, point-in-time recovery and encryption at rest
- Supports event-driven integration, provides actions when data is modified inside a table

## DynamoDB Tables

- A table in DynamoDB is a grouping of items with the same primary key
- Primary key can be a simple primary key (Partition Key - PK) or composite primary key (Partition Key + Sort Key - SK)
- In a table there are no limits to the number of items
- In case of composite keys, the combination of PK and SK should be unique
- Items can have, besides primary key, other data named attributes
- Every item can be different as long as it has the same primary key
- An item can be at max 400 KB
- DynamoDB can be configured with provisioned and on-demand capacity (capacity = speed)
- For on-demand capacity, we have to set:
    - Wite-Capacity Units (WCU): 1 WCU = 1KB per second
    - Read-Capacity Units (RCU): 1 RCU = 4KB per second

## DynamoDB Backups

- On-demand backups:
    - Full copy of the table is retained until the backup is removed
    - On-demand backups can be used restore data and config to same region or cross-region
    - If we restore a backup we can retain or remove indexes
    - Similarly, we can adjust encryption settings
- Point-in-time Recovery:
    - Not enabled by default, has to be enabled
    - It is a continuous record of changes
    - Allows replay to any point in the window (35 days recovery window)
    - From this 35 day window we can restore to another table with a 1 second granularity

## DynamoDB Considerations

- It is a NoSQL database, it is NOT relational, not suited for relational data
- It is a Key/Value database
- Access to DynamoDB tables is via console, CLI, or API (SDK)
- True SQL query language is not supported, DynamoDB offers support for PartiQL (SQL like language)
- Billing: based on RCU/WCU, storage and additional features enabled. Reserved allocation can be purchased for longer commitments

## DynamoDB Operation, Consistency and Performance

- We can chose between to different capacity mode at table creation: on-demand and provisioned
- We may be able to switch between this capacity mode afterwards
- On-demand capacity mode: 
    - Designed for unknown, unpredictable load
    - Requires low administration
    - We don't have to explicitly set capacity settings, all handled by DynamoDB
    - We pay a price per million R or W unit
- Provisioned capacity mode:
    - We set the RCU/WCU per table
- Every operation consumes at least 1RCU/WCU
- 1 RCU is `1 * 4KB` read operation per second for strongly consistent reads, `2 * 4KB` read operations per second for eventual consistent reads
- 1 WCU is `1 * 1KB` write operation per second
- Every table has a RCU and WCU bust pool (300 seconds)
- DynamoDB operations:
    - **Query**:
        - When a query is performed we need to provide a partition key. Optionally we can provide a sort key or a range
        - Query item can return 0 or more items, but we have to specify the partition key every time
        - We can specify specific attribute we would want to be returned, we will be charged for querying the whole item anyway
    - **Scan**:
        - Least efficient operation, but the most flexible
        - Scan moves through a table consuming the capacity of every item
        - Any attribute can be used and any filters can be applied, but scan will consume the capacity for every item scanned through

## DynamoDB Consistency Model

- DynamoDB can operate using two different consistency modes:
    - Eventually consistent
    - Strongly (immediately) consistent
- DynamoDB replicates data cross AZs using storage nodes. Storage nodes have a leader node, which is elected from the existing nodes
- DynamoDB has a fleet of entities which redirect connections to the appropriate storage nodes. Writes are always directed to leader node
- The leader nodes replicates data to other nodes, typically finishing within a few milliseconds
- There are 2 types of reads possible in DynamoDB:
    - Eventually consistent reads:
        - It might happen that we attempt to read data which is outdated (stale) / not present at all
        - We can read double the amount of data with the same number of RCUs
    - Strongly consistent reads:
        - These read operations always use the leader node
        - Not every application can tolerate eventual consistent reads
        - Strongly consistent reads cost two times more than eventual consistent ones

## WCU/RCU Calculation

- Example: we need to store 10 items per second, 2.5K average size per item
    - WCU required: 
        ```
        ROUND UP(ITEM SIZE / 1 KB) => 3
        MULT by average (30) => WCU required = 30
        ```
- Example: we need to retrieve 10 items per second, 2.5K average size per item
    - RCU required:
        ```
        ROUND UP (ITEM SIZE / 4 KB) => 1
        MULT by average read ops per second (10) => Strongly consistent reads = 10, Eventually consistent reads => 5
        ```

## DynamoDB Indexes

- Are way to improve efficiency of data retrieval from DynamoDB
- Indexes are alternative views on table data, allowing the query operation to work in ways that it couldn't otherwise
- Local Secondary Indexes allow to create a view using different sort key, Global Secondary Indexes allow to create create different partition and sort key

### Local Secondary Indexes (LSI)

- **Must be created with the base table!**
- We can have at max 5 LSIs per base table
- LSIs allow an alternative sort key, but with the same partition key
- They share the same RCU and WCU with the main table
- Attributes which can be projected into LSIs: `ALL`, `KEYS_ONLY`, `INCLUDE` (we can specifically pick which attribute to be included)
- Local Secondary Indexes are sparse: only items which have a value in the index alternative sort key are added to the index

### Global Secondary Indexes (GSI)

- They can be created at any time
- It is a default limit of 20 GSIs per base table
- We cane define different partition and sort keys
- GSIs have their own RCU and WCU allocations in case we are using provisioned capacity
- Attributes which can be projected into an index: `ALL`, `KEYS_ONLY`, `INCLUDE`
- GSIs are also sparse, only items which have values in the new PK and optional SK are added to the index
- GSIs are always eventually consistent, the data is replicated from the main table

### LSI and GSI Considerations

- We have to be careful with the projections, more capacity is consumed if we project unnecessary attributes
- If we don't project a specific attribute and require that when querying the index, it will fetch the data from the main table, the query becoming inefficient
- AWS recommends using GSIs as default, LSI only when strong consistency is required

## DynamoDB Streams and Triggers

- A DynamoDB stream is a time ordered list of item changes in a DynamoDB table
- A DynamoDB stream is a 24H rolling window of these changes. Behind the scenes uses Kinesis Streams
- Streams has to be enabled per table basis
- Streams record inserts, updates and deletes
- We can create different view types influencing what is in the stream
- Available view types:
    - `KEYS_ONLY`: the stream will only record the partition key and available sort keys for items which did change
    - `NEW_IMAGE`: stores the entire item with the new state after the change
    - `OLD_IMAGE`: stores the entire state of the item before the change
    - `NEW_AND_OLD_IMAGE`: stores the before/after states of the items in case of a change
- In some cases the new/old states recorded can be empty, example in case of a deletion the new state of an item is blank
- Streams are the foundation for database triggers
- An item change inside a table generate an event, which contains the data which changed
- An action is taken using that data in case of event
- We can use streams and Lambda in case of changes and events
- Streams and triggers are useful for data aggregation, messaging, notifications, etc.

## DynamoDB Accelerator (DAX)

- It is an in-memory cache directly integrated with DynamoDB
- DAX operates within a VPC, designed to be deployed in multiple AZs in a VPC
- DAX is a cluster service, nodes are placed in different AZs. There a primary nodes from which data is replicated into replica nodes
- DAX maintains 2 different caches:
    - Items cache: holds results of (`Batch`)`GetItem` calls
    - Query cache: holds the collection of items based on query/scan parameters
- DAX is accessed via an endpoint. This endpoint load balances across nodes
- Nodes are HA, if primary node fails another node is elected
- DAX can scale UP or scale OUT
- When writing data to DynamoDB, DAX uses write-through caching, the data is written at the same time to the cache as it is written to the DB
- DAX is deployed in a VCP! Any application which wants to use DAX has to be in a VPC as well
- Cache hits are returned in microseconds, cache misses in milliseconds
- DAX is not suitable for applications requiring strongly consistent reads

## DynamoDB Global Tables

- Global tables provide multi-master cross-region replication
- To implement global tables we have to create tables in multiple regions and add them to the same global table (becoming replicate tables)
- DynamoDB utilizes **last writer wins** in conflict resolution
- We can read and write to any region, updates are replicated generally sub-second
- Strongly consistent reads are only supported in the same region as writes
- Global tables provide global HA and global DR/BC

## DynamoDB TTL

- TTL = Time-to-Live
- In order to use TTL we have to enable it on a table and select a specific attribute for the TTL
- The attribute should contain a number representing an epoch (number of seconds)
- A per-partition process periodically runs for checking the current time to the value in the TTL attribute
- Items where the TTL attribute is older than the current time are set to expired
- Another per-partition background process scans for expired items and removes them from tables and indexes, adding a delete event to the streams is enabled
- These processes run on the background without affecting the performance of the table and without any additional charge
- We can configure a dedicated stream linked to the TTL processes, having 24h rolling window for any deletions caused by the TTL processes. Useful if we want to have any housekeeping where we track the TTL events that occur on tables (for example we can implement an un-delete process)