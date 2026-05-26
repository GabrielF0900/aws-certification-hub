# VPC - Nuvem Privada Virtual

## Serviços Públicos vs Privados

- Serviço público: um serviço que é acessado usando endpoints públicos
- Serviço privado: um serviço que é executado dentro de uma VPC
- Qualquer um, privado ou público, cada serviço pode ter permissões para ser acessível
- VPC: rede privada isolada da internet. Não pode comunicar com a rede a menos que estejamos permitindo. Nada da internet pode alcançar os serviços de uma VPC enquanto não configurarmos de outra forma
- Internet Gateway: podemos conectá-lo a uma VPC, isso permitirá que os serviços na VPC se comuniquem com a internet pública

## DHCP em uma VPC

- DHCP - Protocolo de Configuração Dinâmica de Host: oferece auto configuração para recursos de rede
- Cada dispositivo tem um endereço MAC codificado (endereço Camada 2)
- DHCP começa com um broadcast L2 para descobrir um servidor DHCP na rede local
- Uma vez descoberto um servidor DHCP e um cliente DHCP se comunicam, significando que o cliente obterá no final um endereço IP, uma Máscara de Sub-rede e endereço de Gateway Padrão (configuração L3)
- DHCP também configura qual servidor DNS um recurso deve usar em uma VPC
- Também configura servidores NTP, Servidores de Nome NetBios e tipos de nó
- Ao definir qual serviço DNS usar em uma VPC, podemos fornecer explicitamente valores ou definir `AmazonProvidedDNS`
- Também recebemos 1 ou 2 nomes DNS alocados para os serviços na VPC. Um pode ser público se a instância tiver um endereço IP público alocado
- Nomes DNS personalizados: podemos dar nomes DNS personalizados a instâncias EC2 se usarmos nossos próprios servidores DNS personalizados. Para conseguir isso, podemos usar conjuntos de opções DHCP
- Conjuntos de opções DHCP:
    - Uma vez criados, os conjuntos de opções não podem ser alterados
    - Podem ser associados a 0 ou mais VPCs
    - Cada VPC pode ter no máximo 1 conjunto de opções associado (pode ter 0)
    - Se mudarmos um conjunto de opções DHCP associado à VPC, a mudança é imediata, mas qualquer nova configuração apenas afetará qualquer coisa uma vez que uma renovação de DHCP ocorra
    - O que podemos configurar em um conjunto de opções:
        - Servidor DNS (resolvedor Route 53) que podemos usar na VPC
        - Servidor NTP

## Roteador VPC - Aprofundamento

- Está no núcleo de qualquer rede que envolva AWS
- É um roteador virtual em uma VPC
- É HA em todos os AZs em uma região, nenhuma sobrecarga de gerenciamento é necessária
- É escalável, nenhuma sobrecarga de gerenciamento necessária
- O roteador VPC roteia o tráfego entre sub-redes em uma VPC
- Roteia o tráfego da rede externa para dentro e vice-versa
- O roteador VPC tem uma interface em cada sub-rede em uma VPC: endereço `subnet+1` (Gateway Padrão), o primeiro endereço IP em cada sub-rede após o endereço de rede em si
- Controlamos como a VPC roteia o tráfego usando Tabelas de Rota

## Tabelas de Rota VPC

- Cada VPC é criada com uma Tabela de Rota principal (RT), que é a padrão para cada VPC
- Tabelas de rota personalizadas podem ser criadas para cada sub-rede
- Sub-redes podem ser associadas apenas a uma RT que pode ser a principal ou personalizadas
- Se desassociarmos uma RT personalizada de uma sub-rede, a RT principal será anexada a ela
- A RT principal não deve ser alterada, a RT personalizada deve ser usada para quaisquer mudanças de roteamento
- RTs têm rotas, rotas têm uma ordem, a rota mais específica vence
- Associação de Borda: uma tabela de RT é associada a um gateway de rede
- Todas as RTs têm pelo menos uma rota: a rota local que corresponde ao intervalo CIDR da VPC. Essas rotas são não editáveis

## NACL - Listas de Controle de Acesso à Rede

- Uma NACL pode ser considerada como um firewall tradicional em uma VPC AWS
- NACLs estão associadas com sub-redes, cada sub-rede tem uma NACL associada a ela
- A conexão dentro de uma sub-rede não é afetada por NACLs
- NACLs podem ser consideradas firewalls sem estado, portanto podemos falar sobre os seguintes tipos de regras:
    - Regras de entrada: afetam dados que chegam à sub-rede
    - Regras de saída: afetam dados que saem da sub-rede
