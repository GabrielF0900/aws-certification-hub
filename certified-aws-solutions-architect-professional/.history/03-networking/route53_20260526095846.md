# Route53

## Fundamentos de DNS (DNS Fundamentals)

- O DNS é um serviço de descoberta, traduz informações que as máquinas precisam em informações que os humanos precisam e vice-versa
- Exemplo: www.amazon.com => 104.98.34.131
- A base de dados do DNS é uma enorme base de dados distribuída
- O DNS permite que um servidor resolvedor de DNS (DNS resolver) encontre um Arquivo de Zona (Zone File) em um Servidor de Nomes (Name Server - NS) e faça uma consulta a ele, recuperando o endereço IP necessário para um nome de DNS

## Terminologia de DNS

- **Cliente DNS (DNS Client)**: refere-se ao PC, laptop, tablet, etc., de um cliente
- **Resolvedor DNS (DNS Resolver)**: software executado em um dispositivo ou servidor que faz consultas DNS em nosso nome
- **Zona DNS (DNS Zone)**: uma parte da base de dados do DNS (exemplo: amazon.com)
- **Arquivo de Zona (Zone file)**: é uma base de dados física para uma zona, contém todas as informações de DNS para um domínio específico
- **Servidor de Nomes DNS (DNS Name server)**: um servidor que hospeda os arquivos de zona

## Raiz do DNS (DNS Root)

- O DNS é estruturado como uma árvore, e a raiz do DNS (DNS root) está no topo da árvore
- A raiz do DNS é hospedada em 13 servidores de nomes especiais, conhecidos como Servidores Raiz de DNS (DNS Root Servers)
- Arquivo root hints: um arquivo do sistema operacional que contém o endereço de todos os servidores raiz
- Autoridade (Authority): quando algo é confiável no DNS, por exemplo, o arquivo root hints
- Delegação (Delegation): autoridades confiáveis podem delegar uma parte de si mesmas para outras entidades, tornando essas entidades autoritativas para a parte delegada

## Introdução ao Route53

- É um produto de DNS gerenciado
- Fornece 2 serviços principais:
    - Registro de domínios
    - Pode hospedar arquivos de zona em servidores de nomes gerenciados
- É um serviço global, sua base de dados é distribuída globalmente e resiliente

## Zonas Hospedadas (Hosted Zones)

- DNS como serviço
- Permite criar e gerenciar arquivos de zona
- Os arquivos de zona são hospedados em 4 servidores de nomes gerenciados pela AWS
- A zona hospedada pode ser pública (acessível pela internet pública, fazendo parte do sistema de DNS público) ou privada (vinculada a uma ou mais VPCs)
- Uma zona hospedada armazena registros DNS (recordsets)

## Tipos de Registros DNS (DNS Record Types)

- Servidor de Nomes (NS - Name server): permite que a delegação ocorra no DNS
- Registros A e AAAA: mapeiam nomes de host para endereços IP. Registros A mapeiam um nome de host para IPv4, e registros AAAA mapeiam o host para endereços IPv6
- CNAME (nome canônico): mapeia host para registros de host, por exemplo, ftp, mail, www podem referenciar servidores diferentes. CNAMEs não podem apontar diretamente para endereços IP, eles só podem apontar para outros nomes
- Registros MX: usados para o envio de e-mails. Podem ter 2 partes: prioridade e valor. Se incluirmos um ponto (.) no final do domínio para o qual o registro aponta, ele será considerado um FQDN (Fully Qualified Domain Name - Nome de Domínio Totalmente Qualificado)
- Registros TXT (texto): texto arbitrário associado ao domínio. Comumente usado para comprovar a propriedade do domínio

## TTL do DNS - Time To Live (Tempo de Vida)

- Indica por quanto tempo os registros podem ser armazenados em cache
- O servidor resolvedor armazenará os registros pelo período especificado pelo TTL em segundos
- O TTL é um equilíbrio: valores baixos significam mais consultas ao servidor, valores altos significam menos flexibilidade quando os registros são alterados

## Zonas Hospedadas Públicas (Public Hosted Zones)

