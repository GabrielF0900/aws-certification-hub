# Amazon Cognito

- Fornece autenticação, autorização e gerenciamento de usuários para aplicações móvel/web
- Fornece 2 peças principais de funcionalidade:
    - **User Pools**: usado para sign-in, fornece um JSON Web Token (JWT) após autenticação
        - **User Pools não concedem acesso aos serviços AWS!**
        - User Pools fornecem gerenciamento de diretório de usuário e perfis de usuário, sign-up e sign-in com UI web customizável, MFA e outros recursos de segurança
        - Eles permitem social sign-in fornecido por Google, Apple, Facebook, bem como sign-in usando outros tipos de identidade, como provedores de identidade SAML
    - **Identity Pools**: o objetivo do identity pool é trocar um tipo de identidade externa por credenciais AWS temporárias, que podem ser usadas para acessar recursos AWS
        - Identidades Não Autenticadas: pools de identidade podem fornecer acesso aos serviços AWS para usuários convidados (usuários não autenticados)
        - Identidades Federadas: autorizar usuários a acessar temporariamente recursos AWS após autenticar com Google, Facebook, Twitter, SAML 2.0 e até Cognito User Pools

## Conceitos de Cognito

![Conceitos de Cognito](images/CognitoConcepts.png)

---

# Amazon Cognito

- Provides authentication, authorization and user management for mobile/web applications
- Provides 2 main pieces of functionality:
    - **User Pools**: used for sign-in, provides a JSON Web Token (JWT) after authentication
        - **User Pools do not grant access to AWS services!**
        - User Pools provide user directory management and user profiles, sign-up and sing-in with customizable web UI, MFA and other security features
        - They allow social sign-in provided by Google, Apple, Facebook as well as sign in using other identity types such as SAML identity providers
    - **Identity Pools**: the aim of identity pool is to exchange a type of external identity for temporary AWS credentials, which can be used to access AWS resources
        - Unauthenticated Identities: identity pools can provides access to AWS services for guest users (unauthenticated users)
        - Federated Identities: authorize users to temporarily access AWS resources after they authenticated with Google, Facebook, Twitter, SAML 2.0 and event Cognito User Pools

## Cognito concepts

![Cognito Concepts](images/CognitoConcepts.png)
