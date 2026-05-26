# Centro de Identidade IAM (Sucessor do AWS Single Sign-On - SSO)

- Uma forma de usar o repositório de identidade corporativa existente com AWS
- Permite gerenciar centralmente o acesso SSO a múltiplas contas AWS e aplicações comerciais externas também
- Substitui os casos de uso históricos fornecidos por SAML 2.0
- Armazenamento de Identidade Flexível: onde as identidades são armazenadas. Permite que identidades externas sejam trocadas por credenciais AWS
- O Centro de Identidade IAM suporta os seguintes tipos de armazenamentos de identidade:
    - Armazenamento de identidade integrado
    - Microsoft AD Gerenciado pela AWS
    - Microsoft AD on-premise (confiança bidirecional ou AD Connector)
    - Provedor de Identidade Externo - SAML 2.0
- O Centro de Identidade IAM é preferido pela AWS para qualquer federação de identidade "workforce" (empresa) sobre a federação de identidade baseada em SAML 2.0 tradicional

## Arquitetura do Centro de Identidade IAM

![Centro de Identidade IAM](images/AWSSSO.png)

- Um requisito do Centro de Identidade IAM é que devemos ter uma Organização AWS válida criada

---

# IAM Identity Center (Successor to AWS Single Sing-On - SSO)

- A way to use existing enterprise identity store with AWS
- Allows to centrally manage SSO access to multiple AWS accounts and external business applications as well
- Replaces the historical uses cases provided by SAML 2.0
- Flexible Identity store: where identities are stored. Allows for external identities to be swapped with AWS credentials
- IAM Identity Center supports the following type of identity stores:
    - Built-in identity store
    - AWS Managed Microsoft AD
    - On-premise Microsoft AD (Two way trust or AD Connector)
    - External Identity Provider - SAML 2.0
- IAM Identity Center is preferred by AWS for any "workforce" (enterprise) identity federation over the traditional SAML 2.0 based identity federation

## IAM Identity Center Architecture

![IAM Identity Center](images/AWSSSO.png)

- A requirement of IAM Identity Center is that we should have a valid AWS Organization created