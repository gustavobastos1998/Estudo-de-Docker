## O que são volumes?

   - Uma forma prática de persistir dados em aplicações e não depender de containers para isso.

   - Todo dado criado por um container é salvo nele, quando removemos o container os dados são perdidos.

   - Então, precisamos dos volumes para gerenciar os dados e também fazer backups de forma mais simples.


## Tipos de volumes

   - Anônimos: diretórios criados pela flag -v, porém com um nome aleatório.

   - Nomeados: volumes com nomes, podemos referí-los facilmente e saber para que são utilizados no nosso ambiente.

   - Bind mounts: salvamos os dados na nossa máquina, sem o gerenciamento do Docker, informando um diretório com essa finalidade.


## Criando volumes

   - Utilizamos a flag -v na hora de rodar um container. 

   - -v  ::  para criar um volume anônimo usamos "docker run -v /data <container>" onde /data é o diretório que contém o volume anônimo. Também há a possibilidade para de dar nomes para esses volumes colocando "nome_do_volume:" antes do diretório. Exemplo: "docker run -v volume_name:/data <container>". OBS: ao criar volumes nomeados, esse diretório informado na linha de comando deve ser o mesmo que o WORKDIR no Dockerfile + a pasta onde será salvo na sua máquina. Exemplo: WORKDIR = /var/www/html/, diretório na máquina = /messages -> "docker run -v nome_volume:/var/www/html/messages <container>". Para armazenar os valores na nossa máquina, utilizamos o volume Bind Mounts, para isso digitamos "docker run -v /dir/data:/data".


## Bind Mount 

   - Não serve apenas para volumes.

   - Pode ser utilizado para atualização em tempo real do projeto, sem ter que refazer o build da imagem a cada atualização. 

   - Para que isso aconteça, basta retirar a última pasta do diretório de ambas as partes no comando. Exemplo, comando para volume nomeado = docker run -v nome_volume:/var/www/html/messages <container>, já para o bind mount:
   ``` 
   docker run -v C:/Users/Aluno/Estudo-docker/Exemplos-php-volume:/var/www/html/ <container>
   ```