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
  
Using named profiles : https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html
- command : export AWS_PROFILE=user1

Error encounteres:
- https://stackoverflow.com/questions/68463393/cloudformation-template-using-existing-iam-role-in-for-lambda-functions
- Template error: instance of Fn::GetAtt references undefined resource HelloWorldFunctionRole

Difference between SAM template and Cloudformation template :
- https://stackoverflow.com/questions/50140885/difference-between-sam-template-and-cloudformation-template
