# CloudTrail

- É um produto que registra ações de API que afetam contas AWS (exemplo: parar instância EC2, excluir bucket S3)
- Registra chamadas/atividades de API como um Evento do CloudTrail; ações tomadas por usuário, função ou serviço
- O CloudTrail, por padrão, registra os últimos 90 dias no Histórico de Eventos. Está habilitado por padrão sem custo
- Trails: usados para personalizar o histórico do CloudTrail
- Os Trails podem ser de 3 tipos:
    - **Eventos de Gerenciamento**: fornecem informações sobre operações de gerenciamento realizadas em recursos em contas AWS (operação do plano de controle). Exemplo: criar uma instância EC2, encerrar uma instância EC2
    - **Eventos de Dados**: contêm informações sobre operações de recursos realizadas em um recurso ou nele, exemplo: objetos enviados para S3, função Lambda sendo invocada
    - **Eventos de Insights**: o CloudTrail Insights analisa nossos padrões normais de volume de chamadas de API e taxas de erros de API, também chamado de *linha de base*, e gera eventos de Insights quando o volume de chamadas ou as taxas de erro estão fora dos padrões normais
- Por padrão, o CloudTrail registra apenas eventos de gerenciamento
- O CloudTrail é um serviço regional, mas quando criamos um Trail, ele pode ser configurado para operar de duas maneiras:
    - Uma região: registrará apenas eventos da região na qual foi criado
    - Todas as regiões: coleção de trails de todas as regiões
- Um trail de uma região também pode ser configurado para registrar eventos de serviços globais
- A maioria dos serviços registra eventos na região onde o evento ocorreu, mas um pequeno número de serviços (IAM, STS, CloudFront) registra eventos globalmente (us-east-1). Para que um trail aceite eventos globais, ele deve ser um trail de todas as regiões (deve estar habilitado para o trail)
- O histórico de eventos padrão é limitado a 90 dias; com um trail, podemos ser muito mais flexíveis
- Um trail pode armazenar os eventos em buckets S3 definidos indefinidamente, e esses logs podem ser analisados por outras ferramentas (as entradas de log são armazenadas no formato JSON)
- O CloudTrail pode ser integrado com os Logs do CloudWatch, onde podemos usar Filtros de Métricas, por exemplo
- Trail Organizacional:
    - Um trail criado na conta de gerenciamento de uma organização armazenando todos os eventos em cada conta da organização
    - Caso criemos um trail a partir da conta de gerenciamento de uma organização, podemos habilitá-lo para trazer eventos de todas as contas da organização
- O CloudTrail não oferece registro em tempo real!
- Preços do CloudTrail:
    - Histórico de 90 dias habilitado por padrão em cada conta AWS é gratuito
    - Uma cópia dos eventos de gerenciamento é gratuita para cada região em uma conta AWS
    - Outros trails criados são cobrados

---

 # CloudTrail

- Is a product which logs API actions which affects AWS accounts (example: stop EC2 instance, delete S3 bucket)
- It logs API calls/activities as a CloudTrail Event, actions taken by user, role or service
- CloudTrail by default logs the last 90 days in Event History. It is enabled by default at no cost
- Trails: used to customize CloudTrail history
- Trails can be of 3 types:
    - **Management Events**: provide information about management operations performed on resources in AWS accounts (control plane operation). Example: create an EC2 instance, terminate an EC2 instance
    - **Data Events**: contain information about resource operations performed on or in a resource, example: objects uploaded to S3, Lambda function being invoked
    - **Insights Events**: CloudTrail Insights analyzes our normal patterns of API call volume and API error rates, also called the *baseline*, and generates Insights events when the call volume or error rates are outside normal patterns
- By default CloudTrail only logs management events
- CloudTrail is a regional service, but when we create a Trail, it can configured to operate in two ways:
    - One region: only will log events from the region in which it is created
    - All regions: collection of trails from all regions
- A one region trail can be configured to log global services events as well
- Most services log events in the region where the event occurred, but a small number of services (IAM, STS, CloudFront) log events globally (us-east-1). For a trail to accept global events, it has to be all region trail (has to be enabled for the trail)
- The default event history is limited to 90 days, with a trail we can be much more flexible
- A trail can store the events in a defined S3 buckets indefinitely, and these logs can be parsed by other tooling (log entries are stored in JSON format)
- CloudTrail can be integrated with CloudWatch Logs, where we can use Metric Filters for example
- Organizational Trail: 
    - A trail created in the management account of an organization storing all events across every account in the organization
    - In case we create a trail from the management account of an organization, we can enable it to bring events from all of the accounts from the organization
- CloudTrail does not offer real time logging!
- CloudTrail pricing:
    - 90 days history enabled by default in every AWS is free
    - One copy of management events is free for every region in an AWS account
    - Other trails created are charged