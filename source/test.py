from urllib import request
import requests
from io import BytesIO
headers = {'User-Agent': 'Chi dep trai bro'}
payload = {'file': open('E:/WorkSpace/DotNet/app/DoAn/Server_API_Fast/deep-learning-master (1)/deep-learning-master/CV/apps/Recognition/FaceVerify/deploy/database/test_images/messi/2.jpg', 'rb'),'id':'123456'}
url = "http://127.0.0.1:8000/predict"
session = requests.Session()
response = session.post(url, headers=headers, files={'file': open('E:/WorkSpace/DotNet/app/DoAn/Server_API_Fast/deep-learning-master (1)/deep-learning-master/CV/apps/Recognition/FaceVerify/deploy/database/test_images/messi/2.jpg', 'rb'), 'id': 2003})
print("status", response.status_code)
# print("json", response.json())
print("Content:", response.content)