# AWS Security Hub

- Fornece uma visão abrangente do nosso estado de segurança na AWS
- Ajuda-nos a avaliar nosso ambiente AWS em relação aos padrões e melhores práticas do setor de segurança
- O Security Hub coleta dados de segurança em contas da AWS, serviços da AWS e produtos de terceiros compatíveis e nos ajuda a analisar nossas tendências de segurança e identificar os problemas de segurança de maior prioridade
- O Security Hub precisa ser habilitado para ser usado. Existem duas maneiras de habilitar o AWS Security Hub: por integração com o AWS Organizations ou manualmente
- A Organização pode ter um administrador delegado para o Security Hub

## Configuração Central (Central Configuration)

- É um recurso que nos ajuda a configurar e gerenciar o Security Hub em várias contas e regiões da AWS
- Devemos integrar o Security Hub e o Organizations para usar a configuração central. Além disso, devemos designar uma Região de origem (home Region) para usar a configuração central. A home Region é a Região a partir da qual o administrador delegado configura a organização
- A conta do administrador delegado pode criar políticas de configuração do AWS Security Hub para configurar o Security Hub, padrões de segurança e controles de segurança em sua organização
- Configurações de política:
    - As políticas de configuração devem estar associadas para entrar em vigor
    - Uma conta ou OU (Unidade Organizacional) pode ser associada a apenas uma política de configuração
    - As políticas de configuração são completas: As políticas de configuração fornecem uma especificação completa de configurações
    - As políticas de configuração não podem ser revertidas: Não há opção de reverter uma política de configuração depois de associá-la a contas ou OUs
    - As políticas de configuração entram em vigor na sua home Region e em todas as Regiões vinculadas
    - Políticas de configuração são recursos: elas têm um ARN
- Tipos de políticas de configuração:
    - Política de configuração recomendada - fornecida pela AWS
    - Política de configuração personalizada

---

# AWS Security Hub

- Provides a comprehensive view of our security state in AWS
- Helps us assess our AWS environment against security industry standards and best practices
- Security Hub collects security data across AWS accounts, AWS services, and supported third-party products and helps us analyze our security trends and identify the highest priority security issues
- Security Hub needs to be enabled to be used. There are two ways to enable AWS Security Hub, by integrating with AWS Organizations or manually
- Organization can have a delegated administrator for the Security Hub

## Central Configuration

- It is a feature that helps us set up and manage Security Hub across multiple AWS accounts and regions
- We must integrate Security Hub and Organizations to use central configuration. Also, we must designate a home Region to use central configuration. The home Region is the Region from which the delegated administrator configures the organization
- The delegated administrator account can create AWS Security Hub configuration policies to configure Security Hub, security standards, and security controls in your organization
- Policy configurations:
    - Configuration policies must be associated to take effect
    - An account or OU can be associated with only one configuration policy
    - Configuration policies are complete: Configuration policies provide a complete specification of settings
    - Configuration policies can't be reverted: There's no option to revert a configuration policy after you associate it with accounts or OUs
    - Configuration policies take effect in your home Region and all linked Regions
    - Configuration policies are resources: they have an ARN
- Types of configuration polices:
    - Recommended configuration policy - provided by AWS
    - Custom configuration policy