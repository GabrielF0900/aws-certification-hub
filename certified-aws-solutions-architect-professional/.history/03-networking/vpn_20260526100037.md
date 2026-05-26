# VPNs

# Fundamentos de VPN IPsec

- O IPsec é um grupo de protocolos
- Seu objetivo é estabelecer túneis seguros através de redes inseguras. Exemplo: conectar duas redes seguras (peers/pares) pela internet pública
- O IPsec fornece autenticação
- Todo tráfego transferido através do IPsec é criptografado
- O IPsec usa criptografia assimétrica para trocar chaves simétricas e usa estas últimas para a criptografia contínua
- O IPsec possui 2 fases principais:
    - Fase 1 do IKE (Internet Key Exchange)
        - É lenta e pesada
        - É um protocolo que define como as chaves são trocadas
        - Possui 2 versões: v1 (mais antiga) e v2 (mais recente)
        - Usa criptografia assimétrica para entrar em acordo e criar uma chave simétrica compartilhada
        - O fim desta fase resulta em um túnel IKE SA (security association) de fase 1
        ![Arquitetura da fase 1 do IPsec](images/IPSECvpn2.png)
    - Fase 2 do IKE
        - É mais rápida e ágil
        - Usa as chaves acordadas na fase 1
        - Concentra-se em definir o método de criptografia e as chaves usadas para a transferência de dados em massa
        - O resultado final é um túnel IPsec SA de fase 2 (que roda sobre a fase 1)
        ![Arquitetura da fase 2 do IPsec](images/IPSECvpn3.png)
- Existem dois tipos de VPNs - baseados em como elas filtram/correspondem ao tráfego:
    - VPNs baseadas em políticas (Policy-based): conjuntos de regras filtram o tráfego; podemos ter regras diferentes para tipos diferentes de tráfego
    - VPNs baseadas em rotas (Route-based): a correspondência do destino é feita com base no prefixo. Temos um único par de associações de segurança para cada prefixo de rede (menos funcionalidades, porém muito mais simples de configurar)
    ![VPNs baseadas em rotas vs políticas](images/IPSECvpn4.png)

## AWS Site-to-Site VPN

- Uma VPN Site-to-Site é uma conexão lógica entre uma VPC e uma rede local (on-premises) executada pela internet pública. A conexão é criptografada usando IPsec
- Pode ter alta disponibilidade (HA) total se implementada corretamente
- É rápida de provisionar, podendo estar pronta em menos de uma hora (em contraste com o DX)
- Componentes envolvidos na criação de uma conexão VPN:
    - **VPC**
    - **Virtual Private Gateway (VGW)**: é um objeto de gateway que pode ser o destino de uma ou mais regras em uma Tabela de Rotas (Route Table). Pode ser associado a uma única VPC
    - **Customer Gateway (CGW)**: pode se referir a duas coisas diferentes:
        - Frequentemente refere-se à configuração lógica na AWS
        - Ao roteador físico local (on-premises) ao qual a VPN se conecta
    - A própria **Conexão VPN (VPN Connection)**: a conexão que vincula o VGW da AWS ao CGW
- VPN Estática vs Dinâmica:
    - **VPN Estática**:
        - Usa configuração de rede estática: as rotas estáticas são adicionadas às tabelas de rotas do lado da AWS, e as redes estáticas precisam ser identificadas na conexão VPN do lado local (on-premises).
        - É simples, utiliza apenas IPsec, funciona em qualquer lugar, mas possui limitações em termos de balanceamento de carga e failover de múltiplas conexões
    - **VPN Dinâmica**:
        - Usa o protocolo BGP; se o roteador do cliente não suportar BGP, não será possível usar VPNs dinâmicas
        - BGP: permite o roteamento dinâmico instantâneo e o uso de múltiplos links ao mesmo tempo entre as mesmas localidades. Permite o uso de arquiteturas altamente disponíveis (HA)
        - Rotas estáticas ainda podem ser adicionadas manualmente às tabelas de rotas
        - Propagação de rotas (Route propagation): se ativada, significa que as rotas são adicionadas à Tabela de Rotas automaticamente
- Considerações para a VPN:
    - Limitação de velocidade para VPN com 2 túneis: *1.25 Gbps*, uma limitação da AWS. Limitações do roteador do cliente também podem se aplicar
    - Considerações de latência: pode ser inconsistente se o tráfego passar pela internet pública
    - Custo: custo por hora e pelo tráfego de saída (outgoing); limites de dados locais também podem se aplicar
    - Velocidade de configuração: pode ser feita muito rapidamente, em poucas horas ou menos; o IPsec é suportado por uma grande variedade de dispositivos, enquanto o suporte ao BGP é menos comum. As VPNs são sempre mais rápidas de configurar do que qualquer outra tecnologia de conexão privada
    - As VPNs podem ser usadas como backup do Direct Connect ou podem ser usadas sobre o Direct Connect para adicionar uma camada de criptografia

