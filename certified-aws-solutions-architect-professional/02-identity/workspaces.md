# Amazon Workspaces

- Produto de desktop gerenciado como um serviço (DAAS) - desktop Windows/Linux virtual dedicado entregue como um serviço gerenciado
- Ideal para trabalho em casa
- Semelhante a Citrix/Remote Desktop - hospedado dentro da AWS
- Fornece um desktop consistente acessível de qualquer lugar, podemos fazer logout e fazer login novamente de diferentes lugares, aplicações mantendo seu estado
- Podemos ter workspaces Windows e Linux em vários tamanhos
- Podemos usar aplicações comerciais nos workspaces
- Os workspaces podem ser cobrados mensalmente ou por hora. Há um custo de infraestrutura mensal adicional, que é aplicado mesmo quando somos cobrados por hora
- Os workspaces usam Directory Service (Simples, AD, AD Connector) para autenticação e gerenciamento de usuários
- Cada workspace usa um ENI (Elastic Network Interface) injetado em uma VPC
- Os workspaces são acessados usando software cliente de desktop/laptop, a largura de banda está incluída gratuitamente. Para qualquer outro acesso à internet a partir dos workspaces, a infraestrutura VPC normal é usada e cobrada em conformidade
- Os workspaces Windows podem acessar recursos FSx e EC2 Windows
- Qualquer rede híbrida existente também pode ser utilizada para acessar recursos on-premises
- Os workspaces fornecem um volume de sistema e um volume de usuário, ambos podem ser criptografados

## Arquitetura de Workspaces

![Arquitetura de Workspaces](images/AmazonWorkspaces.png)

- Os workspaces injetam um ENI em VPCs gerenciadas pelo cliente, eles funcionam em VPCs gerenciadas pela AWS
- Serviços de diretório também injetam ENIs em VPCs gerenciadas pelo cliente para acesso a arquivos, etc.
- Os workspaces não são altamente disponíveis por design
- Podemos distribuir workspaces em diferentes AZs, mas um workspace em particular pode ser afetado por uma falha de AZ

---

# Amazon Workspaces

- Managed desktop as a service product (DAAS) - dedicated virtual Windows/Linux desktop delivered as a managed service
- Ideal for home working
- Similar to Citrix/Remote Desktop - hosted within AWS
- It provides a consistent desktop accessible from anywhere, we can log off and log back in from different places, applications maintaining their state
- We can have Windows and Linux workspaces in various sizes
- We can use commercial applications on the workspaces
- Workspaces can be charged on monthly or hourly basis. There is an additional monthly infrastructure cost, which is applied even in case when we are billed hourly
- Workspaces use Directory Service (Simple, AD, AD Connector) for authentication and user management
- Each workspace uses an ENI (Elastic Network Interface) injected in a VPC
- Workspaces are accessed using client software from desktop/laptop, bandwidth is included free of charge. For any other internet access from the workspaces normal VPC infrastructure is used and charged accordingly
- Windows workspaces can access FSx and EC2 windows resources
- Any existing hybrid network can be also utilized for accessing on-premise resources
- Workspaces provide a system volume and an user volume, both can be encrypted

## Workspaces Architecture

![Workspaces Architecture](images/AmazonWorkspaces.png)

- Workspaces inject an ENI into customer managed VPCs, they run into AWS managed VPCs
- Directory services also inject ENIs into customer managed VPCs for file access, etc.
- Workspaces are not highly available by design
- We can distribute workspaces in different AZs, but a single workspace in particular can be affected by an AZ failure
