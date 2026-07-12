# CloudFormation

## Recursos Físicos e Lógicos (Physical and Logical Resources)

- O CloudFormation começa com um modelo (template) definido em arquivo YAML ou JSON
- O template contém recursos lógicos (o que queremos criar)
- Templates podem ser usados para criar Stacks (pilhas) do CloudFormation (uma ou várias stacks)
- O trabalho inicial de uma stack é criar recursos físicos com base nos recursos lógicos definidos no template
- Se o template de uma stack for alterado, os recursos físicos também serão alterados
- Se uma stack for excluída, normalmente os recursos físicos serão excluídos

## Pilhas (Stacks)

- Uma stack é uma coleção de recursos da AWS que você pode gerenciar como uma unidade única
- Todos os recursos em uma stack são definidos pelo template do CloudFormation da stack
- Opções da Stack:
    - Tags: pares de chave/valor (key/value) anexados à stack. Podem ser usados para identificar a stack para fins de alocação de custos
    - Permissões: IAM service role (função de serviço) que pode ser assumida pelo CloudFormation
    - Opções de falha da stack (Stack failure options):
        - Especifica o que fazer se algo falhar enquanto a stack é provisionada
        - Opções:
            - Reverter (Roll back) todos os recursos da stack
            - Preservar recursos provisionados com sucesso
    - Política da stack (Stack policy): define os recursos que queremos proteger de atualizações não intencionais durante uma atualização da stack
    - Configuração de reversão (Rollback configuration): podemos monitorar a stack enquanto ela está sendo criada/atualizada e podemos revertê-la caso um limite (threshold) seja violado (exemplo: se algum alarme entrar no estado ALARM)
    - Opções de notificação: podemos especificar um tópico SNS para onde as notificações devem ir
    - Opções de criação da stack (Stack creation options): as seguintes opções estão incluídas para criação da stack, mas não estão disponíveis como parte das atualizações:
        - Tempo limite (Timeout): Especifica a quantidade de tempo, em minutos, que o CloudFormation deve alocar antes de esgotar o tempo limite (timing out) das operações de criação da stack

## Parâmetros de Template e Pseudo Parâmetros

- Os parâmetros de template permitem entrada via console, CLI ou API quando a stack é criada ou atualizada
- Os parâmetros são definidos dentro dos recursos e podem ser referenciados dentro dos recursos lógicos
- Parâmetros podem ter valores padrão (default values), valores permitidos, tamanho mínimo/máximo, padrões permitidos (allowed patterns), no echo (útil para senhas, o valor não é exibido quando digitado) e tipos
- Pseudo Parâmetros:
    - A AWS disponibiliza parâmetros que podem ser referenciados pelo template CF
    - Exemplo:
        - `AWS::Region`
        - `AWS::StackId`
        - `AWS::StackName`
        - `AWS::AccountId`
    - Pseudo parâmetros são parâmetros que não podem ser preenchidos por nós, eles são preenchidos pela AWS e fornecidos para que possamos referenciá-los
- Parâmetros fornecem portabilidade para o template
- Melhores práticas (Best practice):
    - Minimize o número de parâmetros e forneça padrões (defaults) quando aplicável
    - Use pseudo parâmetros sempre que possível

## Funções Intrínsecas (Intrinsic Functions)

- Funções intrínsecas podem ser usadas em templates para atribuir valores a propriedades que não estão disponíveis até o tempo de execução (runtime)
- Exemplos de funções:
    - `Ref` e `Fn::GetAtt`: referenciam um valor de um recurso lógico
    - `Fn::Join` e `Fn::Split`: juntam/separam strings para criar novas
    - `Fn::GetAZs` e `Fn::Select`: obtém zonas de disponibilidade (AZs) em uma região e seleciona uma
    - Condições: `Fn::IF`, `And`, `Equals`, `Not`, `Or`
    - `Fn::Base64` e `Fn::Sub`: codifica strings para base64, substitui variáveis no texto (substitute replacement)
    - `Fn::Cidr`: constrói blocos CIDR
- `Fn::GetAZs` - retorna as AZs disponíveis na região. Se a região tiver uma VPC padrão configurada, ela retorna as AZs que estão disponíveis na VPC padrão

## Mapeamentos (Mappings)