- Uma zona hospedada é uma base de dados DNS para uma seção específica da base de dados DNS global
- As zonas hospedadas são criadas automaticamente quando um domínio é registrado no R53, mas também podem ser criadas separadamente (nesse caso, teremos que atualizar os valores dos servidores de nomes depois)
- Há uma taxa mensal para cada zona hospedada em execução
- Uma zona hospedada armazena registros DNS, como A, AAAA, MX, NS, TXT, etc.
- As zonas hospedadas são autoritativas para um domínio
- Quando uma zona hospedada pública é criada, o R53 aloca 4 servidores de nomes públicos para ela; o arquivo de zona é hospedado nesses servidores de nomes
- Usamos registros NS para apontar para esses servidores de nomes para podermos nos conectar ao DNS global
- Domínios registrados externamente podem apontar para uma zona pública do R53

## Zonas Hospedadas Privadas (Private Hosted Zones)

- Semelhante a uma zona hospedada pública, exceto pelo fato de que não pode ser acessada pela internet pública
- Elas são associadas a VPCs da AWS e só podem ser compartilhadas com VPCs da própria conta. O acesso entre contas (cross-account) é possível
- DNS de visão dividida (Split-view / Split Horizon DNS): é possível criar um DNS de visão dividida para uso público e interno com o mesmo nome de zona. Útil para acessar sistemas a partir da rede privada sem passar pela internet pública

## CNAME vs Registros Alias (Alias Records)

- O problema com o CNAME:
    - Um registro A mapeia um NOME para um Endereço IP
    - Um registro CNAME mapeia um NOME para outro NOME
    - Não podemos ter um registro CNAME para um nome de domínio APEX/naked (domínio raiz)
    - Muitos serviços da AWS usam Nome de DNS (exemplo: ELBs)
- Para fazer o domínio APEX apontar para outro domínio, podemos usar registros ALIAS (Aliases)
- Um registro alias mapeia um NOME para um recurso da AWS
- Pode ser usado tanto para registros apex quanto para registros normais
- Não há cobrança adicional para consultas de alias que apontam para recursos da AWS
- Um alias é um subtipo: podemos ter um alias de registro A e um alias de registro CNAME

## Roteamento Simples (Simple Routing)

- Com o roteamento simples, podemos criar um registro por nome
- Cada registro pode ter múltiplos valores
- No caso de uma requisição, todos os valores do registro são retornados ao cliente
- O cliente escolhe um dos valores e se conecta ao servidor
- Limitações: não suporta verificações de saúde (health checks)!

## Verificações de Saúde (Health Checks)

- As verificações de saúde são separadas dos registros no Route53, mas são utilizadas por eles
- Elas são criadas separadamente e podem ser usadas por registros no Route53
- As verificações de saúde são executadas por uma frota de verificadores (health checkers) distribuída globalmente
- As verificações de saúde não estão limitadas apenas a alvos da AWS; podem ser qualquer serviço com um endereço IP
- Os verificadores testam a saúde a cada 30 segundos (ou 10 segundos com custo adicional)
- As verificações de saúde podem ser TCP, HTTP, HTTPS, HTTP(S) com correspondência de string (String Matching). Uma conexão TCP deve ser concluída em 4 segundos e o endpoint deve responder com um código de status 2xx ou 3xx dentro de 2 segundos após a conexão. Após o recebimento do código de status, o corpo da resposta também deve ser recebido dentro de 2 segundos
- No caso de correspondência de string, o texto deve estar totalmente presente nos primeiros 5120 caracteres do corpo da resposta, caso contrário o endpoint falhará na verificação de saúde
- Com base nas verificações de saúde, o serviço pode ser categorizado como `Healthy` (Saudável) ou `Unhealthy` (Não saudável)
- As verificações de saúde podem ser de 3 tipos:
    - Endpoint: avalia a saúde de um endpoint que especificamos
    - CloudWatch Alarm Checks: reagem a alarmes do CloudWatch
    - Calculated Checks (Verificações Calculadas): verificações que monitoram outras verificações
- Se mais de 18% dos verificadores de saúde relatarem o alvo como saudável, ele será considerado saudável

