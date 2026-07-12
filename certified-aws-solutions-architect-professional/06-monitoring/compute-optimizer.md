# AWS Compute Optimizer

- O AWS Compute Optimizer é um serviço que analisa a configuração e as métricas de utilização de nossos recursos AWS para nos fornecer recomendações de dimensionamento correto
- Gera recomendações de otimização para reduzir o custo e melhorar o desempenho de suas cargas de trabalho
- Recursos e requisitos suportados:
    - Instâncias EC2
    - Grupos de Auto Scaling
    - Volumes EBS
    - Funções Lambda
    - ECS e ECS Fargate
    - Licenças de Software Comercial
    - Instâncias e armazenamento de banco de dados RDS
- O Compute Optimizer requer adesão voluntária (opt-in)
- Analisando métricas: após a adesão, o Compute Optimizer começa a analisar as especificações e as métricas de utilização de recursos do Amazon CloudWatch dos últimos 14 dias
- Aprimorando recomendações: podemos aprimorar as recomendações ativando preferências de recomendação, como o recurso pago de métricas de infraestrutura aprimoradas

---

# AWS Compute Optimizer

- AWS Compute Optimizer is a service that analyzes our AWS resources' configuration and utilization metrics to provide us with rightsizing recommendations
- Generates optimization recommendations to reduce the cost and improve the performance of your workloads
- Supported resources and requirements:
    - EC2 instances
    - Auto Scaling Groups
    - EBS volumes
    - Lambda functions
    - ECS and ECS Fargate
    - Commercial Software Licenses
    - RDS DB instances and storage
- Compute Optimizer is opt-in
- Analyzing metrics: after opt in, Compute Optimizer begins analyzing the specifications and the utilization metrics of resources from Amazon CloudWatch for the last 14 days
- Enhancing recommendations: we can enhance recommendations by activating recommendation preferences, such as the enhanced infrastructure metrics paid feature