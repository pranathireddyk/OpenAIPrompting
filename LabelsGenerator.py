import csv
import json
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
            with open('nonjson.txt', 'a', newline='') as file:
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
        with open('Labels.txt', 'a', newline='') as file:
            file.write(result_json)


def openaiGeneration(keywords, keywords_count, result):
    openai.api_key = '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'
    openai.organization = 'org-LZbZquaU2q5hnjfB6ZLB7Ks4'
    k = keywords_count
    tokens = 0
    try:
        for i in keywords[k:]:
            message = i
            messages = [ {"role": "system", "content": "I want you to find labels on the given input string. Use your own knowledge to determine what the input string is and what it does. If it is a cloud provider-related component, please also include the cloud provider short name in the labels along with related keywords named as labels. Return the answer as a JSON object without any extra text. Do not include generic labels and try to generate as many labels as possible. The labels should be Component and Labels. The component is "} ]
            if message:
                messages[0]["content"] += message
                chat = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo", messages = messages
                )
                reply = chat.choices[0].message.content
                result.append(reply)
                keywords_count += 1
    except Exception as e:
        print(str(e))
        print("Rate limit error at ", keywords_count)
        print("Continuing generating labels for the remaining components.")
        return [keywords_count, result]
    print("All the component labels are generated successfully.")
    return [-1, result]


file = open('Components.csv')
csvreader = csv.reader(file)
keywords = []
for row in csvreader:
    keywords.append(row[0])
result = []
res = 0
while (res != -1):
    ret = openaiGeneration(keywords, res, result)
    res = ret[0]
    result = ret[1]
writeIntoFile(result)