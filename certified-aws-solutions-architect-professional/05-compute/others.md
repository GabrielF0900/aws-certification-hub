# Outros Produtos Relacionados à Computação

## AWS Outposts

- O AWS Outposts é um serviço totalmente gerenciado que estende a infraestrutura, serviços, APIs e ferramentas da AWS para as instalações do cliente
- Um Outpost é um conjunto de capacidade de computação e armazenamento da AWS implantado no site do cliente
- A AWS opera, monitora e gerencia essa capacidade como parte de uma Região AWS
- Podemos criar sub-redes no nosso Outpost e especificá-las ao criar recursos AWS como instâncias EC2, volumes EBS, clusters ECS e instâncias RDS
- As instâncias nas sub-redes do Outpost se comunicam com outras instâncias na Região AWS usando endereços IP privados, todos dentro da mesma VPC
- Nem todo serviço AWS é suportado dentro de um Outpost; para uma lista, veja: https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html#services

## AWS Wavelength

- O AWS Wavelength é como ter uma Zona de Disponibilidade na rede de "borda" de uma operadora de telefonia
- O Wavelength implanta serviços padrão de computação e armazenamento da AWS na borda das redes 5G das operadoras de telecomunicações
- Podemos estender uma nuvem privada virtual (VPC) para uma ou mais Zonas Wavelength
- Podemos então usar recursos AWS como instâncias do Amazon Elastic Compute Cloud (Amazon EC2) para executar aplicações que exigem baixa latência ou resiliência de borda dentro da Zona Wavelength
- Recursos AWS no Wavelength:
    - EC2 Auto Scaling
    - Clusters EKS
    - Clusters ECS
    - EC2 System Manager
    - CloudWatch, CloudTrail
    - CloudFormation
    - Application Load Balancers
- Os serviços no Wavelength fazem parte de uma VPC que está conectada por uma conexão confiável a uma região AWS

---

# Other Compute Related Products

## AWS Outposts

- AWS Outposts is a fully managed service that extends AWS infrastructure, services, APIs, and tools to customer premises
- An Outpost is a pool of AWS compute and storage capacity deployed at a customer site
- AWS operates, monitors, and manages this capacity as part of an AWS Region
- We can create subnets on our Outpost and specify them when we create AWS resources such as EC2 instances, EBS volumes, ECS clusters, and RDS instances
- Instances in Outpost subnets communicate with other instances in the AWS Region using private IP addresses, all within the same VPC
- Not every AWS service is supported within an Outpost, for a list see: https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html#services

## AWS Wavelength

- AWS Wavelength is just like having an Availability Zone in a phone carrier's 'edge' network
- Wavelength deploys standard AWS compute and storage services to the edge of telecommunication carriers' 5G networks
- We can extend a virtual private cloud (VPC) to one or more Wavelength Zones
- We can then use AWS resources such as Amazon Elastic Compute Cloud (Amazon EC2) instances to run the applications that require low latency or edge resiliency within the Wavelength Zone
- AWS resources on Wavelength:
    - EC2 Auto Scaling
    - EKS clusters
    - ECS clusters
    - EC2 System Manager
    - CloudWatch, CloudTrail
    - CloudFormation
    - Application Load Balancers
- The services in Wavelength are part of a VPC that is connected over a reliable connection to an AWS region