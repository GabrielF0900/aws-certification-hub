# Amazon Macie

- É um serviço de segurança e privacidade de dados
- O Macie é um serviço para descobrir, monitorar e proteger dados armazenados em buckets do S3
- Uma vez ativado e direcionado aos buckets, o Macie descobrirá automaticamente os dados e os categorizará como PII (Informações de Identificação Pessoal), PHI (Informações de Saúde Protegidas), Financeiro, etc.
- O Macie usa identificadores de dados. Existem 2 tipos de identificadores de dados:
    - Identificador de Dados Gerenciado (Managed Data Identifier): integrado, pode usar machine learning e correspondência de padrões para analisar e descobrir dados. Foi projetado para detectar dados sensíveis de vários países
    - Identificador de Dados Personalizado (Custom Data Identifier): criado pelos clientes, é proprietário da conta e baseado em expressões regulares (regex)
- Trabalhos de Descoberta (Discovery Jobs): esses trabalhos usarão identificadores de dados para gerenciar e buscar conteúdo sensível. Eles gerarão descobertas (findings) que podem ser usadas para integração com outros serviços da AWS (ex: Security Hub, de onde as descobertas podem ser passadas para o EventBridge) a fim de realizar a remediação automática
- O Macie usa uma arquitetura de múltiplas contas: uma conta é a conta administradora, que pode ser usada para gerenciar o Macie dentro das contas membros para descobrir dados sensíveis
- Essa estrutura de múltiplas contas pode ser feita com o AWS Organizations ou convidando explicitamente as contas no Macie

## Identificadores do Macie (Macie Identifiers)

- Trabalhos de Descoberta de Dados (Data Discovery Jobs): analisam os dados para determinar se os objetos contêm dados sensíveis. Isso é feito usando identificadores de dados
- **Identificadores de Dados Gerenciados (Managed Data Identifiers)**:
    - Criados e gerenciados pela AWS
    - Podem ser usados para detectar uma lista crescente de tipos comuns de dados sensíveis: credenciais, dados financeiros, dados de saúde, identificadores pessoais (endereços, passaportes, etc.)
- **Identificadores de Dados Personalizados (Custom Data Identifiers)**:
    - Podem ser criados por nós, usuários/proprietários da conta AWS
    - Eles usam padrões regex para corresponder aos dados
    - Podemos adicionar palavras-chave opcionais: sequências opcionais que precisam estar próximas à correspondência do regex
    - Distância Máxima de Correspondência (Maximum Match Distance): quão próximas as palavras-chave devem estar do padrão regex
    - Também podemos incluir palavras a serem ignoradas (ignore words)

## Descobertas do Macie (Macie Findings)

- O Macie produzirá 2 tipos de descobertas (findings):
    - **Descobertas de Política (Policy Findings)**: são geradas quando as políticas ou configurações são alteradas de uma forma que reduz a segurança do bucket após o Macie ser ativado
    - **Descobertas de Dados Sensíveis (Sensitive Data Findings)**: geradas quando dados sensíveis são identificados com base nos identificadores
- Tipos de descobertas de política:
    - `Policy:IAMUser/S3BlockPublicAccessDisabled`: todas as configurações de bloqueio de acesso público no nível do bucket foram desativadas para o bucket
    - `Policy:IAMUser/S3BucketEncryptionDisabled`: as configurações de criptografia padrão do bucket foram redefinidas para o comportamento de criptografia padrão do Amazon S3, que é criptografar novos objetos automaticamente com uma chave gerenciada pelo Amazon S3
    - `Policy:IAMUser/S3BucketPublic`: uma ACL ou política de bucket foi alterada para permitir o acesso de usuários anônimos ou de todas as identidades autenticadas do AWS Identity and Access Management (IAM)
    - `Policy:IAMUser/S3BucketSharedExternally`: uma ACL ou política de bucket foi alterada para permitir que o bucket seja compartilhado com uma conta AWS externa à sua organização (que não faz parte dela)
