import requests
import json

credentials = json.load(open("credentials.json"),)

## Input 
input_text = "Today's systems are not personalized enough for learners and generally provide a standard course regardless of the learner's background."
print(input_text)

## Correction
auth_key=credentials['apiKey']
url = credentials['url']

payload1 = dict(auth_key=auth_key, text=input_text, target_lang="FR")
res1 = requests.post(url, data=payload1)

french_output = json.loads(res1.text)['translations'][0]['text']
#print(french_output)

payload2 = dict(auth_key=auth_key, text=french_output, target_lang="EN")
res2 = requests.post(url, data=payload2)

output_text = json.loads(res2.text)['translations'][0]['text']
#print(output_text)

## Comparison
input_list = input_text.split()
output_list = output_text.split()

similarity_list = [0]*len(output_list)
min_len = min(len(input_list), len(output_list))

for i in range(min_len):
    if input_list[i]==output_list[i]:
        similarity_list[i]+=1
for i in range(1,min_len+1):
    if input_list[-i]==output_list[-i]:
        similarity_list[-i]+=1

output_highlight_list = output_list.copy()
for i in range(len(output_highlight_list)):
    if similarity_list[i]!=0:
        output_highlight_list[i]=" "*len(output_highlight_list[i])
    else:
        output_highlight_list[i]="‾"*len(output_highlight_list[i])

print(output_text)
print(' '.join(output_highlight_list))




	