## Roteamento de Failover (Failover Routing)

- Podemos adicionar 2 registros com o mesmo nome (um primário e um secundário)
- As verificações de saúde ocorrem no registro primário
- Se o registro primário falhar nas verificações de saúde, o endereço do registro secundário será retornado
- O roteamento de failover deve ser usado ao configurar um failover ativo-passivo (active-passive)

## Roteamento de Múltiplos Valores (Multi Value Routing)

- O Roteamento de Múltiplos Valores é uma mistura de roteamento simples e de failover
- Com o roteamento de múltiplos valores, podemos criar vários registros com o mesmo nome
- Cada registro pode ter uma verificação de saúde associada
- Quando consultado, até 8 registros são retornados ao cliente. Se houver mais de 8 registros presentes, 8 registros serão selecionados aleatoriamente e retornados
- O cliente escolhe um dos valores e se conecta ao serviço
- Qualquer registro que falhar nas verificações de saúde não será retornado na consulta
- O roteamento de múltiplos valores não substitui um balanceador de carga real

## Roteamento Ponderado (Weighted Routing)

- O Roteamento Ponderado pode ser usado ao buscar uma forma simples de balanceamento de carga ou quando queremos testar novas versões de uma API
- Com o roteamento ponderado, podemos especificar um peso (weight) para cada registro
- Para um determinado nome, o peso total é calculado. Cada registro é retornado dependendo da porcentagem do seu peso em relação ao peso total
- Definir um peso como 0 fará com que o registro não seja retornado. Se todos os registros forem configurados com peso 0, todos eles serão retornados
- O roteamento ponderado pode ser combinado com verificações de saúde. As verificações de saúde não removem os registros do cálculo do peso total. Se um registro foi selecionado, mas estiver não saudável (unhealthy), uma nova seleção será feita até que um registro saudável seja escolhido

## Roteamento Baseado em Latência (Latency-Based Routing)

- Deve ser usado quando se busca otimizar o desempenho e oferecer uma melhor experiência ao usuário
- Para cada registro, podemos especificar uma região
- A AWS mantém uma lista de latências para cada região do mundo (latência de origem-destino)
- Quando uma requisição chega, ela será direcionada para o destino de menor latência com base na localização de onde a requisição está vindo
- O roteamento baseado em latência pode ser combinado com verificações de saúde. Se o registro de menor latência falhar, o segundo registro de menor latência será retornado ao cliente
- A base de dados de latência mantida pela AWS não é atualizada em tempo real

## Roteamento de Geolocalização (Geolocation Routing)

- O roteamento de geolocalização é semelhante ao roteamento baseado em latência, porém, em vez da latência, a localização do cliente e dos recursos é utilizada para determinar as decisões de resolução
- Quando criamos registros, nós os marcamos com uma localização
- Essa localização geralmente é um país (código ISO2), continente ou padrão (default). Também pode haver uma subdivisão; nos EUA, podemos marcar os registros com um estado
- Quando o usuário faz uma consulta, uma verificação de IP identifica a localização do usuário
- A geolocalização não retorna necessariamente o registro fisicamente mais próximo, ela retorna registros relevantes: quando a resolução acontece, a localização do usuário é cruzada com a localização especificada para os registros, e a correspondente é retornada
- A ordem de verificação cruzada é a seguinte:
    1. O R53 verifica o estado (apenas nos EUA)
    2. O R53 verifica o país
    3. O R53 verifica o continente
    4. Retorna o padrão (default) se não houver correspondência anterior
- Se nenhuma correspondência for detectada, uma resposta `NO ANSWER` é retornada
- A geolocalização é ideal para restringir conteúdo com base na localização do usuário
- Também pode ser usada para balanceamento de carga baseado na localização do usuário

## Roteamento de Geoproximidade (Geoproximity Routing)

- A geoproximidade visa fornecer registros o mais próximo possível do cliente, calculando a distância entre o recurso e o cliente e retornando o registro com a menor distância
- Ao usar o roteamento de geoproximidade, definimos regras:
    - A região em que o recurso foi criado, caso seja um recurso da AWS
    - Coordenadas de latitude/longitude para recursos externos
    - Viés (Bias): ajusta como o R53 calcula a distância entre o usuário e o recurso
