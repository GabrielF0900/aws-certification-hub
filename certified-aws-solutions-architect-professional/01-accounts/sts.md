# STS

- Permite assumir funções em contas diferentes ou na mesma conta
- Gera credenciais temporárias (`sts:AssumeRole*`)
- Credenciais temporárias são semelhantes à chave de acesso. Elas expiram e não pertencem diretamente à identidade que assume a função
- Credenciais temporárias geralmente fornecem acesso limitado
- Credenciais temporárias são solicitadas por outra identidade (AWS ou externa - federação de identidade)
- Credenciais temporárias incluem o seguinte:
    - `AccessKeyId`: ID único das credenciais
    - `Expiration`: data e hora da expiração da credencial
    - `SecretAccessKey`: usado para assinar as solicitações para AWS
    - `SessionToken`: token único que deve ser passado com todas as solicitações para AWS
- STS nos permite habilitar federação de identidade

## Assumir uma Função com STS

1. Definir uma função IAM dentro de uma conta ou conta cruzada
2. Definir quais principais podem acessar a função IAM
3. Usar o AWS STS (Secure Token Service) para recuperar a função IAM a que temos acesso (`AssumeRole` API)
4. Credenciais temporárias podem ser válidas de 15 minutos até horas

## Revogar Credenciais Temporárias da Função IAM

- **Política de confiança**: especifica quem pode assumir uma função
- Funções podem ser assumidas por muitas identidades
- Todos que assumem uma função recebem o mesmo conjunto de permissões
- Credenciais temporárias não podem ser canceladas, elas são válidas até expirem
- Credenciais temporárias podem durar mais tempo
- Em caso de vazamento de credenciais, se mudarmos as permissões da política, afetaremos todos os usuários legítimos - não é uma boa ideia para revogar acesso
- Solução: 
    - Revogar todas as sessões existentes aplicando uma política inline `AWSRevokeOlderSessions` à função. Isso será aplicado a todas as sessões existentes, as sessões criadas depois não serão afetadas
    - Não podemos revogar credenciais manualmente!

---

# STS

- Allows to assume roles across different accounts or same accounts
- Generates temporary credentials (`sts:AssumeRole*`)
- Temporary credentials are similar to access key. They expire and they don't directly belong to the identity which assumes the role
- Temporary credentials usually provide limited access
- Temporary credentials are requested by another identity (AWS or external - identity federation)
- Temporary credentials include the following:
    - `AccessKeyId`: unique ID of the credentials
    - `Expiration`: date and time of credential expiration
    - `SecretAccessKey`: used to sign the requests to AWS
    - `SessionToken`: unique token which must be passed with all the requests to AWS
- STS allows us to enable identity federation

## Assume a Role with STS

1. Define an IAM role within an account or cross-account
2. Define which principals can access the IAM role
3. Use the AWS STS (Secure Token Service) to retrieve the IAM role we have access to (`AssumeRole` API)
4. Temporary credentials can be valid from 15 minutes up to hours

## Revoke IAM Role Temporary Credentials

- **Trust policy**: specifies who can assume a role
- Roles can be assumed by many identities
- Everybody who assumes a role, gets the same set of permissions
- Temporary credentials can not be cancelled, they are valid until they expire
- Temporary credentials can last for longer time
- In case of a credential leak if we change the permissions for the policy, we will affect all legitimate users - not a good idea for revoking access
- Solution: 
    - Revoke all existing sessions, by applying an `AWSRevokeOlderSessions` inline policy to the role. This will apply to all existing sessions, sessions created afterwards will not be affected
    - We can not manually revoke credentials!

