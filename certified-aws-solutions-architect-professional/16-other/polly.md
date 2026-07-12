# Amazon Polly

- Converte texto em fala "realista" (life-like)
- O produto recebe texto em idiomas específicos e produz fala nesse idioma específico. O Polly não faz tradução!
- Existem 2 modos em que o Polly opera:
    - TTS Padrão (Standard TTS):
        - Usa uma arquitetura concatenativa
        - Pega fonemas (menores unidades de som) para construir padrões de fala
    - TTS Neural (Neural TTS):
        - Pega fonemas, gera espectrogramas, coloca esses espectrogramas através de uma forma de vocoder que obtém o áudio de saída
        - Maneira muito avançada de gerar uma fala semelhante à humana
- Formatos de saída (Output formats): MP3, Ogg Vorbis, PCM
- O Polly é capaz de usar a Speech Synthesis Markup Language (SSML - Linguagem de Marcação de Síntese de Fala). Esta é uma maneira pela qual podemos fornecer controle adicional sobre como o Polly gera a fala. Podemos fazer com que o Polly enfatize certa parte do texto ou faça certa pronúncia (sussurrar, estilo de fala de apresentador de jornal - Newscaster)

---

# Amazon Polly

- Converts text in "life-like" speech
- The products takes text in specific languages and outputs speech in that specific language. Polly does not do translation!
- There 2 modes that Polly operates in:
    - Standard TTS:
        - Uses a concatenative architecture
        - Takes phonemes (smallest units of sound) to build patterns of speech
    - Neural TTS:
        - Takes phonemes, generate spectograms, it puts those spectograms through a vocoder form which gets the output audio
        - Much advanced way of generating human-like speech
- Output formats: MP3, Ogg Vorbis, PCM
- Polly is capable of using the Speech Synthesis Markup Language (SSML). This is a way we can provide additional control over how Polly generates speech. We can get Polly to emphasis certain part of the text or do certain pronunciation (whispering, Newscaster speaking style)