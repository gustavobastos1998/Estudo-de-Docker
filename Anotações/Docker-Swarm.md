## O que é orquestração de containers?

   - É o ato de conseguir gerenciar e escalar os containers da nossa aplicação

   - Um serviço rege sobre outros, verificando se eles estão funcionando como devem

   - A aplicação estará sempre disponível e saudável com a orquestração de containers.


## O que é Docker Swarm?

   - Ferramenta Docker para orquestrar containers

   - Podemos escalar horizontalmente(cluster) nossos projetos de maneira simples

## Conceitos fundamentais

   - nodes: é uma máquina que faz participa do swarm

   - manager node: node que gerencia os demais nodes, pode haver mais de um

   - worker node: nodes que trabalham em função do manager
   
   - service: um conjunto de tasks que o manager node manda o work node executar
   
   - task: comandos que são executados nos nodes


## Maneiras de executar o swarm

   - Como o swarm é uma ferramenta para orquestração de containers, precisamos de mais máquinas para exemplificar o seu uso

   - Para isso há duas soluções: AWS ou Docker Labs

   - Docker Labs roda no navegador mas expira em 4 horas