# EFS - Elastic File System

- É um sistema de arquivos baseado em rede que pode ser montado em instâncias baseadas em Linux
- Pode ser montado em múltiplas instâncias simultaneamente
- O EFS é uma implementação do formato de sistema de arquivos NFSv4
- Os sistemas de arquivos EFS podem ser montados em uma pasta em sistemas operacionais baseados em Linux
- O armazenamento do EFS existe separadamente do ciclo de vida de uma instância EC2
- Pode ser compartilhado entre muitas instâncias EC2
- É um serviço privado, podendo ser montado via alvos de montagem (mount targets) dentro de uma VPC. Por padrão, o EFS é isolado na VPC na qual foi provisionado
- O EFS pode ser acessado fora da VPC através de redes híbridas: VPN ou DX. O EFS é uma excelente ferramenta para o gerenciamento de armazenamento entre múltiplas unidades de computação
- O EFS é acessível por funções Lambda. O Lambda deve ser configurado para usar a rede da VPC para poder utilizar o EFS
- Alvos de montagem (Mount targets): fornecem endereços IP dentro do intervalo da VPC. Para Alta Disponibilidade (HA), devemos provisionar alvos de montagem em todas as zonas de disponibilidade presentes em uma VPC
- O EFS oferece 2 modos de desempenho:
    - Uso Geral (General Purpose): ideal para casos de uso sensíveis à latência (é o padrão)
    - Max I/O: pode ser usado para escalar para níveis mais altos de taxa de transferência (throughput) agregada. Possui latências mais altas
- O EFS oferece 2 modos diferentes de taxa de transferência (throughput):
    - Bursting (padrão): funciona de forma semelhante ao armazenamento EBS GP2
    - Provisionado (Provisioned): podemos especificar os requisitos de taxa de transferência independentemente do tamanho
- O EFS oferece 3 classes de armazenamento:
    - Standard: para dados que são acessados e modificados frequentemente
    - Acesso Infrequente (IA - Infrequent Access): classe de armazenamento otimizada para custos para dados que são acessados com menor frequência (poucas vezes por trimestre)
    - Archive: para dados que são acessados poucas vezes no ano
- Podemos mover dados automaticamente entre essas classes usando políticas de ciclo de vida (lifecycle policies)

---

# EFS - Elastic File System

- It is a network based file system which can be mounted on Linux based instance
- Can be mounted to multiple instances at once
- EFS it is an implementation of the NFSv4 file system format
- EFS file systems can be mounted in a folder in Linux based operating systems
- EFS storage exists separately from the lifecycle of an EC2 instance
- It can be shared between many EC2 instances
- It is a private service, it can be mounted via mount targets inside a VPC. By default an EFS it is isolated to the VPC in which was provisioned
- EFS can be accessed outside of the VPC over hybrid networking: VPN or DX. EFS is a great tool for storage handling across multiple units of compute
- EFS is accessible for Lambda functions. Lambda has to be configured to use VPC networking in order to use EFS
- Mount targets: provide IP addresses in the range of the VPC. For HA we should provision mount targets in every availability zones present in a VPC
- EFS offers 2 performance modes:
    - General Purpose: ideal for latency sensitive use cases (it is the default)
    - Max I/O: can be used to scale to higher levels of aggregate throughput. Has higher latencies
- EFS offers 2 different throughput modes:
    - Bursting (default): works similar to EBS GP2 storage
    - Provisioned: we can specify throughput requirements independent of the size
- EFS offers 3 storage classes:
    - Standard: for data that is accessed and modified frequently
    - Infrequent Access (IA): cost-optimized storage class for data that is less frequently accessed (few times a quarter)
    - Archive: for data that is accessed a few times a year
- We can automatically move data between these 2 classes using lifecycle policies