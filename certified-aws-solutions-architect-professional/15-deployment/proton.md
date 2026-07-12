# AWS Proton

- É:
    - Um serviço de provisionamento automatizado de infraestrutura como código (IaC) e implantação de aplicativos serverless (sem servidor) e baseados em contêineres:
        - O serviço AWS Proton é uma estrutura (framework) de automação em duas frentes
        - Criamos **modelos de serviço (service templates)** versionados que definem infraestrutura padronizada e ferramentas de implantação para aplicativos serverless e baseados em contêineres
        - O AWS Proton identifica todas as instâncias de serviço existentes que estão usando uma versão de modelo desatualizada para nós
        - Podemos solicitar que o AWS Proton as atualize (upgrade) com um clique
    - Infraestrutura padronizada:
        - As equipes de plataforma podem usar o AWS Proton e modelos de infraestrutura como código versionados
    - Implantações integradas com CI/CD:
        - O AWS Proton provisiona automaticamente os recursos, configura o pipeline CI/CD e implanta o código na infraestrutura definida

---

# AWS Proton

- It is:
    - Automated infrastructure as code provisioning and deployment of serverless and container-based applications:
        - AWS Proton service is a two-pronged automation framework
        - We create versioned **service templates** that define standardized infrastructure and deployment tooling for serverless and container-based applications
        - AWS Proton identifies all existing service instances that are using an outdated template version for us
        - We can request AWS Proton to upgrade them with one click
    - Standardized infrastructure:
        - Platform teams can use AWS Proton and versioned infrastructure as code templates
    - Deployments integrated with CI/CD:
        - AWS Proton automatically provisions the resources, configures the CI/CD pipeline, and deploys the code into the defined infrastructure