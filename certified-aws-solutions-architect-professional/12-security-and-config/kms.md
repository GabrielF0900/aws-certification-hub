# Criptografia e KMS

## Abordagens de Criptografia

- **Criptografia em Repouso (Encryption At Rest)**: projetada para proteger contra ameaças físicas ou adulterações (tempering)
    - Os dados são armazenados em hardware compartilhado de forma criptografada; mesmo que alguém tenha acesso ao hardware, não poderá acessar os dados num formato legível
    - Geralmente usado quando uma parte está envolvida
- **Criptografia em Trânsito (Encryption In Transit)**: visa proteger os dados quando transferidos entre 2 lugares
    - Geralmente usado quando vários indivíduos/sistemas estão envolvidos

## Conceitos de Criptografia

- Texto simples (Plaintext): dados não criptografados, podem ser texto, imagem, outro aplicativo, etc.
- Algoritmo: pedaço de código que recebe texto simples e uma chave (key) e gera dados criptografados. Exemplos de algoritmos: Blowfish, AES, RC4, DES, RC5 e RC6
- Chave (Key): é uma senha
- Texto cifrado (Ciphertext): quando um algoritmo recebe o texto simples e a chave, a saída gerada é o cyphertext (dados criptografados)

## Criptografia Simétrica

- Chaves Simétricas (Symmetric Keys): a mesma chave pode ser usada tanto para criptografia quanto para descriptografia
- Algoritmos de criptografia simétrica: AES-256
- Ótima para criptografia em repouso, não recomendada para criptografia em trânsito

## Criptografia Assimétrica

- Torna muito mais fácil a troca de chaves
- Algoritmos assimétricos: RSA, ElGamal
- Chaves Assimétricas (Asymmetric Keys): são formadas por 2 partes: chave pública (public key) e chave privada (private key)
- Uma chave pública pode ser usada para gerar um texto cifrado que só pode ser descriptografado pela chave privada
- A criptografia assimétrica é usada pelo PGP, SSL, SSH, etc.

## Assinatura (Signing)

- Processo usado para provar a identidade de uma mensagem
- Uma mensagem pode ser assinada com uma chave privada e verificada usando a chave pública

## Esteganografia (Steganography)

- Um processo para ocultar dados criptografados em dados de texto simples

## KMS - Key Management Service (Serviço de Gerenciamento de Chaves)

- É um serviço regional e público
- Permite-nos criar, armazenar e gerenciar chaves criptográficas
- Pode lidar com chaves simétricas e assimétricas
- Pode realizar operações criptográficas, como criptografia e descriptografia
- **As chaves nunca saem do KMS!** Chaves podem ser criadas ou importadas, mas ficam trancadas dentro do KMS
- O KMS também fornece conformidade FIPS 140-2 (L2) <span style="background-color: Red"><-- LEMBRE-SE DISSO</span>

### Chaves KMS (Anteriormente conhecidas principalmente como CMK - Customer Master Keys / Chaves Mestras do Cliente)

- As principais coisas gerenciadas pelo KMS são as chaves do KMS
- Elas são usadas pelo KMS em operações criptográficas
- Elas são lógicas e contêm as seguintes coisas: ID, data, política, descrição e estado
- Cada chave KMS é apoiada por material de chave física (physical key material). O material de chave física pode ser gerado pelo KMS ou importado pelo KMS
- As chaves KMS podem ser usadas para criptografar ou descriptografar dados diretamente para até 4KB de dados

### DEK - Data Encryption Keys (Chaves de Criptografia de Dados)

- As Chaves de Criptografia de Dados (DEKs) são geradas a partir das chaves KMS usando a API `GenerateDataKey`
- Essas chaves podem ser usadas para criptografar/descriptografar dados localmente com tamanho superior a 4KB
- A DEK gerada está vinculada a uma chave KMS específica
- O KMS não armazena a DEK de forma alguma; ela é gerada, fornecida ao usuário e descartada depois
- O KMS fornece 2 versões da chave: uma em texto simples e um texto cifrado criptografado com a CMK
- Espera-se que descartemos a chave de texto simples (plaintext key) assim que criptografarmos os dados
- Os dados criptografados e a chave de criptografia de dados criptografada devem ser armazenados lado a lado
- Para descriptografar os dados, passamos a DEK criptografada de volta ao KMS para ser descriptografada e, com a chave descriptografada, descriptografamos os dados em si

### Conceitos Chave

