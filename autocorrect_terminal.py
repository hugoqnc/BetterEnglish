
import sys
import requests
import json

args = sys.argv
if len(args)!=2:
    print("Error: please specify between quotation marks one sentence to correct.")
    exit()
else:
    input_text = args[1]

credentials = json.load(open("credentials.json"),)

## Correction
auth_key=credentials['apiKey']
url = credentials['url']

payload1 = dict(auth_key=auth_key, text=input_text, target_lang="FR")
res1 = requests.post(url, data=payload1)

french_output = json.loads(res1.text)['translations'][0]['text']

payload2 = dict(auth_key=auth_key, text=french_output, target_lang="EN")
res2 = requests.post(url, data=payload2)

output_text = json.loads(res2.text)['translations'][0]['text']
print(output_text)





	