# AWS AppSync

- O AppSync é um serviço gerenciado que usa *GraphQL*
- É usado para criar APIs na AWS que usam *GraphQL*
- O *GraphQL* facilita para os aplicativos obterem os dados exatos de que precisam. Isso inclui a combinação de dados de vários recursos
- Os conjuntos de dados por trás do *GraphQL* podem incluir:
    - Armazenamentos de dados NoSQL
    - Bancos de dados RDS
    - APIs HTTP
    - etc.
- O AppSync integra-se com (resolvers) DynamoDB, Aurora, ElasticSearch, etc.
- Suporta recursos do cliente usando Lambda
- Fornece suporte para recuperação de dados em tempo real usando protocolos WebSocket ou MQTT sobre WebSocket
- Aplicativos móveis: substituto do Cognito Sync
- Requer um esquema (schema) GraphQL para começar
- Exemplo de esquema GraphQL:

    ```
    type Query {
        human(id: ID!): Human
    }

    type Human {
        name: String
        appearsIn: [Episode]
        starships: [Starship]
    }

    enum Episode {
        NEWHOPE
        EMPIRE
        JEDI
    }

    type Starship {
        name: String
    }
    ```

## Segurança

- Quatro maneiras pelas quais podemos autorizar aplicativos a interagir com o AppSync:
    - API_KEY
    - AWS_IAM
    - OPENID_CONNECT (Provedor OpenID Connect / JWT)
    - AMAZON_COGNITO_USER_POOLS
- Para domínio personalizado e HTTPS, use o CloudFront na frente do AppSync

---

# AWS AppSync

- AppSync is a managed service which uses *GraphQL*
- It is used for building APIs on AWS which use *GraphQL*
- *GraphQL* makes it easy for applications to get the exact data they need. This includes combining data from multiple resources
- Datasets behind *GraphQL* can include:
    - NoSQL data stores
    - RDS databases
    - HTTP APIs
    - etc.
- AppSync integrates with (resolvers) DynamoDB, Aurora, ElasticSearch, etc.
- Supports customer resources using Lambda
- Provides support for real time data retrieval using WebSocket or MQTT on WebSocket protocols
- Mobile applications: replacement for Cognito Sync
- Requires a GraphQL schema for getting started
- Example for GraphQL schema:

    ```
    type Query {
        human(id: ID!): Human
    }

    type Human {
        name: String
        appearsIn: [Episode]
        starships: [Starship]
    }

    enum Episode {
        NEWHOPE
        EMPIRE
        JEDI
    }

    type Starship {
        name: String
    }
    ```

## Security

- Four ways we can authorize applications to interact with AppSync:
    - API_KEY
    - AWS_IAM
    - OPENID_CONNECT (OpenID Connect provider/ JWT)
    - AMAZON_COGNITO_USER_POOLS
- For custom domain & HTTPS, use CloudFront in front of AppSync