# Parte 7 - Node-RED

## Etapa 1 - Criando conta Node-RED

Em primeiro lugar, retorne ao portal IBM Cloud e acesse a lista de recursos.

A seguir acesse o aplicativo de Cloud Foundry instanciado anteriormente.
<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/images/resource-list.png" width="700">
</p>

Então, a fim de visualizar a aplicação Node-RED, clique em **Visit App URL**. 

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/images/nr-0.png" width="600">
</p>

Clique em **Next** e na tela seguinte crie um **Username** e um **Password** de acesso. Para concluir o processo, clique em **Finish**

A seguinte tela deverá ser exibida:
<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/nodered01.png" width="600">
</p>

## Etapa 2 - Acessando sua conta Node-RED

Para acessar a conta Node-RED, clique em **Go to your Node-RED flow editor**.

E então, insira seu **Username** e **Password** para login.

O seguinte *flow* de Node-RED deverá ser exibido:

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/nodered03.png" width="600">
</p>

## Etapa 3 - Configurando flow Node-RED

Para capturar os dados armazenados no IBM Watson IoT Platform, clique duas vezes no nó **IBM IoT App In**, e então em **Device ID**, selecione **All or**. Clique em **Done** para finalizar.

Uma vez o nó do IBM Watson IoT App In configurado, configure o nó **temp**, clicando-o duas vezes.

Na função de pré-inserida, baseado no corpo JSON a ser enviado pela plataforma Watson IoT, deve-se substituir a chave **temp** por **temperature**.

## Instalando o NodeRed Dashboard

### Configuração da instância do NodeRED

No menu de configuração do NodeRED, acesse a opção Manage Pallete

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/nodered04.png" width="200">
</p>

### Tab de Instalação

Nas tabs de opção, acesse a tab Install e digite node-red-dashboard no campo de busca. Escolha a opção

<p align="center">
<img src="https://github.com/cesariojr/iotmeetup/blob/master/content/nodered05.png" width="400">
</p>

***
Links Rápidos :
[Índice](https://github.com/cesariojr/iotmeetup/) - [Parte 1](/content/intro.md) - [Parte 2](/content/prereq.md) - [Parte 3](/content/boilerplate.md) - [Parte 4](/content/platform.md) - [Parte 5](/content/device.md) - [Parte 6](/content/view.md) - [Parte 7](/content/nodered.md) - [Parte 8](/content/next.md)
