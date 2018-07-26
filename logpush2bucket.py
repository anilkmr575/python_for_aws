import boto
import boto.s3
import sys
from boto.s3.key import Key

AWS_ACCESS_KEY_ID = 'AKIAIPU32PYEYHRUDDUQ'
AWS_SECRET_ACCESS_KEY = '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'

bucket_name = AWS_ACCESS_KEY_ID.lower() + 'devopser2'
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
        AWS_SECRET_ACCESS_KEY)


bucket = conn.create_bucket(bucket_name,
    location=boto.s3.connection.Location.DEFAULT)

testfile = "D:\Projects\me_python\python_aws\logs.txt"
print('Uploading %s to Amazon S3 bucket %s' % \
   (testfile, bucket_name))
