# AWS Transit Gateway

- É um hub de trânsito de rede que conecta VPCs entre si e a redes locais (on-premises) usando VPNs Site-to-Site e Direct Connects
- Foi projetado para reduzir a complexidade da arquitetura de rede na AWS
- É um objeto de gateway de rede, altamente disponível (HA) e escalável
- Anexos (Attachments): criamos anexos para que o TGW se conecte a VPCs e redes locais. Os anexos válidos são:
    - Anexos de VPC (VPC attachments)
    - Anexos de VPN Site-to-Site
    - Anexos de Direct Connect Gateway
- Os anexos são configurados em cada sub-rede das VPCs conectadas
- Também podemos emparelhar (peer) transit gateways entre diferentes regiões e/ou contas distintas
- Também podemos anexar transit gateways a conexões DX
- Considerações sobre o Transit Gateway:
    - Suporta roteamento transitivo: um único transit gateway com múltiplos anexos usando tabelas de rotas
    - Pode ser usado para criar redes globais com emparelhamento (peering)
    - Podemos compartilhar transit gateways usando o AWS RAM
    - Os Transit Gateways oferecem arquiteturas menos complexas em comparação com soluções de VPC peering

## Transit Gateway - Deep Dive

- O Transit Gateway possui uma arquitetura hub-and-spoke, podendo se conectar a vários tipos de objetos de rede dentro da AWS
- Integração com o Direct Connect:
    - É necessária uma VIF de Trânsito (Transit VIF) que passa por um DX Gateway
    - O DX Gateway pode ser anexado ao Transit Gateway com um Anexo de Transit Gateway (Transit Gateway Attachment)
    - 1 DX Gateway pode ser anexado a até 3 Transit Gateways
- O Transit Gateway possui uma tabela de rotas padrão que é populada a partir dos anexos:
    - Fornece os intervalos CIDR para as VPCs conectadas
    - Fornece as rotas aprendidas via BGP para as VPNs
    - Para DX Gateways com o Anexo de Transit Gateway, definimos as redes dentro do anexo configurado no lado do DX Gateway
- Podemos emparelhar (peer) TGWs com outros TGWs entre regiões. Podemos emparelhar um TGW com até 50 outros TGWs, e esses TGWs também podem se emparelhar com outros TGWs
- Um TGW por padrão possui uma tabela de rotas
- Todos os anexos usam essa RT (Route Table) para decisões de roteamento e, por padrão, todos os anexos propagam rotas para essa tabela de rotas, exceto os anexos de emparelhamento (peering attachments)
- Todos os anexos podem rotear para todos os outros anexos por padrão

## Transit Gateway Peering

- No caso de anexos de emparelhamento (peering attachments), as rotas não são compartilhadas; precisamos usar rotas estáticas, de forma semelhante ao VPC peering (a AWS recomenda o uso de ASNs exclusivos para melhorias futuras em anúncios de rotas)
- A resolução de DNS público para endereçamento privado não é suportada em emparelhamentos inter-região (inter-region peers)
- A transferência de dados em uma conexão de emparelhamento é criptografada e enviada pela rede global da AWS
- Podemos emparelhar até 50 anexos de emparelhamento por TGW, os quais podem estar em diferentes regiões e diferentes contas AWS

## Roteamento Isolado no Transit Gateway (Transit Gateway Isolated Routing)

- Por padrão:
    - Todos os anexos são associados à mesma tabela de rotas
    - Todos os anexos propagam para a mesma tabela de rotas, fazendo com que todos os anexos tenham conhecimento de quaisquer outros anexos
- Os anexos só podem ser associados a 1 tabela de rotas, mas as tabelas de rotas podem ser associadas a muitos anexos
- Os anexos podem propagar para muitas RTs, inclusive para aquelas com as quais não estão associados
- Se quisermos isolar as redes:
    - Criamos uma tabela de rotas e configuramos todos os anexos para propagarem para essa tabela de rotas
    - Associamos a tabela de rotas apenas aos anexos que queremos que se comuniquem entre si
    - Criamos outra rota e a associamos ao anexo com o qual não queremos comunicação. Configuramos os outros anexos para propagarem para essa tabela de rotas

---

# AWS Transit Gateway

- It is a network transit hub which connects VPCs to each other and to on-premise networks using Site-to-Site VPNs and Direct Connects
- It is designed to reduce the network architecture complexity in AWS
- It is a network gateway object, it is HA and scalable
- Attachments: we create attachments in order for the TGW to connect to VPCs and on-premise networks. Valid attachments are:
    - VPC attachments
    - Site-to-Site VPN attachments
    - Direct Connect Gateway attachments
- Attachments are configured in each subnet of the connected VPCs
- We can also peer transit gateways across cross regions and/or cross accounts
- We can also attach transit gateways to the DX connections
- Transit Gateway Considerations:
    - Supports transitive routing: single transit gateway with multiple attachments using route tables
    - Can be used to create global networks with peering
    - We can share transit gateways using AWS RAM
    - Transit Gateways offer less complex architectures compared to VPC peering solutions

## Transit Gateway - Deep Dive

- Transit gateway is a hub-and-spoke architecture, it can connect to various types of networking objects within AWS
- Integration with Direct Connect:
    - A Transit VIF is required which goes through a DX Gateway
    - The DX Gateway can be attached to the Transit Gateway with a Transit Gateway Attachment
    - 1 DX Gateway can be attached to 3 Transit Gateways
- Transit Gateway has a default route table which is populated from the attachments:
    - For the VPCs we have the CIDR ranges of these VPCs
    - For VPNs we have the routes learned via BGP
    - For DX Gateways with the Transit Gateway Attachment we define the networks within the attachment configured at the DX Gateway side
- We can peer TGWs with other TGWs between regions. We can peer a TGW with up to 50 other TGWs, and these TGWs can also peer with other TGWs
- A TGW by default has one route table
- All attachments use this RT for routing decisions, by default all attachments propagate routes to this route table, exception peering attachments
- All attachments can route to all other attachments by default

## Transit Gateway Peering

- In case of peering attachments routes are not shared, we need to use static routes, similar to VPC peering (AWS recommends using unique ASNs for future enhancements for route advertisements)
- Resolution of public DNS to private addressing is not supported over inter-region peers
- Data transfer over peering connection is encrypted and is sent over AWS network
- We can peer up to 50 peering attachments per TGW, these can be in different regions, different AWS accounts

## Transit Gateway Isolated Routing

- By default:
    - All attachments are associated with the same route table
    - All attachments propagate to the same route table, all attachments are aware of any other attachments
- Attachments can only be associated with 1 route table, route tables can be associated to many attachments
- Attachments can propagate to many RTs, event to those they are not associated with
- If we would want to isolate networks:
    - We create a route table and we configure all attachments to propagate to the route table
    - We associate the route table with only the attachments we would want to communicate with each other
    - We create another route and associate it to the attachment we don't want to communicate with each other. We configure other attachments to propagate to this route table