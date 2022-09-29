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
     ```


## Parando containers

   - *docker stop <id_container ou nome_container>*  ::  para um container, desta maneira liberando os recursos que ele utiliza. 


## Reiniciando containers

   - *docker start <id_container ou nome_container>*  ::  volta a rodar um container antes parado. Caso queira aproveitar um container antigo, opte pelo comando  e não crie um novo com o comando **run**. 

   ### Flags *start*
    -i  ::  torna o container que deseja reutilizar interativo novamente, semelhante a flag -it quando o comando run é executado. 


## Verificar logs do docker

   - *docker logs <id_container>*  ::  exibe as últimas ações realizadas em um container. 

   ### Flags *logs*

    -f  ::  informa as informações de logs em tempo real, ^C para parar a execução do '-f'. 


## Removendo containers

   - *docker rm <id_container ou nome_container>*  ::  remove um container da máquina. Para remover mais de um, basta escrever o id ou o nome do container separado por um espaço. Com o container removido, ele deixará de aparecer no ***docker ps -a***. 

   ### Flags *rm*
    -f  ::  força a parada de um container, pode ser utilizado em um container que está sendo executado no momento, porém, é preferível que utilize o comando stop antes de o fazer, para que não perca algo importante sem checar duas vezes.