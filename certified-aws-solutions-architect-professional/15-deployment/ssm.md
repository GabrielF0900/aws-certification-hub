# AWS Systems Manager (SSM)

- É um produto que nos permite gerenciar e controlar infraestrutura da AWS e on-premise (local)
- O SSM é baseado em agente, o que significa que um agente precisa ser instalado em AMIs baseadas em Windows e Linux
- O SSM gerencia o inventário (quais aplicativos estão instalados, arquivos, configuração de rede, detalhes de hw, serviços, etc.) e pode aplicar patches em ativos (assets)
- Ele também pode executar comandos e gerenciar o estado desejado das instâncias (exemplo: bloquear certas portas)
- Fornece um parameter store (armazenamento de parâmetros) para configurações e segredos (secrets)
- Por fim, fornece o session manager (gerenciador de sessão) usado para conectar com segurança a instâncias EC2, mesmo em VPCs privadas

## Arquitetura do Agente (Agent Architecture)

- Uma instância precisa que o agente do SSM esteja instalado para poder ser gerenciada pelo serviço
- Também precisa de uma função (role) de instância EC2 anexada a ela que permita a comunicação com o serviço
- As instâncias requerem conectividade com o serviço SSM. Isso pode ser feito via IGW (Internet Gateway) ou VPCE (VPC Endpoint)
- No lado on-premises, precisamos criar ativações de instâncias gerenciadas (managed instance activations)
- Para cada ativação receberemos um código de ativação e um ID de ativação

## Comando de Execução do SSM (SSM Run Command)

- Permite-nos rodar comandos em instâncias gerenciadas
- Ele recebe um Documento de Comando (Command Document) e o executa usando o agente instalado na instância
- Ele faz isso sem usar o protocolo SSH/RDP
- Documentos de comando podem ser executados em instâncias individuais, múltiplas instâncias com base em tags ou grupos de recursos (resource groups)
- Documentos de comando podem ser reutilizados e podem ter parâmetros de entrada
- Controle de Taxa (Rate Control): se estivermos rodando comandos em muitas instâncias, podemos controlá-lo usando o rate control. Pode ser baseado em:
    - **Concurrency (Simultaneidade)**: em quantas instâncias o comando deve ser rodado por vez
    - **Error Threshold (Limite de Erro)**: define quantos comandos individuais podem falhar
- A saída (output) dos comandos pode ser enviada para o S3 ou podemos enviar notificações via SNS
- Os comandos podem ser integrados ao EventBridge

## SSM Patch Manager (Gerenciador de Patches do SSM)

- Permite aplicar patches em instâncias Linux e Windows rodando no EC2 ou on-premises
- Conceitos:
    - **Patch Baseline (Linha de base de patch)**: podemos ter muitas destas definidas. Define o que deve ser instalado (quais patches, quais hot-fixes)
    - **Patch Groups (Grupos de patches)**: quais recursos queremos atualizar (patch)
    - **Maintenance Windows (Janelas de Manutenção)**: janelas de tempo em que as atualizações (patches) podem ocorrer
    - **Run Command (Comando de Execução)**: funcionalidade de nível básico para executar o processo de patching. O comando usado para patching é `AWS-RunPatchbaseline`
    - **Concurrency (Simultaneidade)** e **Error Threshold (Limite de Erro)**: (veja acima)
    - **Compliance (Conformidade)**: depois que os patches são aplicados, o system manager pode verificar o sucesso da conformidade em comparação com o que é esperado
- Linhas de base de patch (Patch Baselines):
    - Para Linux: `AWS-[OS]DefaultPatchBaseline` - define patches explicitamente, exemplo: `AWS-AmazonLinux2DefaultPatchBaseline`, `AWS-UbuntuDefaultPatchBaseline` - contêm atualizações de segurança e qualquer atualização crítica
    - Para Windows: `AWS-DefaultPatchBaseline`, `AWS-WindowsPredefinedPatchBaseline-OS`, `AWS-WindowsPredefinedPatchBaseline-OS-Application` - Contêm patches para aplicativos MS também.

---

# AWS Systems Manager (SSM)

- Is a product which lets us manage and control AWS and on-premise infrastructure
- SSM is agent based, which means an agent needs to be installed on Windows and Linux based AMIs
- SSM manages inventory (what application are installed, files, network config, hw details, services, etc.) and can patch assets
- It can also run commands and manage desired state of instances (example: block certain ports)
- It provides a parameters store for configurations and secrets
- Finally it provides session manager used to securely connect to EC2 instances even in private VPCs

## Agent Architecture

- An instances needs the SSM agent to be installed in order to be able to be managed by the service
- It also needs an EC2 instance role attached to it which allows communication with the service
- Instances require connectivity to the SSM service. This can be done via IGW or VPCE
- On the on-premises side we need to create managed instance activations
- For each activation we will receive an activation code and an activation ID

## SSM Run Command

- It allows us to run commands on managed instances
- It takes a Command Document and executes it using the agent installed on the instance
- It does this without using SSH/RDP protocol
- Command documents can be executed on individual instances, multiple instances based on tags or resource groups
- Command documents can be reused and they can have input parameters
- Rate Control: if we are running commands on lot of instances, we can control it by using rate control. It can be based on:
    - **Concurrency**: on how many instances must run the command at a time
    - **Error Threshold**: defines how many individual commands can fail
- Output of commands can be sent to S3 or we can send SNS notifications
- Commands can be integrated with EventBridge

## SSM Patch Manager

- Allows to patch Linux and Windows instances running in EC2 or on-premises
- Concepts:
    - **Patch Baseline**: we can have many of these defined. Defines what should be installed (what patches, what hot-fixes)
    - **Patch Groups**: what resources we want to patch
    - **Maintenance Windows**: time slots when patches can take place
    - **Run Command**: base level functionality to perform the patching process. The command used for patching is `AWS-RunPatchbaseline`
    - **Concurrency** and **Error Threshold**: (see above)
    - **Compliance**: after patches are applied, system manager can check success of compliance compared to what is expected
- Patch Baselines:
    - For Linux: `AWS-[OS]DefaultPatchBaseline` - explicitly defines patches, example: `AWS-AmazonLinux2DefaultPatchBaseline`, `AWS-UbuntuDefaultPatchBaseline` - contain security updates and any critical update
    - For Windows: `AWS-DefaultPatchBaseline`, `AWS-WindowsPredefinedPatchBaseline-OS`, `AWS-WindowsPredefinedPatchBaseline-OS-Application` - Contains patches for MS applications as well.
