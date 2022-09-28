## Comandos 

### Para executar um container

   - docker run <imagem>  ::  O problema com esse comando é que logo após a criação do container e execução da imagem, o container é fechado. 

   - docker run -it <imagem>  ::  Já com a adição do parâmetro '-it' a imagem passa a ser iterativa. Exemplo: docker run -it ubuntu, rodará a imagem oficial que está no hub.docker.com para o ubuntu, fornecendo um terminal linux de imediato sem precisar ter o ubuntu na máquina. 