- As chaves KMS são isoladas numa região e nunca saem do KMS (por padrão)
- O KMS também suporta chaves multirregião, em que as chaves são replicadas para outras regiões
- Existem 2 tipos de chaves: de propriedade da AWS (AWS owned) e de propriedade do cliente (customer owned). No caso de chaves de propriedade do cliente, podemos ter chaves gerenciadas pela AWS (criadas automaticamente) ou chaves gerenciadas pelo cliente (criadas explicitamente pelo cliente)
- As chaves gerenciadas pelo cliente são mais configuráveis. Por exemplo, podemos editar a política de chave para permitir acesso entre contas (cross account) à chave
- As chaves KMS suportam rotação. A rotação é opcional para chaves gerenciadas pelo cliente
- Uma chave KMS contém a chave de apoio (backing key), o material de chave física e todas as chaves de apoio anteriores causadas pela rotação => dados criptografados com chaves anteriores ainda podem ser descriptografados
- Podemos criar aliases para as chaves KMS. Os aliases são por região
- Políticas de chaves e segurança:
    - Políticas de Chave (Recurso): elas são diferentes em comparação com as políticas que outros serviços da AWS têm, pois cada política de chaves do KMS deve permitir explicitamente o acesso da conta AWS proprietária
    - Cada chave KMS tem uma política de chave
    - As chaves KMS são muito granulares

---

# Encryption and KMS

## Encryption Approaches

- **Encryption At Rest**: designed to protect against physical threat or tempering
    - Data is stored in shared hardware in an encrypted form, even if somebody has access to hardware it can not access the data in a readable format
    - General used when one party is involved
- **Encryption In Transit**: aimed to protect data when transferred between 2 places
    - Generally used when multiple individual/systems are involved

## Encryption Concepts

- Plaintext: un-encrypted data, can be text, image, other application, etc.
- Algorithm: peace of code which takes plaintext and a key and generates encrypted data. Examples of algorithms: Blowfish, AES, RC4, DES, RC5 and RC6
- Key: is a password
- Ciphertext: when an algorithm takes the plaintext and the key, the output generated is cyphertext (encrypted data)

## Symmetric Encryption

- Symmetric Keys: the same key can be used for encryption and for decryption as well
- Symmetric encryption algorithms: AES-256
- Great for encryption at rest, not recommended for encryption in-transit

## Asymmetric Encryption

- Makes it much easier to exchange keys
- Asymmetric algorithms: RSA, ElGamal
- Asymmetric Keys: are formed of 2 parts: public key and private key
- A public key can be used to generate cyphertext which can only be encrypted by the private key
- Asymmetric encryption is used by PGP, SSL, SSH, etc.

## Signing

- Process used to prove identity of a message
- A message can be signed with a private key and verified using the public key

## Steganography

- A process to hide encrypted data in plaintext data

## KMS - Key Management Service

- It is a regional and a public service
- Let's us create, store and manage cryptographic keys
- Can handle symmetric and asymmetric keys
- Can perform cryptographic operations such as encryption and decryption
- **Keys never leave KMS!** Keys can be created, imported but they are locked inside KMS
- KMS also provides a FIPS 140-2 (L2) compliance <span style="background-color: Red"><-- REMEMBER THIS</span>

### KMS Keys (Formerly known mainly as CMK - Customer Master Keys)

- Main things managed by KMS are KMS keys
- They are used by KMS in cryptographic operations
- They are logical containing the following things: ID, date, policy, description and state
- Every KMS key is backed by physical key material. The physical key material can be generated by KMS or imported by KMS
- KMS keys can be used to directly encrypt or decrypt data for up to 4KB of data

### DEK - Data Encryption Keys

- Data Encryption Keys are generated from KMS keys using `GenerateDataKey` API
- These keys can be used to locally encrypt/decrypt data with size larger than 4KB
- DEK generated is linked to a specific KMS keys
- KMS does not store the DEK in any way, it is generated and provided to the user and it is discarded afterwards
- KMS provides 2 version of the key a plaintext and a ciphertext encrypted with the CMK
- It is expected from us to discard the plaintext key as soon as we encrypted the data
- The encrypted data and the encrypted data encryption key should be stored side by side
- For decryption of the data we pass back to KMS the encrypted DEK to be decrypted and with the decrypted key we decrypt the data itself

### Key Concepts

- KMS keys are isolated to a region and never leave KMS (by default)
- KMS also supports multi-region keys, where keys are replicated to other regions
- There are 2 types of keys: AWS owned and customer owned. In case of customer owned keys, we can have AWS managed (created automatically) or customer managed keys (created explicitly by the customer)
- Customer managed keys are more configurable. For example, we can edit the key policy to allow cross account access to the key
- KMS keys support rotation. Rotation is optional for customer managed keys
- A KMS key contains the backing key, the physical key material and all previous backing keys caused by rotation => data encrypted with previous keys can still be decrypted
- We can create aliases for KMS keys. Aliases are per region
- Key policies and security:
    - Key Policies (Resource): they are different compared to policies other AWS services have in the way that each KMS keys policy has to explicitly allow access from the owner AWS account
    - Every KMS keys has a key policy
    - KMS keys are very granular