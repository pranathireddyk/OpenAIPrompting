import csv
import json
import time
import openai
def parsed(json_string):
    try:
        k = json.loads(json_string)
        return k
    except:
        print(json_string)
    return None

def writeIntoFile(result):
    parsed_objects = []
    for json_string in result:
        json_temp = parsed(json_string)
        if json_temp:
            parsed_objects.append(json_temp)
            result_json = json.dumps(parsed_objects, indent=2)
            print(result_json)  
    with open('labels2.txt', 'a', newline='') as file:
        file.write(result_json)

def test(result):
    k = []
    t = 0
    for json_string in result:
        try:
            k.append(json.loads(json_string))
            l = json.dumps(k, indent=2)
        except:
            print(l)
        finally:
            for i in range(1000):
                t += 1
                print(t)

messages = [ {"role": "system", "content": "I want you to find labels on the given input string. Use your own knowledge to determine what the input string is and what it does. If it is a cloud provider-related component, please also include the cloud provider short name as a tag along with related keywords named as labels. Format the answer as a JSON object. Do not include generic labels and try to generate as many labels as possible. The labels should be Component, Cloud Provider and Labels."} ]
file = open('Components.csv')
csvreader = csv.reader(file)
keywords = []
for row in csvreader:
    keywords.append(row[0])
result = []
t = 0
try:
    for i in keywords[1368:1400]:
        t += 1
        openai.api_key = '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'
        message = i
        if message:
            messages.append(
                {"role": "user", "content": message},
            )
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            reply = chat.choices[0].message.content
            result.append(reply)
            messages.append({"role": "assistant", "content": reply})
            test(result)
except:
    print("Rate limit error at ", t)
finally:
    writeIntoFile(result)