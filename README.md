emily@LAPTOP-H62FPIST MINGW64 ~/OneDrive/Área de Trabalho/vlocity-flosum/study_vlocity (main)
$ docker run -p 8000:8000 flosumhub/vlocity:1.1.1-beta.1

> snapshot-vlocity@1.1.1-beta.1 start
> node .

2023-08-31T17:11:21.832Z vlocity:api:startAPI Starting up the Express server...
Error on API start up:
[Error: EACCES: permission denied, mkdir '/home/node/app/tmp'] {
  [stack]: "Error: EACCES: permission denied, mkdir '/home/node/app/tmp'",
  [message]: "EACCES: permission denied, mkdir '/home/node/app/tmp'",
  errno: -13,
  code: 'EACCES',
  syscall: 'mkdir',
  path: '/home/node/app/tmp'
}
npm notice 
npm notice New minor version of npm available! 9.6.7 -> 9.8.1
npm notice Changelog: <https://github.com/npm/cli/releases/tag/v9.8.1>
npm notice Run `npm install -g npm@9.8.1` to update!
npm notice 

