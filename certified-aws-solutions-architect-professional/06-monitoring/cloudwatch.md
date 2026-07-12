# CloudWatch

- Fornece serviços para ingestão, armazenamento e gerenciamento de métricas
- É um serviço público - fornece endpoints de espaço público
- Muitos serviços têm integração nativa do plano de gerenciamento com o CloudWatch, por exemplo o EC2. Além disso, o EC2 fornece apenas informações coletadas externamente; para métricas de dentro de um EC2, podemos usar o agente CloudWatch
- O CloudWatch pode ser usado a partir de ambientes on-premises usando o agente ou a API CloudWatch
- O CloudWatch armazena dados de forma persistente
- Os dados podem ser visualizados no console, CLI ou API, mas o CloudWatch também fornece dashboards e detecção de anomalias
- Alarmes CloudWatch: reagem a métricas, podem ser usados para notificar ou realizar ações
- Instâncias em sub-redes públicas podem se conectar ao CloudWatch usando o gateway de internet, e instâncias em sub-redes privadas podem se conectar ao CloudWatch usando o Endpoint de Interface

## CloudWatch - Dados

- **Namespace**: contêiner para métricas, por exemplo: AWS/EC2 para o NS do EC2, AWS/Lambda para o NS do Lambda. É possível ter o mesmo nome de métrica para diferentes serviços; o NS ajuda a segregá-los
- **Ponto de dados**: timestamp, valor, unidade de medida (opcional)
- **Métrica**: conjunto de pontos de dados ordenados por tempo. Exemplo de métricas integradas: `CPUUtilization`, `NetworkIn`, `DiskWriteBytes` para EC2
- Cada métrica tem um `MetricName` e um namespace, por exemplo: CPUUtilization para AWS/EC2
- **Dimensão**: par nome/valor; exemplo: uma dimensão é a forma de separar a métrica `CPUUtilization` de uma instância para outra
- As dimensões podem ser usadas para agregar dados; exemplo: agregar dados para todas as instâncias de um ASG
- **Resolução**: padrão (granularidade de 60 segundos) ou alta (granularidade de 1 segundo)
- **Resolução de métrica**: período mínimo para o qual podemos obter um ponto de dados particular
- Retenção de dados:
    - Granularidade abaixo de 60s é retida por 3 horas
    - Alta resolução pode ser medida, mas custa mais. A resolução determina o período mínimo que pode ser especificado e obter um valor válido. Padrão (60 s) .. Alta (1 s)
    - Granularidade de 60s retida por 15 dias
    - 5 min retido por 63 dias
    - 1 hora retida por 455 dias
- À medida que os dados envelhecem, são agregados e armazenados por um período mais longo com menor resolução
- Estatísticas: obtém dados durante um período e os agrega de determinada forma
- Percentil: posição relativa de um valor dentro do conjunto de dados

## Alarmes CloudWatch

- Alarme: monitora uma métrica durante um período de tempo
- Estados: `ALARM` ou `OK` com base no valor de uma métrica em relação a um limiar ao longo do tempo
- Os alarmes podem ser configurados com uma ou mais ações, que podem iniciar ações em nosso nome. As ações podem ser: enviar notificação para um tópico SNS, tentar uma modificação de política de auto scaling ou usar o Event Bridge para integrar com outros serviços
- Métricas de alta resolução podem ter alarmes de alta resolução

## Logs do CloudWatch

- Os Logs do CloudWatch fornecem dois tipos de funcionalidades: ingestão e assinatura
- O Logs do CloudWatch é um serviço público projetado para armazenar, monitorar e fornecer acesso a dados de log
- Pode fornecer ingestão de logs para produtos AWS nativamente, mas também para on-premises, IoT ou qualquer aplicação
- Agente CloudWatch: usado para fornecer ingestão para aplicações personalizadas
- O CloudWatch também pode ingerir fluxos de log do VPC Flow Logs ou do CloudTrail (eventos de conta e chamadas de API AWS)
- O Logs do CloudWatch é um serviço regional; certos serviços globais enviam seus logs para `us-east-1`
- Os eventos de log consistem em 2 partes:
    - **Timestamp**
    - **Mensagem bruta**
