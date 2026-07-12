# CloudHSM

- Semelhante ao KMS, ele cria, gerencia e protege material criptográfico ou chaves
- O KMS é um serviço compartilhado. A AWS tem um certo nível de acesso ao produto, eles gerenciam o hardware e o software do sistema
- O KMS usa dispositivos HSM nos bastidores (behind the scene)
- O CloudHSM é um verdadeiro HSM (Módulo de Segurança de Hardware) de locatário único (single tenant) hospedado pela AWS <span style="background-color: Red"><-- LEMBRE-SE DISSO PARA O EXAME</span>
- A AWS provisiona o hardware para o CloudHSM, mas eles não têm acesso a ele. No caso de perda de acesso a um dispositivo HSM, não há uma maneira fácil de recuperar o acesso a ele
- O CloudHSM é totalmente compatível com FIPS 140-2 Nível 3 (KMS é compatível com Nível 2 em geral) <span style="background-color: Red"><-- LEMBRE-SE DISSO PARA O EXAME</span>
- O CloudHSM é acessado com APIs de padrões do setor (industry standards): bibliotecas PKCS#11, Java Cryptography Extensions (JCE), Microsoft CryptoNG (CNG). Não é tão integrado a outros serviços da AWS por design (em comparação, o KMS integra-se basicamente a todos os serviços) <span style="background-color: Red"><-- LEMBRE-SE DISSO PARA O EXAME</span>
- O KMS pode usar o CloudHSM como um **armazenamento de chaves personalizado (custom key store)**, integração do CloudHSM com o KMS

## Arquitetura CloudHSM

- Os dispositivos CloudHSM são implantados em uma VPC gerenciada pela AWS, na qual não temos visibilidade
- Eles são injetados em VPCs gerenciadas pelo cliente usando ENIs (Elastic Network Interfaces)
- Para HA (Alta Disponibilidade), precisamos implantar vários dispositivos HSM e configurá-los como um cluster
- Um cliente (client) precisa ser instalado nas instâncias EC2 para conseguir acessar os módulos HSM
- Embora a AWS provisione os dispositivos HSM, nós, como clientes, somos responsáveis pelo gerenciamento das chaves do cliente
- A AWS pode fornecer atualizações de software nos dispositivos HSM, mas elas não devem afetar a parte de armazenamento de criptografia

## Casos de Uso/Limitações do CloudHSM

- Não há integração nativa com os serviços da AWS (exceto o KMS), o que significa que o CloudHSM não pode ser usado para SSE do S3
- O CloudHSM pode ser usado para criptografia no lado do cliente (client-side encryption) antes de fazer upload de dados para o S3
- O CloudHSM pode ser usado para descarregar (offload) o processamento SSL/TLS de servidores web. É econômico e eficiente usar o CloudHSM.
- Bancos de dados Oracle no RDS podem realizar Transparent Data Encryption (TDE) usando o CloudHSM
- O CloudHSM pode ser usado para proteger chaves privadas para uma Autoridade Certificadora Emissora (Issuing Certificate Authority - CA)

---

# CloudHSM

- Similar to KSM, it creates, manages and secures cryptographic material or keys
- KMS is a shared service. AWS has a certain level of access to the product, they manage the hardware and the software of the system
- KMS uses behind the scene HSM devices
- CloudHSM is true single tenant HSM(Hardware Security Module) hosted by AWS <span style="background-color: Red"><-- REMEMBER THIS FOR EXAM</span>
- AWS provisions the hardware for CloudHSM but they do not have access to it. In case of losing access to a HSM device there is no easy way to re-gain the access to it
- CloudHSM is fully compliant with FIPS 140-2 Level 3 (KMS is L2 compliant overall) <span style="background-color: Red"><-- REMEMBER THIS FOR EXAM</span>
- CloudHSM is accessed with industry standards APIs: PKCS#11, Java Cryptography Extensions (JCE), Microsoft CryptoNG (CNG) libraries. It is not that integrated with other AWS services by design (in comparison, KMS integrates with basically every service) <span style="background-color: Red"><-- REMEMBER THIS FOR EXAM</span>
- KMS can use CloudHSM as a **custom key store**, CloudHSM integration with KMS

## CloudHSM Architecture

- CloudHSM devices are deployed into a VPC managed by AWS, on which we don't have visibility
- They are injected into customer managed VPCs using ENIs (Elastic Network Interfaces)
- For HA we need to deploy multiple HSM devices and configure them as a cluster
- A client needs to be installed on the EC2 instances in order to be able to access HSM modules
- While AWS do provision the HSM devices, we as customers are responsible for the management of the customer keys
- AWS can provide software updates on the HSM devices, but these should not affect the encryption storage part

## CloudHSM Use Cases/Limitations

- There is no native integration with AWS services (except KMS) , this means CloudHSM can not be used for S3 SSE
- CloudHSM can be used for client-side encryption before uploading data to S3
- CloudHSM can be used to offload SSL/TLS processing for web servers. It's economical and efficient to use cloud HSM.
- Oracle Databases from RDS can perform Transparent Data Encryption (TDE) using CloudHSM
- CloudHSM can be used to protect private keys for an Issuing Certificate Authority (CA)