### Accelerated Site-to-Site VPN

- Uma melhoria de desempenho para a AWS Site-to-Site VPN que utiliza a rede global da AWS, a mesma rede usada pelo Global Accelerator e pelo CloudFront
- Ao usar uma VPN Site-to-Site clássica, o tráfego passa pela internet pública. Para evitar isso, algumas empresas usam uma VPN Site-to-Site sobre o Direct Connect. Direct Connect oferece um desempenho superior, mas a um custo mais elevado. Como o DX não é uma opção para todos, a VPN Site-to-Site acelerada foi criada para melhorar o desempenho em comparação com as VPNs Site-to-Site clássicas
- Arquitetura da VPN Site-to-Site acelerada:
![VPN Site-to-Site Acelerada](images/AcceleratedS2SVPN1.png)
- A aceleração só pode ser habilitada ao criar um anexo de Transit Gateway! Não é compatível com VPNs que utilizam Virtual Private Gateways (VGW)
- A VPN Site-to-Site acelerada possui uma taxa fixa pelo acelerador e uma taxa pela transferência de dados

## Client VPN

- A VPN Site-to-Site é geralmente usada para conectar uma ou mais instalações empresariais às VPCs da AWS. A Client VPN é semelhante, mas em vez de sites se conectarem à AWS, temos clientes (usuários) individuais
- A Client VPN é uma implementação gerenciada do OpenVPN
- Qualquer dispositivo cliente que possa usar o software OpenVPN é suportado
- Arquiteturalmente, nos conectamos a um endpoint de Client VPN que pode ser associado a uma VPC e a uma ou mais Redes Alvo (Target Networks) para alta disponibilidade
- O faturamento da Client VPN é baseado na associação de rede e em uma taxa horária de uso
- Configuração da Client VPN:
    - Criamos um Client VPN Endpoint e o associamos a uma VPC e a uma ou mais sub-redes dessa VPC
    - Essa associação implanta uma ENI nas sub-redes associadas
    - Só podemos escolher uma sub-rede por AZ
- A Client VPN pode usar diversos métodos de autenticação diferentes (certificados, Cognito User Pool, Identidades Federadas, AWS Directory Service)
- Associamos uma tabela de rotas ao Client VPN Endpoint para configurar o roteamento e a conectividade (para a internet via NAT Gateways, outras VPCs via peering, etc.)
- Essa tabela de rotas é enviada para qualquer cliente que se conecte ao Client VPN Endpoint
- O comportamento padrão é que a tabela de rotas da Client VPN substitui quaisquer rotas locais no cliente, o que significa que os dispositivos clientes não conseguem acessar nada localmente em sua rede local sem que a comunicação passe pelo Client VPN Endpoint
- Podemos usar uma VPN com túnel dividido (split-tunnel), o que significa que quaisquer rotas do Client VPN Endpoint são adicionadas às tabelas de rotas locais do cliente. Isso resolve o problema do comportamento padrão
- O split-tunnel não é o comportamento padrão. Ele deve ser habilitado pelo usuário, caso contrário, todos os dados (incluindo a conexão com a internet pública) passarão pelo túnel

---

# VPNs

# IPSEC VPN Fundamentals

- IPSEC is a group of protocols
- Their aim is to set up secure tunnels across insecure networks. Example: connect two secure networks (peers) over the public internet
- IPSEC provides authentication
- Any traffic transferred through IPSEC is encrypted
- IPSEC is using asymmetric encryption to exchange symmetric keys and use these of ongoing encryption
- IPSEC has 2 main phases:
    - IKE (Internet Key Exchange) Phase 1
        - It is slow and heavy
        - It is a protocol of how keys are exchanged
        - It has 2 versions v1 (older) and v2 (newer)
        - Uses asymmetric encryption to agree on and create a shared symmetric key
        - The end of this phase is an IKE SA (security association) phase 1 tunnel
        ![IPSEC phase 1 architecture](images/IPSECvpn2.png)
    - IKE Phase 2
        - It is faster and more agile
        - Uses the keys agreed in phase 1
        - Is concerned with agreeing on encryption method and keys used for bulk data transfer
        - The end result is an IPSEC SA phase 2 tunnel (runs over phase 1)
        ![IPSEC phase 2 architecture](images/IPSECvpn3.png)
