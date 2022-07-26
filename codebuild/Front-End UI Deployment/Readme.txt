This folder contains buildspec file which automates the process of 
- generating the build file
- uploading the build file into S3 bucket 
- clearing cache in cloudfront distribution

Here,
We have passed values of variables marked by '$' in codebuild environment section.
we have declared the variables in ekey-value pair in the codebuil.
The variables also contains name of the S3 bucket and cloudfront distribution.
