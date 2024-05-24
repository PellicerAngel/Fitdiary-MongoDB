Esta aplicacion depende de la instalacion de una maquina Ubuntu 20.04.

Instalacion de Mongo DB para poder usar la base de datos instalada, con esta guia se podra instalar de forma facil.
https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-20-04-es

Tambien tendremos que tener la biblioteca de Pymongo para que nuestra aplicacion de Python se conecte al servidor de Mongo DB.
Con estos comandos se instalara la libreria:

$ sudo apt-get install python-pip
$ sudo pip install pymongo==2.5.2
