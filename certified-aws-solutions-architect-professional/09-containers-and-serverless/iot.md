# AWS IoT

- IoT - Internet of Things (Internet das Coisas)

## AWS IoT Core

- AWS IoT Core é um conjunto de produtos na AWS, usado para gerenciar milhões de dispositivos IoT
- Dispositivos IoT podem ser sensores de temperatura, vento, água, sensores de luz, sensores de controle de válvulas, etc.
- Todos estes precisam ser registrados em um sistema para permitir comunicação segura para gerenciá-los: provisionamento, atualizações e controle
- A comunicação de ou para dispositivos provavelmente não será confiável (unreliable), então a AWS fornece as *device shadows* (sombras de dispositivos): representações virtuais de dispositivos reais, tendo a mesma configuração registrada do dispositivo real. Podemos ler delas os últimos dados comunicados, essencialmente o dispositivo se comunica com a shadow, os últimos dados registrados podem ser recuperados a qualquer momento depois
- Mensagens de dispositivos são enviadas no formato JSON, usando protocolos MQTT
- AWS IoT fornece regras (rules): integração orientada a eventos com outros serviços da AWS
- Arquitetura AWS IoT:
    [AWS IoT architecture](images/ElasticTranscoder&AWSIoT.png)

## AWS IoT Device Management

- Ajuda-nos a registrar, organizar, monitorar e gerenciar remotamente dispositivos IoT em escala

## AWS IoT Device Defender

- Usado para auditar configurações, autenticar dispositivos, detectar anomalias e receber alertas para nos ajudar a proteger nossa frota de dispositivos IoT

## AWS IoT 1-Click

- Usado para lançar funções AWS Lambda a partir de dispositivos IoT
- Também podemos criar ações na nuvem ou no local (on-premises)

## AWS Greengrass

- AWS Greengrass é uma extensão dos serviços fornecidos pelo AWS IoT, movendo esses serviços para mais perto da borda (edge)
- O Greengrass permite que alguns serviços como computação, mensagens, gerenciamento de dados, sincronização e recursos de ML sejam executados a partir de dispositivos de borda
- Dispositivos com o software Greengrass Core podem executar localmente funções Lambda ou contêineres => a computação pode rodar localmente sem sair da rede local
- O Greengrass fornece *device shadows* locais que são sincronizadas de volta com a AWS
- Permite mensagens usando MQTT
- Permite acesso local ao hardware para funções Lambda

## AWS IoT Analytics

- Usado para executar análises (analytics) em dados de IoT e obter insights para tomar decisões melhores e mais precisas
- Suporta até petabytes de dados de milhões de dispositivos

## AWS IoT Events

- Usado para detectar e responder a eventos de sensores e aplicativos IoT
- Podemos ingerir dados de várias fontes para detectar o estado de nossos processos ou dispositivos e gerenciar proativamente cronogramas de manutenção

## AWS IoT SiteWise

- Simplifica a coleta, organização e análise de dados de equipamentos industriais
- Podemos organizar fluxos de dados de sensores de várias linhas de produção e instalações para impulsionar a eficiência em diferentes locais

## AWS IoT TwinMaker (anteriormente AWS IoT Things Graph)

- Usado para criar gêmeos digitais (digital twins) de sistemas do mundo real, como edifícios, fábricas, equipamentos industriais e linhas de produção
- Usamos isso para identificar e resolver rapidamente anomalias de equipamentos e processos no chão de fábrica, visando melhorar a produtividade e a eficiência do trabalhador

---

# AWS IoT

- IoT - Internet of Things

## AWS IoT Core

- AWS IoT Core is a product set in AWS, used for managing millions of IoT devices
- IoT devices can be temp, wind, water sensors, light sensors, valve control sensors, etc.
- All of these need to be registered into a system to allow secure communication for managing them: provisioning, updates and control
- Communication to or from devices is likely to be unreliable, so AWS provides *device shadows*: virtual representations of actual devices, having the same configuration registered for the actual device. We can read from them the last communicated data, essentially the device communicates with the shadow, the last registered data can be retrieved anytime afterwards
- Device messages are sent JSON format, using MQTT protocols
- AWS IoT provides rules: event-driven integration with other AWS Services
- AWS IoT architecture:
    [AWS IoT architecture](images/ElasticTranscoder&AWSIoT.png)

## AWS IoT Device Management

- Helps us to register, organize, monitor and remotely manage IoT devices at scale

## AWS IoT Device Defender

- Used to audit configurations, authenticate devices, detect anomalies and receive alerts to help us secure our IoT device fleet

## AWS IoT 1-Click

- Used to launch AWS Lambda functions from IoT devices
- We can also create actions in the cloud or on-premises

## AWS Greengrass

- AWS Greengrass is an extension of the services provided by AWS IoT, moving those services closer to the edge
- Greengrass allow some services like compute, messages, data management, sync and ML capabilities to run from edge devices
- Devices with Greengrass Core software can locally run Lambda functions or containers => compute can run locally without leaving the local network
- Greengrass provides local device shadows which are synced back to AWS
- Allows messaging using MQTT
- Allows local hardware access for Lambda functions

## AWS IoT Analytics

- Used to run analytics on IoT data and get insights to make better and more accurate decisions
- Supports up to petabyte of data from millions of devices

## AWS IoT Events

- Used to detect and respond to events from IoT sensors and applications
- We can ingest data from multiple sources to detect the state of our processes or devices and proactively manage maintenance schedules

## AWS IoT SiteWise

- Simplifies collecting, organizing and analyzing industrial equipment data
- We can organize sensor data streams from multiple production lines and facilities to drive efficiencies across locations

## AWS IoT TwinMaker (formerly AWS IoT Things Graph)

- Used to create digital twins of real-world systems such as buildings, factories, industrial equipment and production lines
- We used this to quickly pinpoint and address equipment and process anomalies from the plant floor to improve worker productivity and efficiency