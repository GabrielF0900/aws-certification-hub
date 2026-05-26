# DX - Direct Connect

- É um ponto de entrada físico para a rede da AWS
- É uma conexão de fibra física através da qual podemos acessar os serviços da AWS sem enviar tráfego pela internet pública
- A conexão é entre as instalações da empresa => Localidade DX (DX Location) => Região AWS
- Quando solicitamos uma conexão DX, o que estamos pedindo é, na verdade, uma Alocação de Porta em uma Localidade DX
- A porta possui 2 custos:
    - Custo por hora com base na localidade DX e na velocidade da porta
    - Transferência de dados de saída (outbound); a transferência de dados de entrada (inbound) é gratuita
- Para obter um Direct Connect, precisamos criar uma conexão (entidade lógica) dentro de uma conta AWS. Essa conexão terá um ID exclusivo
- Tempo de provisionamento: semanas ou meses de tempo adicional
- O DX fornece latência baixa e consistente + altas velocidades (1/10/100 Gbps)
- Na localidade DX, teremos que instalar um cross-connect (cabo físico) para conectar nossa própria rede à rede da AWS
![Arquitetura DX](images/DirectConnectArchitecture1.png)

## Arquitetura de Conexão Física do DX

- Um Direct Connect é uma porta física alocada em uma Localidade DX
- Essa porta física fornece velocidades de 1, 10 ou 100 Gbps
- O DX pode ser solicitado diretamente da AWS ou por meio de parceiros (maior variedade de velocidades, com menos opções)
- A porta requer fibra monomodo (single-mode); NÃO há suporte para conexão por cabo de cobre
- Dependendo da velocidade solicitada, faremos a interface com o DX usando os seguintes padrões:
    - **1000BASE-LX** (1310 nm) Transceptor para 1 Gbps
    - **10GBASE-LR** (1310 nm) Transceptor para 10 Gbps
    - **100GBASE-LR4** - 100 Gbps
- A Auto-Negociação deve ser desativada para a conexão
- Configuramos a velocidade da porta; o modo full-duplex deve ser definido manualmente na conexão de rede
- O roteador na localidade DX deve suportar o Border Gateway Protocol (BGP) e a Autenticação MD5 do BGP
- Configurações opcionais:
    - MACsec
    - Detecção de Encaminhamento Bidirecional (BFD - Bidirectional Forwarding Detection)

## Direct Connect - MACsec

- É um recurso de segurança que resolve/mitiga parcialmente um problema antigo do DX: a falta de criptografia nativa
- É um padrão que permite a criptografia de quadros (frames) na rede. Os quadros são a unidade de dados que ocorre na camada 2 do modelo OSI
- O MACsec fornece uma arquitetura de criptografia salto a salto (hop-by-hop) => 2 dispositivos precisam estar lado a lado na camada 2 para utilizar o MACsec (adjacência de camada 2)
- Recursos do MACsec:
    - Confidencialidade: criptografia forte na camada 2, criptografando o EtherType e a carga útil (payload) do quadro
    - Integridade dos dados: adiciona campos adicionais para garantir que os dados não possam ser modificados em trânsito sem que ambas as partes consigam detectar a modificação
    - Autenticidade da origem dos dados: ambas as partes podem verificar que os quadros foram enviados pelo outro par confiável
    - Proteção contra replay (ataque de reprodução)
- O MACsec não substitui o IPsec sobre o DX, pois não é de ponta a ponta (end-to-end)!
- Foi projetado para permitir a transferência em altíssimas velocidades para redes de escala terabit
- Componentes principais do MACsec:
    - **Canal Seguro** (Secure Channel - unidirecional): cada participante do MACsec cria um canal MACsec usado para enviar tráfego
    - Os **Canais Seguros** recebem um identificador (SCI): identifica exclusivamente um canal seguro
    - **Associações Seguras** (Secure Associations): a comunicação que ocorre em cada canal seguro acontece como uma série de sessões temporárias; múltiplas associações seguras ocorrerão em cada canal seguro ao longo da vida útil da conexão. Cada canal seguro geralmente possui uma associação segura por vez (exceto quando as associações estão sendo substituídas)
    - **Encapsulamento MACsec**: tag MACsec de 16 bytes e Valor de Verificação de Integridade (ICV - Integrity Check Value) de 16 bytes. O MACsec modifica os quadros Ethernet inserindo essas tags
    - Protocolo **MACsec Key Agreement** (MKA): gerencia a descoberta, autenticação e geração de chaves
    - **Cipher Suite**: controla como os dados são criptografados: algoritmo, pacotes por chave, rotação de chaves
