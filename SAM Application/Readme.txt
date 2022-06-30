Pre-riqisite:
- install AWC CLI
- install SAM
- configure aws credentails : aws configure
- integrate sam and aws cli
- install docker (optional - for local execution)

video link : https://www.youtube.com/watch?v=MipjLaTp5nA

Commmands:
- command to build : sam build 
  this command will install all dependencies of lambda and compile them in usable forat that SAM and lambda understand
- command to deploy : sam deploy --guided (--guided is optional)
- command to delete stack : sam delete --stack-name (stack name will be asked if not put in command)
  https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-delete.html
  
  
