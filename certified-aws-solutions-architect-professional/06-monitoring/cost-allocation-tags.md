# Tags de Alocação de Custos

- São tags que podemos habilitar para fornecer informações adicionais para qualquer relatório de faturamento na AWS
- As Tags de Alocação de Custos precisam ser habilitadas individualmente por conta ou por organização a partir da conta de gerenciamento
- Existem 2 formas diferentes de Tags de Alocação de Custos:
    - Geradas pela AWS - exemplo: `aws:createdBy` ou `aws:cloudformation:stack-name`. Essas são adicionadas automaticamente pela AWS se as tags de alocação de custos estiverem habilitadas
    - Tags definidas pelo usuário: `user:alguma-coisa`
- Ambos os tipos de tags serão visíveis nos relatórios de custo da AWS e podem ser usadas como filtro
- As Tags de Alocação de Custos aparecem apenas no Console de Faturamento
- Após habilitar as Tags de Alocação de Custos, pode levar até 24 horas para que fiquem visíveis e ativas
- As Tags de Alocação de Custos não são adicionadas retroativamente

---

# Cost Allocation Tags

- Are tags that we can enable to provide additional information for any billing report in AWS
- Cost Allocation Tags needs to enabled individually per account or per organization from the management account
- There 2 different form of Cost Allocation Tags:
    - AWS generated - example: `aws:createdBy` or `aws:cloudformation:stack-name`. These are added automatically by AWS if cost allocation tags are enabled
    - User defined tags: `user:something`
- Both type of tags will be visible in AWS cost reports and can be used as a filter
- Cost Allocation Tags appear only int he Billing Console
- After enabling Cost Allocation Tags, it can take up to 24 hours to be visible and active
- Cost Allocation Tags are not added retroactively