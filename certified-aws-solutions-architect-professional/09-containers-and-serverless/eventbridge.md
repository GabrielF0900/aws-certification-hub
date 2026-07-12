# CloudWatch Events e EventBridge

- Fornecem um fluxo de eventos do sistema quase em tempo real
- Esses eventos descrevem alterações nos serviços da AWS, por exemplo: instância EC2 é iniciada
- O EventBridge é um sistema mais recente que substitui o CloudWatch Events. Ele pode executar a mesma funcionalidade e, além disso, pode lidar com eventos de terceiros e aplicativos personalizados
- Ambos os serviços operam usando um barramento de eventos (event bus). Ambos têm um barramento de eventos padrão
- No CloudWatch Events, há apenas o barramento de eventos padrão, que é explícito e não é exposto à interface do usuário (UI)
- No EventBridge, podemos ter barramentos de eventos adicionais
- Em ambos os sistemas criamos regras que correspondem aos eventos de entrada, ou temos regras baseadas em agendamento
- Os próprios eventos são objetos JSON, incluindo, por exemplo, qual instância EC2 mudou de estado, para qual estado mudou, bem como outras coisas como data e hora

---

# CloudWatch Events and EventBridge

- Deliver a near real-time stream of system events
- These events describe changes in AWS services, example: EC2 instance is started
- EventBridge is a newer system replacing CloudWatch Events. It can perform the same functionality, in addition it can handle events from third-parties and custom applications
- Both of the services operate using an event bus. Both have a default event bus
- In CloudWatch Events there is only the default event bus, which is explicit and it is not exposed to the UI
- In EventBridge we can have additional event buses
- In both systems we create rules matching incoming events, or we have scheduled based rules
- Events themselves are JSON objects, including for example which EC2 instance changed state, in what state changed into as well as other things such as date and time