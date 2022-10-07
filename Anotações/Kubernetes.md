## O que é Kubernetes?

   - Ferramenta de orquestração de containers.

   - Permite a criação de múltiplos containers em diferentes máquinas(nodes).

   - Gerencia serviços, garantindo as aplicações sejam executadas.


## Conceitos fundamentais

   - *Control Plane*: máquina que gerencia o controle dos processos dos nodes, equivalente ao manager no swarm.
   
   - *Nodes*: máquinas gerenciadas pelo Control Plane, equivalente aos workers no swarm.

   - *Pod*: um ou mais containers que estão em um Node.

   - *Deployment*: execução de uma imagem/projeto em um pod.

   - *Services*: serviços que expõem os Pods ao mundo externo.

   - *Kubectl*: cliente de linha de comando para o Kubernetes.


## Minikube 


   - Espécie de simulador de kubernetes, para não precisarmos de vários computadores/servidores.

   - Espécie de simulador de kubernetes, para não precisarmos de vários computadores/servidores. Ferramenta necessária para poder utilizar a orquestração da orquestração de containers.


## Iniciando o Minikube

   - *minikube start --driver=<DRIVER>*  ::  inicia o minikube. O DRIVER vai depender de como foi a instalação(virtualbox, hyperv e docker). Todas atingem o mesmo resultado. Exmplo: ***minikube start --driver=docker*** prepara o kubernetes no docker. OBS: sempre que o computador for reiniciado, esse comando deve ser executado novamente


## Parando o minikube

   - *minikube stop*  ::  para o minikube


## Acessando a dashboard do kubernetes

   - *minikube dashboard*  ::  detalha todo o projeto, informando: serviços, pods etc. É fornecido uma url onde estão todas essas informações.

   ### Flags *dashboard* 
   ```
   --url  ::  usado para obter apenas a url
   ```


## Deployment

   - Parte fundamental do kubernetes.

   - Ele cria o servio querodará nos pods.

   - Definimos uma imagem e um nome, ara posteriomente ser replicado entre os servidores.

   - A partir da criação do deploymente teremos containers rodando.

   - É necessário usar uma imagem que esteja no Dockerhub, por mais que a imagem seja sua e esteja na sua máquina, é necessário dar o push na imagem no hub, sem isso não há como criar o deployment.


## Criando um projeto

   - Primeiramente basta criar o projeto.

   - Após isso, gerar sua imagem com o Dockerfile.

   - Enviar para o Dockerhub.

   - Testar se o container roda essa imagem.

   - Esse projeto pode ser utilizado no kubernetes.


## Criando um deployment

   - *kubectl create deployment <NOME> --image=<IMAGEM>*  ::  cria o deployment que é onde rodamos os containers das aplicações nos Pods, desta maneira o projeto será orquestrado pelo kubernetes. O nome da imagem que é dada no comando build é utilizada neste também, que é o mesmo nome do repositório remoto no hub.


## Checando Deployments

   - *kubectl get deplyments*  ::  verifica um deployment. 

   - Checamos se tudo está correto com o deployment e na recepção do projeto pelo Pod.

   - *kubectl describe deployments*  ::  recebe mais detalhes dos deployments. Conseguimos saber se o projeto está de fato rodando e o que está rodando nele.


## Checando Pods

   - *kubectl get pods*  ::  verifica os Pods.

   - *kubectl describe pods*  ::  recebe mais detalhes sobre os pods.


## Configurações do kubernetes

   - *kubectl config view*  ::  verifica como o kubernetes está configurado, no caso recebe informações importantes baseadas no minikube, que é onde o kubernetes está sendo executado.


## Services 

   - As aplicações do kubernetes não se conectam com o mundo exterior.

   - Para resolver esse problema, criamos um service que possibilita expor pods

   - Os Pods são criados para serem destruídos e perderem tudo, ou seja, os dados gerados neles também são apagados. Isso acontece para que o kubernetes reinicia os pods a todo momento, ou troca por outro, para resolver algum problema.

   - O service é uma entidade separada dos pods, que expõe eles a uma rede.


## Criando service

   - *kubectl expose deployment <NOME> --type=<TIPO> --port=<PORTA>*  ::  cria um serviço e expõe os pods. O NOME na linha de comando é o nome de um deployment já criado, o tipo de service mais comum utilizado é o LoadBalancer, esse expõe todos os pods, e uma porta deve ser informada para onde o serviço será consumido.


## Gerando ip de acesso

   - *minikube service <NOME>*  ::  gera um ip que aparece no terminal e também uma aba no navegador é aberta com o projeto. Desta maneira, temos um projeto rodando pelo kubernetes. Esse NOME deve ser o mesmo que é utilizado na criação do deployment.


