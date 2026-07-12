# AWS SAM - Serverless Application Model (Modelo de Aplicativo Serverless)

- Um aplicativo serverless não é apenas uma função Lambda, ele pode incluir muitos outros serviços, como:
    - Código de front-end e ativos hospedados no S3 e CloudFront
    - Endpoint de API - API Gateway
    - Computação - Lambda
    - Banco de dados - DynamoDB
    - Fontes de eventos, permissões e muito mais...
- O grupo de produtos e recursos SAM dentro da AWS tem 2 partes principais:
    - Especificação de modelo (template) do AWS SAM, que é uma extensão do CloudFormation. Adiciona componentes a modelos do CloudFormation projetados especificamente para aplicativos serverless: Transforms, Globals & Resources (pode incluir recursos normais do CFN, bem como específicos do SAM)
    - AWS SAM CLI permite testes locais, invocação local e implantações (deployments) na AWS

---

# AWS SAM - Serverless Application Model

- A serverless application is not just a Lambda function, it can include many more services such as:
    - Front end code and assets hosted by S3 and CloudFront
    - API endpoint - API Gateway
    - Compute - Lambda
    - Database - DynamoDB
    - Event sources, permissions and more...
- The SAM group of products and features within AWS has 2 main parts:
    - AWS SAM template specification, which is an extension of CloudFormation. Adds components to CloudFormation templates designed specifically for serverless applications: Transforms, Globals & Resources (can include normal CFN resources as well as SAM specific ones)
    - AWS SAM CLI allows local testing, local invocation and deployments into AWS