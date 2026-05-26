# AWS Global Accelerator

- Projetado para otimizar o fluxo de dados do usuário para a AWS
- Semelhante ao CloudFront, ambos melhoram o desempenho ao se comunicar com serviços hospedados na AWS
- O Global Accelerator fornece 2 endereços IP **anycast**. Endereços IP anycast são um tipo especial de endereço IP
- Endereços IP normais são chamados de endereços IP **unicast**, que se referem a um único dispositivo na rede
- Por outro lado, os endereços IP anycast podem ser usados por vários dispositivos ao mesmo tempo, e o tráfego será roteado para o dispositivo mais próximo da origem
- O Global Accelerator usa as Localidades da AWS Edge (Edge Locations). Como várias localidades anunciam os mesmos endereços IP anycast, o tráfego será roteado para a Edge Location mais próxima do usuário
- A AWS possui sua própria rede dedicada composta por links de fibra. As Edge Locations encaminham o tráfego para essa rede, melhorando o desempenho

## CloudFront vs Global Accelerator

- O CloudFront aproxima o conteúdo do cliente armazenando-o em cache na Edge Location. O Global Accelerator aproxima o cliente do serviço, fornecendo acesso à rede global da AWS
- O Global Accelerator é um produto de rede: funciona para quaisquer aplicações TCP/UDP, incluindo aplicações web (HTTP/HTTPS). O CloudFront armazena em cache apenas conteúdo HTTP/HTTPS
- O Global Accelerator não armazena nada em cache. Ele não entende o protocolo HTTP/HTTPS

---

# AWS Global Accelerator

- Designed to optimize the flow of data from user to AWS
- Similar to CloudFront, both improve performance when communicating with services hosted in AWS
- Global Accelerator provides 2 **anycast** IP addresses. Anycast IP addresses are special type of IP addresses
- Normal IP addresses are called **unicast** IP addresses, these refer to one device in the network
- In contrast anycast IP addresses can be used by multiple devices at the same time, the traffic will be routed to the device closest to the source
- Global Accelerator uses the AWS Edge Locations. Since multiple locations advertise the given anycast IP addresses, the traffic will be routed to the Edge Location closer to the user
- AWS has its own dedicated network consisting in fiber links. Edge Locations relay traffic to this network improving performance

## CloudFront vs Global Accelerator

- CloudFront moves the content closer to the customer by caching it on the Edge Location. Global Accelerator moves the customer closer to the service pe providing access to the AWS global network
- Global Accelerator is a network product: works on any TCP/UDP applications including web apps (HTTP/HTTPS). CloudFront only caches HTTP/HTTPS content
- Global Accelerator does not cache anything. It does not understand the HTTP/HTTPS protocol