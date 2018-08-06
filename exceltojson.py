import boto3
import json
import pandas as pd
def lambda_handler(event, context):
    s3 = boto3.resource('s3')
    object=s3.Object('newsourcebucket','MIC.xls')
    df=pd.read_excel(object,sheetname='MIC List by CC')
    newdict=df.to_json()
    s3.Object('newtargetbucket', 'MIC.json').put(
            Body=(bytes(json.dumps(newdict, indent=2).encode('UTF-8')))
    #copying original excel file
    copy_source={
        'Bucket':'newsourcebucket',
        'Key':'MIC.xls'
    }
    target_bucket=s3.Bucket('newtargetbucket')
    target_bucket.copy(copy_source,'onemorecopy.xls')
    
    return 'Excel File Successfully converted to JSON'