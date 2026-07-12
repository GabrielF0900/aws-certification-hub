# Firewalls de Rede e DNS da AWS (AWS Network and DNS Firewalls)

## AWS Network Firewall

- O AWS Network Firewall é um serviço de firewall de rede, com monitoramento de estado (stateful), gerenciado, e de detecção e prevenção de intrusões (intrusion detection and prevention) para a sua nuvem privada virtual (VPC)
- É um appliance de rede gerenciado usado para filtrar o tráfego de entrada/saída
- Numa VPC, ele é implantado em uma sub-rede separada com um Firewall Endpoint (Ponto de Extremidade do Firewall)
- Possui um mecanismo de regras (rules engine) flexível que fornece controle refinado (fine-grained) sobre o tráfego de rede
- Os recursos enviam tráfego para a sub-rede do firewall, o firewall redirecionará o tráfego para o gateway (internet gateway, transit gateway, conexão DX, IPSEC VPN)
- O firewall endpoint usa o gateway load balancer
- A configuração da tabela de rotas (Route table) é necessária para que a sub-rede protegida consiga enviar tráfego de saída para o gateway load balancer
- A implantação do Network Firewall pode ser gerenciada com o AWS Organizations e o AWS Firewall Manager
- Recursos do Network Firewall:
    - Firewall stateful e stateless
    - Sistema de Prevenção de Intrusão (Intrusion Prevention System - IPS)
    - Filtragem da Web (Web filtering)
- Na sub-rede do firewall não devemos implantar nenhum recurso
- Para HA (Alta Disponibilidade), devemos alocar uma sub-rede por AZ

## Route 53 Resolver DNS Firewall

- Permite-nos filtrar e regular o tráfego DNS de saída para VPCs
- As requisições são roteadas pelo Route 53 Resolver para consultas DNS, o DNS Firewall ajudará a evitar a exfiltração de dados via DNS
- Podemos monitorar e controlar os domínios que a aplicação pode consultar
- Podemos usar o AWS Firewall Manager para configurar e gerenciar centralmente o DNS Firewall

---

# AWS Network and DNS Firewalls

## AWS Network Firewall

- AWS Network Firewall is a stateful, managed, network firewall and intrusion detection and prevention service for your virtual private cloud
- It is a managed network appliance used to filter incoming/outgoing traffic
- In a VPC it is deployed in a separate subnet with a Firewall Endpoint
- Has a flexible rules engine which gives a fine-grained control over network traffic
- Resources send traffic to the firewall subnet, the firewall will redirect traffic to the gateway (internet gateway, transit gateway, DX connection, IPSEC VPN)
- The firewall endpoint uses gateway load balancer
- Route table configuration is needed for the protected subnet to be able to send outgoing traffic to the gateway load balancer
- Network Firewall deployment can be managed with AWS Organizations and AWS Firewall Manager
- Network Firewall features:
    - Stateful and stateless firewall
    - Intrusion Prevention System (IPS)
    - Web filtering
- In the firewall subnet we should not deploy any resources
- For HA we should allocate a subnet per AZ

## Route 53 Resolver DNS Firewall

- Allows us to filter and regulate outbound DNS traffic for VPCs
- Requests route through Route 53 Resolver for DNS queries, the DNS Firewall will help prevent DNS exfiltration of data
- We can monitor and control the domains application can query
- We can use AWS Firewall Manager to centrally configure and manage DNS Firewall