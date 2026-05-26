# AWS Control Tower

- O trabalho do Control Tower é permitir configuração rápida e fácil de um ambiente multi-conta
- O Control Tower orquestra outros serviços AWS para fornecer esta funcionalidade
- Usa Organizações, Centro de Identidade IAM, CloudFormation, AWS Config e muito mais
- É essencialmente uma evolução das Organizações AWS adicionando mais recursos, inteligência e automação

## Recursos do Control Tower

- **Landing Zones**: é o ambiente multi-conta
    - Fornece via outros serviços AWS:
        - SSO/Federação de ID
        - Logging e auditoria centralizada
- **Guard Rails**: usado para detectar/obrigar regras e padrões em todas as contas
- **Account Factory**: automatiza e padroniza a criação de novas contas
- **Dashboard**: visão única de todo o ambiente
- Quando o Control Tower é configurado, ele cria OUs:
    - OU Fundamental (segurança)
    - OU Customizado (sandbox)
- Dentro da OU Fundamental, o Control Tower cria duas contas:
    - Conta de Auditoria: para usuários que precisam acessar informações de auditoria fornecidas pelo Control Tower
    - Conta de Arquivo de Log: para usuários que precisam acessar todas as informações de log de todas as contas inscritas dentro da Landing Zones
- Dentro da OU Customizada, Account Factory provisionam contas AWS de forma automatizada
- Para estas novas contas temos modelos de base para configurações:
    - Modelo de Baseline de Conta
    - Modelo de Baseline de Rede (cookie cutter)
- O Control Tower utiliza CloudFormation sob o capó para implementar toda esta automação
- Também usa AWS Config e SCPs para implementar Account Guard Rails

## Landing Zones

- É um recurso projetado para que qualquer pessoa possa implementar um ambiente multi-conta *bem arquitetado*
- Home Region: a região onde inicialmente implantamos o produto
- Uma Landing Zone cria as OUs de Segurança e Sandbox, podemos criar outras OUs e contas também
- Landing Zones utiliza o Centro de Identidade IAM para múltiplas contas e Federação de ID
- Uma Landing Zone fornece monitoramento e notificações via CloudWatch e SNS
- Podemos permitir que usuários finais provém novas contas de uma Landing Zone usando Service Catalog

## Guardrails

- São regras para governança multi-conta
- Existem 3 tipos diferentes de regras:
    - Obrigatória
    - Fortemente Recomendada
    - Eletiva
- Os Guardrails funcionam de duas maneiras diferentes:
    - Preventiva: nos impede de fazer coisas
        - São implementadas usando SCPs
        - São aplicadas ou não habilitadas
        - Exemplo: permitir ou negar regiões; desabilitar mudanças de política de bucket na Org
    - Detetiva: verificação de conformidade
        - Usa Regras AWS Config para detectar violações de conformidade
        - Estes tipos de Guardrails são *limpos*, *em violação* ou *não habilitados*
        - Exemplo: verificar se CloudTrail está habilitado; verificar se instâncias EC2 tém IPv4 público anexado

## Account Factory

- Permite provisionamento automatizado de contas
- Isto pode ser feito por administradores em nuvem ou usuários finais (com permissões apropriadas)
- Os Guardrails são aplicados automaticamente às contas provisionadas
- O administrador da conta pode ser dado a um usuário nomeado que provisiona a conta ou a outro usuário
- As contas podem ser configuradas com configurações de conta e rede padrão
- Pode ser totalmente integrado com um SDLC de negócios

---

# AWS Control Tower

- Control Tower's job is to allow quick and easy setup of a multi-account environment
- Control Tower orchestrates other AWS services to provide this functionality
- It is using Organizations, IAM Identity Center, CloudFormation, AWS Config and more
- It is essentially an evolution of AWS Organizations adding more features, intelligence and automation

## Control Tower Features

- **Landing Zones**: it is the multi-account environment
    - Provides via other AWS services:
        - SSO/ID Federation
        - Centralized logging and auditing
- **Guard Rails**: used to detect/mandate rules and standards across all accounts
- **Account Factory**: automates and standardizes new account creation
- **Dashboard**: single page oversight of the entire environment
- When Control Tower is set up, it creates to OUs:
    - Foundational OU (security)
    - Custom OU (sandbox)
- Inside the Foundational OU Control Tower creates two accounts:
    - Audit Account: for users who needs access to audit information provided by Control Tower
    - Log Archive Account: for users who need access to all log information to all enrolled accounts within the Landing Zones
- Within the Custom OU Account Factory will provision AWS accounts in an automated way
- For these new accounts we have bases templates for configurations:
    - Account Baseline template
    - Network Baseline template (cookie cutter)
- Control Tower utilizes CloudFormation under the hood to implement all of these automation
- It also uses both AWS Config and SCPs to implement account Guard Rails

## Landing Zones

- It is a feature designed that anyone should be able to implement a *well architected* multi-account environment
- Home Region: the region where we initially deploy the product
- A Landing Zone creates the Security and Sandbox OUs, we can create other OUs and accounts as well
- Landing Zones utilizes the IAM Identity Center for multiple-accounts and ID Federation
- A Landing Zone provides monitoring and notifications via CloudWatch and SNS
- We can allow end-users to provision new accounts from a Landing Zone using Service Catalog

## Guardrails

- They are rules for multi-account governance
- There are 3 different types of rules:
    - Mandatory
    - Strongly Recommended
    - Elective
- Guardrails function in two different ways:
    - Preventive: stop us from doing things
        - They are implement using SCPs
        - They are enforced or not enabled
        - Example: allow or deny regions; disallow bucket policy changes in the Org
    - Detective: compliance check
        - Uses AWS Config Rules to detect compliance violations
        - These types of Guardrails are either *clear*, *in violation* or *not enabled*
        - Example: check if CloudTrail is enabled; check if EC2 instances have public IPv4 attached

## Account Factory

- Allows automated account provisioning
- This can be done by either cloud administrators or end users (with appropriate permissions)
- Guardrails are automatically applied to the provisioned accounts
- Account admin can be given to a named user who provisions the account or to another user
- Accounts can be configured with standard account and network configurations
- Can be fully integrated with a businessess SDLC