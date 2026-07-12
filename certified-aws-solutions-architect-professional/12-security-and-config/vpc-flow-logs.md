# VPC Flow Logs (Logs de Fluxo da VPC)

- Ferramentas de diagnóstico essenciais para redes complexas
- Eles capturam apenas os metadados do pacote, não capturam o conteúdo do pacote. Para o conteúdo do pacote, é necessário instalar um analisador de pacotes (packet sniffer) numa instância
- Os metadados podem incluir: IP de origem/destino, portas de origem/destino, tamanho do pacote, outros metadados visíveis externamente, etc.
- Os Flow Logs podem capturar dados em vários pontos diferentes:
    - Aplicado a uma VPC: todas as interfaces naquela VPC
    - Sub-rede: apenas em cada interface de rede da sub-rede
    - Interface de rede: monitora o tráfego apenas em uma interface específica
- Os VPC Flow Logs NÃO são em tempo real, há um atraso entre o tráfego que sai das interfaces monitoradas e seu aparecimento nos flow logs <span style="color: red;">EXAME</span>
- Flow logs podem ser configurados para usar o S3, CloudWatch Logs ou Kinesis Firehose como destino
- Flow logs podem ser configurados para capturar dados apenas em conexões aceitas, apenas em conexões rejeitadas ou podem capturar metadados de todas as conexões.

## Conteúdo do Registro do VPC Flow Logs

- `<version>`
- `<account-id>`
- `<interface-id>`
- `<srcaddr>`: endereço IP de origem
- `<dstaddr>`: endereço IP de destino
- `<srcport>`: porta de origem, 0 se nenhuma porta for usada (exemplo: no caso de ping ICMP)
- `<dscport>`: porta de destino
- `<protocol>`: ICMP=`1`, TPC=`6`, UDP=`17`, etc. <span style="color: red;">Precisa lembrar para o EXAME</span>
- `<packets>`
- `<bytes>`
- `<start>`
- `<end>`
- `<action>`: o tráfego é `ACCEPT`ed (aceito) ou `REJECT`ed (rejeitado)
- `<log-status>`

## Notas

- VPC Flow Logs não registram todo o tráfego; coisas como comunicação com o IP de metadados (169.254.169.254), servidor de sincronização de horário da AWS (AWS time sync server - 169.254.169.123), DHCP, servidor DNS da Amazon e licença do Amazon Windows não são gravadas

---

# VPC Flow Logs

- Essential diagnostic tools for complex networks
- They only capture packet metadata, they do not capture packet content. For packet content a packet sniffer is required to be installed on an instance
- Metadata can include: source/destination IP, source/destination ports, packet size, other externally visible metadata, etc.
- Flow logs can capture data at various different points:
    - Applied to a VPC: all interfaces in that VPC
    - Subnet: every network interface in the subnet only
    - Network interface: only monitor traffic at a specific interface
- VPC Flow Logs are NOT realtime, there is delay between traffic leaving monitored interfaces and showing up in the flow logs <span style="color: red;">EXAM</span>
- Flow logs can be configured to use S3, CloudWatch Logs or Kinesis Firehose for the destination
- Flow logs can be cofigured to capture data only at accepted connections, only at rejected connections or they can capture metadata at all connections.

## VPC Flow Logs Record Content

- `<version>`
- `<account-id>`
- `<interface-id>`
- `<srcaddr>`: source IP address
- `<dstaddr>`: destination IP address
- `<srcport>`: source port, 0 if no port is used (example in case of ICMP ping)
- `<dscport>`: destination port
- `<protocol>`: ICMP=`1`, TPC=`6`, UDP=`17`, etc. <span style="color: red;">Need to remember for EXAM</span>
- `<packets>`
- `<bytes>`
- `<start>`
- `<end>`
- `<action>`: traffic is `ACCEPT`ed or `REJECT`ed
- `<log-status>`

## Notes

- VPC Flow Logs do not log all the traffic, things like the communication with the metadata IP (169.254.169.254), AWS time sync server (169.254.169.123), DHCP, Amazon DNS server and Amazon Windows license is not recorded
