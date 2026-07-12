# Amazon Fraud Detector

- É um serviço de detecção de fraudes totalmente gerenciado
- Permite-nos observar várias tendências históricas e outros dados relacionados para identificar qualquer fraude potencial em relação a certas atividades exclusivas, como criação de novas contas, pagamentos ou finalizações de compras de convidados (guest checkouts)
- Nós fazemos o upload de alguns dados históricos e temos que escolher um tipo de modelo:
    - Fraude Online (Online Fraud): precisa de poucos dados históricos
    - Fraude de Transação (Transaction Fraud): ideal quando temos um histórico transacional de um cliente, identifica pagamentos suspeitos
    - Assunção de Conta (Account Takeover): usado para identificar phishing ou outro ataque de base social
- Os eventos são pontuados (scored), com base nisso podemos criar regras/decisões para reagir a eventos de acordo com a nossa atividade de negócios

---

# Amazon Fraud Detector

- Is a fully managed fraud detection service
- Allows us to look at various historical trends and other related data and identify any potential fraud as it related to certain only activities such as new account creation, payments or guest checkouts
- We upload some historical data and we have to chose a model type:
    - Online Fraud: needs little historical data
    - Transaction Fraud: idean when we have a transactional history for a customer, identifies suspect payments
    - Account Takeover: used to identify phishing or another social based attack
- Events are scored, based on which we can create rules/decisions to react to events according to our business activity