# SNS - Simple Notification Service (Serviço de Notificação Simples)

- É um serviço de mensagens pub-sub (publicação/assinatura) altamente disponível, durável e seguro
- É um serviço público da AWS: requer conectividade de rede com um endpoint público
- Coordena o envio e a entrega de mensagens
- As mensagens têm cargas úteis (payloads) <= 256 KB
- Os tópicos SNS (SNS Topics) são a entidade base do SNS. Sobre esses tópicos, as permissões são controladas e as configurações são definidas
- Um publicador (publisher) envia mensagens a um tópico
- Os tópicos podem ter assinantes (subscribers) que receberão mensagens de um tópico
- Assinantes suportados são:
    - HTTP(s)
    - Email (JSON)
    - Filas SQS
    - Notificações Push Móveis (Mobile Push Notifications)
    - Mensagens SMS
    - Funções Lambda
- O SNS é usado em toda a AWS para notificações, por exemplo, o CloudWatch o usa extensivamente
- É possível aplicar filtros a um assinante
- Arquitetura Fan-out: tópico único com vários assinantes de fila SQS
- O SNS oferece status de entrega para os assinantes suportados, que são HTTP, Lambda e SQS
- O SNS suporta tentativas de entrega (delivery retries)
- O SNS é um serviço HA e escalável dentro de uma região
- O SNS suporta Criptografia no Lado do Servidor (Server Side Encryption - SSE)
- Podemos usar acesso entre contas (cross-account) a um tópico por meio de políticas de tópico

---

# SNS - Simple Notification Service

- It is a highly available, durable, secure, pub-sub messaging service
- It is a public AWS service: requires network connectivity with a public endpoint
- It coordinates the sending and delivery of messages
- Messages are <= 256 KB payloads
- SNS Topics are the base entity of SNS. On this topics are permissions controlled and configurations defined
- A publisher sends messages to a topic
- Topics can have subscribers which will receive messages from a topic
- Supported subscribers are:
    - HTTP(s)
    - Email (JSON)
    - SQS queues
    - Mobile Push Notifications
    - SMS messages
    - Lambda Functions
- SNS is used across AWS for notifications, example CloudWatch uses it extensively
- It is possible to apply filters to a subscriber
- Fan-out architecture: single topic with multiple SQS queue subscribers
- SNS offers delivery status for supported subscribers which are HTTP, Lambda and SQS
- SNS supports delivery retries
- SNS it is a HA and scalable service within a region
- SNS supports Server Side Encryption (SSE)
- We can use cross-account access to a topic via topic policies