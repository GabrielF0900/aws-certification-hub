# AWS Secrets Manager

- Ele compartilha funcionalidades com o SSM Parameter Store
- O Secrets Manager é projetado especificamente para segredos, por exemplo: senhas, Chaves de API (API Keys)
- Pode ser usado via Console, CLI, API ou SDKs
- Suporta a rotação automática de segredos usando funções Lambda
- Para certos serviços da AWS, o Secrets Manager oferece integração direta, como o RDS (sincronização automática quando os segredos são rotacionados)
- Os segredos são criptografados usando KMS

---

# AWS Secrets Manager

- It does share functionality with SSM Parameter Store
- Secrets Manager is designed specifically for secrets, example passwords, API Keys
- It is usable via Console, CLI, API or SDK's
- It supports the automatic rotation of secrets using a Lambda functions
- For certain AWS services, Secrets Manager offers direct integration, such as RDS (automatic synchronization when the secrets are rotated)
- Secrets are encrypted using KMS