- As regras podem **PERMITIR** e explicitamente **NEGAR** tráfego
- As regras são processadas em ordem:
    1. Uma NACL determina se as regras de entrada ou saída se aplicam
    2. Começa no número de regra mais baixo, avalia o tráfego em relação a cada regra até haver uma correspondência (baseada no intervalo de IP, porta, protocolo)
    3. O tráfego é permitido/negado com base na regra
- A última regra é uma negação implícita em cada NACL, se nenhuma regra anterior se aplicar, o tráfego será negado
- NACL padrão: quando uma VPC é criada, uma NACL padrão é anexada a ela. A NACL padrão está permitindo todo o tráfego
- NACLs personalizadas: 
    - Podemos criá-las e anexá-las a sub-redes
    - Cada NACL tem uma regra padrão que nega todo o tráfego. Isto tem a prioridade mais baixa
- NACLs podem ser associadas a muitas sub-redes diferentes, no entanto cada sub-rede pode ter apenas uma NACL associada a ela em qualquer momento
- NACLs não estão cientes de nenhum recurso lógico em uma VPC, eles estão cientes de IPs, CIDRs e protocolos

## SG - Grupos de Segurança

- Grupos de Segurança são firewalls com estado, significando que eles detectam tráfego de resposta para uma solicitação e automaticamente permitem esse tráfego
- SGs não têm regras explícitas **NEGAR**, eles podem ser usados para bloquear atores maliciosos (use NACLs para isso)
- SGs suportam regras IP/CIDR e também permitem referenciar recursos lógicos
- SGs estão anexados a Elastic Network Interfaces (ENI), quando anexamos um SG a um EC2, o SG será anexado ao ENI primário
- SGs são capazes de referenciar recursos lógicos, ex. outros grupos de segurança ou auto-referência

## Zonas Locais AWS

- Região Pai: região AWS regular
- Zonas Locais estão anexadas a regiões pais e operam na mesma região geográfica
- Nomeação de Zona Local: `us-east-las-1` - < região pai > - < identificador de Zona Local (código de cidade internacional) >. Exemplos: `us-west-2-lax-1a`, `us-west-2-lax-1b`
- Podemos ter várias Zonas Locais na mesma cidade
- Zonas Locais operam como pontos independentes e independentes, elas têm sua própria conexão independente com a internet
- Geralmente, elas suportam Direct Connect
- Uma VPC em uma região pai pode ser estendida com sub-redes de uma Zona Local. Nessas sub-redes criamos nossos recursos como normalmente
- Esses recursos se beneficiarão de latências super baixas (no caso querermos acessá-los de uma premissa comercial próxima)
- Algumas coisas em uma Zona Local ainda utilizarão a região pai: por exemplo Zonas Locais terão redes privadas com a região pai, no entanto se criarmos backups para um EBS na Zona Local, isso utilizará o S3 da região pai
- Zonas Locais podem ser consideradas como um AZ adicional (mas perto de nossa localização => latência mais baixa), elas não têm AZ integrado
- Nem todos os produtos AWS suportam Zonas Locais. Dentre os que suportam, muitos deles são opt-in e também muitos deles têm limitações
- Zonas Locais devem ser usadas quando precisamos do desempenho máximo

## Roteamento Avançado de VPC

- **Sub-redes estão associadas com 1 tabela de rota (RT) apenas, nada mais nada menos!**
- Esta tabela de rota é ou a tabela de rota principal da VPC ou uma tabela de rota personalizada
- No caso de uma associação de tabela de rota personalizada com uma sub-rede, a tabela de rota principal é desassociada. No caso da RT personalizada ser removida, a RT principal é associada novamente com a sub-rede
- RT pode ser associada a um internet gateway (IGW) ou gateway privado virtual (VGW)
- IPv4/6 são tratados separadamente dentro de uma RT
- As rotas enviam tráfego com base em um destino para um alvo
- As tabelas de rota têm um máximo de 50 rotas estáticas e 100 rotas dinâmicas
- Quando um tráfego chega a uma interface (IGW, VGW), ele é correspondido à tabela de rota relevante
- Todas as rotas de uma tabela de rota são avaliadas - correspondência de maior prioridade é usada
- As tabelas de rota podem conter 2 tipos de rotas:
    - Rotas estáticas: adicionadas manualmente por nós
    - Rotas propagadas: adicionadas quando habilitadas por nós na VPC ou em qualquer RT individual
