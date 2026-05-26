# IAM: Gerenciamento de Identidade e Acesso

- Ao acessar AWS, a conta raiz **nunca** deve ser usada. Os usuários devem ser criados com as permissões apropriadas. IAM é central para AWS
- **Usuários**: Uma pessoa física
- **Grupos**: Funções (admin, devops) Equipes (engenharia, design) que contêm um grupo de usuários
- **Funções**: Uso interno dentro dos recursos AWS
    - **Funções de Conta Cruzada**: funções usadas para serem assumidas por outra conta AWS para ter acesso a alguns recursos em nossa conta
- **Políticas (documentos JSON)**: Define o que cada um dos anteriores pode e não pode fazer. **Nota**: IAM tem políticas gerenciadas predefinidas
    - Existem 3 tipos de políticas:
        - Gerenciada pela AWS
        - Gerenciada pelo Cliente
        - Políticas Inline
- **Políticas Baseadas em Recursos**: políticas anexadas aos serviços AWS como S3, SQS

## Funções IAM vs Políticas Baseadas em Recursos

- Quando assumimos uma função (usuário, aplicação ou serviço), abrimos mão de nossa permissão original e assumimos a permissão atribuída à função
- Ao usar uma política baseada em recurso, o principal não precisa abrir mão de nenhuma permissão
- Exemplo: usuário na conta A precisa verificar uma tabela DynamoDB na conta A e despejá-la em um bucket S3 na conta B. Neste caso, se assumirmos uma função na conta B, não seremos capazes de verificar a tabela na conta A
  
## Melhores práticas

- Um Usuário IAM por pessoa **APENAS**
- Uma Função IAM por Aplicação
- Credenciais IAM **NUNCA** devem ser compartilhadas
- Nunca escreva credenciais IAM em seu código. **NUNCA**
- Nunca use a conta RAIZ exceto para configuração inicial
- É melhor dar aos usuários o mínimo de permissões para realizar seu trabalho

---

# IAM: Identity and Access Management

- When accessing AWS, the root account should **never** be used. Users must be created with the proper permissions. IAM is central to AWS
- **Users**: A physical person
- **Groups**: Functions (admin, devops) Teams (engineering, design) which contain a group of users
- **Roles**: Internal usage within AWS resources
    - **Cross Account Roles**: roles used to assumed by another AWS account in order to have access to some resources in our account
- **Policies (JSON documents)**: Defines what each of the above can and cannot do. **Note**: IAM has predefined managed policies
    - There are 3 types of policies:
        - AWS Managed
        - Customer Managed
        - Inline Policies
- **Resource Based Policies**: policies attached to AWS services such as S3, SQS

## IAM Roles vs Resource Based Policies

- When we assume a role (user, application or service), we give up our original permission and take the permission assigned to the role
- When using a resource based policy, principal does not have to give up any permissions
- Example: user in account A needs to scan a DynamoDB table in account A and dump it in an S3 bucket in account B. In this case if we assume a role in account B, we wont be able to scan the table in account A
  
## Best practices

- One IAM User per person **ONLY**
- One IAM Role per Application
- IAM credentials should **NEVER** be shared
- Never write IAM credentials in your code. **EVER**
- Never use the ROOT account except for initial setup
- It's best to give users the minimal amount of permissions to perform their job