- O MACsec pode ser definido tanto em uma conexão DX quanto em um Grupo de Agregação de Links (LAG - Link Aggregation Group)
- Configurando o MACsec: associamos um par CAK/CKN à conexão, tanto no(s) roteador(es) AWS DX quanto no roteador do lado do cliente
- É possível estender o MACsec da localidade DX até o lado do cliente
- Isso requer uma extensão física dedicada do cross-connect até as instalações da empresa; esse tipo de extensão exige Adjacência de Camada 2

## Processo de Conexão DX

- Uma conexão DX começa em uma Localidade DX, que contém equipamentos da AWS e também equipamentos do cliente/provedor
- A AWS não é dona dessa instalação (nem o provedor) - trata-se de um data center que pertence a terceiros
- Um grande data center é uma coleção de gaiolas (cages), que são áreas alugadas por clientes específicos
- Apenas a equipe do data center pode conectar as coisas; somente eles têm acesso ao espaço entre as gaiolas para interconectá-las
- A conexão dessas gaiolas só pode ser feita pelos membros da equipe do data center quando possuírem autorização de todas as partes
- Essa autorização é chamada de **Carta de Autorização - Acesso às Instalações do Cliente (LOA-CFA - Letter of Authorization Customer Facility Access)**
- É um formulário que concede acesso para que um cliente solicite à equipe do data center a conexão com o equipamento de outro cliente
- Processo de conexão DX:
![Processo de Conexão DX](images/DXConnectionProcess.png)

## Interfaces Virtuais (VIFs) DX, Sessões BGP + VLAN

- As conexões DX são conexões de camada 1 (cabos físicos) executando protocolos de camada 2 (Link de Dados)
- Precisamos de uma maneira de nos conectar a vários tipos de redes de camada 3 (IP) — como VPCs e zonas públicas — através de uma única conexão DX => é aqui que as Interfaces Virtuais (VIFs) se tornam úteis
- As VIFs nos permitem rodar múltiplas redes de camada 3 sobre um Direct Connect de camada 2
- Uma VIF é simplesmente uma Sessão de Emparelhamento BGP (BGP Peering Session) => algo que troca prefixos que permitem que o tráfego seja roteado de um ponto ao outro
- Tudo isso é isolado dentro de uma VLAN
- Uma VLAN isola diferentes redes de camada 3 usando marcação de VLAN (VLAN tagging)
- O BGP troca prefixos, o que significa que cada extremidade sabe quais redes estão de cada lado; a autenticação MD5 do BGP garante que apenas dados autenticados sejam aceitos por ambos os lados
- Podem ser executados 3 tipos de VIFs sobre o DX:
    - VIF Privada (Private VIF): usada para se conectar a redes privadas da AWS, ou seja, VPCs
    - VIF Pública (Public VIF): usada para se conectar a serviços da Zona Pública
    - VIF de Trânsito (Transit VIF): permite a integração entre o DX e o Transit Gateways
![VIFs DX - Sessão BGP + VLAN](images/DXBGPSessonVLAN.png)
- Um único DX dedicado pode ter no total 50 VIFs públicas/privadas, bem como 1 VIF de Trânsito
- VIFs Hospedadas (Hosted VIFs): podemos compartilhar VIFs com outras contas AWS. Podem ser conectadas a um gateway virtual privado (VGW) em uma VPC de outra conta

## VIFs Privadas (Private VIFs)