- Regra de avaliação para as rotas: 
    1. Prefixo mais longo vence, exemplo /32 vence sobre /24, /16 ou /0. Rotas mais específicas sempre vencam!
    2. Rotas estáticas têm prioridade sobre rotas propagadas
    3. Para quaisquer rotas aprendidas por propagação:
        1. DX
        2. VPN Estática
        3. VPN BGP
        4. AS_PATH (termo BGP usado para representar o caminho entre dois ASNs; é a distância dentro de dois sistemas autônomos diferentes): rotas com um AS_PATH mais curto venceriam sobre os AS_PATH mais longos

## Roteamento de Ingresso

- Todo o tráfego de saída é roteado para um eletrodoméstico de segurança
- O eletrodoméstico de segurança está sentado na sub-rede pública que tem uma RT atribuída a ela. Esta RT envia todo o tráfego não correspondido para o IGW e qualquer coisa para a rede corporativa através do VGW
- Roteamento de ingresso permite atribuir tabelas de rota a gateways (Tabelas de rota de Gateway). **Tabelas de rota de Gateway** podem ser anexadas a internet gateways ou gateways virtuais e podem ser usadas para tomar ação em tráfego de entrada (rotear para uma instância de segurança para avaliação)
![Roteamento de Ingresso](images/AdvancedRouting5.png)

## Capacidade IPv6 em VPCs

- Endereços IPv6 são todos publicamente roteáveis
- NAT não é usado para IPv6, IPv6 não precisa de tradução de endereço de rede simplesmente por causa do número enorme de endereços IPv6 disponíveis
- IPv6 precisa ser habilitado manualmente em uma VPC. Podemos trazer nosso próprio endereço IP em uma VPC ou utilizar um intervalo fornecido pela AWS
- No caso de endereços IPv6 fornecidos pela AWS, a AWS alocará um intervalo /56 uniq à VPC. Este intervalo será completamente uniq e todos os endereços serão publicamente roteáveis
- Se escolhermos alocar um intervalo de IP para uma VPC, a AWS usará um par hex para alocar unicamente endereços IP às sub-redes
- O roteamento é tratado separadamente para os endereços IPv6, teremos rotas IPv4 e rotas IPv6
- Gateway de internet exclusivo de saída: semelhante ao gateway NAT, permite tráfego de saída negando tráfego de entrada no caso de endereçamento IPv6. Gateways NAT ou instâncias não suportam IPv6!
- Apenas um internet gateway pode ser associado a uma VPC, mas podemos ter internet gateway e gateway de internet exclusivo de saída associados à mesma VPC. São 2 coisas diferentes
![Arquitetura IPv6](images/IPv6EOIGW.png)
- IPv6 pode ser configurado ao criar uma VPC/sub-rede ou podemos migrar uma VPC existente para IPv6
- Podemos habilitar IPv6 em sub-redes específicas apenas
- Podemos apontar tráfego IPv6 para internet gateway e gateways de internet exclusivos de saída também
- Nem todos os serviços na AWS suportam IPv6!

## Estrutura VPC Avançada - Quantos AZs para HA?

- O número de AZ necessário para HA:
    - AZs de Buffer: número de falhas de AZ toleradas (geralmente 1 para questões do exame)
    - AZs Nominais: o número de AZs que podemos usar para operações normais: o número de AZs disponíveis em uma região - AZs de Buffer (exemplo: 6 AZs disponíveis, falha tolerada é 1 AZ => 6 - 1 = 5)
- Às vezes este cálculo pode influenciar qual região podemos usar, uma vez que o número de AZs pode diferir por região
- Instâncias nominais: o número instâncias necessárias para a aplicação para a carga de negócios
- Mais eficiente HA com custos ideais: Instâncias Nominais / AZs Nominais => número ideal de instâncias por AZ

## Estrutura VPC Avançada - Sub-redes e Camadas

- Sub-redes públicas podem ser configuradas para não dar endereços IP públicos a todas as instâncias por padrão. Podemos alocar explicitamente endereços IP públicos para alguns recursos
- Se nenhum IP público for endereçado a um recurso em uma sub-rede pública, ele não será acessível de fora
- Grupos de segurança: podemos restringir o tráfego de entrada permitindo tráfego apenas de instâncias selecionadas
- Quantas sub-redes um aplicativo precisa:
    - Não precisamos de sub-redes públicas e privadas para endereçamento e segurança. Isso pode ser configurado em uma sub-rede. Exceção a isto: filtrar tráfego usando uma NACL
    - Precisamos de sub-redes diferentes para roteamento diferente
    - Balanceadores de carga voltados para a internet podem se comunicar com instâncias privadas. Balanceador de carga voltado para a internet precisa ser executado em uma sub-rede pública
    - Número de sub-redes necessárias: número de sub-redes necessárias para o APP * AZs
    - Gateway NAT: não podemos ter o Gateway NAT na mesma sub-rede em que também gostaríamos que os recursos o usassem. Razão: não podemos ter 2 rotas padrão na Tabela de Rota

