# Parte 1 - Introdução

## Fundamentos de Internet das Coisas - IoT (Internet of Things)

A Internet das Coisas é um conjunto de tecnologias que vem evoluindo há décadas, e nos últimos anos, a expansão de conectividade, criação de plataformas de prototipação, barateamento de dispositivos micro controlados e embarcados e tecnologias de computação em nuvem propiciaram que a Internet das Coisas entrasse no nosso dia a dia tecnológico.

As principais tecnologias combinam capacidades de computação, comunicação e controle, simultaneamente e podem ser aplicadas em diversas áreas e combinadas com outras tecnologias.

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/iot.png" width="400">
</p>

Figura 1: Definição de "coisa" digital
Fonte: Silvio Meira, 12/12/2016, blog ikewai
SINAIS do FUTURO IMEDIATO, #1: internet das coisas. http://www.ikewai.com/WordPress/2016/12/12/sinais-do-futuro-imediato-1-internet-das-coisas/

As seguintes tecnologias evoluiram nos últimos anos e possibilitaram que soluções de Internet das Coisas se tornassem realidade:
1. Conectividade móvel com grande abrangência e velocidade
2. Popularização da computação em nuvem, com redução do custo de processamento e de armazenamento dos dados
3. Disponibilização de APIs públicas para facilitar a integração multiplataforma (hardware, mobile e web)
4. Amadurecimento do IPv6, dando a possibilidade de um endereço único por dispositivo
5. Oferta massiva de sensores mais baratos, menores e com baixo consumo de energia
6. Massificação do Open Hardware, impulsionando a criação de soluções no formato DIY (Do It Yourself)
7. Aumento do número de ferramentas Open Source para Big Data e Machine Learning, visando tratar o volume, variedade e velocidade de produção dos dados
8. Amadurecimento de tecnologias web voltadas para programação de dispositivos e equipamentos

Essas tecnologias podem cobrir desde redes de comunicação (2G/3G/4G, WiFi, BLE, ZigBee, LoRa, etc), plataformas de prototipação (Arduino, Raspberry Pi, NodeMCU, etc) e plataformas profissionais embarcadas (ARM, PIC, etc), Tecnologias de Automação (CLPs, PCs Industriais, sistemas supervisórios/SCADA, MES, etc) protocolos novos e legados (HTTP, MQTT, COAP, AMQP, OPC-UA, etc), tecnologias de segurança (TLS/SSL, criptografia, segurança lógica e física, etc) que irão conectar-se com aplicações através de APIs e das mais diversas linguagens de programação.

## Protocolo MQTT

O protocolo MQTT (Message Queuing Telemetry Transport) foi desenvolvido pela IBM para possibilitar transferÊncia de dados com uso mínimo de largura de banda e gasto mínima de bateria de dispositivos, conectando oleodutos através de conexão via satélite.

Embora o MQTT esteja amplamente associado ao termo "Message Queuing Telemetry Transport", o nome MQTT é proveniente de um produto IBM chamado MQseries e pode ser visto como um protocolo de mensagens de publicação / assinatura baseado em TCP / IP usando o modelo cliente / servidor.

Atualmente é um padrão aberto e ganhou grande aceitação no ambiente IoT e mantém seus objetivos iniciais, como qualidade de entrega de dados de serviço, reconhecimento contínuo de sessão, implementação simples com uma pilha de protocolo leve, especialmente útil em dispositivos embarcados com capacidades limitadas.

O protocolo MQTT é baseado em TCP/IP e todos os clientes e o broker precisam ter uma pilha TCP/IP. O tamanho máximo do payload é de 131072 bytes (128K). Veja a representação simplificada do modelo ISO/OSI na figura abaixo:

* Adaptado de https://developer.bosch.com/web/xdk/mqtt1

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/mqtt.png" width="400">
</p>

***
*Links Rápidos :*
[Índice](https://github.com/cesariojr/iotmeetup/) - [Parte 1](/content/intro.md) - [Parte 2](/content/prereq.md) - [Parte 3](/content/boilerplate.md) - [Parte 4](/content/platform.md) - [Parte 5](/content/device.md) - [Parte 6](/content/view.md) - [Parte 7](/content/nodered.md) - [Parte 8](/content/next.md)

