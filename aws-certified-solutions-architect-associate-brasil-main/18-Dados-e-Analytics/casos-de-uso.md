# Casos de Uso

## Cenario 1: Pico de acesso em janela curta

**Padrao recomendado:** camada gerenciada com escala automatica e desacoplamento.  
**Motivo:** absorve variacao sem intervencao manual intensa.  
**Sinal de prova:** termos como “pico imprevisivel”, “manter latencia” e “baixo esforco operacional”.

## Cenario 2: Requisito de auditoria e conformidade

**Padrao recomendado:** identidade granular, trilha de auditoria e criptografia fim a fim.  
**Motivo:** garante rastreabilidade e protecao de dado sensivel.  
**Sinal de prova:** “compliance”, “registro de acesso”, “dados sensiveis”.

## Cenario 3: Reducao de custo com mesma experiencia

**Padrao recomendado:** ajustar classe/capacidade pelo perfil real de consumo.  
**Motivo:** evita overprovisioning e reduz gasto recorrente.  
**Sinal de prova:** “otimizacao de custo”, “padrao de uso conhecido”, “sem degradar UX”.

## Cenario 4: Evolucao incremental de arquitetura

**Padrao recomendado:** comecar simples, com componentes gerenciados e pontos de extensao claros.  
**Motivo:** acelera entrega e reduz risco de complexidade prematura.  
**Sinal de prova:** “entrega rapida”, “crescimento gradual”, “equipe pequena”.
