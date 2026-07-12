# Gerenciamento de Faturamento e Custos da AWS

## Cost Explorer

- Rastreia e analisa seu uso da AWS. É gratuito para todas as contas
- Inclui um relatório padrão que ajuda a visualizar os custos e o uso associados aos nossos CINCO principais serviços AWS que geram custos, e fornece um detalhamento de todos os serviços na visualização em tabela
- Podemos visualizar dados dos últimos 12 meses, prever quanto provavelmente gastaremos nos próximos três meses e obter recomendações sobre quais Instâncias Reservadas comprar
- O Cost Explorer deve ser habilitado antes de poder ser usado. O proprietário da conta pode habilitá-lo

## Relatórios de Custo e Uso da AWS

- O relatório de Custo e Uso da AWS fornece informações sobre nosso uso de recursos AWS e os custos estimados para esse uso
- O relatório de Custo e Uso da AWS é um arquivo `.csv` ou uma coleção de arquivos `.csv` armazenados em um bucket S3. Qualquer pessoa com permissões para acessar o bucket S3 especificado pode ver os arquivos de relatório de faturamento
- Podemos usar o relatório de Custo e Uso para rastrear a utilização, as cobranças e as alocações de Instâncias Reservadas
- Para granularidade de tempo, podemos escolher uma das seguintes opções:
    - Por hora: se quisermos que os itens no relatório sejam agregados por hora
    - Diário: se quisermos que os itens no relatório sejam agregados por dia
    - Mensal: se quisermos que os itens no relatório sejam agregados por mês
- O relatório pode ser carregado automaticamente no AWS Redshift e/ou AWS QuickSight para análise

## AWS Budgets

- Nos permite definir orçamentos personalizados que nos alertarão quando nossos custos ou uso excederem ou for previsto exceder o valor orçado
- Com o Budgets, podemos visualizar as seguintes informações:
    - Quão perto nosso plano está do valor orçado ou dos limites do nível gratuito
    - Nosso uso até o momento, incluindo quanto usamos de nossas Instâncias Reservadas e Planos de Economia comprados
    - Nossas cobranças estimadas atuais da AWS e quanto nosso uso previsto incorrerá em cobranças até o final do mês
    - Quanto do nosso orçamento foi usado
- As informações do orçamento são atualizadas até três vezes ao dia
- Tipos de Orçamentos:
    - **Orçamentos de Custo**: planejar quanto queremos gastar em um serviço
    - **Orçamentos de Uso**: planejar quanto queremos usar de um ou mais serviços
    - **Orçamentos de Utilização de RI**: definir um limiar de utilização e receber alertas quando o uso de RI cair abaixo desse limiar
    - **Orçamentos de Cobertura de RI**: definir um limiar de cobertura e receber alertas quando o número de horas de instância cobertas por RIs cair abaixo desse limiar
- Os orçamentos podem ser rastreados diariamente, mensalmente, trimestralmente ou anualmente, e podemos personalizar as datas de início e término
- Os alertas de orçamento podem ser enviados por e-mail e/ou tópico Amazon SNS
- Os dois primeiros orçamentos criados são gratuitos

---

# AWS Billing and Cost Management

## Cost Explorer

- Tracks and analyzes your AWS usage. It is free for all accounts
- Includes a default report that helps visualize the costs and usage associated with our TOP FIVE cost-accruing AWS services, and gives you a detailed breakdown on all services in the table view
- We can view data for up to last 12 months, forecast how much we are likely to spend for the next tree months and get recommendations on what Reserved Instances to purchase
- Cost Explorer must be enabled before it can be used. The owner of the account can enable it

## AWS Cost and Usage Reports

-  AWS Cost and Usage report provides information about our usage of AWS resources and estimated costs for that usage
- The AWS Cost and Usage report is a `.csv` file or a collection of `.csv` files that is stored in an S3 bucket. Anyone who has permissions to access the specified S3 bucket can see the billing report files
- We can use the Cost and Usage report to track your Reserved Instance Utilization, charges, and allocations
- For time granularity, we can choose one of the following:
    - Hourly: if we want our items in the report to be aggregated by the hour
    - Daily: if we want our items in the report to be aggregated by the day
    - Monthly: if we want our items in the report to be aggregated by month
- Report can be automatically uploaded into AWS Redshift and/or AWS QuickSight for analysis

## AWS Budgets

- Allows us to set custom budgets that will alert us when our costs or usage exceed or are forecasted to exceed your budgeted amount
- With Budgets, we can view the following information:
    - How close our plan is to our budgeted amount or to the free tier limits
    - Our usage to date, including how much you have used of your Reserved Instances and purchased Savings Plans
    - Our current estimated charges from AWS and how much your predicted usage will incur in charges by the end of the month
    - How much of our budget has been used
- Budget information is updated up to three times a day
- Types of Budgets:
    - **Cost budgets**: plan how much we want to spend on a service
    - **Usage budgets**: plan how much we want to use one or more services
    - **RI utilization budgets**: define a utilization threshold and receive alerts when your RI usage falls below that threshold
    - **RI coverage budgets**: define a coverage threshold and receive alerts when the number of your instance hours that are covered by RIs fall below that threshold
- Budgets can be tracked at the daily, monthly, quarterly, or yearly level, and we can customize the start and end dates
- Budget alerts can be sent via email and/or Amazon SNS topic
- First two budgets created are free of charge