- A geoproximidade permite definir um viés: pode ser um viés positivo (`+`) ou negativo (`-`), aumentando ou diminuindo o tamanho da região. Podemos influenciar a distância de roteamento com base nesse viés

## Interoperabilidade do Route53

- O Route53 atua tanto como registrador de domínios (domain registrar) antiquanto como hospedagem de domínios (domain hosting)
- Também podemos registrar domínios usando outros serviços externos
- Etapas que ocorrem quando registramos um domínio usando o R53:
    - O R53 aceita a taxa de registro
    - Aloca 4 Servidores de Nomes (Name Servers)
    - Cria um arquivo de zona (hospedagem de domínio) nesses servidores de nomes
    - O R53 se comunica com o registrador do domínio de nível superior (TLD) e adiciona o endereço dos 4 servidores de nomes para o domínio em questão
- Route53 atuando apenas como registrador (registrar):
    - Pagamos pelo domínio para o Route53, mas os servidores de nomes são alocados por outra entidade
    - Temos que alocar os servidores de nomes no Route53, que se comunicará com o registro do domínio de nível superior
- Usando o Route53 apenas para hospedagem (hosting):
    - Geralmente usado para domínios existentes. O domínio é registrado em um terceiro
    - Criamos uma zona hospedada dentro do R53 e fornecemos o endereço dos servidores de nomes para o terceiro

## Implementando DNSSEC com o Route53

- O DNSSEC pode ser habilitado pelo console e pela CLI
- Uma vez iniciado, o processo começa no KMS; um par de chaves assimétricas é necessário/criado dentro do KMS
- As chaves de assinatura de chave (KSK - Key-signing keys) são criadas a partir dessa chave do KMS, tanto a parte pública quanto a privada, que serão usadas pelo R53
- Essas chaves precisam estar na região us-east-1
- Em seguida, o R53 cria internamente as chaves de assinatura de zona (ZSK - Zone-signing keys)
- Depois, o R53 adiciona as partes públicas da KSK e da chave de assinatura de zona em um registro de chave DNS dentro da zona hospedada; isso informa a todo resolvedor DNSSEC quais chaves públicas usar para verificar as assinaturas em quaisquer outros registros
- A chave de assinatura de chave privada é usada para assinar esses registros de chave DNS e criar os registros RRSIG e DNSKEY
- Neste ponto, a assinatura está configurada (etapa 1)
- Em seguida, o R53 precisa estabelecer a cadeia de confiança com a zona pai (parent zone)
- A zona pai precisa adicionar um registro DS (Delegated Signer), que é um hash da parte pública da KSK
- Se o domínio foi registrado com o R53, o console da AWS ou a CLI podem ser usados para fazer essa alteração. O R53 fará a ligação com o domínio de nível superior apropriado e adicionará o registro DS delegado
- Se o domínio foi criado externamente, teremos que adicionar esse registro manualmente
- Uma vez feito isso, o domínio de nível superior confiará neste domínio com o registro DS delegado
- A zona do domínio assinará cada registro com a KSK ou com a ZSK
- Ao habilitar o DNSSEC, devemos garantir a configuração de Alarmes do CloudWatch, especificamente criando alarmes para `DNSSECInternalFailure` e `DNSSECKeySigningKeyNeedingAction`, pois ambos necessitam de intervenção urgente

## DNS Avançado de VPC e Endpoints de DNS (Advanced VPC DNS and DNS Endpoints)

