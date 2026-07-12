# SWF - Simple Workflow Service (Serviço Simples de Fluxo de Trabalho)

- Permite-nos construir fluxos de trabalho usados para coordenar atividades em componentes distribuídos (exemplo: fluxo de pedidos)
- Permite construir fluxos de trabalho complexos, automatizados e que envolvem humanos
- É o predecessor do Step Functions, usa instâncias/servidores
- Permite o uso dos mesmos padrões/antipadrões, como fluxos de trabalho de longa duração
- A AWS recomenda usar Step Functions por padrão em vez de SWF; use o SWF apenas se houver um fluxo de trabalho muito específico que exija isso
- Fluxo de trabalho (Workflow): conjunto de atividades que realizam algum objetivo, junto com a lógica que coordena as atividades
- Dentro dos fluxos de trabalho temos tarefas de atividade (activity task) e trabalhadores de atividade (activity workers)
- Um trabalhador (worker) é um programa que criamos para executar tarefas
- Fluxos de trabalho têm decisores (deciders), aplicativos que rodam em uma unidade de computação da AWS
- Decisores agendam tarefas de atividade, fornecem dados de entrada para trabalhadores de atividade, processam eventos e encerram o fluxo de trabalho quando o objetivo é concluído
- Os fluxos de trabalho do SWF podem ser executados por no máximo 1 ano

## SWF vs Step Functions

- Padrão: Step Functions - eles são serverless (sem servidor), exigem menor sobrecarga de administração (admin overhead)
- AWS Flow Framework - maneira de definir fluxos de trabalho suportados pelo SWF
- Sinais externos para intervir no processo, precisamos do SWF
- Lançar fluxos filhos (child flows) e fazer com que o processamento retorne ao pai, precisamos usar o SWF
- Lógica de decisão sob medida/complexa (Bespoke/complex decision logic): use SWF (o aplicativo decisor personalizado pode ser codificado por nós, podemos implementar a lógica que quisermos)
- Integração com o Mechanical Turk: use SWF (arquitetura sugerida pela AWS)

---

# SWF - Simple Workflow Service

- Allows us to build workflows used to coordinate activities over distributed components (example: order flow)
- Allows to build complex, automated and human involved workflows
- It is the predecessor of Step Functions, it uses instances/servers
- It allows the usage of the same patterns/anti patterns like long running workflows
- AWS recommends defaulting to Step Functions instead of SWF, use SWF only if there is very specific workflow that requires it
- Workflow: set of activities that carry out some objective together with the logic that coordinates the activities
- Within workflows we have activity task and activity workers
- A worker is program that we create to perform tasks
- Workflows have deciders, applications that run on an unit of compute of AWS
- Deciders schedule activity tasks, provides input data to activity workers, processes events and ends the workflow when the object is completed
- SWF workflows can run for max 1 year

## SWF vs Step Functions

- Default: Step Functions - they are serverless, they require lower admin overhead
- AWS FLow Framework - way of defining workflows supported by SWF
- External Signals to intervene in process, we need SWF
- Launch child flows and have the processing return to parent, we need ot use SWF
- Bespoke/complex decision logic: use SWF (custom decider application can be coded by us, we can implement whatever logic we want)
- Mechanical Turk integration: use SWF (suggested AWS architecture)