# Amazon MQ

- SNS e SQS são serviços da AWS que usam APIs da AWS
- SNS fornece tópicos que são canais de comunicação de um para muitos (one to many), SQS fornece filas que são canais de comunicação de um para um (one to one)
- Tanto SNS quanto SQS são serviços públicos, HA (Altamente Disponíveis) e integrados à AWS
- Organizações maiores já podem usar sistemas de mensagens on-premise, que não são totalmente compatíveis com SNS e SQS
- Amazon MQ é um broker (corretor) de mensagens de código aberto, é uma implementação gerenciada do Apache ActiveMQ
- Ele suporta a API JMS e protocolos como AMQP, MQTT, OpenWire e STOMP
- Ele fornece filas e tópicos
- Ele usa serviços de message broker que podem ser de instância única (teste, dev) e par HA (Active/StandBy para produção)
- Ao contrário do SQS e SNS, o Amazon MQ não é um serviço público, ele roda em uma VPC
- Ele não tem integração nativa com outros serviços da AWS da mesma forma que o SNS/SQS
- Considerações sobre o Amazon MQ:
    - Por padrão, devemos escolher SNS/SQS para implementações mais novas
    - Devemos usar o Amazon MQ se migrarmos de um sistema existente com pouca ou nenhuma alteração de aplicativo
    - Devemos usar o Amazon MQ se precisarmos de APIs como JMS ou protocolos como AMQP, MQTT, OpenWire, STOMP
    - Amazon MQ requer a rede privada apropriada

---

# Amazon MQ

- SNS and SQS are AWS services using AWS APIs
- SNS provides topics which are one to many communication channels, SQS provides queues which are one to one communication channels
- Both SNS and SQS are public services, HA and AWS integrated
- Larger organization might already use on-premise messaging systems, which are not entirely compatible with SNS and SQS
- Amazon MQ is an open-source message broker, is a managed implementation of Apache ActiveMQ
- It supports the JMS API and protocols such as AMQP, MQTT, OpenWire and STOMP
- It provides both queues and topics
- It uses message broker services which can be single instance (test, dev) and HA pair (Active/StandBy for production)
- Unlike SQS and SNS, Amazon MQ is not a public service, it runs in a VPC
- It does not have native integration with other AWS services in the same way as SNS/SQS
- Amazon MQ considerations:
    - By default we should chose SNS/SQS for newer implementation
    - We should use Amazon MQ if we migrate from an existing system with little to no application change
    - We should use Amazon MQ if we need APIs such as JMS or protocols such as AMQP, MQTT, OpenWire, STOMP
    - Amazon MQ requires the appropriate private networking