- Em cada VPC, o endereço IP final .2 é reservado para o DNS (VPC.2)
- Em cada sub-rede, o final .2 é reservado para o Route53 Resolver
- Por meio desse endereço, os recursos da VPC podem acessar as zonas hospedadas públicas e privadas associadas do R53
- O Route53 Resolver só é acessível a partir da VPC, tornando a integração de rede híbrida problemática tanto para entrada (inbound) quanto para saída (outbound)
![Ambientes de DNS Isolados](images/Route53Endpoints1.png)
- Solução para o problema antes da introdução dos endpoints do Route53:
![Antes dos Endpoints do Route53](images/Route53Endpoints2.png)
- Endpoints do Route53:
    - São entregues como interfaces de VPC (ENIs) que podem ser acessadas via VPN ou DX
    - 2 tipos diferentes de endpoints:
        - Entrada (Inbound): o ambiente local (on-premises) pode encaminhar requisições para o Route53 Resolver
        - Saída (Outbound): interfaces em múltiplas sub-redes usadas para fazer contato com o DNS local (on-premises)
        - Regras controlam quais requisições são encaminhadas
        - Endpoints de saída possuem endereços IP atribuídos que podem ser incluídos na lista de permissões (allowlist/whitelist) local
- Arquitetura de endpoints do Route53:
![Arquitetura de Endpoints do Route53](images/Route53Endpoints3.png)
- O Route53 Endpoints é entregue como um serviço
- Eles possuem alta disponibilidade (HA) e escalam automaticamente com base na carga
- Podem lidar com cerca de 10 mil consultas por segundo por endpoint

---

# Route53

## DNS Fundamentals

- DNS is a discovery service, translate information which machines need into information that humans need and vice-versa
- Example: www.amazon.com => 104.98.34.131
- DNS database is a huge distributed database
- DNS allows a DNS resolver server to find a Zone File ova Name Sever (NS) and query the it, retrieving the necessary IP address for a DNS name

## DNS Terminology

- **DNS Client**: refers to a customer PC, laptop, tablet, etc.
- **DNS Resolver**: software running on a device or a server which queries DNS on our behalf
- **DNS Zone**: a part of the DNS database (example: amazon.com)
- **Zone file**: it is a physical database for a zone, contains all the DNS information for a particular domain
- **DNS Name server**: a server which hosts the zone files

## DNS Root

- DNS is structures like a tree, DNS root is at the top of the tree
- DNS root is hosted in 13 special nameservers, known as DNS Root Servers
- Root hints file: an OS file containing the address of all root servers
- Authority: when something is trusted in DNS, example root hints file
- Delegation: trusted authorities can delegate a part of themselves to other entities, those entities becoming authoritative for the part delegated

## Route53 Introduction

- It is a managed DNS product
- Provides 2 main services:
    - Register domains
    - Can host zone files on managed nameservers
- It is a global service, its database is distributed globally and resilient

## Hosted Zones

- DNS as a service
- Let's us create and manage zone files
- Zone files are hosted on 4 AWS managed nameservers
- A hosted zone can be public, accessible for the public internet, part of the public DNS system, or it can be private, linked to one or more VPC(s)
- A hosted zone stores DNS records (recordsets)

## DNS Record Types

- Name server (NS): allow delegation to occur in DNS
- A and AAAA records: map host names to IP addresses. A records maps a host name to IPv4, AAAA maps the host to IPv6 addresses
- CNAME (canonical name): maps host to host records, example ftp, mail, www can reference different servers. CNAME can not point directly to IP addresses, they can point to other names only
- MX records: used for sending emails. Can have 2 parts: priority and value. If we include a dot (.) in the end of the domain to which the record points, that will co considered as a FQDN (Fully Qualified Domain Name)
- TXT (text) records: arbitrary text to domain. Commonly used to prove domain ownership

## DNS TTL - Time To Live

- Indicates how long records can be cached for
- Resolver server will store the records for the amount of time specified by the TTL in seconds
- TTL is a balance: low values means less queries to the server, high values mean less flexibility when the records are changed

## Public Hosted Zones

- A hosted zone is DNS database for a given section of the global DNS database
- Hosted zones are created automatically when a domain is registered in R53, they can be created separately as well (we will have to update the name severs values after that)
- There is a monthly fee for each running hosted zone
- A hosted zone hosts DNS records, example A, AAAA, MX, NS, TXT etc.
- Hosted zones are authoritative for a domain
- When a public hosted zone is created, R53 allocates 4 public name servers for it, on these name servers the zone file is hosted
- We use NS records to point at these name servers to be able to connect to the global DNS
- Externally registered domains can point to R53 public zone

## Private Hosted Zones