- São usadas para acessar os recursos dentro de uma VPC da AWS usando endereços IP privados
- Os recursos podem ser acessados com seu IP privado usando VIFs privadas; IPs públicos e Elastic IPs não funcionarão
- As VIFs privadas são associadas a um Virtual Private Gateway (VGW), que pode ser associado a 1 VPC. Isso deve estar na mesma região onde a conexão da localidade DX termina
- 1 VIF Privada = 1 VGW = 1 VPC (existem maneiras de contornar isso usando VIFs de Trânsito)
- Não há criptografia nas VIFs privadas; o DX não adiciona criptografia e as VIFs privadas também não (há alternativas para isso, como o uso de HTTPS)
- Com VIFs privadas, podemos usar quadros normais ou Jumbo Frames (MTU de 1500 ou 9001)
- Usando um VGW, a propagação de rotas fica ativada por padrão
- Criando VIFs privadas:
    - Escolha a conexão sobre a qual a VIF será executada
    - Escolha VGW (padrão) ou Direct Connect Gateway
    - Escolha quem é o proprietário da interface (esta conta ou outra conta)
    - Escolha um ID de VLAN - 802.1Q, que precisa corresponder à configuração do cliente
    - Precisamos inserir o ASN do BGP local (on-premises), seja público ou privado. Se for privado, use de 64512 a 65535
    - Podemos escolher os IPs ou gerá-los automaticamente
    - A AWS anunciará o intervalo CIDR da VPC e os IPs do BGP Peer (`/30`)
    - Podemos anunciar prefixos corporativos padrão ou específicos (**máximo de 100** - este é um limite RÍGIDO, caso contrário a interface entrará em estado ocioso/idle)
- Arquitetura de VIFs privadas:
    ![Arquitetura de VIFs Privadas](images/DXPrivateVIFS.png)
- Principais objetivos de aprendizado:
    - VIFs privadas são usadas para acessar serviços privados da AWS
    - VIF Privada => 1 VGW => 1 VPC
    - A VPC precisa estar na mesma região que a localidade DX
    - O VGW tem um ASN atribuído pela AWS
    - Sobre a VIF privada roda o BGP com IPv4 ou IPv6 (conexões de emparelhamento BGP separadas)
    - Configuramos nosso próprio AS na VIF, que pode ser um ASN privado ou público

## VIFs Públicas (Public VIFs)

- São usadas para acessar serviços da zona pública da AWS: tanto serviços públicos quanto serviços que possuem um IP Elastic público
- Elas não oferecem acesso direto a serviços privados de VPC
- Podemos acessar todas as regiões da zona pública com uma única VIF pública através da rede global da AWS
- A AWS anuncia todos os intervalos de IP públicos da AWS para nós; todo o tráfego para os serviços da AWS passará pela rede global da AWS
- Podemos anunciar quaisquer IPs públicos de nossa propriedade via BGP; caso não tenhamos IPs públicos, podemos trabalhar com o suporte da AWS para que nos aloquem alguns
- VIFs públicas oferecem suporte a comunidades BGP bidirecionais
- Os prefixos anunciados não são transitivos, ou seja, nossos prefixos não saem da AWS
- Criar uma VIF pública:
    - Selecionamos a conexão sobre a qual a VIF será executada
    - Escolhemos o proprietário da interface (esta conta ou outra)
    - Escolhemos a VLAN - 802.1Q, que precisa corresponder à configuração do cliente
    - Escolhemos o ASN do BGP do lado do cliente (o ideal é que seja um ASN público para aproveitar a funcionalidade total oferecida pelas VIFs públicas)
    - Configuramos a autenticação MD5 e selecionamos os endereços IP de emparelhamento opcionais
    - Temos que selecionar quais prefixos queremos anunciar
- Arquitetura de VIFs públicas:
![Arquitetura de VIFs Públicas](images/DXPublicVIFS.png)

## Direct Connect VIF Pública + VPN

- O uso de uma VPN nos fornece um túnel criptografado e autenticado
- Arquiteturalmente, ter uma VPN sobre o DX usa uma VIF Pública + endpoints públicos de um VGW ou TGW
- Com uma VPN, nos conectamos a IPs públicos que pertencem a um VGW ou TGW
- Uma VPN é agnóstica em relação ao trânsito: podemos nos conectar via VPN a um VGW ou a um TGW pela internet ou pelo DX
- A VPN fornece criptografia de ponta a ponta entre um Customer Gateway (CGW) e o TGW/VGW, enquanto o MACsec funciona salto a salto (single-hop)
- As VPNs têm amplo suporte de fornecedores
- As VPNs possuem mais sobrecarga (overhead) criptográfica em comparação ao MACsec
- Uma VPN pode ser provisionada imediatamente, podendo ser usada enquanto o DX está sendo implantado e/ou como um backup do DX
![VPN sobre DX](images/DXPublicVIFVPN.png)

## Direct Connect Gateways (DXGW)

