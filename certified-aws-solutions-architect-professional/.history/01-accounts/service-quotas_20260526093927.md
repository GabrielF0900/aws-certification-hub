# Cotas de Serviço AWS

- Define quanto de uma "coisa" podemos usar dentro de uma conta AWS
- Exemplo:
    - Número de instâncias EC2 em certos momentos por região
    - Número de usuários IAM por contas AWS
- Os serviços geralmente têm uma cota padrão por região
- Os serviços globais podem ter uma cota por conta em vez de por região
- A maioria das cotas de serviço pode ser aumentada conforme necessário
- Algumas cotas de serviço não podem ser alteradas, exemplo: número de usuários IAM por conta (5000)
- Quanto maior o aumento, mais tempo é necessário para que a solicitação de mudança seja aprovada
- Endpoint e cotas de serviço: [https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html)
- **Cotas de Serviço**: 
    - Do console podemos ir para a página *Service Quotas*, onde podemos criar dashboards para as cotas que queremos monitorar
    - Podemos solicitar mudanças de cotas deste serviço para certos serviços
    - *Modelo de solicitação de cota*: podemos predefinir a solicitação de valor de cota para novas contas em uma organização AWS
    - Podemos criar um Alarme CloudWatch baseado em uma cota de serviço particular
- Método legado para aumentar cotas: criar um ticket de suporte selecionando aumento de cota de serviço
- Também podemos solicitar aumento de cota de serviço a partir da CLI. API de referência: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/request-service-quota-increase.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/request-service-quota-increase.html)

---

# AWS Service Quotas

- Defines how much of a "thing" we can use inside of an AWS account
- Example:
    - Number of EC2 instances at a certain times per region
    - Number of IAM users per AWS accounts
- Services usually have a default per region quota
- Global services may have a per account quota instead per region
- Most services quotas can be increased as needed
- Some service quotes can not be changed, example: number of IAM users per account (5000)
- The higher the increase, the more time is needed to get the change-request approved
- Service endpoint and quotas: [https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html)
- **Service Quotas**: 
    - From the console we can go to *Service Quotas* page, where we can create dashboards for quotas we want to monitor
    - We can request quota changes from this service for certain services
    - *Quote request template*: we can predefine quota value request for new accounts in an AWS organization
    - We can create a CloudWatch Alarm based on a particular service quota
- Legacy method to increase quotas: create a support ticket selecting service quota increase
- We can request service quota increase from the CLI as well. Reference API: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/request-service-quota-increase.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/request-service-quota-increase.html)