---

# VPC - Virtual Private Cloud

## Public vs Private Services

- Public service: a service which is accessed by using public endpoints
- Private service: a service which runs inside a VPC
- Either private or public, every service can have permissions in order to be accessible
- VPC: private network isolated from the internet. Can't communicate to the network unless we are allowing it. Nothing from the internet can reach the services from a VPC as long as we do not configure it otherwise
- Internet Gateway: we can connect it to a VPC, this will allow the services in the VPC to communicate with the public internet

## DHCP in a VPC

- DHCP - Dynamic Host Configuration Protocol: offers auto configuration for network resources
- Every device has a hard-coded MAC address (Layer 2 address)
- DHCP begins with a L2 broadcast to discover a DHCP server on the local network
- Once discovered a DHCP server and a DHCP clients communicate, meaning that the client will get in the end an IP address, a Subnet Mask and Default Gateway address (L3 configuration)
- DHCP also configures which DNS server should a resource use in a VPC
- Also configures NTP servers, NetBios Name Servers and Node types
- When we are setting which DNS service to use in a VPC we can either explicitly provide values or we can set `AmazonProvidedDNS`
- We also get allocated 1 or 2 DNS names for the services in the VPC. One can be public if the instance has a public IP address allocated
- Custom DNS names: we can give custom DNS names to EC2 instances if we use our own custom DNS servers. To accomplish these we can use DHCP option sets
- DHCP options sets:
    - Once created option sets can not be changed
    - Can be associated with 0 or more VPCs
    - Each VPC can have a max of 1 option set associated (it can have 0)
    - We we change a DHCP option set associated to the VPC, the change is immediate, but any new setting will only affect anything once a DHCP renew occurs
    - What we can configure in an option set:
        - DNS server (Route 53 resolver) what we can use in the VPC
        - NTP server

## VPC Router Deep Dive

- Is at the core of any network which involves AWS
- Is a virtual router in a VPC
- It is HA across al AZs in a region, no management overhead is required
- It is scalable, no management overhead required
- VPC routes routes traffic between subnets in a VPC
- Routes traffic from external network into the and vice-versa
- VPC router has an interface in every subnet in a VPC: `subnet+1` address (Default Gateway), the first IP address in each subnet after the network address itself
- We control how the VPC routes traffic using Route Tables

## VPC Route Tables

- Every VPC is created with a main Route Table (RT), which is the default for every VPC
- Custom route tables can be created for each subnet
- Subnets can be associated with only one RT which can be the main one or custom
- If we disassociate a custom RT form a subnet, the main RT will be attached to it
- Main RT should not be changed, custom RT should be used for any routing changes
- RT have routes, routes have an order, the most specific route wins
- Edge Association: a RT tables is associated with network gateway
- All RTs have at least one route: the local route which matches the VPC cidr range. These routes are un-editable

## NACL - Network Access Control Lists

- A NACL can be considered to be a traditional firewall in an AWS VPC
- NACLs are associated with subnets, every subnet has a NACL associated to it
- Connection inside a subnet are not affected by NACLs
- NACls can be considered stateless firewalls, so we can talk about the following type of rules:
    - Inbound rules: affect data coming into the subnet
    - Outbound rules: affects data leaving from the subnet
- Rules can explicitly **ALLOW** and explicitly **DENY** traffic
- Rules are processed in order:
    1. A NACL determines if a the inbound or outbound rules apply
    2. It starts from the lower rule number, evaluates traffic against each rule until is a match (based on IP range, port, protocol)
    3. Traffic is allowed/denied based on the rule
- Last rule is an implicit deny in every NACL, if no rule before that applies, traffic will be denied
- Default NACL: when a VPC is created, a default NACL is attached to it. The default NACL is allowing all traffic
- Custom NACLs: 
    - We can create them and attach them to subnets
    - Each NACL has a default rule that denies all traffic. This has the lowest priority
- NACLs can be associated to many different subnet, however each subnet can have only one NACL associated to it at any time
- NACL are not aware af any logical resources within a VPC, they are aware of IPs, CIDRs and protocols

## SG - Security Groups