- Os Eventos de Log podem ser coletados em Fluxos de Log. Os Fluxos de Log são sequências de eventos de log compartilhando a mesma fonte
- Grupos de Log: são coleções de Fluxos de Log. Podemos definir retenção, permissões e criptografia nos grupos de log. Por padrão, os grupos de log armazenam dados indefinidamente
- Filtro de Métrica: pode ser definido no grupo de log e procurará padrões nos eventos de log. Essencialmente cria uma métrica dos fluxos de log ao procurar ocorrências de certos padrões definidos por nós (exemplo: logs de SSH com falha nos eventos)
- Exportar logs do CloudWatch:
    - **Exportação para S3**: podemos criar uma tarefa de exportação (`Create-Export-Task`) que pode levar até 12 horas. Não é em tempo real. É criptografado usando SSE-S3
    - **Assinatura**: entrega de logs em tempo real. Devemos criar um filtro de assinatura para os seguintes destinos: Kinesis Data Firehose (quase em tempo real), OpenSearch (ElasticSearch) usando Lambda ou Lambda personalizado, Kinesis Data Streams (qualquer consumidor KCL)
- Filtros de assinatura podem ser usados para criar uma arquitetura de agregação de logs

## Dashboards CloudWatch

- Uma ótima forma de configurar dashboards para acesso rápido às métricas principais
- Os dashboards são globais
- Os dashboards podem incluir gráficos de diferentes regiões
- Podemos alterar o fuso horário e o intervalo de tempo dos dashboards
- Podemos configurar atualização automática (10s, 1m, 2m, 5m, 15m)
- Preços:
    - 3 dashboards (até 50 métricas) gratuitamente
    - $3/dashboard/mês

## CloudWatch Synthetics Canary

- Os Synthetics Canary são scripts configuráveis que monitoram APIs e URLs
- Esses scripts destinam-se a reproduzir o que um cliente faria para encontrar problemas antes que o aplicativo seja implantado em produção
- Também podem ser usados para verificar a disponibilidade e latência de nossos endpoints
- Podem armazenar dados de tempo de carregamento e capturas de tela da UI
- Têm integração com Alarmes CloudWatch
- Os scripts podem ser escritos em Node.js ou Python
- Fornecem acesso programático a um navegador Chrome sem interface gráfica
- Podem ser executados uma vez ou regularmente
- Blueprints do Canary:
    - Monitor de Heartbeat: carrega URL, armazena captura de tela e um arquivo de arquivo HTTP
    - API Canary: testa funções básicas de leitura e escrita de uma API REST
    - Verificador de Links Quebrados: verifica todos os links dentro de uma página
    - Monitoramento Visual: compara uma captura de tela tirada durante uma execução do canary com uma captura de tela de referência
    - Gravador Canary: usado com o CloudWatch Synthetics Recorder - usado para gravar ações em um site e gerar automaticamente um script de teste para isso
    - Construtor de Fluxo de Trabalho GUI: verifica se ações podem ser realizadas em uma página web (exemplo: testar uma página web com um formulário de login)

---

# CloudWatch

- Provides services to ingest, store and manage metrics
- It is a public service - provides public space endpoints
- Many services have native management plan integration with CloudWatch, for example EC2. Also, EC2 provides external gathered information only, for metrics from inside an EC2 we can use CloudWatch agent
- CloudWatch can be used from on-premises using the agent or the CloudWatch API
- CloudWatch stores data in a persistent way
- Data can be viewed from the console, CLI or API, but also CloudWatch also provides dashboards and anomaly detection
- CloudWatch Alarms: react to metrics, can be used to notify or to perform actions
- Instances in public subnet can connect to cloudwatch using Internet gateway and the instances in the private subnets can connect to the cloudwatch usig Interface Endpoint.

## CloudWatch - Data

