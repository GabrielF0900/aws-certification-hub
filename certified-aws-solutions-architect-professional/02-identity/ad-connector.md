# AD Connector (Serviços de Diretório)

- O AD Connector fornece um par de endpoints de diretório em uma VPC
- Ele injeta ENIs em sub-redes em uma VPC
- Uma vez injetado, o conector AD aparece como um diretório nativo para outras instâncias AWS capazes de usar um serviço de diretório
- Redireciona solicitações para um servidor de diretório on-premise existente, o que significa que nenhum dado de diretório é armazenado na AWS
- O conector AD nos permite usar serviços AWS que exigem um diretório AD (como Workspaces) e usar isso com um serviço de diretório on-premises => não precisamos implantar um diretório AD adicional na AWS
- Existem 2 tamanhos de serviços de diretório *pequeno* e *grande*, embora não haja limites de usuário explícitos, o tamanho escolhido impacta a quantidade de computador alocada pela AWS para o conector
- Podemos usar vários conectores para distribuir a carga
- O diretório AD é colocado em 2 sub-redes em VPCs em diferentes zonas de disponibilidade => resiliente a falha de AZ
- O conector deve ser configurado para apontar para pelo menos um serviço de diretório on-premise => precisamos fornecer informações da conta para que o conector possa se autenticar
- Requer uma rede funcionando para o serviço on-premise, caso contrário não funcionará (rede privada via Direct Connect ou VPN)

## Arquitetura do AD Connector

![AD Connector](images/DirectoryServiceADConnector.png)

## Casos de Uso para AD Connector

- Projetos de prova de conceito, não queremos mover nosso Active Directory para AWS para isso
- Temos uma infraestrutura pequena na AWS e não queremos mover o Active Directory para AWS
- Razões legais/conformidade - não queremos armazenar informações de usuário na AWS
- Para requisitos maiores use AWS Directory Service

---

# AD Connector (Directory Services)

- AD Connector provides a pair of directory endpoints in a VPC
- It injects ENIs into to subnets in a VPC
- Once injected AD connector appears as a native directory to other AWS instances capable of using a directory service
- Redirects requests to an existing on-premise directory server, which means no directory data is stored in AWS
- AD connector allows us to use AWS services which do require an AD directory (such as Workspaces) and use this with an on-premises directory service => we don't need to deploy additional AD directory in AWS
- There are 2 sizes of directory services *small* and *large*, while there are no explicit user limits, the chosen size does impact the amount of compute allocated by AWS for the connector
- We can use multiple connector to distribute the load
- AD directory is placed in 2 subnets in a VPCs in different availability zones => resilient to AZ failure
- The connector should be configured to point to at least one on-premise directory service => we need to provide account information for the connector to be able to authenticate itself
- Requires a working network to on-premise service, otherwise wont work (private network via Direct Connect or VPN)

## AD Connector Architecture

![AD Connector](images/DirectoryServiceADConnector.png)

## Use cases for AD Connector

- Prof of concept projects, we don't want to move our Active Directory to AWS for it
- We have a small infrastructure in AWS and we don't want to move the Active Directory to AWS
- Legal/compliance reasons - we don't want to store user info in AWS
- For larger requirements use AWS Directory Service