- O Direct Connect é um serviço regional
- Assim que a conexão DX é estabelecida, podemos usar VIFs públicas para acessar todos os serviços públicos da AWS em todas as regiões
- As VIFs privadas só podem acessar VPCs na mesma região da AWS através de VGWs
- O Direct Connect Gateway é um dispositivo de rede global: ele é acessível em todas as regiões
- Nós nos integramos a ele no lado local criando uma VIF privada e associando-a a um DX Gateway em vez do Virtual Private Gateway (VGW). Isso integra o roteador local com o DX Gateway
- No lado da AWS, criamos associações de VGW em qualquer VPC de qualquer região da AWS
- Os DX Gateways permitem rotear através deles para os ambientes locais e vice-versa. Eles NÃO permitem que as VPCs conectadas ao gateway se comuniquem entre si
- Podemos ter até 10 conexões de VGW por DX Gateway
- 1 conexão DX pode ter até 50 VIFs privadas, cada uma suportando 1 DX Gateway, e 1 DX Gateway supera 10 associações de VGW => podemos conectar até 500 VPCs
- O DX Gateway não tem custo; cobramos apenas pelo trânsito de dados
![Arquitetura do DX Gateway](images/DirectConnectGateway3.png)
- DX Gateways entre contas (Cross-account): múltiplas contas podem criar propostas de associação para um DX Gateway

## VIFs de Trânsito e Transit Gateway (TGW)

- Um DX Gateway não faz roteamento entre as VPCs associadas a ele; ele apenas roteia do ambiente local para o lado da AWS ou vice-versa
- Os Transit Gateways são regionais; é possível fazer o emparelhamento (peering) de TGWs, permitindo conexões entre regiões
- Os Transit Gateways utilizam uma arquitetura hub-and-spoke; qualquer recurso associado a um TGW pode se comunicar com qualquer outro recurso associado a esse mesmo TGW
- Essa arquitetura também funciona com TGWs emparelhados
- Arquitetura DX-TGW:
   ![Arquitetura DX-TGW](images/DXGateway4.png)
- Um DX suporta até 50 VIFs públicas e privadas e apenas 1 VIF de Trânsito
- Podemos conectar até 3 Transit Gateways a um único Direct Connect Gateway
- Um DX Gateway individual pode ser usado com VPCs e VIFs privadas OU com Transit Gateways e VIFs de trânsito, **NUNCA AMBOS** ao mesmo tempo!
- Considerações:
    - O DX Gateway não faz roteamento entre seus anexos (attachments); é por isso que a conexão de emparelhamento entre TGWs é necessária
    - Cada TGW pode ser anexado a até 20 DX Gateways
    - Cada TGW suporta até 5000 anexos e até 50 anexos de emparelhamento
- Problemas de roteamento do DX Gateway:
    - O DX Gateway só permite comunicações de uma VIF privada para os gateways virtuais privados associados
    - Com um Transit Gateway podemos resolver isso, se conectarmos o DX Gateway a um Transit Gateway (funciona apenas em uma região)

## Resiliência e Alta Disponibilidade (HA) do Direct Connect

- Para melhorar a resiliência:
    - Solicite 2 portas DX em vez de uma => 2 cross-connects, 2 roteadores DX do cliente se conectando a 2 roteadores locais
    - Conecte-se a 2 localidades DX, tendo roteadores de cliente e roteadores locais em edifícios diferentes (geograficamente separados)
- Arquitetura DX sem resiliência:
![Resiliência DX NENHUMA](images/DirectConnectResilience1.png)
- Arquitetura DX resiliente:
![Resiliência DX OK](images/DirectConnectResilience2.png)
- Arquitetura DX com resiliência aprimorada:
![Resiliência DX MELHOR](images/DirectConnectResilience3.png)
- Arquitetura DX com resiliência extrema:
![Resiliência DX EXCELENTE](images/DirectConnectResilience4.png)

## Grupos de Agregação de Links (LAG) do Direct Connect

- LAG: permite pegar múltiplas conexões físicas e configurá-las para agir como uma só
- Sob a perspectiva de velocidade, um LAG pode ter:
    - 2 portas, cada uma de 100 Gbps
    - 4 portas, com a velocidade de cada uma sendo menor que 100 Gbps
- Podemos criar um LAG com a velocidade máxima de 200 Gbps
- Os LAGs oferecem resiliência, embora a AWS não os comercialize explicitamente como tal. Eles não oferecem resiliência contra falhas de hardware ou falha de uma localidade inteira
- Os LAGs usam uma arquitetura Ativo/Ativo, e no máximo 4 conexões podem fazer parte do LAG
- Todas das conexões devem ter a mesma velocidade e terminar na mesma localidade DX
- Um LAG possui um atributo chamado `minimumLinks`: o LAG permanece ativo desde que o número de conexões operacionais seja maior ou igual a esse valor
![DX LAG](images/DirectConnectLAG.png)

