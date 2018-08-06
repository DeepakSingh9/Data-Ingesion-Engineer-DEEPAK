import boto3
import json
import pandas as pd
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    #getting xls file saved in newsourcebucket
    object=s3.Object('newsourcebucket','MIC.xls')
    
    #using pandas read_excel method to read the file
    df=pd.read_excel(object,sheetname='MIC List by CC')
    
    #converting the file to json
    newdict=df.to_json()
    
    #dumping the same file to source bucket
    s3.Object('newsourcebucket', 'MIC.json').put(
            Body=(bytes(json.dumps(newdict, indent=2).encode('UTF-8')))
        
    #copying original  file from source to destination
    copy_source={
        'Bucket':'newsourcebucket',
        'Key':'MIC.json'
    }
    target_bucket=s3.Bucket('newtargetbucket')
    target_bucket.copy(copy_source,'MIC.json')
    
    return 'Excel File Successfully converted to JSON'
