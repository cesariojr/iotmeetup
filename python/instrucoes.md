# Instruções de como usar o IBM Watson IoT Platform com Python 2.7 and 3.x 

O código exemplo anexo demonstra o uso simples do Python para interagir com o IBM Watson IoT Platform.

Preparação, instalação, dependências e mais informações estão do GitHub oficial:

https://github.com/ibm-watson-iot/iot-python


## Python module for interacting with the [IBM Watson IoT Platform](https://internetofthings.ibmcloud.com).

-  [Python 3.7](https://www.python.org/downloads/release/python-373/)  (recommended)
-  [Python 2.7](https://www.python.org/downloads/release/python-2716/)

Note: Support for MQTT with TLS requires at least Python v2.7.9 and openssl v1.0.1


## Dependencies

-  [paho-mqtt](https://pypi.python.org/pypi/paho-mqtt)
-  [iso8601](https://pypi.python.org/pypi/iso8601)
-  [pytz](https://pypi.python.org/pypi/pytz)
-  [requests](https://pypi.python.org/pypi/requests)


## Installation

Install the [latest version](https://pypi.org/project/wiotp-sdk/) of the library with pip

```
# pip install wiotp-sdk
```


## Uninstall

Uninstalling the module is simple.

```
# pip uninstall wiotp-sdk
```

## Legacy ibmiotf Module

Version `0.4.0` of the old [ibmiotf](https://pypi.python.org/pypi/ibmiotf) pre-release is still available, if you do not wish to upgrade to the new version, we have no plans to remove this from pypi at this time, however it will not be getting any updates.


## Documentation

https://ibm-watson-iot.github.io/iot-python/

https://github.com/ibm-watson-iot/iot-python
