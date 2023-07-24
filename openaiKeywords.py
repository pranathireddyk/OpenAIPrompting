import csv
import json
import time
import openai
import re

def parsed(json_string):
    try:
        json_data = json.loads(json_string)
        return json_data
    except:
        pattern = r"{\s*\"Component\":.*?}"
        match = re.findall(pattern, json_string, re.DOTALL)
        try:
            json_data = json.loads(match[0])
            return json_data
        except:
            with open('non-json.txt', 'a', newline='') as file:
                file.write(json_string)
    return None

def writeIntoFile(result):
    parsed_objects = []
    result_json = None
    for json_string in result:
        json_temp = parsed(json_string)
        if json_temp:
            parsed_objects.append(json_temp)
            result_json = json.dumps(parsed_objects, indent=2)
    if result_json:
        with open('test.txt', 'a', newline='') as file:
            file.write(result_json)


file = open('Questions.csv')
csvreader = csv.reader(file)
openai.api_key = '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'
openai.organization = 'org-LZbZquaU2q5hnjfB6ZLB7Ks4'
keywords = []
for row in csvreader:
    keywords.append(row[0])
result = []
keywords_count = 0
tokens = 0
try:
    for i in range(len(keywords)):
        message = keywords[i] + "'"
        messages = [ {"role": "system", "content": "I want you to find labels on the given input string. Use your own knowledge to determine what the input string is and what it does. If it is a cloud provider-related component, please also include the cloud provider short name in the labels along with related keywords named as labels. Return the answer as a JSON object without any extra text. Do not include generic labels and try to generate as many labels as possible. The labels should be Component and Labels. The component is '"} ]
        if message:
            messages[0]["content"] += message
            tokens += len(re.findall(r'\w+', messages[0]["content"]))
            if tokens > 8000:
                time.sleep(70)
                tokens = tokens - 8000
            try:
                chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages=messages
                )
                reply = chat.choices[0].message.content
                result.append(reply)
                keywords_count  += 1
            except:
                i -= 1
except Exception as e:
    print(str(e))
    print("Rate limit error at ", keywords_count )
finally:
    writeIntoFile(result)
