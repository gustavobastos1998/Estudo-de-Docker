## O que são networks no Docker?

   - Uma forma de gerenciar a conexão do Docker com outras plataformas ou entre containers.

   - As networks são criadas separadas dos containers, como os volumes.

   - A network deixa muito simples a comunicação entre containers.


## Tipos de conexão

   ### Externa
   
   - Conexão com uma API

   ### Com o host

   - Comunicação com a máquina que está executando o Docker.

   ### Entre containers

   - Comunicação que utiliza o driver bridge e permite a comunicação entre dois ou mais containers.


## Tipos de rede (drivers)

   - Bridge: o mais comum e padrão do Docker, utilizado para conectar containers entre si.

   - Host: conexão entre a máquina hosteando o Docker e o container. 

   - macvlan: conexão a um container por um MAC address.

   - none: remove todas as conexões de rede de um container.

   - plugins: permite extenções de terceiros para criar outras redes.


## Conexão entre containers

   - Duas imagens distintas em containers separados, onde precisam se conectar para inserir em um banco de dados, por exemplo.

   - A rede bridge é utilizada para fazer essa conexão.