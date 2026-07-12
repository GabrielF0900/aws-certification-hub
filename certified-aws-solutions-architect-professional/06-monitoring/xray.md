# AWS X-Ray

- É uma aplicação de rastreamento distribuído. Foi projetada para rastrear sessões através de uma aplicação
- O X-Ray recebe dados de muitos serviços (API Gateway, Lambda, DynamoDB) como parte de uma aplicação e fornece uma visão geral única do fluxo da sessão
- Conceitos fundamentais do X-Ray:
    - **Cabeçalho de Rastreamento**: quando um usuário se conecta a uma aplicação com o X-Ray habilitado, um **ID de rastreamento** é gerado e incorporado em um cabeçalho de rastreamento. Este cabeçalho é usado para rastrear a requisição em todos os serviços suportados
    - **Segmentos**: os serviços suportados enviam dados ao X-Ray usando segmentos. Os segmentos são blocos de dados contendo informações sobre host/ip, requisição, resposta, trabalho realizado (tempos), problemas
    - **Subsegmentos**: os segmentos podem conter subsegmentos para mais granularidade. Podem conter detalhes de outros serviços como parte do componente da aplicação
    - **Gráfico de Serviços**: documento JSON detalhando serviços e recursos que compõem a aplicação
    - **Mapa de Serviços**: representação visual de um gráfico de serviços pelo console X-Ray
- Para fornecer dados do X-Ray ao serviço AWS X-Ray, podemos fazer o seguinte:
    - EC2: instalar o Agente X-Ray
    - ECS: o agente é instalado em qualquer tarefa
    - Lambda: habilitar o X-Ray
    - Beanstalk: o agente vem pré-instalado
    - API Gateway: pode ser habilitado por opção de estágio
    - SNS e SQS: podem ser habilitados
- Os serviços requerem permissão IAM para enviar dados ao serviço X-Ray

---

# AWS X-Ray

- It is a distributed tracing application. It designed to track sessions through an application
- X-Ray takes data from many services (API Gateway, Lambda, DynamoDB) as part of an application and gives on single overview of the session flow
- Fundamental concepts of X-Ray:
    - **Tracing Header**: when an user connects to an application with X-Ray enabled, a **tracing ID** is generated an embedded into a tracing header. This header is used to track the request across all supported services
    - **Segments**: supported services send data to X-Ray using segments. Segments are data blocks containing host/ip, request, response, work done (times), issues information
    - **Subsegments**: segments can contain subsegments for more granularity. This can contain details to other services as part of the application component
    - **Service Graph**: JSON document detailing services and resources which make up the application
    - **Service Map**: visual representation of a service graph by the X-Ray console
- In order to provide X-Ray data to the AWS X-Ray service we can do the following:
    - EC2: install X-Ray Agent
    - ECS: agent is installed in any task
    - Lambda: enable X-Ray
    - Beanstalk: agent is preinstalled
    - API Gateway: can be enabled per stage option
    - SNS and SQS: can be enabled
- Services require IAM permission in order ot send data to X-Ray service