## Verificando serviços

   - *kubectl get services*  ::  obtem detalhes dos serviços criados

   - *kubectl describe services/<NOME>*  :: descreve com mais detalhes um serviço específico.


## Replicando aplicação

   - *kubectl scale deployment/<NOME> --replicas=<NUMERO>*  ::  replica a aplicação para outros pods. Usar o comando ***minikube dashboard*** para verificar as mudanças na orquestração.


## Verificar número de réplicas

   - *kubectl get rs*  ::  checa o número de réplicas, desta maneira temos o status das réplicas do projeto.


## Diminuir número de réplicas

   - *kubectl scale deployment/<NOME> --replicas=<NUMERO_MENOR>*  ::  o comando é o mesmo para replicar o deployment, porém basta diminuir o número de réplicas, o kubernetes se encarrega de reduzir o número de servidores da orquestração.


## Atualizar imagem

   - *kubectl set image deployment/<NOME> <NOME_CONTAINER>=<NOVA_IMAGEM>*  ::  atualiza a imagem. Para isso, devemos ir atrás do nome do container que é dado pelo dashboard dentro do Pod, devemos pegar o node manager(control plane), desta maneira, ao atualizar o control plane os os nodes serão atualizados após a atualização. Outro detalhe é que a nova imagem deve ser outra versão que a atual, devido a isso, devemos subir uma outra versão da nossa imagem no dockerhub com uma nova tag.


## Desfazer alteração

   - *kubectl rollout undo deployment/<NOME>*  ::  desfaz uma alteração. Para verificarmos uma alteração utilizamos ***kubectl rollout status deployment/<NOME>***. Se utilizarmos em conjunto com ***kubectl get pods*** é possível indentificar problemas. Esses problemas seriam por exemplo, a alteração para uma imagem que não existe, o comando de update da nova imagem não aponta erro, porém quando as imagens forem inseridas aos pods percebemos que, com auxilio do comando ***kubectl get pods*** que os status deles estão apontando um erro.


## Deletar serviço

   - *kubectl delete service <NOME>*  ::  deleta o serviço do kubernetes, desta maneira os Pods não terão mais conexão externa. Portanto, não teremos mais acesso a eles. 


## Deletar um Deployment

   - *kubectl delete deployment <NOME>*  ::  deleta um deployment, desta forma paramos os pods.


## Modo Declarativo

   - Semelhante ao Docker Compose, guiado por um arquivo.

   - Torna as configurações mais simples, já que o comando indicará o arquivo que deverá ser lido.

   - YAML também é utilizado para escrever o arquivo de kubernetes.


## Chaves mais utilizadas

   - apiVersion: versão da ferramenta utilizada
   - kind: tipo do arquivo (deployment, service)
   - metadata: descreve algum objeto, inserindo chaves como name
   - replicas: número de réplicas de nodes/pods
   - containers: definir as especificações de containers como: nome e imagem


## Executando arquivo de Deployment

   - *kubectl apply -f <arquivo>*  ::  executa o arquivo de deployment. Tem que garantir que o minikube está rodando.


## Parando o Deployment de modo declarativo

   - *kubectl delete -f <arquivo>*  ::  para a execução do deployment baseado no arquivo, o pods são excluídos e os serviços finalizados. O kubernetes entende qual deployment parar graças ao arquivo passado por parâmetro.


## Executando service de modo declarativo

   - *kubuctl apply -f <arquivo>*  ::  idêntico ao deployment, porém no corpo do arquivo o kind dele é diferente.


## Parando serviço de modo declarativo

   - *kubectl delete -f <arquivo>*  :: idêntico ao deploymente, deleta o serviço. Não apaga os pods, porém não tem mais acesso ao serviço no navegador.


## Atualizando o projeto no modo declarativo

   - Primeiramente cria uma nova versão e sobe no dockerhub.

   - Depois basta alterar no arquivo de deployment a tag e reaplicar o comando de apply.


## Unindo arquivo do projeto

   - Precisa unir o deployment e o serviço em um arquivo

   - A separação de objetos (deployment e service) para o YAML é com ---. Na hora da criação do arquivo yaml, basta colocar "---" antes e depois de todo o corpo para o service e deployment.

   - Desta maneira cada um deles será executado.

   - Colocar service antes de deployment (boa prática)!

   - Muito útil para salvar tempo, pois só precisa de um comando para rodar o projeto todo. Desta maneira só precisa dar apply no arquivo que une o deployment e service.