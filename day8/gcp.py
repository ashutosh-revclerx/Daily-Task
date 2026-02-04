# ==========================================
# Day 8: GCP Signed URL
# ==========================================

from google.cloud import storage

def generate_signed_upload_url():
    client = storage.Client()
    bucket = client.bucket("my-gcs-bucket")
    blob = bucket.blob("uploads/sample.txt")

    url = blob.generate_signed_url(
        expiration=3600,
        method="PUT"
    )
    return url

if __name__ == "__main__":
    print("✅ GCP Signed Upload URL:")
    print(generate_signed_upload_url())