- There are two types of VPNs - how they match traffic:
    - Policy based VPNs: rule sets match traffic, we can have different rules for different types of traffic
    - Route based VPNs: target matching is done based on prefix. We have a single pair of security associations for each network prefix (less functionality, much simpler to set up)
    ![Route vs Policy Based VPNs](images/IPSECvpn4.png)

## AWS Site-to-Site VPN

- A Site-to-Site VPN is a logical connections between a VPC and an on-premise network running over the public internet. The connection is encrypted using IPSec
- Can be fully HA if it is implemented correctly
- It is quick to provision, it can be provisioned in less than an hour (contrast to DX)
- Components involved in creating a VPN connection:
    - **VPC**
    - **Virtual Private Gateway (VGW)**: it is a gateway object which can be the target of one or more rules in a Route Tables. It can be associated to a single VPC
    - **Customer Gateway (CGW)**: can refer to 2 different things:
        - Often is referred to the logical configuration in AWS
        - Physical on-premises router which the VPN connects to
    - **VPN Connection** itself: the connection linking the VGW from the AWS to the CGW
- Static vs Dynamic VPN:
    - **Static VPN**:
        - Uses static network configuration: static routes are added to the route tables AWS side, static networks has to be identified on the VPN connection on-premise side. 
        - It is simple, it just uses IPSec, works anywhere, having limitation on terms of load-balancing and multi-connection failover
    - **Dynamic VPN**:
        - Uses BGP protocol, if customer router does not support BGP, we can not use dynamic VPNs
        - BGP: allows routing on the fly, allows multiple links to be used at once between the same locations. Allows using HA available architectures
        - Static routes can still be added to the route tables manually
        - Route propagation: if enabled means that routes are added ro the Route Table automatically
- Considerations for VPN:
    - Speed Limitation for VPN with 2 tunnels: *1.25 Gbps*, AWS limitation. Customer router limitation might also apply
    - Latency considerations: can be inconsistent if the traffic goes through the public internet
    - Cost: hourly cost for outgoing traffic, on-premises data caps might also apply
    - Speed of setup: can done very quickly, within hours or less; IPSec is supported by a wide variety of devices, BGP support is less common. VPNs are always quicker to setup then any other private connection technologies
    - VPNs can be used for Direct Connect backup or they can be used over the Direct Connect for adding a layer of encryption

### Accelerated Site-to-Site VPN

- Performance enhancement for AWS Site-to-Site VPN that uses the AWS global network, the same network used for Global Accelerator and CloudFront
- Using a classic Site-to-Site VPN, the traffic goes through the public internet. In order to avoid this, some companies use a Site-to-Site VPN over Direct Connect. Direct Connect offers more better performance, but at a higher cost. Since DX is not an option for everybody, accelerated Site-to-Site VPN was created to improve performance compared to classic Site-to-Site VPNs
- Accelerated Site-to-Site VPN architecture:
![Accelerated Site-to-Site VPN](images/AcceleratedS2SVPN1.png)
- Acceleration can be enabled when creating a Transit Gateway attachment only! Not compatible with VPNs using Virtual Private Gateways (VGW)
- Accelerated Site-to-Site VPN has a fixed accelerator cost fee and a data transfer fee

## Client VPN

- Site-to-Site VPN is generally used for one or more business premisses to connect to AWS VPCs. ClientVPN is similar, but instead of sites connecting to AWS, we have individual clients
- A ClientVPN is a managed implementation of OpenVPN
- Any client device which can use the OpenVPN software is supported
- Architecturally we connect to a Client VPN endpoint which can be associated with one VPC and with one ore more Target Networks (high availability)
- Client VPN billing is based on network association and hourly fee for usage
- Client VPN setup:
    - We crate a Client VPN Endpoint and associate it with a VPC and one or more subnets from the VPC
    - This association places an ENI into the subnets associated
    - We can only pick one subnet per AZ
- Client VPN can use many different methods of authentication (certificates, Cognito User Pool, Federated Identities,  AWS Directory Service)
- We associate a route table to the Client VPN Endpoint in order to set up routing and connectivity (to internet via NAT Gateways, other VPCs with peering, etc.)
- This route table is pushed to any client which connects to the Client VPN Endpoint
- The default behavior is the Client VPN route table replaces any local routes on the client, meaning the client devices can not access anything locally on their local network without having communication going through the Client VPN Endpoint
- We can use split tunnel VPN, meaning that any routes from the Client VPN Endpoint are added to local client route tables. This solves the problem with the default behavior
- Split tunnel is not the default behavior. It must be enabled by the user, otherwise all the data (including connection to the public internet) will go via the tunnel