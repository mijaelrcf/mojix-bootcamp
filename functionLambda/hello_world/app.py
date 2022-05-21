import boto3
import uuid

def upload_to_aws(local_file, s3_file):
    s3 = boto3.client('s3')
    
    nameFileSplit = s3_file.split(".")
    nameFile = uuid.uuid4() + "." nameFileSplit[1]

    try:
        s3.upload_file(local_file, os.environ['BUCKET_NAME'], nameFile)
        url = s3.generate_presigned_url(
            ClientMethod='get_object',
            Params={
                'Bucket': os.environ['BUCKET_NAME'],
                'Key': s3_file
            },
            ExpiresIn=24 * 3600
        )

        print("Upload Successful", url)
        return url
    except FileNotFoundError:
        print("The file was not found")
        return None
    except NoCredentialsError:
        print("Credentials not available")
        return None