Só pra documentar o que fiz na minha maquina pessoal pq não tenho licensa do docker no banco:
1- subi a imagem docker da flosum, de uns 15 dias atrás
docker pull flosumhub/vlocity:1.2.4
2 - passar para um arquivo tar ou tar.gz ou qualquer merda de extensão
 docker save flosumhub/vlocity:1.2.4 > image.tar
3 - depois pode extrair usando tar xfv ou na preguiça extrai no windows(meu caso)
4 - depois de extrair só ir no arquivo de package.json pra ver que versão ão usando da vlocity, no caso a de 8 meses atras, o link do fonte da vlocity é esse:
https://github.com/vlocityinc/vlocity_build/tree/v1.17.6
que realmente é umas das ultimas da vlocity, olhando no site do npm
https://www.npmjs.com/package/vlocity/v/1.17.6?activeTab=code
agora pq diaxo querem saber se ta na ultima isso eu não sei.  
Só pra alinhar, a próxima versão depois da 1.17.6 é a 1.17.8(latest até o momento, hoje é dia 24/08 umas 18 horas)
Abaixo o que tinha no package.json do docker da flosum, aumentei o tamanho da letra onde fala a versão usada, e um print do vscode com esse arquivo:
{
  "name": "snapshot-vlocity",
  "version": "1.2.4",
  "description": "",
  "main": "dist/index.js",
  "scripts": {
    "compile": "javascript-obfuscator src --output dist --target node",
    "compile:prod": "bash build.sh",
    "start": "node .",
    "dev": "nodemon -r dotenv/config src/index.js"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "adm-zip": "^0.5.2",
    "body-parser": "^1.19.0",
    "crc-32": "^1.2.0",
    "debug": "^4.2.0",
    "dotenv-safe": "^8.2.0",
    "express": "^4.17.1",
    "fs-extra": "10.0.0",
    "helmet": "^7.1.0",
    "js-yaml": "^3.13.1",
    "jsforce": "1.11.1",
    "puppeteer": "22.15.0",
    "uuid": "^8.3.0",
    "vlocity": "1.17.6",
    "xterm-colors": "^1.0.1"
  },
  "devDependencies": {
    "eslint": "^7.11.0",
    "eslint-config-airbnb-base": "^14.2.0",
    "eslint-plugin-import": "^2.22.0",
    "javascript-obfuscator": "^4.0.2",
    "nodemon": "^2.0.6"
  }
}
print do vscode