- Tipos de descobertas de dados sensíveis:
    - `SensitiveData:S3Object/Credentials`: o objeto contém dados de credenciais sensíveis, como chaves de acesso secretas da AWS ou chaves privadas
    - `SensitiveData:S3Object/CustomIdentifier`: o objeto contém texto que corresponde aos critérios de detecção de um ou mais identificadores de dados personalizados
    - `SensitiveData:S3Object/Financial`: o objeto contém informações financeiras sensíveis, como números de contas bancárias ou números de cartões de crédito
    - `SensitiveData:S3Object/Multiple`: o objeto contém mais de uma categoria de dados sensíveis
    - `SensitiveData:S3Object/Personal`: o objeto contém informações pessoais sensíveis — informações de identificação pessoal (PII), como números de passaporte ou números de carteira de motorista; informações de saúde pessoais (PHI), como seguro saúde ou números de identificação médica; ou uma combinação de PII e PHI

---

# Amazon Macie

- It is a data security and data privacy service
- Macie is a service to discover, monitor and protect data stored in S3 buckets
- Once enabled and pointed to buckets, Macie will automatically discover data and categorize it as PII, PHI, Finance etc.
- Macie is using data identifier. There are 2 types of data identifier:
    - Managed Data Identifier: built-in, can use machine learning, pattern matching to analyze and discover data. It is designed to detect sensitive data from many countries
    - Custom Data Identifier: created by clients, they are proprietary to accounts and they are regex based
- Discovery Jobs: these jobs will use data identifiers to manage and search for sensitive content. They will generate findings which can be used for integration with other AWS services (ex: Security Hub from where findings can be passed to Event Bridge) in order to do automatic remediation
- Macie uses multi account architecture: one account is the administrator account which can used to manage Macie within the member accounts to discover sensitive data
- This multi-account structure can be done with AWS Organizations or by explicitly inviting accounts in Macie

## Macie Identifiers

- Data Discovery Jobs: analyzes data in order to determine wether the objects contain sensitive data. This is done using data identifiers
- **Managed Data Identifiers**:
    - Created and managed by AWS
    - Can be used to detect a growing list of common sensitive data types: credentials, financial data, health data, personal identifiers (addresses, passports, etc.)
- **Custom Data Identifiers**:
    - Can be created by us, AWS account users/owners
    - They are using regex patterns to match data
    - We can add optional keywords: optional sequences that need to be in the proximity to regex match
    - Maximum Match Distance: how close keywords are to regex pattern
    - We can also include ignore words

## Macie Findings

- Macie will produce 2 types of findings:
    - **Policy Findings**: are generated when the policies or settings are changed in a way that reduces the security of the bucket after Macie is enabled
    - **Sensitive Data Findings**: generated when sensitive data is identified based on identifiers
- Types if policy findings:
    - `Policy:IAMUser/S3BlockPublicAccessDisabled`: all bucket-level block public access settings were disabled for the bucket
    - `Policy:IAMUser/S3BucketEncryptionDisabled`: default encryption settings for the bucket were reset to default Amazon S3 encryption behavior, which is to encrypt new objects automatically with an Amazon S3 managed key
    - `Policy:IAMUser/S3BucketPublic`: an ACL or bucket policy for the bucket was changed to allow access by anonymous users or all authenticated AWS Identity and Access Management (IAM) identities
    - `Policy:IAMUser/S3BucketSharedExternally`: an ACL or bucket policy for the bucket was changed to allow the bucket to be shared with an AWS account that's external to (not part of) your organization
- Types of sensitive data findings:
    - `SensitiveData:S3Object/Credentials`: object contains sensitive credentials data, such as AWS secret access keys or private keys
    - `SensitiveData:S3Object/CustomIdentifier`: object contains text that matches the detection criteria of one or more custom data identifiers
    - `SensitiveData:S3Object/Financial`: object contains sensitive financial information, such as bank account numbers or credit card numbers
    - `SensitiveData:S3Object/Multiple`: object contains more than one category of sensitive data
    - `SensitiveData:S3Object/Personal`: object contains sensitive personal information—personally identifiable information (PII) such as passport numbers or driver's license identification numbers, personal health information (PHI) such as health insurance or medical identification numbers, or a combination of PII and PHI