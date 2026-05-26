# AWS Transfer Family

- É um produto que fornece um serviço gerenciado de transferência de arquivos
- Ele nos permite transferir arquivos de/para o S3 ou EFS
- Ele fornece servidores gerenciados que suportam vários protocolos. Permite fazer o upload/download de dados no S3 ou EFS usando protocolos diferentes dos suportados nativamente por eles
- Permite que interajamos com ambos os serviços usando os seguintes protocolos:
    - FTP (File Transfer Protocol): protocolo de transferência de arquivos não criptografado
    - FTPS (File Transfer Protocol Secure): protocolo de transferência de arquivos com criptografia TLS
    - SFTP (SSH File Transfer Protocol): transferência de arquivos sobre SSH
    - Applicability Statement 2 (AS2): transferência de dados estruturados B2B (Business-to-Business)
- O Transfer Family suporta uma ampla variedade de identidades: gerenciadas pelo serviço (service-managed), Directory Service, personalizadas (Lambda/APIGW)
- Fluxos de Trabalho de Transferência de Arquivos Gerenciados (MFTW - Managed File Transfer Workflows): mecanismo serverless de fluxo de trabalho de arquivos:
    - Pode ser usado quando arquivos são enviados; podemos definir fluxos de trabalho para determinar o que acontece com o arquivo assim que o upload é realizado

## Tipos de Endpoint do Transfer Family (Transfer Family Endpoint Types)

- Dentro do Transfer Family, criamos servidores que podemos imaginar como os pontos de acesso (access points) de front-end para o nosso armazenamento
- Eles expõem o S3 e o EFS por meio de um ou mais dos protocolos suportados
- A forma como acessamos esses servidores depende de como configuramos os endpoints do serviço:
    - Público (Public): executado na zona pública da AWS, acessível pela internet pública
        - Sem necessidade de configurar componentes de rede
        - O único protocolo suportado é o SFTP
        - O endpoint possui um IP dinâmico que pode mudar; devemos usar o DNS para acessá-lo
        - Não podemos controlar quem irá acessá-lo usando recursos como NACLs ou security groups
    - VPC - Acesso à Internet (VPC - Internet Access)
        - Executado dentro de uma VPC
        - Podemos usar os protocolos SFTP/FTPS e AS2
        - Qualquer recurso com conectividade à VPC (DX/VPN) pode acessá-lo como se estivesse rodando dentro da VPC
        - O Transfer Family fornece um IP estático para ele
        - SG/NACLs são suportados
        - É alocado um Elastic IP estático para ele, o que permite que seja acessado através da internet pública
    - VPC - Interno (VPC - Internal)
        - Executado dentro de uma VPC
        - Podemos usar os protocolos SFTP/FTPS/FTP e AS2
        - Qualquer recurso com conectividade à VPC (DX/VPN) pode acessá-lo como se estivesse rodando dentro da VPC
        - O Transfer Family fornece um IP estático para ele
        - SG/NACLs são suportados

## Outros Recursos (Other Features)

- Ele é multi-AZ => resiliente e escalável
- O custo é baseado por servidor provisionado por hora + transferência de dados
- Com FTP/FTPS, apenas o Directory Service e IDPs customizados são suportados
- O FTP só pode ser usado internamente dentro de uma VPC
- O AS2 deve ser exclusivamente do tipo VPC Internet/Internal; não podemos usar o tipo de endpoint público
- Casos de uso do Transfer Family:
    - Quando precisamos de acesso ao S3/EFS, mas utilizando os protocolos suportados
    - Integração com fluxos de trabalho existentes
    - Uso de MFTW para criar novos fluxos de trabalho

---

# AWS Transfer Family

- Is a product which provides managed file transfer service
- It allows us to transfer files to/from S3 or EFS
- It provides managed servers which provides various protocols. Allows us to upload/download data to S3 or EFS using protocols different the ones natively supported by S3 of EFS
- Allow us to interact with both of these services using the following protocols:
    - FTP (File Transfer Protocol): unencrypted file transfer protocol
    - FTPS (File Transfer Protocol Secure): file transfer protocol with TLS encryption
    - SFTP (SSH File Transfer Protocol): file transfer over SSH
    - Applicable Statement 2 (AS2): transfer structured B2B data
- Transfer Family supports a wide range of identities: service managed, Directory Service, custom (Lambda/APIGW)
- Managed File Transfer Workflows (MFTW): serverless file workflow engine:
    - Can be used when file are uploaded, we can define workflows as to what happened to the file as it gets uploaded

## Transfer Family Endpoint Types

- Within Transfer Family we create servers which we can think of as the front-end accesspoint to our storage
- They present S3 and EFS via one or more supported protocol
- How we access these servers depends on how configure the service's endpoints:
    - Public: runs on the AWS public zone, accessible to the public internet
        - No networking components to configure
        - Only supported protocol is SFTP
        - The endpoint has a dynamic IP which can change, we should use DNS to access it
        - We can't control who will access it using features such as NACLs or security groups
    - VPC - Internet Access
        - Runs in a VPC
        - We can use SFTP/FTPS and AS2 protocols
        - Anything that has connectivity to the VPC (DX/VPN) can access it as it was running inside the VPC
        - Transfer Family provides a static IP for it
        - SG/NACLs are supported
        - It is allocated an Elastic IP for it which is static, which allows it to be accessed over the public internet
    - VPC - Internal
        - Runs inside a VPC
        - We can use SFTP/FTPS/FTP and AS2 protocols
        - Anything that has connectivity to the VPC (DX/VPN) can access it as it was running inside the VPC
        - Transfer Family provides a static IP for it
        - SG/NACLs are supported

## Other Features

- It is multi-AZ => resilient and scalable
- Cost is based for provisioned server per hour + data transfer
- With FTP/FTPS only Directory Service and Custom IDP is supported
- FTP can only be used internally within a VPC
- AS2 has to be VPC Internet/Internal only, we cannot use the public endpoint type
- Use cases for Transfer Family:
    - In case we need access to S3/EFS but using the supported protocols
    - Integration with existing workflows
    - Using MFTW to create new workflows