---

# DX - Direct Connect

- It is a physical entry point into the AWS network
- It is a physical fibre connection through which we can access AWS services without sending traffic through the public internet
- The connection is between the business premises => DX Location => AWS Region
- When we order a DX connection, what we order is actually a Port Allocation at a DX Location
- The port has 2 costs:
    - Hourly cost based on the DX location and speed of the port
    - Outbound data transfer, inbound data transfer is free of charge
- In order to get a Direct Connect we have to create a connection (logical entity) inside an AWS account. This connection will have an unique ID
- Provisioning time: weeks/months of extra time
- DX provides low and consistent latency + high speeds (1/10/100 Gbps)
- In the DX location we will have to install a cross-connect (physical cable) in order to connect our own network to the AWS network
![DX architecture](images/DirectConnectArchitecture1.png)

## DX Physical Connection Architecture

- A Direct Connect is a physical port allocated at a DX Location
- This physical port provides 1, 10 or 100 Gbps speed
- DX can be ordered directly from AWS or through partners (wider range of speeds, with less options)
- The port requires single-mod fibre, NO copper cable connection supported
- Depending on the speed we order we will interface with DX using the following standards:
    - **1000BASE-LX** (1310 nm) Transreceiver for 1 Gbps
    - **10GBASE-LR** (1310 nm) Transreceiver for 10 Gbps
    - **100GBASE-LR4** - 100 Gbps
- Auto-Negotiation should be disabled for the connection
- We configure the port speed, full-duplex should be manually set on the network connection
- The router in the DX location should support Border Gateway Protocol (BGP) and BGP MD5 Authentication
- Optional configurations:
    - MACsec
    - Bidirectional Forwarding Detection (BFD)

## Direct Connect - MACsec

- It is a security feature that improves/partially improves a long-standing problem with DX: lack of builtin encryption
- It is a standard which allows frames on the network to be encrypted. Frames are the unit of data which occur at the layer 2 of the OSI model
- MACsec provides a hop by hop encryption architecture => 2 devices need to be next to each other at layer 2 to order MACsec (layer 2 adjacency)
- MACsec features:
    - Confidentiality: strong encryption at layer 2 by encryption the frame's EtherType and payload
    - Data integrity: adds additional fields to ensure that data cannot be modified in transit without both parties being able to detect the modification
    - Data origin authenticity: both parties can see that frames were been sent by other trusted peer
    - Replay protection
- MACsec does not replaces IPSEC over DX, it is not end-2-end!
- It is designed to allow transfer for super high speeds for terabit networks
- MACsec key components:
    - **Secure Channel** (unidirectional): each MACsec participant creates a MACsec channel that is used to send traffic
    - **Secure Channels** are assigned an identifier (SCI): uniquely identifies a secure channel
    - **Secure Associations**: communication that occurs on each secure channel, takes place as a series of transient sessions, multiple secure associations will take place on each secure channel over the lifetime of the connection. Each secure channel generally has 1 secure association at a time (exception when the associations are being replaced)
    - **MACsec encapsulation**: 16 bytes MACsec tag & 16 bytes of Integrity Check Value (ICV). MACSec modifies Ethernet frames by inserting these tags
    - **MACSec Key Agreement** protocol: manages discovery, authentication and key generation
    - **Cipher Suite**: controls how the data is encrypted: algorithm, packets per key, key rotation
- MACsec can be defined either ona DX connection on a Link Aggregation Group (LAG)
- Configuring MACsec: we associate a CAK/CKN pair with the connection on both the AWS DX router(s) and customer side's router
- It is possible to extend MACsec from the DX location ot the customer side
- This requires a dedicated physical extension of the cross connect to the business premises; this type of extension requires Layer 2 Adjacency

## DX Connection Process

- A DX connection begins in a DX Location, which contains AWS equipment and also customer/provider equipment
- AWS does not own this facility (neither does the provider) - it is a data center owned by a third party
- A large data center is collection of cages, these cages are areas that specific customers rent
- Only the staff at the data center can connect stuff together, only they have access to the space in-between the cages to connect different cages together
- Connecting these cages can be done only by staff members only when they have authorization from all parties
- The authorization is called **Letter of Authorization Customer Facility Access (LOA-CFA)**
- It is form that gives the access from one customer to get the data center staff to connect to the equipment of another customer
- DX connection process:
![DX Connection Process](images/DXConnectionProcess.png)

