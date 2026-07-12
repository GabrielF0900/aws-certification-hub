# Elastic Transcoder e AWS Elemental MediaConvert

- MediaConvert é um produto da AWS relativamente novo que substitui o Elastic Transcoder
- MediaConvert é um superconjunto de recursos fornecidos pelo Transcoder
- Ambos os sistemas são sistemas de transcodificação de vídeo baseados em arquivo
- São serviços de transcodificação serverless pelos quais pagamos por uso
- Para ambos, adicionamos jobs a pipelines (ET) ou filas (MC)
- Os arquivos são carregados do S3, processados e armazenados de volta no S3
- MC suporta EventBridge para sinalização de jobs (job signalling)
- Exemplo de arquitetura ET/MC:
    [ET/MC architecture](images/ElasticTranscoder&MediaConvert.png)
- Usamos esses produtos quando precisamos converter mídia em um pipeline de processamento de mídia serverless orientado a eventos (event-driven)

## Escolhendo entre ET e MC

- ET é legado, por padrão devemos escolher o MC
- O MC suporta mais codecs, design para volume maior e processamento paralelo
- MC suporta preços reservados
- ~~ET exigido para WebM(VP8/VP9), GIF animado, MP3, Vorbis e WAV.~~ Todos esses codecs são suportados para o MC. Para todo o resto, devemos usar o MediaConvert

---

# Elastic Transcoder and AWS Elemental MediaConvert

- MediaConvert a fairly new AWS product replacing Elastic Transcoder
- MediaConvert is a superset of features provided by Transcoder
- Both of the systems are file based video transcoding systems
- They are serverless transcoding services for which we pay per use
- For both we add jobs to pipelines (ET) or queues (MC)
- Files are loaded from S3, processed and stored back to S3
- MC supports EventBridge for job signalling
- ET/MC architecture example:
    [ET/MC architecture](images/ElasticTranscoder&MediaConvert.png)
- We use these products when we need to the media convert in a serverless, event-driven media processing pipeline

## Choosing between ET and MC

- ET is legacy, by default we should chose MC
- MC supports more codecs, design for larger volume and parallel processing
- MC supports reserved pricing
- ~~ET required for WebM(VP8/VP9), animated GIF, MP3, Vorbis and WAV.~~ All of these codecs are supported for MC. For everything else we should use MediaConvert