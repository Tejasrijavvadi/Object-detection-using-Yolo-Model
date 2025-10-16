import os, requests
from glob import glob

AI_URL = "http://localhost:8001/detect"
folder = "test_images"

for path in glob(os.path.join(folder, "*.*")):
    filename = os.path.basename(path)
    print("Processing:", filename)
    with open(path, "rb") as f:
        resp = requests.post(AI_URL, files={"file": (filename, f, "image/jpeg")})
        print(resp.status_code, resp.text[:200], "...\n")
