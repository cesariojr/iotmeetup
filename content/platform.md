# Parte 4 - Registrando um novo dispositivo no IBM Watson IoT Platform

## Objetivos

Este laboratório mostrará como registrar seu dispositivo simulado com o IBM Watson IoT Platform. No laboratório você aprenderá:

- Como navegar para o console do IBM Watson IoT Platform
- Como definir um tipo de dispositivo e registrar um dispositivo na plataforma IoT

### Introdução

Antes de poder conectar um dispositivo no IBM Watson IoT Platform, você precisa definir como o dispositivo se conectará à plataforma e também registrar o dispositivo para gerar um token de acesso para o dispositivo. Isso será usado para verificar a identidade do dispositivo.

Você precisa decidir como deseja agrupar dispositivos, por função, por tipo de hardware, etc. Cada dispositivo registrado na plataforma deve ser registrado em um tipo de dispositivo. Não há restrições sobre como os dispositivos são agrupados e os tipos de dispositivos. Para esta oficina, criaremos um tipo de dispositivo representando os dispositivos simulados.

### Etapa 1 - Acessar o console do IBM Watson IoT Platform

No menu lateral esquerdo do portal IBM Cloud, clique em **Resource List** e busque a seção **Cloud Foundry Apps**.
Você deve ver seu bloilerplate criado na parte anterior, conforme figura abaixo:




e, no item **Cloud Foundry Services**, selecione o serviço iotf criado. Isso levará você ao serviço da Plataforma IoT. Inicie o console.

### Etapa 2 - Adicionar um novo tipo de dispositivo para dispositivos ESP8266

Etapa 2 - Adicionar um novo tipo de dispositivo para dispositivos ESP8266 Navegue até a seção Devices do console e selecione a seção **Device Types**. Pressione o botão **+ Add device type** e insira o seguinte:

- Tipo : Certifique-se de que o dispositivo esteja selecionado (NÃO gateway)
- Nome : Escreva **ESP8266**
- Descrição : Escreva **Esp8266 environment monitor**

Selecione **Next** depois **Done**

### Etapa 3 - Registre sua placa ESP8266 na plataforma IoT

Agora você tem a oportunidade de registrar um dispositivo. Continue com o fluxo simples e pressione **Register Device**. O tipo de dispositivo ESP8266 deve ser pré-selecionado. Agora você precisa inserir um ID de dispositivo exclusivo. Novamente, você pode escolher como deseja identificar dispositivos. Para o workshop, use um formato simples, como **dev01**.

Pressione o botão **Next** duas vezes e você será solicitado a fornecer um token. Ao desenvolver, recomendo escolher um token que você possa lembrar facilmente. Eu configurei todos os meus dispositivos para usar o mesmo token ao desenvolver, mas obviamente isso não é uma boa prática de produção.

Cada vez que você conectar o dispositivo, o token precisará ser apresentado ao servidor e, assim que o dispositivo for registrado, não há como recuperar um token. Você precisará excluir e registrar novamente o dispositivo se o token for perdido.

Digite um token para o seu dispositivo (incluindo letras e números) e pressione **Next**. Você verá um resumo do dispositivo. Pressione **Done** para concluir o registro do dispositivo. Agora você verá uma página de detalhamento do dispositivo - essa é a última chance de ver o token. Depois de sair desta página, o token não pode ser recuperado. Anote a Organization ID, o Device Type, o Device ID e o Auth Token.

***
*Links Rápidos :*
[Índice](https://github.com/cesariojr/iotmeetup/) - [Parte 1](/content/intro.md) - [Parte 2](/content/prereq.md) - [Parte 3](/content/boilerplate.md) - [Parte 4](/content/platform.md) - [Parte 5](/content/device.md) - [Parte 6](/content/view.md) - [Parte 7](/content/nodered.md) - [Parte 8](/content/next.md)

