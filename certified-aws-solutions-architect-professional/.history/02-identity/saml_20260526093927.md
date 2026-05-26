# Federação de Identidade SAML 2.0

- A federação permite que usuários fora da AWS assumam uma função temporária para acessar recursos AWS
- Estes usuários assumem a função de acesso do provedor de identidade
- SAML 2.0 - Linguagem de Marcação de Asserção de Segurança
- SAML 2.0 permite usar **indiretamente** identidades on-premise com AWS (console e CLI)
- A federação baseada em identidade SAML 2.0 é usada quando temos um provedor de identidade baseado em empresa que é compatível com SAML 2.0
- A federação baseada em SAML 2.0 é ideal quando temos uma equipe de gerenciamento de identidade existente gerenciando acesso a outros serviços, incluindo AWS
- Se queremos manter uma única fonte da verdade e/ou temos mais de 5000 usuários, recomenda-se usar federação baseada em SAML 2.0
- A federação usa funções IAM e Credenciais Temporárias AWS (validade de 12 horas)

## Processo de Autenticação de Federação de Identidade SAML 2.0 - Acesso à API

![SAML 2.0 API da Federação](images/SAML2.0FederationAPI.png)

## Processo de Autenticação de Federação de Identidade SAML 2.0 - Acesso ao Console AWS

![SAML 2.0 Console da Federação](images/SAML2.0FederationConsole.png)

## Federação SAML 2.0

- Precisamos configurar confiança entre IAM AWS e SAML (ambos os sentidos)
- SAML 2.0 habilitou SSO baseado em web entre domínios
- Usa a API STS: `AssumeRoleWithSAML`
- É a forma antiga de fazer federação, a forma recomendada pela AWS é usar **Amazon Single Sign On (SSO)**

---

# SAML 2.0 Identity Federation

- Federation lets user outside of AWS to assume a temporary role for access AWS resources
- These users assume identity provider access role
- SAML 2.0 - Security Assertion Markup Language
- SAML 2.0 allows to **indirectly** use on-premise identities with AWS (console and CLI)
- SAML 2.0 based identity federation is used when we have and enterprise based identity provider which is SAML 2.0 compatible
- SAML 2.0 based federation is ideal when we have an existing identity management team managing access to other services including AWS
- If we are looking to maintain a single source of truth and/or we have more than 5000 users, SAML 2.0 based federation is recommended to be used
- Federation is using IAM Roles and AWS Temporary Credentials (12 hours validity)

## SAML 2.0 Identity Federation Authentication Process - API Access

![SAML 2.0 Federation API](images/SAML2.0FederationAPI.png)

## SAML 2.0 Identity Federation Authentication Process - AWS Console Access

![SAML 2.0 Federation Console](images/SAML2.0FederationConsole.png)

## SAML 2.0 Federation

- We need to setup trust between AWS IAM and SAML (both ways)
- SAML 2.0 enabled web based, cross domain SSO
- Uses the STS API: `AssumeRoleWithSAML`
- It is the old way of doing federation, recommended way by AWS is to use **Amazon Single Sign On (SSO)**