import requests
# from playsound import playsound
import json
# from os import chdir
json_data = {
    "action": "echo"
}

# url ='http://18.183.196.94:8081/handle'
header = {'Content-Type':'application/json'}
url ='http://localhost:80/handle'
# url ='http://localhost:8081'
d = json.dumps(json_data)
response = requests.post(url,headers = header,data = d)
# response = requests.post(url,headers = header)
print("respose status "+str(response.status_code))
f = open("audio3.wav","wb")
f.write(response.content)
f.close()
# chdir("/Users/lakky/raspy/post")
# playsound("audio3.wav")




