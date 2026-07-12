# AWS Systems Manager Parameter Store

- Usado para armazenar configurações do sistema (documentos, configurações, segredos, strings) de maneira resiliente, segura e escalável
- Armazena dados num formato chave-valor (key-value)
- Muitos serviços da AWS têm integração nativa com o Parameter Store
- O Parameter Store oferece a disponibilidade para armazenar 3 tipos diferentes de valores: Strings, Listas de Strings (StringLists) e Strings Seguras (SecureStrings)
- Podemos armazenar códigos de licença, strings de banco de dados, configurações completas e senhas no Parameter Store
- Os valores podem ser armazenados de forma hierárquica. Diferentes versões dos valores também são armazenadas
- O Parameter Store pode armazenar texto simples (plaintext) e texto cifrado (ciphertext), que pode ser descriptografado usando a integração com o KMS
- Parâmetros Públicos (Public Parameters): parâmetros mantidos e fornecidos pela AWS, exemplo: AMIs mais recentes por região
- O Parameter Store é um serviço público
- O Parameter Store é fortemente integrado ao IAM

---

# AWS Systems Manager Parameter Store

- Used to store system configurations (documents, configurations, secrets, strings) in a resilient, secure and scalable way
- Stores data in a key-value format
- Many AWS services have native integration with Parameter Store
- Parameter store offers the availability to store 3 different type of values: Strings, StringLists and SecureStrings
- We can store license codes, database strings, full configs and passwords in Parameter Store
- Values can be stored in a hierarchical way. Different versions of the values are also stored
- Parameter Store can store plaintext and ciphertext which can be decrypted using the KMS integration
- Public Parameters: parameters maintained and provided by AWS, example: latest AMIs per region
- Parameter Store is public service
- Parameter Store is tightly integrated with IAM