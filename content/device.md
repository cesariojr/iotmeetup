# Parte 5 - Como enviar dados do simulador de dispositivo para a IoT no IBM Watson IoT Platform

## Introdução

No laboratório anterior, você criou uma entrada para o simulador do dispositivo no IBM Watson IoT Platform.
Agora, queremos torná-lo um aplicativo do Internet of Things, adicionando o MQTT para enviar os dados para a plataforma IoT.

Começaremos usando uma conexão MQTT sem TLS (não segura). No entanto, a IBM Watson IoT Platform é configurada para bloquear todas as conexões não seguras por padrão, portanto, é necessário configurar sua instância do Watson IoT para permitir a conexão não segura.

## Etapa 1 - Configurar o IBM Watson IoT Platform para permitir conexões não seguras

No console da plataforma IoT para a instância conectada ao seu aplicativo Boilerplate, entre na seção **Security** e, em seguida, o **Connection Security**. 

Altere o nível de segurança padrão para **TLS Optional**, aceite a mensagem de aviso pressionando o botão Ok e, em seguida, **Save** a alteração. Sua instância da plataforma IoT agora aceitará conexões MQTT não seguras.

<p align="center">
  <img src="https://github.com/cesariojr/iotmeetup/blob/master/content/security.png" width="600">
</p>

## Etapa 2 - Conectar com o simulador de dispositivo na IBM Watson IoT Platform

Ao conectar-se na IBM Watson IoT Platform, há alguns requisitos em alguns parâmetros usados durante a conexão.
A [documentação da plataforma](https://cloud.ibm.com/docs/services/IoT/reference/security?topic=iot-platform-connect_devices_apps_gw#connect_devices_apps_gw) oferece mais detalhes:

1. Os seguintes parâmetros possibilitam a conexão e publicação de dados:
   - Organization ID
   - Device type
   - Device id
   - Device token
   - Tópico: iot-2/evt/status/fmt/json
   
2. Acesse o App Watson IoT Sensor Simulator no endereço http://watson-iot-sensor-simulator.mybluemix.net/

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/iotsim.png" width="400">
</p>

3. Será apresentada a tela de registro, onde você deve fornecer os dados de org id, device type, device id e device token criados no laboratório anterior.

Após o registro, uma tela similar a figura abaixo deve ser exibida:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/devicesim.png" width="300">
</p>

Pronto ! Agora você tem o simulador de dispositivos configurado e conectado na IBM Watson IoT Platform.

Acesse o menu **Dispositivos** ou **Devices** e selecione o dispositivo criado (simulador01) e você deve ver os dados chegando em tempo real do simulador para a IBM Watson IoT Platform

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/json.png" width="600">
</p>

***
Links Rápidos :
[Índice](https://github.com/cesariojr/iotmeetup/) - [Parte 1](/content/intro.md) - [Parte 2](/content/prereq.md) - [Parte 3](/content/boilerplate.md) - [Parte 4](/content/platform.md) - **[Parte 5](/content/device.md)** - [Parte 6](/content/view.md) - [Parte 7](/content/nodered.md) - [Parte 8](/content/next.md)

