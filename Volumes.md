## O que são volumes?

   - Uma forma prática de persistir dados em aplicações e não depender de containers para isso.

   - Todo dado criado por um container é salvo nele, quando removemos o container os dados são perdidos.

   - Então, precisamos dos volumes para gerenciar os dados e também fazer backups de forma mais simples.


## Tipos de volumes

   - Anônimos: diretórios criados pela flag -v, porém com um nome aleatório.

   - Nomeados: volumes com nomes, podemos referí-los facilmente e saber para que são utilizados no nosso ambiente.

   - Bind mounts: salvamos os dados na nossa máquina, sem o gerenciamento do Docker, informando um diretório com essa finalidade.