- **Namespace**: container for metrics e.g. AWS/EC2 for EC2 NS, AW/Lambda for lambda NS. Its possible to have same mertic name for different service, NS helps to segregate them.
- **Data point**: timestamp, value, unit of measure (optional)
- **Metric**: time ordered set of data point. Example of builtin metrics: `CPUUtilization`, `NetworkIn`, `DiskWriteBytes` for EC2
- Every metric has a `MetricName` and a namespace e.g. CPUUtilization for AWS/EC2
- **Dimension**: name/value pair, example: a dimension is the way for `CPUUtilization` metric to be separated from one instance to another
- Dimensions can be used to aggregate data, example aggregate data for all instances for an ASG
- **Resolution**: standard (60 second granularity) or high (1 second granularity)
- **Metric resolution**: minimum period that we can get one particular data point for
- Data retention:
    - sub 60s granularity is retained for 3 hours
    - High resolution can be measured but they cost more. Resolution determines the minimum period which ca be specified and get a valid value. Standard (60 Sec) .. High (1 Sec)
    - 60s granularity retained for 15 days
    - 5 min retained for 63 days
    - 1 hour retained for 455 days
- As data ages, its aggregated and stored for longer period of time with less resolution
- Statistics: get data over a period and aggregate it in a certain way
- Percentile: relative standing of a value within the dataset

## CloudWatch Alarms

- Alarm: watches a metric over a period of time
- States: `ALARM` or `OK` based on the value of a metric against a threshold over time
- Alarms can be configured with one or more actions, which can initiate actions on our behalf. Actions can be: send notification to an SNS topic, attempt an auto scaling policy modification or use Event Bridge to integrate with other services
- High resolution metrics can have high resolution alarms

## CloudWatch Logs

- CloudWatch Logs provides two type of functionalities: ingestion and subscription
- CloudWatch Logs is a public service designed to store, monitor and provide access logging data
- Can provide logging ingestion for AWS products natively, but also for on-premises, IOT or any application
- CloudWatch Agent: used to provide ingestion for custom applications
- CloudWatch can also ingest log streams from VPC Flow Logs or CloudTrail (account events and AWS API calls)
- CloudWatch Logs is regional service, certain global services send their logs to `us-east-1`
- Log events consist of 2 parts:
    - **Timestamp**
    - **Raw message**
- Log Events can be collected into Log Streams. Log Streams are sequence of log events sharing the same source
- Log Groups: are collection of Log Streams. We can set retention, permissions and encryption on the log groups. By default log groups store data indefinitely
- Metric Filter: can be defined on the log group and will look for pattern in the log events. Essentially creates a metric from the log streams by looking at occurrences of certain patterns defined by us (example: failed SSH logs in events)
- Export logs from CloudWatch:
    - **S3 Export**: we can create an export task (`Create-Export-Task`) which will take up to 12 hours. Its not real time. It is encrypted using SSE-S3.
    - **Subscription**: deliver logs in real time. We should create a subscription filter for the following destination: Kinesis Data Firehose (near real time), OpenSearch (ElasticSearch) using Lambda or custom Lambda, Kinesis Data Streams (any KCL consumer)
- Subscription filters can be used to create a logging aggregation architecture

## CloudWatch Dashboards

- A great way to setup dashboards for quick access to key metrics
- Dashboards are global
- Dashboards can include graphs from different regions
- We can change the time zone and time range of the dashboards
- We can setup automatic refresh (10s, 1m, 2m, 5m, 15m)
- Pricing:
    - 3 dashboards (up to 50 metrics) for free
    - $3/dashboard/month

## CloudWatch Synthetics Canary

- Synthetics Canary are configurable scripts that will monitor APIs and URLs
- These scripts meant to reproduce what a customer would do in order to find issues before the app is deployed to production
- They can be also used to check the availability and latency of our endpoints
- They can store load time data and screenshots of the UI
- They have integration with CloudWatch Alarms
- The scripts can be written in Node.js or Python
- Provides programmatic access to a headless Chrome browser
- They can be run once or on a regular basis
- Canary Blueprints:
    - Heartbeat Monitor: load URL, store screenshot and an HTTP archive file
    - API Canary: test basic read and write functions of a REST API
    - Broken Link Checker: check all links inside a page
    - Visual Monitoring: compare a screenshot taken during a canary run with a baseline screenshot
    - Canary Recorder: used with CloudWatch Synthetics Recorder - used to record actions on a website and automatically generate a test script for that
    - GUI Workflow Builder: verifies that actions can be taken on a webpage (example: test a webpage with a login form)