- Templates podem conter um objeto `Mappings` que pode conter chaves (keys) para objetos de valores (values)
- Os mapeamentos podem ter um nível ou chaves de segundo nível
- Os mapeamentos usam outra função intrínseca `Fn::FindInMap`
- Os mapeamentos são usados para melhorar a portabilidade do template
- Exemplo:
    ```
    Mappings:
        RegionMap:
            us-east-1:
                HVM64: 'ami-xxx'
                HVMG2: 'ami-yyy'
            us-east-2:
                HVM64: 'ami-zzz'
                HVMG2: 'ami-vvv'
    ```

## Saídas (Outputs)

- A seção `Outputs` em um template é opcional
- Podemos declarar valores nesta seção que ficarão visíveis como saída no CLI/Console
- A saída (Output) estará acessível de uma stack pai (parent stack) ao usar aninhamento (nesting)
- As saídas podem ser exportadas, permitindo referências entre stacks (cross-stack references)
- Exemplo:
    ```
    Outputs:
        WordPressUrl:
            Description: 'texto de descrição'
            Value: !Join['', 'https://', !GetAtt Instance.DNSName]
    ```

## Condições (Conditions)

- Permite que a stack reaja a certas condições e mude a infraestrutura com base nelas
- São declaradas numa seção opcional chamada `Conditions`
- Podemos declarar muitas condições, cada uma delas sendo avaliada como `TRUE` (VERDADEIRO) ou `FALSE` (FALSO)
- Condições são avaliadas antes da criação dos recursos
- Condições usam outras funções intrínsecas: `AND`, `EQUALS`, `IF`, `NOT`, `OR`
- Qualquer recurso pode ter uma condição associada que definirá se o recurso será criado ou não
- Exemplos: podemos ter condições que são avaliadas com base no ambiente (dev, test, prod) em que o template é executado
- Exemplo de condição:
    ```
    Conditions:
        IsProd: !Equals
            - !Ref EnvType
            - `prod`
    ```
- Condições podem ser aninhadas (nested)

## DependsOn (Depende De)

- Permite-nos estabelecer dependências entre recursos
- O CFN tenta ser eficiente criando/atualizando/excluindo recursos em paralelo
- Além disso, ele tenta determinar uma ordem de dependência (exemplo: VPC => SUBNET => EC2) usando referências ou funções
- A dependência pode ser definida usando a propriedade `DependsOn` para especificar o recurso do qual dependemos
- `DependsOn` pode aceitar um único recurso ou uma lista de recursos

## Políticas de Criação, Condições de Espera e cfn-signal (Creation Policies, Wait Conditions and cfn-signal)

- As Políticas de Criação, Condições de Espera e sinais do cfn (cfn-signals) fornecem algumas maneiras de notificar o CFN com detalhes (sinais) sobre a conclusão ou não da criação de recursos
- Podemos configurar o CFN para aguardar um determinado número de sinais de sucesso
- Também configuramos um tempo limite (timeout) dentro do qual os sinais são recebidos (máximo de 12H)
- Se o número de sinais de sucesso for recebido dentro do tempo limite, as stacks do CFN mudam para `CREATE_COMPLETE`
- O `cfn-signal` é um utilitário (utility) rodando nas instâncias EC2 enviando sinais de sucesso/falha ao CFN
- Se o tempo limite for atingido e o número de sinais de sucesso não for alcançado, a criação da stack falhará
- Para o provisionamento de EC2 e ASG, devemos usar uma `CreationPolicy` (Política de Criação)
- Para outros requisitos, podemos optar por usar uma `WaitCondition` (Condição de Espera)
- Uma `WaitCondition` é definida como um recurso lógico, o que significa que pode ter a propriedade `DependsOn`. Ela pode ser usada como um portão (gait/gate) de progresso geral no template
- Uma `WaitCondition` depende de um `WaitHandle` (Identificador de Espera), que é outro recurso lógico. Seu trabalho é gerar uma URL pré-assinada (presigned url) que pode ser usada para enviar sinais à `WaitCondition`
- Com o `WaitHandle` podemos repassar (pass back) dados para o template. Esses dados podem ser recuperados usando a função `!GetAtt WaitCondition.Data`

## Stacks Aninhadas (Nested Stacks)

- A maioria dos projetos simples utilizará geralmente uma stack CFN
- Stacks podem ter limites:
    - Limite de recursos: 500 recursos por stack
    - Não podemos reutilizar recursos facilmente, exemplo referenciar uma VPC
