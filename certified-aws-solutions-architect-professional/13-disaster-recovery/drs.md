# AWS Elastic Disaster Recovery (DRS)

- Minimiza o tempo de inatividade (downtime) e a perda de dados com a recuperação rápida e confiável de aplicativos on-premises (locais) e baseados na nuvem (cloud-based), usando armazenamento acessível (affordable), computação mínima e recuperação point-in-time (em um ponto no tempo)
- Podemos aumentar a resiliência de TI quando usamos o AWS Elastic Disaster Recovery para replicar aplicativos locais ou baseados na nuvem rodando em sistemas operacionais compatíveis
- Configuramos um agente DRS em nossos servidores de origem (source servers) para iniciar a replicação segura de dados
- Nossos dados são então replicados em uma sub-rede de área de preparação (staging area subnet) em nossa conta AWS
- A staging area é projetada para reduzir custos usando armazenamento acessível e computação mínima
- O AWS Elastic Disaster Recovery converte automaticamente nossos servidores para inicializar (boot) e rodar nativamente na AWS quando lançamos instâncias para simulações (drills) ou recuperação
- Se precisarmos recuperar aplicativos, você pode iniciar instâncias de recuperação na AWS em minutos

---

# AWS Elastic Disaster Recovery (DRS)

- Minimizes downtime and data loss with fast, reliable recovery of on-premises and cloud-based applications using affordable storage, minimal compute, and point-in-time recovery
- We can increase IT resilience when you use AWS Elastic Disaster Recovery to replicate on-premises or cloud-based applications running on supported operating systems
- We set up a DRS agent on our source servers to initiate secure data replication
- Our data is then replicated in a staging area subnet in our AWS account
- The staging area is designed to reduce costs by using affordable storage and minimal compute
- AWS Elastic Disaster Recovery automatically converts our servers to boot and run natively on AWS when we launch instances for drills or recovery
- If we need to recover applications, you can launch recovery instances on AWS within minutes