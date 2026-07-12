# SQS - Simple Queue Service

- O SQS fornece filas de mensagens gerenciadas
- É um serviço público da AWS
- É totalmente gerenciado com filas altamente disponíveis e de alto desempenho por design
- As filas vêm em dois tipos: Padrão (Standard - ordenação com melhor esforço) e FIFO (garante uma ordem)
- As mensagens adicionadas à fila têm tamanho de até 256 KB
- `VisibilityTimeout` (Tempo limite de visibilidade): quando um cliente recebe uma mensagem, a mensagem fica oculta por um período de tempo. O `VisibilityTimeout` é o período concedido ao cliente para processar a mensagem
- Se o cliente processar a mensagem, ele deve excluí-la da fila. Se a mensagem não for excluída, após o `VisibilityTimeout` a mensagem estará disponível para outros clientes
- **Filas de mensagens mortas (Dead-Letter queues - DLQ)**: todas as mensagens não processadas podem ser enviadas para cá após um determinado número de tentativas. Permite diferentes tipos de processamento nas mensagens
- Filas podem ser usadas para dimensionamento (scaling) por ASGs, Lambdas podem ser invocadas com base em mensagens na fila

## Filas SQS Standard vs FIFO

- Standard:
    - As mensagens são entregues pelo menos uma vez
    - A ordem de entrega não é garantida (ordenação de melhor esforço - best-effort)
    - Elas não têm limitações de desempenho
- FIFO:
    - As mensagens são entregues exatamente uma vez
    - A ordem de entrega é garantida como a mesma em que as mensagens foram enviadas
    - O desempenho é limitado: 3.000 mensagens por segundo com envio em lote (batching) ou até 300 mensagens por segundo sem lote
    - Também está disponível um modo de alto rendimento (high throughput) para filas FIFO
    - Filas FIFO devem ter o sufixo `.fifo` para serem filas FIFO válidas

## Faturamento do SQS

- Com o SQS, somos cobrados por solicitação (request)
- Com 1 solicitação, podemos receber entre 1 e 10 mensagens de até 64 KB no total
- O SQS é menos econômico se fizermos pesquisas (poll) com mais frequência

## Pesquisa SQS (SQS Polling)

- Pesquisando filas SQS:
    - **Pesquisa curta (Short polling)** (imediata): pode retornar 0 ou mais mensagens. Ela retornará imediatamente se não houver mensagens na fila
    - **Pesquisa longa (Long polling)**: podemos especificar o valor `waitTimeSecond` que pode ser de até 20 segundos para esperar por mensagens durante a pesquisa. Ela usa menos solicitações do que a pesquisa curta

## Criptografia e Segurança SQS

- O SQS suporta criptografia em repouso (KMS) e criptografia em trânsito
- O acesso a uma fila é baseado em políticas de identidade e políticas de fila
- As políticas de fila podem permitir acesso entre contas (cross-account)

## Biblioteca de Cliente Estendida SQS (SQS Extended Client Library)

- O SQS tem um limite de tamanho de mensagem de 256 KB
- A Extended Client Library pode ser usada quando quisermos enviar mensagens maiores que esse tamanho
- Ela pode processar grandes cargas úteis (payloads) e armazenar o volume dessas cargas no S3
- Quando enviamos uma mensagem usando a API `SendMessage`, a biblioteca faz o upload do conteúdo para o S3 e armazena um link para esse conteúdo na mensagem
- Ao receber uma mensagem, a biblioteca carrega o payload do S3 e substitui o link pelo payload na mensagem
- Ao excluir uma mensagem de uma fila, o grande payload no S3 também será excluído
- A Extended Client Library pode lidar com mensagens de até 2 GB
- Ela tem uma implementação em Java. Bibliotecas equivalentes estão disponíveis para outras linguagens

## Filas de Atraso SQS (SQS Delay Queues)

- As filas de atraso (delay queues) nos permitem adiar a entrega de mensagens em filas SQS
- Para uma fila de atraso, configuramos um valor `DelaySeconds`. Mensagens adicionadas à fila ficarão invisíveis pela quantidade de `DelaySeconds`
- O valor padrão de `DelaySeconds` é 0, o valor máximo é 15 minutos. Para que uma fila seja uma fila de atraso, o valor deve ser definido como maior que 0
- Tempos de mensagem permitem que a invisibilidade seja definida por mensagem, substituindo a configuração da fila. Os valores mínimo/máximo são os mesmos. A configuração por mensagem não é suportada para filas FIFO

## Filas de Mensagens Mortas SQS (SQS Dead Letter Queues - DLQ)

