
Could you please clarify some doubts about the docker code?


When uploading the docker image, I already need to point a user and a password, as stated in flossumpmd's dockerhub documentation
Something like:
![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)



I understand that in the url that we are going to make available, they will send exactly that user and password that appears in the code + the user and password (the same one that we uploaded in the docker image) that we inserted in the fields of the settings for PMD in the flosum, right?





Will they always return the same token in the login result? As in the print below.




Another question: the command to call the PMD analysis does not use the login at any time, is that right?



Sorry for the questions, but the security team will question me about this login and its security and I need to be sure of the information to be able to see a way that the bank does not prevent the docker upload in the aws.