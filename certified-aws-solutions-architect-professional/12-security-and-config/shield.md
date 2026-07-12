# AWS Shield

- Fornece proteção contra ataques DDoS
- Fornece um conjunto personalizado de proteção contra ataques DDoS
- Oferece proteção contra todos os ataques DDoS conhecidos de infraestrutura de Camada 3 e Camada 4: ataques Volumétricos de Rede (L3), Ataques de Protocolo de Rede (L4), por exemplo, TCP SYN Floods
- Vem em 2 formas:
    - **Shield Standard (Padrão)**:
        - É gratuito para todos os clientes da AWS
        - A proteção fica no perímetro da rede (isso pode ser na região/VPC ou na borda da AWS no caso de uso do CloudFront)
        - Protege contra ataques comuns de camada de Rede (L3) e Transporte (L4)
        - Obtemos a melhor proteção se usarmos Route 53, CloudFront ou Global Accelerator
        - Ele não fornece nada contra a capacidade proativa de qualquer forma de configuração explícita configurável
    - **Shield Advanced (Avançado)**:
        - Custa US$ 3.000 por mês por organização, lock-in (fidelidade) de 1 ano + cobrança por dados (SAÍDA / OUT) / mês. O custo não é por conta; se quisermos proteção para várias contas, devemos ter certeza de que elas estão na mesma organização
        - Expande a gama de produtos que podem ser protegidos: CloudFront, Global Accelerator, Route53, qualquer coisa associada a um EIP (exemplo: instâncias EC2), balanceadores de carga (ALB, CLB, NLB)
        - A proteção oferecida pelo Shield Advanced não é automática. Precisamos habilitá-la no Shield Advanced ou como parte da política AWS Firewall Manager Shield Advanced
        - O Shield Advanced fornece acesso a uma equipe de resposta avançada 24/7 chamada AWS Shield Response Team (SRT)
        - Fornece seguro financeiro (financial insurance) para qualquer aumento de pagamentos em caso de ataques DDoS
        - Recursos adicionais do Shield Advanced:
            - Integração com WAF:
                - O Shield Advanced integra-se com o WAF para proteger contra ataques de Camada de Aplicação (L7)
                - Inclui as taxas básicas do AWS WAF para web ACLs, regras e web requests
            - Visibilidade em tempo real de eventos e ataques DDOS
            - Detecção baseada em integridade (Health-based detection): verificações de integridade (health checks) específicas do aplicativo usadas pela equipe de engajamento proativo para fornecer detecção e mitigação mais rápidas de quaisquer problemas
            - Grupos de proteção (Protection groups):
                - Podemos criar agrupamentos de recursos que o Shield Advanced protege
                - Podemos definir os critérios de associação aos grupos; qualquer novo recurso será adicionado automaticamente

---

# AWS Shield

- Provides protection against DDoS attacks
- Provides a custom designed set of protection against DDoS attacks
- Offers protection against all known infrastructure Layer 3 and Layer 4 DDoS attacks: Network Volumetric attacks (L3), Network Protocol Attacks (L4) for example TCP SYN Floods
- Comes in 2 forms:
    - **Shield Standard**:
        - It is free of charge for all AWS customers
        - Protection is at the perimeter of the network (this can be either at the region/VPC or AWS edge in case of CloudFront usage)
        - Protects against common Network (L3) and Transport (L4) layer attacks
        - We get the best protection if we use Route 53, CloudFront or Global Accelerator
        - It does not provide anything against proactive capability of any form of explicit configurable configuration
    - **Shield Advanced**:
        - Costs $3000 per month per organization, 1 year lock-in + charge for data (OUT) / month. Cost is not per account, if we want protection for multiple accounts, we have to make sure they are in the same organization
        - Expands the range of products which can be protected: CloudFront, Global Accelerator, Route53, anything associated with am EIP (example EC2 instances), load balancers (ALB, CLB, NLB)
        - Protection offered by Shield Advanced is not automatic. We need to enable it in Shield Advanced or as part as AWS Firewall Manager Shield Advanced policy
        - Shield Advanced provides access to 24/7 advanced response team named AWS Shield Response Team (SRT)
        - Provides financial insurance for any increase of payments in case of DDoS attacks
        - Additional Shield Advanced features
            - Integration with WAF:
                - Shield Advanced integrates with WAF to protect against Application Layer (L7) attacks
                - Includes basic AWS WAF fees for web ACLs, rules and web requests
            - Real time visibility of DDOS events and attacks
            - Health-based detection: application specific health checks used by proactive engagement team to provide faster detection and mitigation of any issues
            - Protection groups:
                - We can create grouping of resources that Shield Advanced protects
                - We can define the criteria of membership for groups, any new resource will automatically be added