- Existem 2 maneiras de arquitetar projetos multi-stack:
    - Stacks Aninhadas (Nested Stacks)
    - Referências entre Stacks (Cross-Stack References)
- Nested Stacks:
    - Root Stack (Stack Raiz): a stack que é criada primeiro, criada manualmente ou usando alguma automação
    - Uma Parent Stack (Stack Pai) é a controladora de qualquer stack que ela cria imediatamente
    - Uma stack raiz pode criar stacks aninhadas tendo várias stacks pai
    - Uma stack raiz pode ter parâmetros e saídas (assim como uma stack normal)
- Uma stack pode ter outra stack do CFN como recurso usando o tipo `AWS::CloudFormation::Stack` que precisa de uma url para o template
- Podemos fornecer valores de entrada para as stacks aninhadas. Precisamos fornecer valores a quaisquer parâmetros de uma stack aninhada se o parâmetro não tiver um valor padrão definido
- Quaisquer saídas (outputs) de uma stack aninhada são retornadas para a stack raiz, podendo ser referenciadas como `NESTEDStack.Outputs.XXX`
- O benefício de uma stack aninhada é reutilizar o mesmo template, e não a stack real criada
- Devemos usar stacks aninhadas quando quisermos vincular os ciclos de vida de diferentes stacks

## Referências Entre Stacks (Cross-Stack References)

- Stacks CFN são projetadas para serem isoladas e autossuficientes (self-contained)
- Com stacks aninhadas podemos reutilizar apenas o código; com referências cross-stack podemos referenciar recursos criados por outras stacks
- As saídas (Outputs) normalmente não são visíveis a partir de outras stacks, com exceção de stacks aninhadas onde a stack pai pode referenciar a saída da stack aninhada
- As saídas de um template podem ser exportadas tornando-as visíveis a partir de outras stacks
- As exportações (Exports) devem ter nomes únicos na região
- Para usar os recursos exportados, podemos usar a função intrínseca `Fn::ImportValue`
- Cross-region (inter-região) ou cross-account (entre contas) não é suportado para referências cross-stack

## StackSets (Conjuntos de Stacks)

- Permite criar/atualizar/excluir infraestrutura em muitas regiões ou muitas contas
- StackSets são contêineres numa conta de administrador (conta onde o StackSet é aplicado, não precisa ser nenhuma conta especial)
- StackSets contêm instâncias de stack (stack instances - contêineres para stacks individuais) que referenciam stacks
- Instâncias de stack e stacks são criadas em contas de destino (target accounts)
- Cada stack criada por um StackSet é uma stack criada em uma região em uma conta
- Segurança: podemos usar funções gerenciadas por conta própria (self-managed roles) ou funções gerenciadas pelo serviço (service-managed roles - tudo tratado pelo produto). O CFN assumirá uma função (role) para interagir com as contas de destino
- Terminologia:
    - Contas Concorrentes (Concurrent Accounts): um valor especificando em quantas contas podemos implantar ao mesmo tempo
    - Tolerância a Falhas (Failure Tolerance): quantidade de implantações individuais que podem falhar antes de declarar o próprio StackSet como falho
    - Reter Stacks (Retain Stacks): remove instâncias de stack de um StackSet, mas retém a infraestrutura
- Casos de uso de StackSet:
    - Criar Regras do AWS Config
    - Criar IAM Roles (Funções do IAM) para acesso entre contas (cross-account)

## DeletionPolicy (Política de Exclusão)

- Se excluirmos um recurso lógico de um template, por padrão o recurso físico será excluído pelo CFN
- Com certos tipos de recursos isso pode causar perda de dados
- Com a política de exclusão (deletion policy), podemos definir em cada recurso para **Delete** (excluir - padrão), **Retain** (reter) ou **Snapshot** (se compatível)
- Os recursos suportados para snapshot são: volumes EBS, ElastiCache, Neptune, RDS, Redshift
- Com o snapshot, antes do recurso físico ser excluído, um snapshot é feito
- As políticas de exclusão se aplicam apenas à operação de exclusão (delete), NÃO à operação de substituição (replace)!

## Stack Roles (Funções de Stack)

- Por padrão, o CFN usa as permissões da identidade que inicia a criação da stack
- As funções de stack do CFN (CFN stack roles) são um recurso em que o CFN pode assumir uma função (role) para ganhar permissões e criar recursos de uma stack, sem a necessidade do iniciador ter as permissões necessárias
- A identidade que cria a stack não precisa de permissões de recurso, apenas `PassRole`

