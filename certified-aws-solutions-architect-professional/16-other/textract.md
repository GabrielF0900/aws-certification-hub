# Amazon Textract

- É um produto de ML (Machine Learning) usado para detectar e analisar texto contido em documentos de entrada como JPEG, PNG, PDF ou TIFF
- A saída (output) é o texto extraído, a estrutura desse texto e qualquer análise que possa ser executada nesse texto
- Para a maioria dos documentos, o Textract é capaz de operar de forma síncrona (tempo real)
- Para documentos grandes, operará de forma assíncrona
- O pagamento é por uso (pay per usage), havendo preços personalizados disponíveis para grandes volumes de documentos
- Casos de uso do Textract:
    - Detecção de texto e do relacionamento entre o texto, exemplo: recibo - datas, itens, preços. Também oferece metadados sobre o texto: onde o texto ocorre
    - Análise de documento:
        - Para documentos genéricos pode detectar nomes, endereços, data de nascimento, etc.
        - Para recibos: preços, fornecedores (vendors), itens de linha (line items), datas, etc.
        - Documentos de identidade: abstração de certos campos para poder armazená-los em uma tabela de um banco de dados
- Pode ser integrado com outros serviços da AWS

---

# Amazon Textract

- Is a ML product used to detect and analyse text contained in input documents such as JPEG, PNG, PDF or TIFF
- The output is extracted text, structure of that text and any analysis that can be performed on that text
- For most documents the Textract is capable to operate in a synchronous way (real time)
- For large documents it will operate in asynchronous way
- It is pay per usage, custom pricing being available for large volume of documents
- Use cases of Textract:
    - Detection of text and the relationship between the text, example receipt - dates, items, prices. It also offers metadata about the text: where the ext occurs
    - Document analysis:
        - For generic documents might detect names, addresses, birth date, etc.
        - For receipts: prices, vendors, line items, dates, etc.
        - Identity documents: abstraction of certain fields to being able to store them in a table of a database
- It can be integrated with other AWS services