
# Data Preparation Pipeline using Lambda ,S3 and Pandas

We will be using pandas to convert Excel file into json stored in AWS S3 running the code on  AWS Lambda.

## Getting Started

Since pandas is not available on AWS we will have to create a lambda package with pandas.The deployment "functionversion0.py" code will be uploaded and zipped with it.

Architecture:
a)AWS lambda (for the server less code)
b)2 aws s3 :source and destination bucket for storing and saving.Also will trigger the lambda for conversion process when a file is added to S3 source bucket
aws 
c)EC2:  to prepare the deployment package
d)aws cloudwatch logs :optional, to check if events are working fine in the initial stage 


### steps involved

1.create a deployment package
follow the below mentioned tutorial to make a deployment package
https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example-deployment-pkg.html#with-s3-example-deployment-pkg-python

In the code section use the code provided with in this repo.

in step 7 where we are installing libraries install pandas also

2.Create the Execution Roles:

give lambda policy access to use ec2 zipped code ,s3 and cloudwatch logs.Use it for roles and select this role when creating lambda function.

3.Create a lambda function ,in this case "Functionversion0".Manually or through AWS CLI.


### Manual Test
1.Add a file to the Souce bucket .
2.Look for json file with same name and .json extension in destination bucket.
