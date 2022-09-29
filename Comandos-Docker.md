## Executar container

- docker run <imagem>  ::  O problema com esse comando é que logo após a criação do container e execução da imagem, o container é fechado. 

   ### Flags  *run*
- ```
  -d  ::  executar um container com a flag '-d' dizemos que ele fica "detached". A imagem desse container fica rodando na máquina sem ocupar o terminal, executando em background. 
  
  --name  ::  define um nome para o container.

   -it  ::  Já com a adição da flag '-it' a imagem passa a ser iterativa. Exemplo: docker run -it ubuntu, rodará a imagem oficial que está no hub.docker.com para o ubuntu, fornecendo um terminal linux de imediato sem precisar ter o ubuntu na máquina.
  ```


## Verificar containers executados

   - docker ps | docker container ls  ::  Exibe quais containers estão sendo executados no momento. 
   
   ### Flags *ps*
   - ```
       - -a  ::  Mostra todos os containers já executados na máquina. 
     ```


## Expor portas

   - Os containers de docker não tem conexão com nada além deles. Portanto, para fazer essa conexão utilizamos a flag '-p' ao dar **run** em um container, especificando a porta do container, lembrando que essa porta da imagem que é servida pelo container deve existir, e a porta onde eu queira por na minha máquina. Exemplo : ***docker run nginx -p 80:80***, desta maneira, o container será acessível na porta 80 do localhost.

   ### Flags *run*
   - ```
     -p <numero_porta_localhost>:<numero_porta_container>  ::  utilizado para expor portas e conectá-las ao localhost. 

     --rm  ::  remove automaticamente o container após sua utilização, após dar o stop no container ele some do docker ps -a.
     ```


## Parando containers

   - *docker stop <id_container ou nome_container>*  ::  para um container, desta maneira liberando os recursos que ele utiliza. 


## Reiniciando containers

   - *docker start <id_container ou nome_container>*  ::  volta a rodar um container antes parado. Caso queira aproveitar um container antigo, opte pelo comando  e não crie um novo com o comando **run**. 

   ### Flags *start*
   - ```
     -i  ::  torna o container que deseja reutilizar interativo novamente, semelhante a flag -it quando o comando run é executado.
   ```


## Verificar logs do docker

   - *docker logs <id_container>*  ::  exibe as últimas ações realizadas em um container. 

   ### Flags *logs*
   - ```
     -f  ::  informa as informações de logs em tempo real, ^C para parar a execução do '-f'. 
   ```


## Removendo containers

   - *docker rm <id_container ou nome_container>*  ::  remove um container da máquina. Para remover mais de um, basta escrever o id ou o nome do container separado por um espaço. Com o container removido, ele deixará de aparecer no ***docker ps -a***. 

   ### Flags *rm*
   - ```
     -f  ::  força a parada de um container, pode ser utilizado em um container que está sendo executado no momento, porém, é preferível que utilize o comando stop antes de o fazer, para que não perca algo importante sem checar duas vezes.
   ```
    

## Copiando arquivos de containers

   - *docker cp <container>:<path_fonte> <path_destino>*  ::  copia arquivos de um diretório para um container ou vice-versa. O container deve estar rodando para que haja a cópia.


## Verificar informações de processamento

   - *docker top <container>*  ::  verifica dados de execução de um container. Desta maneira, temos acesso a quando ele foi criado, id, descrição do comando CMD do Dockerfile.


## Verificar dados de um container

   - *docker inspect <container>*  ::  verifica informações como: id, data de criação, imagem e muito mais.


## Verificar processamento

   - *docker stats <container>*  ::  verifica os processos que estão sendo executados em um container. Temos acesso ao processamento e memória gasta por ele.


## Login com o Dockerhub

   - *docker login*  ::  faz o login com sua conta dockerhub.


## Logout com o Dockerhub

   - *docker logout*  ::  faz o logout com a conta dockerhub, não permitindo enviar imagens pois não é mais autenticado.


## Iniciando imagem

   - *docker build <path_do_Dockerfile>*  ::  'builda' a imagem a partir do Dockerfile indicado pelo diretório.

   ### Flags *build*
   - ```
     -t  ::  atribui um nome à imagem criada. É possível inserir nome e tag ao mesmo tempo, exemplo: docker build -t nome:tag <path_do_Dockerfile>.
   ```


## Download de imagens

   - *docker pull <imagem>*  ::  faz o download da imagem específica, desta maneira caso vá ser usado em outro container, a imagem já estará pronta para ser utilizada.


## Alterando o nome da imagem e tag

   - *docker tag <imagem> <nome>*  ::  modifica o nome da imagem.

   - *docker tag <imagem> <nome>:<tag>*  ::  também podemos modificar a tag da imagem, servindo como uma versão da imagem.

   - *docker tag <imagem> <nome>:<tag>*  ::  modifica o nome e tag de uma imagem atribuida a um id.


## Removendo imagens

   - *docker rmi <imagem>*  ::  remove a imagem desejada. Se algum container estiver utilizando a imagem, uma exception será levantada.

   ### Flags *rmi*
   - ```
     -f  ::  força a remoção da imagem.
   ```

## Removendo imagens e containers

   - *docker system prune*  ::  remove imagens, containers e networks não utilizado.