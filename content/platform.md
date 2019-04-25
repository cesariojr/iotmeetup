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
Você deve ver o boilerplate criado na parte anterior, conforme figura abaixo:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp.png" width="500">
</p>

Clique no nome da sua aplicação e a seguinte tela deve aparecer

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp2.png" width="500">
</p>

Na seção **Conexões** ou **Connections**, clique na entrada do serviço IBM Watson IoT Platform, conforme figura abaixo:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp3.png" width="500">
</p>

Finalmente, na tela baixo, clique na opção **Abrir** ou **Launch**:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp4.png" width="500">
</p>

### Etapa 2 - Adicionar o dispositivo simulado no IBM Watson IoT Platform

Dentro do serviço IBM Watson IoT Platform, você chegar na seguinte tela:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp5.png" width="500">
</p>

Na tela acima, selecione:
1. No menu lateral esquerdo a opção **Devices** ou **Dispositivos** ou;
2. Na parte direita da tela, clique no botão **Add Device** ou **Adicionar Dispositivo**

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp5.png" width="500">
</p>

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp6.png" width="500">
</p>

A seguinte tela sera exibida:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp7.png" width="500">
</p>

**Preencha os campos conforme a tela abaixo:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp8.png" width="500">
</p>

- Device Type ou Tipo de Dispositivo: escreva **simulador**
- Device ID ou ID do Dispositivo: escreva **simulador01**
- Selecione **Next** na tela abaixo:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp9.png" width="500">
</p>

- Na próxima tela, você deve selecionar o token de autenticação (ou senha) para acesso ao dispositivo. Você pode deixar a IBM Watson IoT Platform gerar um token automaticamente ou você pode fornecer um token.
No nosso laboratório, iremos fornecer o token, conforme tela abaixo:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp10.png" width="500">
</p>

**IMPORTANTE: O token deve seguir as regras de segurança propostas pelo serviço e uma vez que você fornecer o token, guarde a informação com segurança. A responsabilidade pela criação e manutenção do token é do usuário**

A seguinte tela será apresentada para confirmação dos dados:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp11.png" width="500">
</p>

Clique no botão **Done** e a tela final será apresentada:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/wiotp12.png" width="500">
</p>

**Guarde com segurança os dados apresentados.Essa é a página de detalhamento do dispositivo - essa é a última chance de ver o token. Depois de sair desta página, o token não pode ser recuperado.**

**Anote a Organization ID, o Device Type, o Device ID e o Auth Token.**

Pronto! Agora você já tem um dispositivo simulado configurado na IBM Watson IoT Platform.

***
Links Rápidos :
[Índice](https://github.com/cesariojr/iotmeetup/) - [Parte 1](/content/intro.md) - [Parte 2](/content/prereq.md) - [Parte 3](/content/boilerplate.md) - [Parte 4](/content/platform.md) - [Parte 5](/content/device.md) - [Parte 6](/content/view.md) - [Parte 7](/content/nodered.md) - [Parte 8](/content/next.md)