- Similar to a public hosted zone except it can not be accessed from the public internet
- They are associated with VPCs from AWS and it only can be shared with VPCs from the account. Cross account access is possible
- Split-view (Split Horizon) DNS: it is possible to create split-view (split-horizon) DNS for public and internal use with the same zone name. Useful for accessing systems from the private network without accessing the public internet

## CNAME vs Alias Records

- The problem with CNAME:
    - An A record maps a NAME to an IP Address
    - A CNAME records maps a NAME to another NAME
    - We can not have a CNAME record for an APEX/naked domain name
    - Many AWS services use DNS Name (example: ELBs)
- For the APEX domain to point to another domain, we can use ALIAS records
- An alias record maps a NAME to an AWS resource
- Can be used for both apex and normal records
- There is no additional charge for alias requests pointing at AWS resources
- An alias is a subtype, we can have an A record alias and a CNAME record alias

## Simple Routing

- With simple routing with can create one record per name
- Each record can have multiple values
- In case of a request, all the values for the record are returned to the client
- The client choses one of the values an connects to the server
- Limitations: does not support health checks!

## Health Checks

- Health checks are separate from, but used by records in Route53
- They are created separately and they can be used by records in Route53
- Health checks are performed by a fleet of health checkers distributed globally
- Health checks are not just limited to AWS targets, can be any service with an IP address
- Health checkers check every 30s (or 10s at extra cost)
- Health checks can be TCP, HTTP, HTTPS, HTTP(S) with String Matching. A TCP connections should be completed in 4s and endpoint should respond with a 2xx or 3xx status code within 2s after connections. After the status code is received, the response body should also be received within 2 seconds
- In case of string matching the text should be present entirely in the first 5120 characters of the request body or the endpoint fails the health check
- Based on the health checks the service can be categorized as `Healthy` or `Unhealthy`
- Health checks can be of 3 types:
    - Endpoint: assess the health of an endpoint we specify
    - CloudWatch Alarm Checks: they react to CloudWatch alarms
    - Calculated Checks: checks of other checks
- If 18%+ of the health checkers report the target as healthy, the target is considered healthy

## Failover Routing

- We can add 2 records of the same name (a primary and a secondary)
- Health checks happen on the primary record
- If the primary record fails the health checks, the address of the secondary record is returned
- Failover routing should be used when we configure active-passive failover

## Multi Value Routing

- Multi Value Routing is mixture to simple and failover routing
- With multi value routing we can create many records with the same name
- Each record can have an associated health check
- When queried, 8 records are returned to the client. If more than 8 records are present, 8 records will be randomly selected and returned
- The client picks one a of the values and connects to the service
- Any records which fails the health checks won't be returned when queried
- Multi value routing is not a substitute for an actual load balancer

## Weighted Routing

- Weighted Routing can be used when looking for a simple form of load balancing or when we want to test new versions of an API
- With weighted routing we can specify a weight for each record
- For a given name the total of weight is calculated. Each record is returned depending on the percentage of the record compared to the total weight
- Setting a weight to 0, the record will not be returned. If every record is set to 0, all of them will be returned
- Weighted routing can be combined with health checks. Health checks don't remove records from the calculation of the total weight. If a record is selected, but it is unhealthy, another selection will be made until a healthy record is selected

## Latency-Based Routing

- Should be used when we trying to optimize for performance and better user experience
- For each record we can specify an region
- AWS maintains a list of latencies for each region from the world (source - destination latency)
- When a request comes in, it will be directed to the lowest latency destination based on the location from where the request is coming from
- Latency-based routing can be combined with health checks. If the lowest latency record fails, the second lowest latency record will be returned to the client
- The latency database maintained by AWS is not updated in real time

## Geolocation Routing

- Geolocation routing is similar to latency-based routing, only instead of latency the location of customer and resources is used to determine the resolution decisions
- When we create records, we tag the records with a location
- This location is generally a country (ISO2 code), continent or default. There can be also a subdivision, in USA we can tag records with a state
- When the user does a query, an IP checks verifies the location is the user
- Geolocation does not return the closest record, it returns relevant records: when the resolution happens, the location of the user is cross-checked with the location specified for the records and the matching on is returned
- Order of the cross-checks is the following:
    1. R53 checks the state (US only)
    2. R53 checks the country
    3. R53 checks the continent
    4. Returns default if not previous match
