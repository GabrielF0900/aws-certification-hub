# AWS Certificate Manager - ACM

- O HTTPS (SSL/TSL) foi projetado para resolver problemas de segurança que ocorriam com o HTTP
- O HTTPS fornece criptografia de dados em trânsito (in-transit) e certificados para provar a identidade
- O ACM pode funcionar como uma autoridade certificadora (Certificate Authority - CA) pública ou uma autoridade certificadora (CA) privada
- No caso de uma CA privada, as aplicações precisam ser configuradas para confiar na CA privada
- Com o ACM, podemos gerar ou importar certificados
- Se o ACM gerar o certificado, ele poderá renová-lo automaticamente. Se importado, o usuário é responsável pela renovação <span style="color: red;">EXAME</span>
- O ACM só pode implantar (deploy) certificados em serviços suportados (serviços na AWS que são integrados ao ACM)
- Nem todos os serviços são suportados. Os serviços integrados ao ACM são os seguintes: load balancers, CloudFront, Cognito, Elastic Beanstalk, App Runner, API Gateway, AWS Nitro Enclaves, OpenSearch, AWS Network Firewall. O EC2, por exemplo, não é suportado <span style="color: red;">EXAME</span>
- O ACM é um serviço regional
- Os certificados não podem sair da região em que foram gerados ou importados. Para usar um certificado num ALB em ap-southeast-2, o certificado precisa estar no ACM em ap-southeast-2 (o ACM é um serviço regional!!!) <span style="color: red;">EXAME</span>
- Para serviços globais como o CloudFront, os certificados devem ser armazenados em **us-east-1**!

---

# AWS Certificate Manager - ACM

- HTTPS (SSL/TSL) was designed to address security problems occurred with HTTP
- HTTPS provides data encryption in-transit and certificates to prove the identity
- ACM can function as a public certificate authority or a private certificate authority (CA)
- In case of a private CA applications need to be configured to trust the private CA
- With ACM we can generate or import certificates
- If ACM generates the certificate, it can renew it automatically. If imported, the user is responsible for renewal <span style="color: red;">EXAM</span>
- ACM can only deploy certificates to supported services (services in AWS which are integrated with ACM)
- Not all services all supported. Services which integrate with ACM are the following: load balancers, CloudFront, Cognito, Elastic Beanstalk, App Runner, API Gateway, AWS Nitro Enclaves, OpenSearch, AWS Network Firewall. EC2, for example, is not supported <span style="color: red;">EXAM</span>
- ACM is a regional service
- Certificates cannot leave the region they are generated or imported in, to use a certificate within an ALB in ap-southeast-2, the certificate needs to be in ACM in ap-southeast-2 (ACM is a regional service!!!) <span style="color: red;">EXAM</span>
- For global Services such as CloudFront, certificates should be stored in **us-east-1** !