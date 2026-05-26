# BGP - Border Gateway Protocol

- O BGP é um protocolo de roteamento
- Usado para controlar como os dados fluem do ponto A para o ponto B
- O BGP é composto por muitas redes autogerenciadas conhecidas como Sistemas Autônomos (AS - Autonomous Systems)
- Um AS pode ser uma rede grande, uma coleção de rotas, etc., e é visto como uma caixa preta a partir da perspectiva do BGP
- Cada AS recebe um número atribuído pela IANA, chamado ASN
- Os ASNs têm 16 bits de comprimento e variam de 0 a 65535, sendo que o intervalo de 64512 a 65534 é privado
- Também podemos ter números ASN de 32 bits (isso está fora do escopo deste exame)
- Os ASNs são usados pelo BGP para identificar diferentes entidades na rede
- O BGP foi projetado para ser confiável e distribuído, e opera na porta TCP/179
- Não é automático; a comunicação entre dois AS deve ser feita manualmente
- Os Sistemas Autônomos trocam informações de topologia de rede entre si
- O BGP é um protocolo de vetor de caminho (path-vector protocol): ele troca o melhor caminho para um destino entre pares (peers), e esse caminho é chamado de **ASPATH** (Autonomous System Path)
- O BGP não leva em consideração a velocidade ou as condições do link, ele foca apenas no caminho
- iBGP - BGP interno (internal BGP), roteamento dentro de um AS
- eBGP - BGP externo (external BGP), roteamento entre ASs
- Exemplo de BGP:
    ![BGP 101](images/BorderGatewayProtocol101.png)
- O BGP sempre escolhe o caminho mais curto. Existem maneiras de influenciar o caminho expandindo-o artificialmente (fazendo o *prepend* de si mesmo no caminho)

---

# BGP - Border Gateway Protocol

- BGP is a routing protocol
- Used to control how data flows from point A to point B
- BGP is made up from a lot of self managing networks know as Autonomous Systems (AS)
- AS could be a large network, collection of routes etc. and is viewed as a black box from BGP perspective
- Each AS is allocated a number by IANA, named ASN
- ASNs are 16 bit in length and range from 0 to 65535, the range from 64512 to 65534 is private
- We can get 32 bit ASN numbers as well (this is out of scope for this exam)
- ASNs are used by the BGP to identify different entities on the network
- BGP is designed to be reliable and distributed, and it operates of TCP/179
- It is not automatic, the communication between to AS should be done manually
- Autonomous Systems do exchange network topology information between them
- BGP is a path-vector protocol: it exchanges the best path to a destination between peers, the path is called **ASPATH** (Autonomous System Path)
- BGP does not take into account link speed or condition, it focuses on path only
- iBGP - internal BGP, routing within an AS
- eBGP - external BGP, routing between AS's
- BGP example:
    ![BGP 101](images/BorderGatewayProtocol101.png)
- BGP always choses the shortest path. There are ways to influence the path by artificially expending the path (prepending itself to the path)