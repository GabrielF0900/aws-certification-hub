# AWS Trusted Advisor

- Fornece orientação em tempo real para provisionar recursos de acordo com as melhores práticas da AWS
- É um produto de nível de conta; não requer a instalação de nenhum agente
- Fornece uma série de verificações e recomendações em 5 áreas principais:
    - Otimização de Custos e Recomendações
    - Desempenho
    - Segurança
    - Tolerância a Falhas
    - Limite de Serviço
- O Trusted Advisor não é um serviço gratuito, pelo menos se quisermos aproveitar ao máximo
- A versão gratuita está disponível se a conta tiver planos de suporte básico ou desenvolvedor
- A versão gratuita fornece 7 verificações básicas:
    - Permissões de bucket S3 (permissões de acesso aberto)
    - Grupos de Segurança - portas específicas sem restrição
    - Uso de IAM
    - MFA na Conta Raiz
    - Snapshots Públicos do EBS
    - Snapshots Públicos do RDS
    - 50 verificações de limite de serviço: verifica os 50 limites de serviço mais comuns e identifica aqueles onde estamos acima de 80% desse limite
- Qualquer coisa além dessas verificações básicas requer planos de suporte empresarial ou enterprise
- Com suporte empresarial e enterprise, obtemos mais 115 verificações
- Também obtemos acesso à API de Suporte da AWS
- A API de Suporte da AWS permite acesso programático às funções de suporte da AWS:
    - Podemos obter os nomes e identificadores das verificações que a AWS oferece
    - Podemos solicitar a execução de uma verificação do Trusted Advisor em contas e recursos
    - Permite obter resumos e informações detalhadas programaticamente
    - Permite solicitar atualização do Trusted Advisor
- A API de Suporte da AWS permite abrir tickets de suporte programaticamente e gerenciá-los
- Com suporte empresarial e enterprise, obtemos integração com o CloudWatch => podemos definir respostas orientadas a eventos para ações

## Planos de Suporte da AWS

- Suporte Básico:
    - Está incluído para clientes AWS e é gratuito
    - Para o Trusted Advisor com este plano de suporte, obtemos 7 verificações básicas (veja acima)
- Desenvolvedor:
    - Para o Trusted Advisor, obtemos as mesmas 7 verificações básicas (veja acima)
- Empresarial:
    - Obtemos o conjunto completo de verificações e recomendações
    - Obtemos acesso programático ao Trusted Advisor
- Enterprise:
    - Igual ao empresarial

## Bom Saber

- Podemos verificar se um bucket S3 é público, mas não podemos verificar se os objetos são públicos em um bucket. Para monitorar isso, poderíamos usar CloudWatch Events/S3 Events
- Limites de Serviço:
    - Os limites só podem ser monitorados no Trusted Advisor
    - Casos precisam ser criados manualmente no Centro de Suporte da AWS para aumentar os limites

---

# AWS Trusted Advisor

- Provides real time guidance to provision resources against AWS best practices
- It is an account level product, requires no agent to be installed
- Provides a number of checks and recommendations in 5 major areas:
    - Cost Optimization & Recommendations
    - Performance
    - Security
    - Fault Tolerance
    - Service Limit
- Trusted Advisor is not a free service, at least if we want to get out the most of it
- The free version is available if the account has basic or developer support plans
- The free version provides 7 basic core checks <span style="color: #ff5733;">(Remember them for EXAM)</span> :
    - S3 bucket permissions (open access permissions)
    - Security Groups - specific ports unrestricted
    - IAM use
    - MFA on Root Account
    - EBS Public Snapshots
    - RDS Public Snapshots
    - 50 service limit checks: checks the 50 most common service limits and identifies any where we are over 80% of that limit
- Anything beyond these basic checks requires business or enterprise support plans
- With business and enterprise support we get further 115 checks
- We also get access to the AWS Support API
- AWS Support API allows for programmatic access for AWS support functions:
    - We can get the names and identifiers for the checks AWS offers
    - We can request a Trusted Adviser check runs against accounts and resources
    - Allows to get summaries and detailed information programmatically
    - Allows request for Truster Advisor refresh
- AWS Support API allows to programmatically open support ticket, and manage them
- With business and enterprise support we get CloudWatch integration => we can define event driven responses to actions

## AWS Support Plans

- Basic Support:
    - Is included for AWS customers and it is free
    - For Trusted Advisor with this support plan we get 7 core checks (see them above)
- Developer:
    - For Trusted Advisor we get the same 7 base core checks (see them above)
- Business:
    - We ge the full set of checks and recommendation
    - We get programmatic access to Trusted Advisor
- Enterprise:
    - Same as business

## Good to Know

- We can check if an S3 bucket is made public, but we cannot check if objects are public in a bucket. Monitoring this we might use CloudWatch Events/S3 Events instead
- Service Limits:
    - Limits can only be monitored in Trusted Advisor
    - Cases have to be created manually in AWS Support Centre to increase limits