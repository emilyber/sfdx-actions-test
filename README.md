
Could you please clarify some doubts about the docker code?


When uploading the docker image, I already need to point a user and a password, as stated in flossumpmd's dockerhub documentation
Something like:

![Alt text](docker.png)



I understand that in the url that we are going to make available, they will send exactly that user and password that appears in the code + the user and password (the same one that we uploaded in the docker image) that we inserted in the fields of the settings for PMD in the flosum, right?
![Alt text](senhas.png)




Will they always return the same token in the login result? As in the print below.

![Alt text](mesmo_token_sempre.png)


Another question: the command to call the PMD analysis does not use the login at any time, is that right?

![Alt text](pmd_não_precisasenha.png)

Sorry for the questions, but the security team will question me about this login and its security. I need to be sure of how the login is to see how to insert a security gate validated by the bank.