- Filas de Mensagens Mortas são projetadas para ajudar a lidar com falhas recorrentes durante o processamento de mensagens de uma fila
- Cada vez que uma mensagem é recebida, o `ReceiveCount` é incrementado. Para não processar a mesma mensagem repetidamente, definimos um `maxReceiveCount` e uma DLQ para uma fila. Depois que o número de tentativas for maior que `maxReceiveCount`, a mensagem é empurrada para a DLQ
- Com uma DLQ, podemos definir alarmes para sermos notificados em caso de falha
- As mensagens na DLQ podem ser analisadas posteriormente
- Cada fila (incluindo DLQ) tem um período de retenção para mensagens. Cada mensagem tem um `mq-timestamp` que representa quando a mensagem foi adicionada à fila. Caso uma mensagem seja movida para uma DLQ, esse carimbo de data/hora não é alterado
- Geralmente, o período de retenção para uma DLQ deve ser mais longo em comparação com as filas normais
- Uma única DLQ pode ser usada para várias fontes

---

# SQS - Simple Queue Service

- SQS provides managed message queues
- It is a public AWS service
- It is fully managed with highly available and highly performant queues by design
- Queues come in two types: Standard (ordering is best effort) and FIFO (guarantee an order)
- Messages added to the queue are up to 256 KB in size
- `VisibilityTimeout`: when a client receives a message, the message is hidden for a period of time. The `VisibilityTimeout` is the period which is given to the client in order to process the message
- If the client processes the message, it has to delete the message from the queue. If the message is not deleted, after the `VisibilityTimeout` the message will be available for other clients
- **Dead-Letter queues**: all unprocessed messages can be sent here after a given number of retries. Allows different types of processing on the messages
- Queues can be used for scaling by ASGs, Lambdas can be invoked based on messages in the queue

## SQS Standard vs FIFO Queues

- Standard: 
    - Messages are delivered at least once
    - The order of the delivery is not guaranteed (best-effort ordering)
    - They don't have performance limitations
- FIFO: 
    - Messages are delivered exactly once
    - The order of the delivery is guaranteed to be the same as the messages were sent
    - Performance is limited: 3000 messages per second with batching or up to 300 messages per second without batching
    - There is also available a high throughput mode for FIFO queues
    - FIFO queues have to have `.fifo` suffix in order to be valid FIFO queues

## SQS Billing

- With SQS we are billed per request
- With a 1 request we can receive between 1 and 10 messages up to 64 KB total
- SQS is less cost effective if we poll more frequently

## SQS Polling

- Polling SQS queues:
    - **Short polling** (immediate): can return 0 or more messages. It will return immediately if there are no messages on the queue
    - **Long polling**: we can specify `waitTimeSecond` value which can be up to 20 seconds to wait form messages when polling. It uses fewer requests than short polling

## SQS Encryption and Security

- SQS supports encryption at rest (KMS) and encryption in transit
- Access to a queue is based on identity policies and queue policies
- Queue policies can allow cross-account access

## SQS Extended Client Library

- SQS has a message size limit of 256 KB
- Extended Client Library can be used when we want to send messages larger than this size
- It can process large payloads and have the bulk of the payloads stored in S3
- When we send a message using `SendMessage` API, the library uploads the content to S3 and stores a link to this content in the message
- When receiving a message, the library loads the payload from S3 and replaces the link with the payload in the message
- When deleting a message from a queue, the large S3 payload will also be deleted
- The Extended Client Library can handle messages up to 2 GB
- It has an implementation in Java. Equivalent libraries are available for other languages

## SQS Delay Queues

- Delay queues allow us to postpone the delivery of messages in SQS queues
- For a delay queue we configure a `DelaySeconds` value. Messages added to the queue will be invisible for the amount of `DelaySeconds`
- The default value of `DelaySeconds` is 0, the max value is 15 minutes. In order for a queue to be delay queue, the value should be set to be greater than 0
- Message times allows a per-message basis invisibility to be set, overriding the queue setting. Min/max values are the same. Per message setting is not supported for FIFO queues

## SQS Dead Letter Queues (DLQ)

- Dead Letter Queues are designed to help handle reoccurring failures while processing messages from a queue
- Every time a message is received, the `ReceiveCount` is incremented. In order to not process the same message over and over again, we define a `maxReceiveCount` and a DLQ for a queue. After the number of retries is greater than the `maxReceiveCount`, the message is pushed into the DLQ
- Having a DLQ, we can define alarms to get notified in case of a failure
- Messages in DLQ can be further analyzed
- Every queue (including DLQ) have a retention period for messages. Every message has an `mq-timestamp` which represents when was the message was added to the queue. In case a message is moved into a DLQ, this timestamp is not altered
- Generally the retention period for a DLQ should be longer compared to normal queues
- A single DLQ can be used for multiple sources