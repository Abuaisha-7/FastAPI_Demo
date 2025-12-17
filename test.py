import os
import requests

public_key = os.getenv("IMAGEKIT_PUBLIC_KEY")
private_key = os.getenv("IMAGEKIT_PRIVATE_KEY")
file_path = "hello.png"  # small test file

with open(file_path, "rb") as f:
    files = {"file": (file_path, f)}
    data = {"fileName": file_path}

    response = requests.post(
        "https://upload.imagekit.io/api/v1/files/upload",
        files=files,
        data=data,
        auth=(public_key, private_key)
    )

print(response.status_code)
print(response.text)
