# AWS PrivateLink

- Permite nos conectar a serviços hospedados por outras contas AWS
- Podemos nos conectar a eles diretamente ou podemos utilizar serviços de parceiros do AWS Marketplace
- Em ambos os casos, esses serviços são apresentados em nossa VPC como endereços IP privados e ENIs
- O AWS PrivateLink é a base técnica para os Interface Endpoints
- Para Alta Disponibilidade (HA), devemos garantir a implantação de múltiplos endpoints. Recomendado um por AZ em cada sub-rede que precisa consumir o serviço
- O PrivateLink suporta apenas IPv4 e TCP (~~IPv6 não é suportado!~~, veja: https://aws.amazon.com/about-aws/whats-new/2022/05/aws-privatelink-ipv6/)
- O DNS Privado (Private DNS) é suportado para sobrescrever nomes de DNS públicos (se houver um DNS público fornecido pelo serviço que consumimos)
- Os endpoints do PrivateLink podem ser acessados via Direct Connect, Site-to-Site (S2S) VPN e VPC Peering

## VPC Endpoints 

### Gateway Endpoints

- Os Gateway endpoints fornecem acesso privado aos serviços suportados: **S3** e **DynamoDB**
- Eles permitem que qualquer recurso em uma VPC estritamente privada acesse o S3/DynamoDB
- Criamos um gateway endpoint por serviço, por região, e o associamos a uma ou mais sub-redes em uma VPC
- Alocamos um gateway endpoint a uma sub-rede, e uma *Lista de Prefixos* (Prefix List) é adicionada à tabela de rotas da sub-rede. Essa lista de prefixos aponta para o gateway endpoint
- Qualquer tráfego direcionado ao S3/DynamoDB passará pelo gateway endpoint e não pelo internet gateway
- Os Gateway endpoints são altamente disponíveis em todas as AZs de uma região; eles não ficam diretamente dentro de uma VPC/sub-rede específica
- **Política de endpoint (Endpoint policy)**: define quais coisas podem ser acessadas/conectadas por meio do endpoint (exemplo: um subconjunto específico de buckets do S3)
- Os Gateway endpoints só podem ser usados para acessar serviços na mesma região
- Os Gateway endpoints permitem o uso de buckets do S3 estritamente privados: os buckets do S3 podem ser configurados como privados para permitir o acesso apenas a partir do gateway endpoint. Isso ajuda a evitar vazamentos de dados (*Leaky Buckets*)
- Os Gateway endpoints são objetos de gateway lógicos e só podem ser acessados de dentro da VPC atribuída

### Interface Endpoints

- Os Interface endpoints fornecem acesso privado a serviços públicos da AWS, de forma semelhante aos Gateway Endpoints
- Historicamente, eles eram usados para fornecer acesso a outros serviços além do S3 e DynamoDB; recentemente, a AWS passou a permitir que os interface endpoints também forneçam acesso ao S3
- A diferença entre gateway endpoints e interface endpoints é que os interface endpoints não possuem alta disponibilidade (HA) por padrão. Os interface endpoints são adicionados às sub-redes como uma ENI (Elastic Network Interface)
- Para obter alta disponibilidade (HA), precisamos adicionar um interface endpoint em cada sub-rede por AZ dentro de uma VPC
- É possível atribuir Security Groups aos interface endpoints (os gateway endpoints não permitem SGs)
- Também podemos usar políticas de endpoint, semelhante aos gateway endpoints
- Os Interface endpoints suportam apenas TCP sobre IPv4
- Os Interface endpoints usam o PrivateLink por baixo dos panos (behind the scenes)
- Os Gateway endpoints usam listas de prefixos, enquanto os interface endpoints usam DNS. Os interface endpoints fornecem um novo nome de DNS para cada serviço com o qual se comunicam
- Os Interface endpoints recebem uma série de nomes de DNS:
    - DNS Regional do Endpoint (Endpoint Region DNS)
    - DNS Zonal do Endpoint (Endpoint Zonal DNS)
    - PrivateDNS: sobrescreve o DNS padrão do serviço por uma nova versão que aponta para o interface endpoint

## VPC Endpoints Policies

- As políticas de endpoint não concedem acesso a nenhum serviço da AWS de forma isolada
- As identidades que acessam os recursos ainda precisam de suas próprias permissões para acessá-los
- Uma política de endpoint apenas limita o acesso se o serviço for acessado através daquele endpoint específico
- A política de endpoint contém uma política e condições (quem tem acesso a quê)
- As políticas são comumente usadas para limitar o que as VPCs privadas podem acessar

---

# AWS PrivateLink

- Allows us to connect to services hosted by other AWS accounts 
- We can connect to them directly or we can utilize AWS Marketplace partner services
- In both cases these services are presented in our VPC as private IP address ans ENIs
- AWS PrivateLink is the technical basis for Interface Endpoints
- For HA we should make sure we deploy multiple endpoint. Recommended one per AZ in each subnet we need to consume the service
- PrivateLink supports IPv4 and TCP only (~~IPv6 is not supported!~~, see: https://aws.amazon.com/about-aws/whats-new/2022/05/aws-privatelink-ipv6/)
- Private DNS is supported for overriding public DNS names (if there is a public DNS provided by the service we consume)
- PrivateLink endpoints can be accessed through Direct Connect, S2S VPN and VPC Peering

## VPC Endpoints 

### Gateway Endpoints

- Gateway endpoints provide private access to supported services: **S3** and **DynamoDB**
- They allow any resource in a private only VPC to access S3/DynamoDB
- We crate a gateway endpoint per service per region and associate it to one or more subnets in a VPC
- We allocate a gateway endpoint to a subnet, a *Prefix List* is added to the route table for the subnet. This prefix lists targets the gateway endpoint
- Any traffic targeted to S3/DynamoDB will go through the gateway endpoint and not through the internet gateway
- Gateway endpoints are highly available across all AZs in a region, they are not directly inside a VPC/subnet
- **Endpoint policy**: allows what things can be connected to the by the endpoint (example: a particular subset of S3 buckets)
- Gateway endpoints can be used to access services in the same region only
- Gateway endpoints allow private only S3 buckets: S3 buckets can be set to private allowing only access from the gateway endpoint. This will help prevent *Leaky Buckets*
- Gateway endpoints are logical gateway objects, they can be only accessed from inside the assigned VPC

### Interface Endpoints

- Interface endpoints provide private access to AWS public services similar to Gateway Endpoints
- Historically they have been used to provide access to services other than S3 and DynamoDB, recently AWS allowed interface endpoints to provide access to S3 as well
- Difference between gateway endpoints and interface endpoints is that interface endpoints are not HA by default. Interface endpoints are added to subnets as an ENI
- In order to have HA, we have to add an interface endpoint to every subnet per AZ inside of a VPC
- Interface endpoints are able to have security groups assigned to them (gateway endpoints do not allow SGs)
- We can also use endpoints policies, similar to gateway endpoints
- Interface endpoints support TCP only over IPv4
- Interface endpoints use PrivateLink behind the scene
- Gateway endpoints use prefix lists, interface endpoints use DNS. Interface endpoints provide a new DNS name for every service they are meant communicate with
- Interface endpoints are given a number of DNS names:
    - Endpoint Region DNS
    - Endpoint Zonal DNS
    - PrivateDNS: overrides the default service DNS with a new version pointing to interface endpoint

## VPC Endpoints Policies

- Endpoints policies don't grant access to any AWS services in isolation
- Identities accessing resources still need they permissions to access resources
- An endpoint policy only limits access if the service is accessed to the specific endpoint
- The endpoint policy contains a policy and conditions (who has access to what)
- Policies are commonly used to limit what private VPCs can access