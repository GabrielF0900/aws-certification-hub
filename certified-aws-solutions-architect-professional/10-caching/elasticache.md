# ElastiCache

- É um banco de dados em memória (in-memory database) para aplicações que precisam de alto desempenho (high-end performance)
- É ordens de magnitude mais rápido que um BD clássico, mas não possui persistência (is not persistence)
- O ElastiCache fornece 2 mecanismos (engines) diferentes: Managed Redis (Redis gerenciado) e MemcacheD como um serviço
- O ElastiCache pode ser usado para cargas de trabalho com muitas leituras (read heavy workloads) com requisitos de baixa latência
- Pode ser usado para a redução de cargas de trabalho de banco de dados, reduzindo assim o custo acumulado pelo uso intenso do banco de dados
- Pode ser usado para armazenar dados de sessão, tornando aplicações stateful (com estado) em stateless (sem estado)
- O uso do ElastiCache requer alterações no código da aplicação!

## Redis vs MemcacheD

- Ambos oferecem acesso aos dados em tempo inferior a um milissegundo (sub-millisecond)
- O MemcacheD suporta estruturas de dados simples (string), enquanto o Redis pode suportar tipos de dados mais avançados: listas, conjuntos (sets), conjuntos ordenados (sorted sets), hashes, arrays de bits (bit arrays), etc.
- O Redis suporta a replicação de dados em várias Zonas de Disponibilidade (AZs), o MemcacheD suporta vários nós (nodes) com sharding (fragmentação) manual, mas não suporta "verdadeira" replicação entre AZs por razões de escalabilidade
- O Redis suporta backups e restaurações, o MemcacheD não suporta persistência
- O MemcacheD é multithread (múltiplas linhas de execução) por design, pode aproveitar melhor CPUs multithread e pode oferecer melhor desempenho
- O Redis suporta transações (várias operações de uma só vez)
- Ambos os motores podem suportar uma variedade de tipos de instâncias

---

# ElastiCache

- It is an in-memory database for application which need high-end performance
- It is orders of magnitude faster than a classic DB, but is not persistence
- ElastiCache provides 2 different engines: Managed Redis and MemcacheD as a service
- ElastiCache can be used for read heavy workloads with low latency requirements
- Can be used for reduction of database workloads, by this reducing cost accumulated by heavy database usage
- Can be used to store session date, making stateful applications stateless
- Using ElastiCache requires application code changes!

## Redis vs MemcacheD

- Both offer sub-millisecond access to data
- MemcacheD supports simple data structures (string), while Redis can support more advanced type of data: lists, sets, sorted sets, hashes, bit arrays, etc.
- Redis supports replication of data across multiple AZs, MemcacheD supports multiple nodes with manual sharding, but it does not supports "true" replication across AZs for scalability reasons
- Redis supports backups and restores, MemcacheD does not support persistance
- MemcacheD is multi-threaded by design, can take better advantage of multithreaded CPUs, can offer better performance
- Redis supports transactions (multiple operations at once)
- Both of these engines can support a ranges of instance types