## DX Virtual Interfaces BGP Sessions + VLAN

- DX Connections are a layer 1 connections (physical cables) running layer 2 protocols (Data Link)
- We need a way to connect to multiple types of layer 3 (IP) networks (VPCs and public zones) over a single DX connection => this is where Virtual Interfaces (VIFs) come in handy
- VIFs allows us to run multiple layer 3 networks over a layer 2 direct connect
- A VIF is simply a BGP Peering Session => something which exchanges prefixes which allow traffic to be router to one point to the other
- All of this is isolated within a VLAN
- A VLAN isolates different layer 3 networks using VLAN tagging
- BGP exchanges prefixes, which means each end knows which networks are at each side; BPG MD5 authentication means that only authenticated data will accepted by either type
- 3 types of VIFs can be run over DX:
    - Private VIF: used to connect ot AWS private networks, so VPCs
    - Public VIF: used to connect to Public Zone Service
    - Transit VIF: allow integration between DX and Transit Gateways
![DX VIFs - BGP Session + VLAN](images/DXBGPSessonVLAN.png)
- A single dedicated DX can have in total 50 public/private VIFs, as well as 1 Transit VF
- Hosted VIFs: we can share VIFs with other AWS accounts. Can be connected to a virtual private gateway in a VPC of the other account

## Private VIFs

- They are used to access the resources inside 1 AWS VPC using private IP addresses
- Resources can be accessed with their private IP using private VIFs, public IPs and Elastic IPs wont work
- Private VIFs are associated with a Virtual Private Gateway (VGW) which can be associated to 1 VPC. This has to be in the same region where the DX location connection terminates
- 1 Private VIF = 1 VGW = 1 VPC (there are ways around this using Transit VIFs)
- There is no encryption on private VIFs, DX is not adding encryption and neither is the private VIFs (there are ways around this, example using HTTPS)
- With private VIFs we can use normal or Jumbo Frames (MTU of 1500 or 9001)
- Using VGW, route propagation is enabled by default
- Creating private VIFs:
    - Pick the connection the VIF will run over
    - Chose VGW (default) or Direct Connect Gateway
    - Chose who owns the interface (this account or another account)
    - Choose a VLAN id - 802.1Q which needs to match the customer config
    - We need to enter the BGP ASN of on-premises (public or private). If private use 64512 to 65535
    - We can choose IPs or auto generate them
    - AWS will advertise the VPC CIDR range and the BGP Peer IPs (`/30`)
    - We can advertise default or specific corporate prefixes (**max 100** - this is HARD limit, the interface will go into an idle state)
- Private VIFs architecture:
    ![Private VIFs Architecture](images/DXPrivateVIFS.png)
- Key learning objectives:
    - Private VIFs are used to access private AWS services
    - Private VIF => 1 VGW => 1 VPC
    - VPC needs to be in the same region as the DX location
    - VGW has an AWS assigned
    - Over the private VIF runs the BGP with IPv4 or IPv6 (separate BPG peering connections)
    - We configure our own AS on the VIF, which can be private ASN or public ASN

## Public VIFs

- Are used to access AWS public zone services: both public services and services which have a public Elastic IP
- They offer no direct access to private VPC services
- We can access all public zone regions with one public VIF across AWS global network
- AWS advertises all AWS public IP ranges to us, all traffic to AWS services will go over the AWS global network
- We can advertise any public IPs we own over BGP, in case we don't have public IPs, we can work with AWS support to allocate some to us
- Public VIFs support bi-directional BGP communities
- Advertised prefixes are not transitive, our prefixes don't leave AWS
- Create a public VIF:
    - We pick the connection the VIF will run over
    - We chose the interface owner (this account or another)
    - Chose VLAN - 802.1Q, which needs to match the customer configuration
    - Chose the customer side BGP ASN (ideally this is public ANS for full functionality offered by public VIFs)
    - Configure MD5 authentication and select optional peering IP addresses
    - We have to select which prefixes we want to advertise
- Public VIFs architecture:
![Public VIFs Architecture](images/DXPublicVIFS.png)

## Direct Connect Public VIF + VPN

