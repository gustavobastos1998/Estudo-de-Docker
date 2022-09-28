## Comandos 

### Para executar um container

   - docker run <imagem>  ::  O problema com esse comando é que logo após a criação do container e execução da imagem, o container é fechado. 

   ### Flags

       - -it  ::  Já com a adição da flag '-it' a imagem passa a ser iterativa. Exemplo: docker run -it ubuntu, rodará a imagem oficial que está no hub.docker.com para o ubuntu, fornecendo um terminal linux de imediato sem precisar ter o ubuntu na máquina. 

## Verificar containers executados

   - docker ps | docker container ls  ::  Exibe quais containers estão sendo executados no momento. 
   
   ### Flags
   
       - -a  ::  Mostra todos os containers já executados na máquina. 