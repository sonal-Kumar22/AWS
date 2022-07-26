This folder contains buildspec file which automates the process of 
- generating the build file
- uploading the build file into S3 bucket 
- clearing cache in cloudfront distribution

Here,
We have passed values of variables marked by '$' in codebuild environment section.
we have declared the variables in key-value pair in the codebuild.
The variables also contains name of the S3 bucket and cloudfront distribution present in the env where codebuild is created.

echo "REACT_APP_OKTA_ISSUER=$REACT_APP_OKTA_ISSUER" >> .env.development
- this lines will create a file named env.development & store key-value in .env.development file like -> REACT_APP_OKTA_ISSUER=value
yarn install
- this command installs yarn package
yarn run build:dev
- this command creates a build using command stored under "build:dev" like -> "build:dev": "env-cmd -f .env.development react-scripts build"