## `AWS::CloudFormation::Init` e `cfn-init`

- CloudFormationInit é um sistema simples de gerenciamento de configurações
- Diretivas de configuração são armazenadas no template
- `AWS::CloudFormation::Init` é parte do recurso lógico da instância EC2. Com ele podemos especificar configurações que serão aplicadas à instância EC2 criada
- O User Data é procedural (COMO as coisas devem ser feitas) / o `cfn-init` é um estado desejado (O QUE queremos que ocorra)
- `cfn-init` pode ser multiplataforma (cross-platform) e idempotente
- O acesso aos dados do CFN init é feito com o script auxiliar `cfn-init` que deve ser instalado na instância

## `cfn-hup`

- `cfn-init` é uma ferramenta auxiliar (helper tool) que roda apenas uma vez como parte do bootstrapping (user data)
- Se o `AWS::CloudFormation::Init` for atualizado, o `cfn-init` não rodará novamente
- `cfn-hup` é uma ferramenta auxiliar que pode ser instalada nas instâncias EC2
- Ela detectará alterações nos metadados (metadata) dos recursos
- Quando a alteração é detectada, ela pode rodar ações configuráveis. Pode rodar o `cfn-init` novamente se necessário

## Conjuntos de Alterações (Change Sets)

- Os Change Sets nos permitem prever as alterações que acontecerão após atualizarmos uma stack
- Podemos ter vários change sets e visualizar cada um deles
- Podemos escolher qual change set queremos aplicar executando-o

## Custom Resources (Recursos Personalizados)

- O CloudFormation não suporta tudo na AWS
- Os Custom Resources permitem que o CFN se integre a qualquer coisa que ele ainda não suporte ou que não vá suportar de jeito nenhum
- Com Custom Resources podemos estender o CFN para fazer coisas que ele não suporta nativamente (exemplo: buscar configuração de terceiros)
- Arquitetura de custom resources:
    - O CFN envia dados para um endpoint (ponto de extremidade) definido no custom resource
    - Esse endpoint pode ser uma função Lambda ou um tópico SNS
    - Quando um custom resource é criado/atualizado/excluído, o CFN envia eventos para esse endpoint contendo a operação e quaisquer informações de propriedades adicionais
    - A computação (função Lambda) pode responder a esses dados personalizados, informando-o sobre o sucesso/falha de sua execução

---

# CloudFormation

## Physical and Logical Resources

- CloudFormation begins with a template defined in YAML or JSON file
- The template contains logical resources (what we want to create)
- Templates can be used to create CloudFormation Stacks (one ore many stacks)
- The initial job of a stack is to create physical resources based on the logical resources defined in the template
- If a stack's template are changed, physical resources are changed as well
- If a stack is deleted, normally the physical resources are deleted

## Stacks

- A stack is a collection of AWS resources that you can manage as a single unit
- All the resources in a stack are defined by the stack's CloudFormation template
- Stack options:
    - Tags: key/value pairs attached to the stack. Can be used to identify the stack for cost allocation purposes
    - Permissions: IAM service role that can be assumed by CloudFormation
    - Stack failure options:
        - Specifies what to do if something fails while the stack is provisioned
        - Options:
            - Roll back all stack resources
            - Preserve successfully provisioned resources
    - Stack policy: defines the resources that we want to protect from unintentional updates during a stack update
    - Rollback configuration: we can monitor the stack while it is being created/updated and we can roll it back in case a threshold is breached (example if any alarm goes to ALARM state)
    - Notification options: we can specify an SNS topic where notifications should go
    - Stack creation options: following options are included for stack creation, but aren't available as part of stack updates:
        - Timeout: Specifies the amount of time, in minutes, that CloudFormation should allot before timing out stack creation operations

## Template Parameters and Pseudo Parameters

- Template parameters allow input via the console, CLI or API when the stack is created or updated
- Parameters are defined within the resources and they can be referenced from within the logical resources
- Parameters can have default values, allowed values, min/max length, allowed patterns, no echo (useful for passwords, the value is not displayed when typed) and types
- Pseudo Parameters: 
    - AWS makes available parameters which can be referenced by the CF template
    - Example:
        - `AWS::Region`
        - `AWS::StackId`
        - `AWS::StackName`
        - `AWS::AccountId`
    - Pseudo parameters are parameters which can not be populated by us, they are populated by AWS and provided for us to reference them
