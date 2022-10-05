## Iniciando o Swarm

   - *docker swarm init*  ::  inicializa o swarm

   ### Flags *init* 

    ```
    --advertise-addr  ::  em alguns casos precisamos declacar o IP com essa flag, isso fará com que a máquina vire um node manager
    ```
      

## Listando nodes ativos

   - *docker node ls*  ::  lista os nodes ativos no cluster, usado para monitorar o que o swarm está orquestrando. Somente nodes managers podem utilizar esse comando.


## Adicionando novos nodes

   - *docker swarm join --token <TOKEN> <IP>:<PORTA>*  ::  adiciona um node como worker. Após utilizar o comando de init, o docker labs informa o comando completo com token, ip e port para ser utilizado. Basta ir em outra máquina e colar o comando especificado pelo docker labs após sua inicialização. 


## Subindo um novo serviço

   - *docker service create --name <nome> <imagem>*  ::  inicializa um serviço, mas o que ele faz é gerar um container que roda na máquina. Desta forma teremos um container novo sendo adicionado ao nosso manager e esse serviço será gerenciado pelo swarm. Alguns serviços exigem flags a mais, como o nginx que é um serviço web, ele exige a flag -p para expor as portas.

   ### Flags *create* 
   ```
   --replicas <numero>  ::  usado para aumentar o número de réplicas de um serviço. Desta maneira uma task será emitida para os Workers também.
   ```


## Listando serviços

   - *docker service ls*  ::  lista serviços do swarm. Assim como o comando ***docker node ls***, somente managers têm acesso a esse comando. 


## Removendo serviços

   - *docker service rm <nome>*  ::  remove um serviço. O serviço para de rodar, isso pode significar parar um container que está rodando


## Aumentando o número de réplicas