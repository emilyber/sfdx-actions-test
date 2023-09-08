

$ docker run -ti -p 8000:8000 flosumhub/vlocity:1.1.3

> snapshot-vlocity@1.1.3 start
> node .

  vlocity:api:startAPI Starting up the Express server... +0ms
Error on API start up:
[Error: EACCES: permission denied, mkdir '/home/node/app/tmp'] {
  [stack]: "Error: EACCES: permission denied, mkdir '/home/node/app/tmp'",
  [message]: "EACCES: permission denied, mkdir '/home/node/app/tmp'",
  errno: -13,
  code: 'EACCES',
  syscall: 'mkdir',
  path: '/home/node/app/tmp'
}