- If no match is detected, the a `NO ANSWER` is returned
- Geolocation is ideal for restricting content based on the location of the user
- It can be used for load-balancing based on user location as well

## Geoproximity Routing

- Geoproximity aims to provide records as close to the customer as possible, aims to calculated the distance between to resource and customer and return the record with the lower one
- When using geoproximity, we define rules:
    - Region the resource is created in, if it is an AWS resource
    - Lat/lon coordinate for external resources
    - Bias: adjust how R53 calculates the distance between the user and the resource
- Geoproximiy allows defining a bias: it can be a `+` or `-` bias, increasing or decreasing the region size. We can influence the routing distance based on this bias

## Route53 Interoperability

- Route53 acts as a domain registrar and as a domain hosting
- We can also register domains using other external services
- Steps happening when we register a domain using R53:
    - R53 accepts the registration fee
    - Allocates 4 Name Servers
    - Creates a zone file (domain hosting) on the NS
    - R53 communicates with the registry of the top level domain and adds the address of the 4 NS for the given domain
- Route53 acting as a registrar only:
    - We pay for the domain for Route53 but the name servers are allocated by other entity
    - We have to allocate the name servers to Route53 which will communicate with the top level domain registry
- Using Route53 for hosting only:
    - Generally used for existing domains. The domain is registered at third party
    - We create a hosted zone inside R53 and provide the address of the name servers to the third party

## Implementing DNSSEC with Route53

- DNSSEC can be enabled form the console and from the CLI
- Once initiated, the process starts with KMS, an asymmetric key pair is required/created within KMS
- The key-signing keys (KSK) is created from this KMS key, both the public and private ones which will be used by R53
- These keys need to be in us-east-1
- Next, R53 creates the zone-signing keys (ZSK) internally
- Next, R53 adds the KSK and zone-signing key public parts into a DNS key record within the hosted zone, this tells every DNSSEC resolver which public keys to use to verify signatures on any other records
- The private key signing key used to sign those DNS key records and create the RRSIG and DNSKEY records
- At this point signing is configured (step 1)
- Next, R53 has to establish the chain of trust with the parent zone
- The parent zone needs ot add a DS record, which is hash of the public part of the KSK
- If the domain was registered with R53, the AWS console or the CLI can be used to make this change. R53 will liaise with the appropriate top-level domain and add the delegated sign record
- If the domain was created externally, we will have to add this record manually
- Once done, the top level domain will trust this domain with the delegated sign record (DS)
- The domain zone will sign each record either with the KSK or with the ZSK
- When enabling DNSSEC we should make sure we configure CloudWatch Alarms, specifically create alarms for `DNSSECInternalFailure` and `DNSSECKeySigningKeyNeedingAction`, both of these need urgent intervention

## Advanced VPC DNS and DNS Endpoints

- In every VPC the VPC.2 IP address is reserved for the DNS
- In every subnet the .2 is reserved for Route53 resolver
- Via this address VPC resources can access R53 Public and associated private hosted zones
- Route53 resolver is only accessible from the VPC, hybrid network integration is problematic both inbound and outbound
![Isolated DNS Environments](images/Route53Endpoints1.png)
- Solution to the problem before Route53 endpoints were introduced:
![Before Route53 Endpoints](images/Route53Endpoints2.png)
- Route53 endpoints:
    - Are deliver as VPC interfaces (ENIs) which can be accessed over VPN or DX
    - 2 different type of endpoints:
        - Inbound: on-premises can forward request to the R53 resolver
        - Outbound: interfaces in multiple subnets used to contact on-premises DNS
        - Rules control what requests are forwarded
        - Outbound endpoints have IP addresses assigned which can be whitelisted on-prem
- Route53 endpoint architecture:
![Route53 Endpoints Architecture](images/Route53Endpoints3.png)
- Route53 endpoints are delivered as a service
- They are HA and they scale automatically based on load
- They can handle around 10k queries per second per endpoint