- Security Groups are stateful firewalls, meaning they detect response traffic to a request and they automatically allow that traffic
- SGs do not have explicit **DENY** rules, they can be used to block bad actors (use NACLs for this)
- SGs support IP/CIDR rules and also allow to reference logical resources
- SGs are attached to Elastic Network Interfaces (ENI), when we attach a SG to an EC2, the SG will be attached to the primary ENI
- SGs are capable to reference logical resources, ex. other security groups or self referencing

## AWS Local Zones

- Parent Region: regular AWS region
- Local Zones are attached to parent regions and they operate in the same geographical region
- Local Zone naming: `us-east-las-1` - < parent region > - < Local Zone identifier (international city code) >. Examples: `us-west-2-lax-1a`, `us-west-2-lax-1b`
- We can have multiple Local Zones in the same city
- Local Zones operate as their own independent points, they have their own independent connection to the internet
- Generally, they support Direct Connect
- A VPC in a parent region can be extended with subnets from a Local Zone. In these subnets we create our resources as normal
- These resources will benefit from super low latencies (in case we want to access them from a business premises nearby)
- Some things within a Local Zone will still utilize the parent region: for example Local Zones will have private networking with the parent region, however if we create backups for an EBS in the Local Zone, this will utilize the S3 from the parent region
- Local Zones can be considered as one additional AZ (but near our location => lower latency), they don't have builtin AZ
- Not all AWS products support Local Zones. From the ones which do support, many of them are opt-in an also many of them have limitations
- Local Zones should be used when we need the highest performance

## Advanced VPC Routing

- **Subnets are associated with 1 route table (RT) only, no more noe less!**
- This route table is either the main route table from the VPC or a custom route table
- In case of a custom route table association with a subnet, the main route table is disassociated. In case the custom RT is removed, the main RT is associated again with the subnet
- RT can associated with an internet gateway (IGW) or virtual private gateway (VGW)
- IPv4/6 are handled separately within a RT
- Routes send traffic based on a destination to a target
- Route tables have a maximum of 50 static routes and 100 dynamic routes
- When a traffic arrives to an interface (IGW, VGW), it is matched to the relevant route table
- All routes from a route table are evaluated - highest-priority matching is used
- Route tables can contain 2 types of routes:
    - Static routes: added manually by us
    - Propagated routes: added when enabled by us on the VPC or on any individual RT
- Evaluation rule for the routes: 
    1. Longest prefix wins, example /32 wins over /24, /16 or /0. More specific routes always win!
    2. Static routes take priority over propagated routes
    3. For any routes learned by propagation:
        1. DX
        2. VPN Static
        3. VPN BGP
        4. AS_PATH (BPG term used to represent the path between two ASNs; it is the distance within two different autonomous systems): routes with a shorter AS_PATH would win over the longer AS_PATH ones

## Ingress Routing

- All outgoing traffic is routed to a security appliances
- The security appliance is sitting in the public subnet which has a RT assigned to it. This RT sends all unmatched traffic out through the IGW and anything for the corporate network through the VGW
- Ingress routing allows to assign route tables to gateways (Gateway route tables). **Gateway route tables** can be attached to internet gateways or virtual gateways and can be used to take action on inbound traffic (route to a security instance for assessment)
![Ingress Routing](images/AdvancedRouting5.png)

## IPv6 Capability in VPCs

- IPv6 addresses are all publicly routable
- NAT is not used for IPv6, IPv6 does not need network address translation simply because of the huge number of available IPv6 addresses
- IPv6 needs to be manually enabled on a VPC. We can either bring our own IP address in a VPC or utilize an AWS provided range
- In case of AWS provided IPv6 addresses, AWS will allocate an uniq /56 range to the VPC. This range will be entirely uniq and all addresses will be publicly routable
- If we chose to allocate an IP range for a VPC, AWS will use a hex pair to uniquely allocate IP addresses to the subnets
- Routing is handled separately for the IPv6 addresses, we will have IPv4 routes and IPv6 routes
- Egress only internet gateway: similar to NAT gateway, allows outbound traffic denying inbound traffic in case of IPv6 addressing. NAT gateways or instances do not support IPv6!
- Only one internet gateway can be associated with a VPC, but we can have both internet gateway and egress only internet gateway associated to the same VPC. They are 2 different things
![IPv6 Architecture](images/IPv6EOIGW.png)
- IPv6 can be set up while creating a VPC/subnet or we can migrate an existing VPC to IPv6
- We can enable IPv6 on specific subnets only
- We can point IPv6 traffic to internet gateway and egress only internet gateways as well
- Not every service in AWS supports IPv6!
