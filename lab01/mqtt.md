*Links Rápidos :*
[Início](/README.pt.md) - [Parte 1](../part1/README.md) - [Parte 2](../part2/README.md) - [Parte 3](../part3/README.md) - [Parte 4](../part4/README.md)
***
**Parte 2** - [Registro de Dispositivo](DEVICE.md) - [**Aplicação**](APP.md) - [MQTT](MQTT.md) - [Certificado Servidor](CERT1.md) - [Certificado Cliente](CERT2.md)
***

# Connecting Device to the Watson IoT Platform using MQTT

## Objetivos

In this lab you will learn how to add MQTT messaging to an application. You will learn:

- How to connect to a MQTT broker using unsecured connection
- How to use MQTT to connect to the Watson IoT platform

### Introdução

No laboratório anterior, você construiu o aplicativo de sensor autônomo. Agora, queremos torná-lo um aplicativo do Internet of Things, adicionando o MQTT para enviar os dados para a plataforma IoT.

Começaremos usando uma conexão MQTT não segura e, na próxima seção, protegeremos a conexão. No entanto, a plataforma Watson IoT é configurada para bloquear todas as conexões não seguras por padrão, portanto, é necessário configurar sua instância do Watson IoT para permitir a conexão não segura.

### Etapa 1 - Configurar a plataforma Watson IoT para permitir conexões não seguras

Abra o console da plataforma IoT para a instância conectada ao seu aplicativo Boilerplate. No painel (* ≡ * -> * Dashboard *), selecione o aplicativo e, na seção de visão geral, selecione a plataforma IoT no painel de conexões).

Inicie o console da plataforma IoT e, em seguida, alterne para a seção Configurações. Em Segurança, selecione Segurança da conexão e, em seguida, pressione o botão **Política de segurança de conexão aberta**. Altere o Nível de segurança padrão para **TLS Opcional**, aceite a mensagem de aviso pressionando o botão Ok e, em seguida, **Salvar** a alteração. Sua instância da plataforma IoT agora aceitará conexões MQTT não seguras. Deixe a janela do navegador mostrando o console da IoT Platform aberto, pois você precisará obter algumas informações ao adicionar o código MQTT ao aplicativo ESP8266.


### Etapa 2 - Como funciona

Ao conectar-se à plataforma Watson IoT, há alguns requisitos em alguns parâmetros usados durante a conexão.
A [documentação da plataforma](https://console.bluemix.net/docs/services/IoT/reference/security/connect_devices_apps_gw.html#connect_devices_apps_gw) oferece mais detalhes:

1. Os seguintes parâmetros possibilitam a conexão e publicação de dados:
   - org id
   - device type
   - device id
   - device token
   - formato tópico para publicar dados : iot-2/evt/< **event id** >/fmt/<  **format string** >
   - iot-2/evt/status/fmt/json
   
  
2. App Watson IoT Sensor Simulator (http://watson-iot-sensor-simulator.mybluemix.net/)

Acesse o link http://watson-iot-sensor-simulator.mybluemix.net/

<img src="https://github.com/cesariojr/iotmeetup/blob/master/lab01/iotsim.png" width="400">


***
**Parte 2** - [Registro de Dispositivo](DEVICE.md) - [**Aplicação**](APP.md) - [MQTT](MQTT.md) - [Certificado Servidor](CERT1.md) - [Certificado Cliente](CERT2.md)
***
*Links Rápidos :*
[Início](/README.pt.md) - [Parte 1](../part1/README.md) - [Parte 2](../part2/README.md) - [Parte 3](../part3/README.md) - [Parte 4](../part4/README.md)
