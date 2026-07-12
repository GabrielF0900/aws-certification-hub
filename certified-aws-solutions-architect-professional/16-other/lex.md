# Amazon Lex e Amazon Connect

## Amazon Lex

- Fornece interfaces de conversação (conversational interfaces) por texto ou voz (Lex para voz, Lex para Alexa)
- Alimenta o serviço Alexa
- O Lex fornece 2 principais partes de funcionalidade:
    - Reconhecimento automático de fala (ASR - Automatic speech recognition) - fala em texto
    - Compreensão de Linguagem Natural (NLU - Natural Language Understanding) - intenção (intent)
- O Lex nos permite incorporar a compreensão de voz e texto aos nossos aplicativos
- Escala bem, integra-se com outros serviços da AWS, é rápido de implantar e tem um modelo de precificação de pagamento conforme o uso (pay as you go)
- Casos de uso:
    - Chatbots
    - Assistentes de Voz
    - Bots de Perguntas e Respostas (Q&A Bots)
    - Bots de Informação/Empresariais (Info/Enterprise Bots)

## Amazon Connect

- É um contact center (central de atendimento) como serviço
- Não requer infraestrutura on-premises (local)
- É omnichannel (omnicanal): voz e chat, entrada (incoming) e saída (outgoing)
- Integra-se com redes PSTN para voz tradicional, permitindo-nos aceitar chamadas recebidas e fazer chamadas de saída usando as redes de telefonia celular tradicionais
- Os agentes podem se conectar usando a internet de qualquer lugar
- O AWS Connect pode se integrar com outros serviços, como Lambda/Lex, para inteligência e recursos adicionais
- É rápido de provisionar, fornece precificação pay as you go. É escalável

---

# Amazon Lex and Amazon Connect

## Amazon Lex

- Provides text or voice conversational interfaces (Lex for voice, Lex for Alexa)
- Powers the Alexa service
- Lex provides 2 main bits of functionality:
    - Automatic speech recognition (ASR) - speech to text
    - Natural Language Understanding (NLU) - intent
- Lex allows us to build voice and text understanding into our applications
- It scales well, integrates with other AWS services, it is quick to deploy and it has a pay as you go pricing model
- Use cases:
    - Chatbots
    - Voice Assistants
    - Q&A Bots
    - Info/Enterprise Bots

## Amazon Connect

- It is a contact center as a service
- Requires no infrastructure in on-premises
- It is omnichannel: voice and chat, incoming and outgoing
- Integrates with PSTN networks for traditional voice, allowing us to accept incoming calls and make outgoing calls using the traditional cellular phone networks
- Agents can connect using the internet from anywhere
- AWS Connect can integrate with other services such as Lambda/Lex for additional intelligence and features
- It is quick to provision, provides a pay as you go pricing. It is scalable