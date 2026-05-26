# Organizações AWS

- Conta AWS Padrão: é uma conta que não está em uma Organização AWS
- Criamos uma Organização AWS a partir de uma conta AWS padrão
- A organização não é criada nesta conta, apenas usamos a conta para criar a organização. A conta padrão então se torna a **Conta de Gerenciamento** (costumava ser chamada de *Master Account*)
- Usando a Conta de Gerenciamento, podemos convidar outras contas para a organização
- Quando uma conta padrão ingressa em uma organização, ela muda para **Conta de Membro** dessa organização
- Organizações têm 1 Conta de Gerenciamento e 0 ou mais Contas de Membro
- Podemos criar uma estrutura de contas AWS em uma organização. Podemos agrupar contas por unidades de negócios, função ou estágio de desenvolvimento, etc.
- Esta estrutura é hierárquica, é uma árvore invertida
- No topo desta árvore está o contêiner raiz da organização (apenas um contêiner dentro da organização, NÃO confundir com o usuário raiz)
- Este contêiner raiz pode conter outros contêineres, estes contêineres são conhecidos como **Unidades Organizacionais (OU)**
- OUs podem conter contas (contas de Gerenciamento/Membro) ou outras OUs

## Faturamento Consolidado

- É um recurso importante das Organizações AWS
- O método de faturamento individual de cada conta da organização é removido, as contas de membro passam seu faturamento pela Conta de Gerenciamento (**Conta Pagadora**)
- Usando faturamento consolidado obtemos uma única fatura mensal. Isso cobre a Conta de Gerenciamento e todas as Contas de Membro da Organização
- Ao usar benefícios de reserva de organização e descontos são reunidos, significando que a organização pode se beneficiar como um todo dos gastos de cada conta AWS dentro da organização

## Melhores Práticas

- Ter uma única conta na qual os usuários podem fazer login e assumir funções IAM para acessar outras contas da organização
- A conta com todas as identidades pode ser a Conta de Gerenciamento ou pode ser outra Conta de Membro (*Login Account*)

## `OrganizationAccountAccessRole`

- Esta é uma função IAM usada para acessar a conta adicionada/criada recentemente em uma organização
- Esta função será criada automaticamente se criarmos a conta a partir de uma organização existente
- Esta função deve ser criada manualmente na conta de membro se a conta foi convidada para a organização

# Políticas de Controle de Serviço (SCP)

- São um recurso das Organizações AWS usado para restringir contas AWS
- São documentos JSON
- Podem ser anexadas à raiz da organização, a uma ou mais OUs ou a contas AWS individuais
- SCPs herdam através da árvore da organização
- A Conta de Gerenciamento é especial: mesmo que tenha SCPs anexadas (diretamente ou através de uma OU) não será afetada pela SCP
- SCPs são limites de permissão de conta:
    - Limitam o que a conta (incluindo o usuário raiz da conta) pode fazer
    - Nunca podemos restringir um usuário raiz de uma conta, mas podemos restringir a conta em si, portanto essas restrições se aplicarão ao usuário raiz também
- **SCPs não concedem nenhuma permissão!** Estas são apenas um limite para restringir o que é e não é permitido em uma conta
- SCPs podem ser usadas de duas maneiras:
    - Lista de negação (padrão): permitir por padrão e bloquear acesso a certos serviços
        - `FullAWSAccess`: política aplicada por padrão à organização e todas as OUs quando habilitamos SCPs. Esta política significa que por padrão nada é restringido
        - SCPs não concedem permissões, mas quando são habilitadas, há uma negação padrão para tudo. É por isso que a política `FullAWSAccess` é necessária
        - Regras de prioridade SCP:
            1. Negação Explícita
            2. Permitir
            3. Negação Padrão (implícita)
        - Benefícios das listas de negação é que conforme a AWS expande a lista de ofertas de serviços, novos serviços estarão disponíveis para contas (baixa sobrecarga administrativa)
    - Lista de permissão: bloquear por padrão e permitir certos serviços
        - Para implementar listas de permissão:
            1. Remover a política `FullAWSAccess`
            2. Adicionar quaisquer serviços que deveriam ser permitidos em uma nova política
        - Listas de permissão são mais seguras, mas exigem mais sobrecarga administrativa

---

# AWS Organizations

- Standard AWS account: it is an account which is not in an AWS Organization
- We create an AWS Organization from a standard AWS account
- The organization is not created in this account, we just use the account to create the organization. The standard account then becomes the **Management Account** (used to be called *Master Account*)
- Using the Management Account we can invite other accounts into the organization
- When a standard account joins an organization, it will change to **Member Account** of that organization
- Organizations have 1 Management Account and 0 or more Member Accounts
- We can create a structure of AWS accounts in an organization. We can group accounts by things such as business units, function or development stage, etc.
- This structure is hierarchical, it is an inverted tree
- At the top of this tree is the root container of the organization (just a container within the organization, NOT to be confused with the root user)
- This root container can contain other containers, this containers are known as **Organizational Units (OU)**
- OUs can contains accounts (Management/Member accounts) or other OUs

## Consolidated Billing

- It is an important feature of AWS Organizations
- The individual billing method of each account from the organization is removed, the member accounts pass their billing through the Management Account (**Payer Account**)
- Using consolidated billing we get a single monthly bill. This covers the Management Account and all the Member Accounts of the Organization
- When using organization reservation benefits and discounts are pooled, meaning the organization can benefit as a whole for the spending of each AWS account within the org

## Best Practices

- Have a single account into which users can log into and assume IAM roles in order to access other accounts from the org
- The account with all the identities may be the Management Account or it can be another Member Account (*Login Account*)

## `OrganizationAccountAccessRole`

- This is an IAM role used to access the newly added/created account in an organization
- This role will be created automatically if we create the account from an existing organization
- This role has to be created manually in the member account if the account was invited into the organization

# Service Control Policies (SCP)

- They are a feature of AWS Organizations used to restrict AWS accounts
- They are JSON documents
- They can be attached to the root of the organization, to one or more OUs or to individual AWS accounts
- SCPs inherit down through the organization tree
- The Management Account is special: even if it has SCPs attached (directly or through an OU) it wont be affected by the SCP
- SCPs are account permission boundaries:
    - They limit what the account (including the root user of the account) can do
    - We can never restrict a root user from an account, but we can restrict the account itself, hence these restrictions will apply to the root user as well
- **SCPs don't grant any permissions!** This are just a boundary to limit what is and is not allowed in an account
- SCPs can be used in two ways:
    - Deny list (default): allow by default and block access to certain services
        - `FullAWSAccess`: policy applied by default to the org an all OUs when we enable SCPs. This policy means tha by default nothing is restricted
        - SCPs don't grant permissions, but when they are enabled, there is a default deny for everything. This is why the `FullAWSAccess` policy is needed
        - SCP priority rules:
            1. Explicit Deny
            2. Allow
            3. Default (implicit) deny
        - Benefits of deny lists is that as AWS is extends the list of service offerings, new services will be available for accounts (low admin overhead)
    - Allow list: block by default and allow certain services
        - To implement allow lists:
            1. Remove the `FullAWSAccess` policy
            2. Add any services which should be allowed in a new policy
        - Allow lists are more secure, but they require more admin overhead