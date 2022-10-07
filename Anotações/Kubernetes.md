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

