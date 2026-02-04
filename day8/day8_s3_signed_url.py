
import boto3

def generate_signed_upload_url():
    s3 = boto3.client("s3")

    url = s3.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": "my-ai-bucket",
            "Key": "uploads/sample.txt"
        },
        ExpiresIn=3600
    )
    return url

if __name__ == "__main__":
    print("✅ AWS S3 Signed Upload URL:")
    print(generate_signed_upload_url())
