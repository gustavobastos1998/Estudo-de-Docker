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