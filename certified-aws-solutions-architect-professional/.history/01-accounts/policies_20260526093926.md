# Políticas

- As políticas IAM definem permissões para uma ação independentemente do método que você usa para executar a operação

## Tipos de políticas

- **Políticas baseadas em identidade**: anexar políticas gerenciadas e inline às identidades IAM (usuários, grupos aos quais os usuários pertencem ou funções). As políticas baseadas em identidade concedem permissões a uma identidade
- **Políticas baseadas em recursos**: anexar políticas inline a recursos. Os exemplos mais comuns de políticas baseadas em recursos são políticas de bucket do Amazon S3 e políticas de confiança de função IAM. As políticas baseadas em recursos concedem permissões a uma entidade principal especificada na política. Os principais podem estar na mesma conta que o recurso ou em outras contas
- **Limites de permissão**: use uma política gerenciada como limite de permissão para uma entidade IAM (usuário ou função). Essa política define as permissões máximas que as políticas baseadas em identidade podem conceder a uma entidade, mas não concede permissões. Os limites de permissão não definem as permissões máximas que uma política baseada em recursos pode conceder a uma entidade
- **SCPs das Organizações**: use uma política de controle de serviço (SCP) das Organizações AWS para definir as permissões máximas para membros da conta de uma organização ou unidade organizacional (OU). SCPs limitam permissões que políticas baseadas em identidade ou políticas baseadas em recursos concedem a entidades (usuários ou funções) dentro da conta, mas não concedem permissões
- **Listas de controle de acesso (ACLs)**: use ACLs para controlar quais principais em outras contas podem acessar o recurso ao qual a ACL está anexada. As ACLs são semelhantes às políticas baseadas em recursos, embora sejam o único tipo de política que não usa a estrutura de documento de política JSON. As ACLs são políticas de permissões entre contas que concedem permissões à entidade principal especificada. As ACLs não podem conceder permissões a entidades dentro da mesma conta
- **Políticas de sessão**: passar políticas avançadas de sessão quando você usa a AWS CLI ou API AWS para assumir uma função ou um usuário federado. As políticas de sessão limitam as permissões que a função ou as políticas baseadas em identidade do usuário concedem à sessão. As políticas de sessão limitam permissões para uma sessão criada, mas não concedem permissões. Para mais informações, consulte Políticas de Sessão

## Aprofundamento em Políticas

- Anatomia de uma política: documento JSON com `Effect`, `Action`, `NotAction` (condição inversa de `Action`), `Resource`, `Conditions` e `Policy Variables`
- Ordem de prioridade de permissões na AWS é: negar (explícito) > permitir > negar (implícito). Uma política sempre assume uma negacão padrão (implícita) => se não permitirmos explicitamente fazer algo, não seremos capazes de fazé-lo
- Uma `NEGACÃO` explícita sempre tem precedência sobre `PERMITIR`
- Melhor prática: use o menor privilégio para máxima segurança
    - Access Advisor: uma ferramenta para ver permissões concedidas e quando foram última vez acessadas
    - Access Analyzer: usado para analisar recursos compartilhados com entidades externas
- Políticas Gerenciadas Comuns:
    - `AdministratorAccess`
    - `PowerUserAccess`: não permite nada relacionado a IAM, organizações e conta (com algumas exceções), caso contrário semelhante ao acesso do administrador
- Condição de política IAM:

    ```
    "Condition": {
        "{condition-operator}": {
            "{condition-key}": "{condition-value}"
        }
    }
    ```

- Operadores:
    - String: `StringEquals`, `StringNotEquals`, `StringLike`, etc.
    - Numérico: `NumericEquals`, `NumericNotEquals`, `NumericLessThan`, etc.
    - Data: `DateEquals`, `DateNotEquals`, `DateLessThan`, etc.
    - Booleano
    - IpAddress/NotIpAddress:
        - `"Condition": {"IpAddress": {"aws:SourceIp": "192.168.0.1/16"}}`
    - ArnEquals/ArnLike
    - Null
        - `"Condition": {"Null": {"aws:TokenIssueTime": "192.168.0.1/16"}}`
