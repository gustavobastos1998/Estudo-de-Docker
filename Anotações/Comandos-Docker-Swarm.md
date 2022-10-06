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
   --replicas <numero>  ::  usado para aumentar o número de réplicas de um serviço. Desta maneira uma task será emitida para os Workers também. A orquestração incia de fato com essa flag.

   --network <network_name>  ::  informa a rede a qual o serviço estará conectado
   ```


## Listando serviços

   - *docker service ls*  ::  lista serviços do swarm. Assim como o comando ***docker node ls***, somente managers têm acesso a esse comando. 


## Removendo serviços

   - *docker service rm <nome>*  ::  remove um serviço. O serviço para de rodar, isso pode significar parar um container que está rodando


## Testando a orquestração swarm

   - O node Manager ele garante que os serviços estejam rodando em seus dependentes de maneira correta, isso implica que caso um dos workers finalize um container, após alguns segundos o manager levanta esse serviço novamente. Para remover o container de um dos workers, é necessário usar a flag -f, para não ter que dar stop no container, pois a reinicialização do serviço no node worker é rápido.


## Checando token do Swarm

   - *docker swarm join-token manager*  ::  recupera o token para incluir nodes manager no swarm. Útil para dar join em outra instância futuramente. 

   - *docker swarm join-token worker*  ::  recupera o token para incluir nodes worker no swarm. Útil para dar join em outra instância futuramente.


## Informações do swarm

   - *docker info*  ::  verifica detalhes do swarm que o docker está utilizando. ID do node, número de nodes, número de managers são algumas das informações que esse comando mostra.


## "Removendo" instância do swarm

   - *docker swarm leave*  ::  executada em uma determinada instância "removendo-a", ela não é considerada mais um node para o swarm. O swarm não remove o node de fato, apenas muda o status dele para down, fazendo com que esse node não tenha mais acesso as funcionalidades do swarm.


## Removendo node do swarm

   - *docker node rm <id>*  ::  remove um node do swarm, neste caso o node é removido de fato do swarm o container continuará rodando na instância. É preciso utilizar o -f. Para adicionar novamente basta utilizar o ***docker swarm join-token <parametro>*** de acordo com a necessidade.


## Inspecionar serviços

   - *docker service inspect <id_service>*  ::  informa detalhes sobre um serviço.


## Verificar containers ativos

   - *docker service ps <id>*  ::  lista os containers que estão rodando e também os que receberam baixa (***docker swarm leave***). Funciona de maneira parecida a flag '-a' no comando ***docker ps -a***. 


## Rodando compose com swarm

   - *docker stack deploy -c <arquivo.yaml> <nome>*  ::  roda o compose com o swarm, desta maneira o arquivo compose será executado, porém estamos em modo swarm e utilizaremos os nodes como réplicas.


## Aumentar réplicas do stack

   - *docker service scale <nome>=<numero_replicas>*  ::  pode criar réplicas nos workers nodes. Desta forma as outras máquinas receberão as tasks a serem executadas.


## Fazer um node não receber mais tasks

   - *docker node update --availability drain <id_node>*  ::  desta forma, um node para de receber ordens de um manager. O status drain não recebe mais tasks e caso queira voltar a receber, basta utilizar o parâmetro active.


## Atualizar parâmetro

   - *docker service update --image <imagem> <id_servico>*  ::  atualiza as configurações dos nodes, apenas os nodes active receberão essas atualizações.

   ```
   - --network  ::  insforma uma network a qual o serviço irá fazer parte, atualizando-a.
   ```


## Criar rede para swarm

   - A conexão entre instâncias usa um driver(tipo de rede) diferente, o *overlay*.

   - Criamos a rede primeiro com ***docker network create***.

   - Ao criar um service adicionamos a flag --network <rede> parainserir as instâncias na nova rede.