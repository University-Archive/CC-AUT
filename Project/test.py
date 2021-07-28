import requests
import json

# req = requests.get("http://localhost:5000", data=json.dumps({
req = requests.get("http://172.18.0.4:50051/", data=json.dumps({
    # "code": "/media/ali/2A4CA3370389FB76/University/Sem8/CC/Project/max.py",
    # "code": "/media/ali/2A4CA3370389FB76/University/Sem8/CC/Project/average.py",
    "code": "/media/ali/2A4CA3370389FB76/University/Sem8/CC/Project/programs/min.py",
    # "code": "/media/ali/2A4CA3370389FB76/University/Sem8/CC/Project/sort.py",
    "input": "/media/ali/2A4CA3370389FB76/University/Sem8/CC/Project/inputs/inp.txt",
    "output": "/media/ali/2A4CA3370389FB76/University/Sem8/CC/Project/out.txt"
}))

print(req.json())