- Variáveis de Política e Tags:
    - `${aws:username}`: exemplo `"Resource:["arn:aws:s3:::mybucket/${aws:username}/*"]`
    - Específico da AWS:
        - `aws:CurrentTime`
        - `aws:TokenIssueTime`
        - `aws:PrincipalType`: indica se o principal é uma conta, usuário, federado ou função assumida
        - `aws:SecureTransport`
        - `aws:SourceIp`
        - `aws:UserId`
    - Específicos do Serviço:
        - `ec2:SourceInstanceARN`
        - `s3:prefix`
        - `s3:max-keys`
        - `sns:EndPoint`
        - `sns:Protocol`
    - Baseados em Tags:
        - `iam:ResourceTag/key-name`
        - `iam:PrincipalTag/key-name`

## Limites de Permissão

- Apenas permissões de IDENTIDADE são impactadas por limites - qualquer política de recurso é aplicada integralmente
- Os limites de permissão podem ser aplicados a Usuários IAM e Funções IAM
- Os limites de permissão não concedem acesso a nenhuma ação. Eles definem permissões máximas que uma identidade pode receber
- Casos de uso para limites de permissão:
    - Problema de delegação: se dermos permissões elevadas a um usuário, ele/ela poderia se promover para ter permissões de administrador ou poderia criar outro usuário com permissões elevadas
    - A solução é ter um limite que proba mudanças das suas próprias permissões do usuário e proba criar outros usuários/funções com permissões elevadas

## Lógica de Avaliação de Política

- Componentes envolvidos nas avaliações de política:
    - SCPs da Organização
    - Políticas de Recursos
    - Limites de Identidade IAM
    - Políticas de Sessão
    - Políticas de Identidade
- Lógica de avaliação de política - mesma conta:
    ![lógica de avaliação de política - mesma conta](images/PolicyEvaluation1.png)
- Lógica de avaliação de política - conta diferente:
    ![lógica de avaliação de política - conta diferente](images/PolicyEvaluation2.png)

## Simulador de Políticas AWS

- Ao criar novas políticas customizadas você pode testá-las aqui:
  - https://policysim.aws.amazon.com/home/index.jsp
  - Esta ferramenta de política pode te economizar tempo em caso sua declaração de política customizada seja negada
- Alternativamente, você pode usar a CLI:
    - Alguns comandos da AWS CLI (nem todos) contém a opção `--dry-run` para simular chamadas de API. Isso pode ser usado para testar permissões.
    - Se o comando for bem-sucedido, você obterá a mensagem: `Request would have succeeded, but DryRun flag is set`
    - Caso contrário, você obterá a mensagem: `An error occurred (UnauthorizedOperation) when calling the {policy_name} operation`

---

# Policies

- IAM policies define permissions for an action regardless of the method that you use to perform the operation

## Policy types

- **Identity-based policies**: attach managed and inline policies to IAM identities (users, groups to which users belong, or roles). Identity-based policies grant permissions to an identity
- **Resource-based policies**: attach inline policies to resources. The most common examples of resource-based policies are Amazon S3 bucket policies and IAM role trust policies. Resource-based policies grant permissions to a principal entity that is specified in the policy. Principals can be in the same account as the resource or in other accounts
- **Permissions boundaries**: use a managed policy as the permissions boundary for an IAM entity (user or role). That policy defines the maximum permissions that the identity-based policies can grant to an entity, but does not grant permissions. Permissions boundaries do not define the maximum permissions that a resource-based policy can grant to an entity
- **Organizations SCPs**: use an AWS Organizations service control policy (SCP) to define the maximum permissions for account members of an organization or organizational unit (OU). SCPs limit permissions that identity-based policies or resource-based policies grant to entities (users or roles) within the account, but do not grant permissions
- **Access control lists (ACLs)**: use ACLs to control which principals in other accounts can access the resource to which the ACL is attached. ACLs are similar to resource-based policies, although they are the only policy type that does not use the JSON policy document structure. ACLs are cross-account permissions policies that grant permissions to the specified principal entity. ACLs cannot grant permissions to entities within the same account
- **Session policies**: pass advanced session policies when you use the AWS CLI or AWS API to assume a role or a federated user. Session policies limit the permissions that the role or user's identity-based policies grant to the session. Session policies limit permissions for a created session, but do not grant permissions. For more information, see Session Policies