- Using a VPN gives us an encrypted and authenticated tunnel
- Architecturally, having a VPN over DX uses a Public VIF + VGW/TGW public endpoints
- With a VPN we connect to public IPs which belong to a VGW or TGW
- A VPN is transit agnostic: we can connect using a VPN to VGW or a TGW over the internet or over DX
- A VPN is end-to-end encryption between a Customer Gateway (CGW) and TGW/VGW, while MACsec is single hop based
- VPNs have wide vendor support
- VPNs have more cryptographic overhead compared to MACsec
- A VPN can be provided immediately, can be used while DX is provisioned and/or as a DX backup
![VPN over DX](images/DXPublicVIFVPN.png)

## Direct Connect Gateways

- Direct Connect is a regional service
- Once a DX connection is up, we can use public VIFs to access all AWS Public Services in all AWS regions
- Private VIFs can only access VPCs in the same AWS regions via VGWs
- Direct Connect Gateway is a global network device: it is accessible in all regions
- We integrate with it on the on-premises side by creating a private VIF and associate this with a DX Gateway instead of the Virtual Private Gateway (VGW). This integrates the on-premises router with the DX Gateway
- On the AWS side we create VGW associations in any VPC in any AWS regions
- DX gateways allow to route through them to the on-premises environments and vice-versa. They don't allow VPCs connected to the gateway to communicate with each other
- We can have 10 VGW attachments per DX Gateway
- 1 DX connection can have up to 50 private VIFs, each of which support 1 DX gateway and 1 DX gateway supports 10 VGW association => we can connect up to 500 VPCs
- DX gateway don't have a cost, we have cost for data transit only
![DX Gateway Architecture](images/DirectConnectGateway3.png)
- Cross-account DX Gateways: multiple account can create association proposal for a DX gateway

## Transit VIFs and TGW

- A DX Gateway does not route between the associated VPCs to that gateway, it only routes from on-premises to AWS side or vice-versa
- Transit Gateways are regional, it is possible to peer TGWs allowing connections between regions
- Transit Gateways are hub-and-spoke architecture, anything associated with a TGW is able to communicate with anything other associated to that TGW
- This architecture also works within peered TGWs
- DX-TGW Architecture:
   ![DX-TGW Architecture](images/DXGateway4.png)
- A DX supports up to 50 public and private VIFs and only 1 Transit VIF
- We can connect up to 3 Transit Gateways to a Direct Connect Gateway
- An individual DX gateway can be used with VPCs and private VIFs or with Transit Gateways and transit VIFs, **NOT BOTH** at the same time!
- Consideration:
    - DX gateway does not route between its attachments, this is why the peering connection between TGWs is required
    - Each TGW can be attached up to 20 DX gateways
    - Each TGW supports up 5000 attachments, up to 50 peering attachments
- DX Gateway routing problems:
    - DX gateway only allows communications from a private VIF to any associated virtual private gateways
    - With a transit gateway we can solve this, if we connect the DX gateway to a transit gateway (works only in one region)

## Direct Connect Resilience and HA

- To improve resilience:
    - Order 2 DX ports instead of one => 2 cross connects, 2 customer DX routes connecting to 2 on-premises routes
    - Connect to 2 DX locations, have to customer routers and 2 on-premises routers in different buildings (geographically separated)
- Not resilient DX architecture:
![DX resilience NONE](images/DirectConnectResilience1.png)
- Resilient DX architecture:
![DX resilience OK](images/DirectConnectResilience2.png)
- Improved resilient DX architecture:
![DX resilience BETTER](images/DirectConnectResilience3.png)
- Extreme resilient DX architecture:
![DX resilience GREAT](images/DirectConnectResilience4.png)

## Direct Connect Link Aggregation Groups (LAG)

- LAG: allows to take multiple physical connections and configure them to act as one
- From speed perspective a LAG can have:
    - 2 ports, each 100 Gbps
    - 4 ports, the speed of each being less than 100 Gbps
- We can create a LAG with the maximum speed of 200 Gbps
- LAG do provide resilience, although AWS does not market them as such. They do not provide any resilience regarding hardware failure or the failure of entire location
- LAGs use an Active/Active architecture, maximum 4 connection can be part of the LAG
- All connections must have the same speed and terminate at the same DX location
- A LAG has an attribute called `minimumLinks`: the LAG is active as long as the number of working connections is greater or equal to this value
![DX LAG](images/DirectConnectLAG.png)