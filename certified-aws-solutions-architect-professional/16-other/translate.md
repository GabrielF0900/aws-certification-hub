# Amazon Translate

- É um serviço de tradução de texto baseado em ML (Machine Learning)
- Traduz o texto do idioma nativo para outros idiomas uma palavra de cada vez
- O processo de tradução tem duas partes:
    - O Codificador (Encoder) lê o texto fonte => produz uma representação semântica (significado)
    - O Decodificador (Decoder) lê o significado => escreve para o idioma de destino (target language)
- O mecanismo de atenção (Attention mechanism) garante que o "significado" seja traduzido
- O Textract é capaz de detectar o idioma do texto de origem (source text language)
- Casos de uso:
    - Experiência do usuário multilíngue (Multilingual user experience)
    - Traduzir dados de entrada (mídias sociais/notícias/comunicações)
    - Independência de idioma para outros serviços da AWS: podemos ter outros serviços como Comprehend, Transcribe e Polly que operam em informações; o Transcribe fará com que esses serviços operem de forma independente do idioma. Pode ser usado para analisar dados armazenados no S3, RDS, DDB, etc.
    - Comumente usado para integração com outros serviços/Apps/plataformas

---

# Amazon Translate

- Is a text translation service based in ML
- Translates text from native language to other languages one word at a time
- Translation process has two parts:
    - Encoder reads the source text => outputs a semantic representation (meaning)
    - Decoder reads in the meaning => writes to the target language
- Attention mechanism ensures "meaning" is translated
- Textract is capable to detect the source text language
- Use cases:
    - Multilingual user experience
    - Translate incoming data (social media/news/communications)
    - Language-independence for other AWS services: we might have other services such as Comprehend, Transcribe and Polly which operate on information; Transcribe will make this services operate in a language independent way. It can used to analyze data stored in S3, RDS, DDB, etc.
    - Commonly used for integration with other services/Apps/platforms