- Parameters provide portability for the template
- Best practice:
    - Minimize number of parameters and provide defaults where applicable
    - Use pseudo parameters where possible

## Intrinsic Functions

- Intrinsic functions can be used in templates to assign values to properties that are not available until runtime
- Examples of functions:
    - `Ref` and `Fn::GetAtt`: reference a value from one logical resource
    - `Fn::Join` and `Fn::Split`: join/split strings to create new ones
    - `Fn::GetAZs` and `Fn::Select`: get availability zones in a regions and select one
    - Conditions: `Fn::IF`, `And`, `Equals`, `Not`, `Or`
    - `Fn::Base64` and `Fn::Sub`: encode strings to base64, substitute replacement on variables in the text
    - `Fn:Cidr`: build CIDR blocks
- `Fn::GetAZs` - returns the available AZs in region. If the region has a default VPC configured, it return the AZs which are available in the default VPC

## Mappings

- Templates can contain a `Mappings` objects which can contain keys to values objects
- Mappings can have one level or tep and second level keys
- Mappings use another intrinsic function `Fn::FindInMap`
- Mappings are used to improve template portability
- Example:
    ```
    Mappings:
        RegionMap:
            us-east-1:
                HVM64: 'ami-xxx'
                HVMG2: 'ami-yyy'
            us-east-2:
                HVM64: 'ami-zzz'
                HVMG2: 'ami-vvv'
    ```

## Outputs

- The `Outputs` section in a template is optional
- We can declare values in this section which will be visible as output in the CLI/Console
- Output will be accessible from a parent stack when using nesting
- Outputs can be exported allowing cross-stack references
- Example:
    ```
    Outputs:
        WordPressUrl:
            Description: 'description text'
            Value: !Join['', 'https://', !GetAtt Instance.DNSName]
    ```

## Conditions

- Allows stack to react to certain conditions and change infrastructure based on those
- They declared in an optional section named `Conditions`
- We can declare many conditions, each of them being evaluated to `TRUE` or `FALSE`
- Conditions are evaluated before resources are created
- Conditions use other intrinsic functions: `AND`, `EQUALS`, `IF`, `NOT`, `OR`
- Any resource can have associated a condition which will define if the resource will be created or not
- Examples: we can have conditions which evaluate based on the environment (dev, test, prod) in which the template is executed
- Condition example:
    ```
    Conditions:
        IsProd: !Equals
            - !Ref EnvType
            - `prod`
    ```
- Conditions can be nested

## DependsOn

- Allows us to establish dependencies between resources
- CFN tried to be efficient by creating/updating/deleting resources in parallel
- Also, it tries to determine a dependency order (example: VPC => SUBNET => EC2) by using references or functions
- Dependency can be defined using the `DependsOn` property specify the resource on which we depend on
- `DependsOn` can accept a single resource or a list of resources

## Creation Policies, Wait Conditions and cfn-signal

- Creation Policies, Wait Conditions and cfn-signals provide a few ways to notify CFN with details signals on completion or not of creation of resources
- We can configure CFN to wait for a certain number of success signals
- We also configure a timeout within which the signals are received (max 12H)
- The the number of success signals are received within the timeout, CFN stacks moves to `CREATE_COMPLETE`
- `cfn-signal` is an utility running on the EC2 instances sending success/failure signals to CFN
- If the timeout is reached and the number of success signals are not met, the stack will fail creation
- For provisioning EC2 and ASG, we should us a `CreationPolicy`
- For other requirements we might chose to use a `WaitCondition`
- A `WaitCondition` is defined as a logical resource, meaning it can have `DependsOn` property. It can be used as a general progress gait in the template
- A `WaitCondition` relies on a `WaitHandle`, which is another logical resource. Its job is to generate a presigned url which can be used to send signals to `WaitCondition`
- With `WaitHandle` we can pass back data to the template. This data can be retrieved using the `!GetAtt WaitCondition.Data` function

## Nested Stacks

- Most simple projects will generally utilize a CFN stack
- Stacks can have limits:
    - Resource limit: 500 resources per stack
    - We can't easily reuse resources, example reference a VPC
- There are 2 ways to architect multi-stack projects:
    - Nested Stacks
    - Cross-Stack References