## Policies Deep Dive

- Anatomy of a policy: JSON document with `Effect`, `Action`, `NotAction` (inverse condition of `Action`), `Resource`, `Conditions` and `Policy Variables`
- Priority order of permissions in AWS is: deny (explicit) > allow > deny (implicit). A policy always assumes a default (implicit) deny => if we do not allow explicitly to do something, we wont be able to do it
- An explicit `DENY` has always precedence over `ALLOW`
- Best practice: use least privilege for maximum security
    - Access Advisor: a tool for seeing permissions granted and when last accessed
    - Access Analyzer: used of analyze resources shared with external entities
- Common Managed Policies:
    - `AdministratorAccess`
    - `PowerUserAccess`: does not allow anything regarding to IAM, organizations and account (with some exceptions), otherwise similar to admin access
- IAM policy condition:

    ```
    "Condition": {
        "{condition-operator}": {
            "{condition-key}": "{condition-value}"
        }
    }
    ```

- Operators:
    - String: `StringEquals`, `StringNotEquals`, `StringLike`, etc.
    - Numeric: `NumericEquals`, `NumericNotEquals`, `NumericLessThan`, etc.
    - Date: `DateEquals`, `DateNotEquals`, `DateLessThan`, etc.
    - Boolean
    - IpAddress/NotIpAddress:
        - `"Condition": {"IpAddress": {"aws:SourceIp": "192.168.0.1/16"}}`
    - ArnEquals/ArnLike
    - Null
        - `"Condition": {"Null": {"aws:TokenIssueTime": "192.168.0.1/16"}}`
- Policy Variables and Tags:
    - `${aws:username}`: example `"Resource:["arn:aws:s3:::mybucket/${aws:username}/*"]`
    - AWS Specific:
        - `aws:CurrentTime`
        - `aws:TokenIssueTime`
        - `aws:PrincipalType`: indicates if the principal is an account, user, federated or assumed role
        - `aws:SecureTransport`
        - `aws:SourceIp`
        - `aws:UserId`
    - Service Specific:
        - `ec2:SourceInstanceARN`
        - `s3:prefix`
        - `s3:max-keys`
        - `sns:EndPoint`
        - `sns:Protocol`
    - Tag Based:
        - `iam:ResourceTag/key-name`
        - `iam:PrincipalTag/key-name`

## Permission Boundaries

- Only IDENTITY permissions are impacted by boundaries - any resource policies are applied full
- Permission boundaries can be applied to IAM Users and IAM Roles
- Permission boundaries don't grant access to any action. They define maximum permissions an identity can receive
- Use cases for permission boundaries:
    - Delegation problem: if we give elevated permissions to an user, he/she could promote itself to have administrator permissions or could create another user with administrator permissions
    - Solution is to have a boundary which forbids changing its onw user's permissions and forbid creating other users/roles with elevated permissions

## Policy Evaluation Logic

- Components involved in a policy evaluations:
    - Organization SCPs
    - Resource Policies
    - IAM Identity Boundaries
    - Session Policies
    - Identity Policies
- Policy evaluation logic - same account:
    ![policy evaluation logic - same account](images/PolicyEvaluation1.png)
- Policy evaluation logic - different account:
    ![policy evaluation logic - different account](images/PolicyEvaluation2.png)

## AWS Policy Simulator

- When creating new custom policies you can test it here:
  - https://policysim.aws.amazon.com/home/index.jsp
  - This policy tool can you save you time in case your custom policy statement's permission is denied
- Alternatively, you can use the CLI:
    - Some AWS CLI commands (not all) contain `--dry-run` option to simulate API calls. This can be used to test permissions.
    - If the command is successful, you'll get the message: `Request would have succeeded, but DryRun flag is set`
    - Otherwise, you'll be getting the message: `An error occurred (UnauthorizedOperation) when calling the {policy_name} operation`