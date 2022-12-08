COMO RESOLVER CONFLITOS DEVELOP TO MAIN

O banco não permite push direto para branch develop e/ou main, logo segue uma possibilidade caso caia em conflito nesse Pull request, mas esse doc não é um diretiva do coe, cada desenvolvedor pode resolver o conflito da maneira que acha melhor, isso é apenas uma possibilidade:

>>> antes de tudo, feche o PR aberto.

1 - crie uma nova branch em cima da branch main

- entre no git bash:

git clone link_teu_repo
- comandos abaixo é para deixar as branchs de develop e main atualizadas na sua maquina loca:
git checkout develop
git pull
git checkout main
git pull

- crie uma nova branch para resolver o conflito, ele será o clone da main.
git checkout -b "feature/exemplo_resolvendo_conflito"

- fazendo isso ficará logada na tua branch nova

2 - Jogue o que está na develop na tua branch nova "feature/exemplo_resolvendo_conflito"
- ainda no git bash
git merge develop --no-ff

3 - agora é a hora de resolver o conflito

- ainda no git bash

code .

- ele abrirá o vscode, espere carregar que será mostrado os arquivos com problema de conflito, caso queria ver os arquivos em lista via linha de comando  digite "git status" no terminal do vscode

- clique nas opções "accept incoming changing" ou "accept current changing" no arquivo de acordo com a sua analise.
- no terminal do vscode digite
git add . && git commit -m "correcao de conflito da develop para main"
git push -u origin feature/exemplo_resolvendo_conflito

- o evento de push acima vai disparar o action de validação de complience (aqui é fluxo esteira)
- espera o PR abrir automaticamente
- edite o PR para disparar a esteira novamente e gerar a versão do pacote e implantar em IT
- finalizado clique em "merge" e "confirme merge"
- isso vai disparar a esteira que implanta em UAT
- finalizando a esteira vai ser aberto o PR da develop para a Main
- analise se o conflito continua, estando ok
- siga o fluxo normal de mudança