- Nested Stacks:
    - Root Stack: the stack which is created first, created manually or using some automation
    - A Parent Stack is the parent of any stack which it immediately creates
    - A root stack can create nested stacks having several parent stacks
    - A root stack can have parameters and outputs (just like a normals stack)
- A stack can have another CFN stack as a resource using `AWS::CloudFormation::Stack` type which needs an url to the template
- We can provide input values to the nested stacks. We need to supply values to any parameters from a nested stack if the parameter does not have a default value defined
- Any outputs of a nested stack are returned to the root stack which can be referenced as `NESTEDStack.Outputs.XXX`
- Benefits of a nested stack is to reuse the same template, not the actual stack created
- We should use nested stacks when we want to link the life cycles of different stacks

## Cross-Stack References

- CFN stacks are designed to be isolated and self-contained
- With nested stacks we can reuse code only, with cross-stack references we can reference resources created by other stacks
- Outputs are normally not visible from other stacks, exception being nested stacks which case the parent stack can reference the nested stack output
- Outputs of a template can be exported making them visible from other stacks
- Exports must have unique names in the region
- To use the exported resources we can use `Fn::ImportValue` intrinsic function
- Cross-region or cross-account is not supported for cross-stack references

## StackSets

- Allows to create/update/delete infrastructure across many regions or many accounts
- StackSets are containers in an admin account (account where the StackSet is applied, it does not have to be any special account)
- StackSets contain stack instances (containers for individual stacks) which reference stacks
- Stack instances and stacks are created in target accounts
- Each stack created by a StackSet is a stack created in one region in one account
- Security: we can use self-managed roles or service-managed roles (everything handled by the product). CFN will assume a role to interact with the target accounts
- Terminology:
    - Concurrent Accounts: a value specifying how in how many accounts can we deploy at the same time
    - Failure Tolerance: amount of individual deployments which can fail before declaring the StackSet itself as failed
    - Retain Stacks: remove stack instances from a StackSet but retain the infrastructure
- StackSet use cases:
    - Crate AWS Config Rules
    - Create IAM Roles for cross-account access

## DeletionPolicy

- If we delete a logical resource from a template, by default the physical resource will be deleted by CFN
- With certain type of resources this can cause data loss
- With deletion policy, we can define on each resource to **Delete** (default), **Retain** or **Snapshot** (if supported)
- Supported resources for snapshot are: EBS volumes, ElastiCache, Neptune, RDS, Redshift
- With snapshot before the physical resource is deleted, a snapshot is taken
- Deletion policies only apply to delete operation, NOT replace operation!

## Stack Roles

- By default CFN uses the permissions of the identity who initiates the stack creation
- CFN stack roles is feature where CFN can assume a role to gain permissions to create resources from a stack without the need for the initiator to have the necessary permissions
- The identity creating the stack does not need resource permissions, only `PassRole`

## `AWS::CloudFormation::Init` and `cfn-init`

- CloudFormationInit is a simple configuration management system
- Configuration directive are stored in the template
- `AWS::CloudFormation::Init` is part of EC2 instance logical resource. With this we can specify configurations which will be applied to the created EC2 instance
- User Data is procedural (HOW should things to be done) / `cfn-init` is a desired state (WHAT we want to occur)
- `cfn-init` can be cross-platform and idempotent
- Accessing the CFN init data is done with the `cfn-init` helper script which should be installed on the instance

## `cfn-hup`

- `cfn-init` is a helper tool running once as part of bootstrapping (user data)
- If the `AWS::CloudFormation::Init` is updated, `cfn-init` is not rerun
- `cfn-hup` is a helper tool which can be installed on EC2 instances
- It will detect changes in the resources metadata
- When change is detected, it can run configurable actions. It might rerun `cfn-init` if necessary

## Change Sets

- Change Sets let us preview the changes that will happen after we update a stack
- We can have multiple change sets and preview each of them
- We can chose which change set we want to apply by executing it

## Custom Resources

- CloudFormation doesn't support everything in AWS
- Custom Resources let CFN integrate with anything it does not yet support or wont support at all
- With Custom Resources we can extend CFN to do things which it does not natively support (example: fet configuration from a third party)
- Architecture of custom resources:
    - CFN sends data to an endpoint defined in the custom resource
    - This endpoint might be a Lambda function or an SNS topic
    - When a custom resources is created/update/deleted, CFN sends events to this endpoint containing the operation and any additional property information
    - The compute (Lambda function) can respond to this custom data, letting it know of the success/failure of its execution