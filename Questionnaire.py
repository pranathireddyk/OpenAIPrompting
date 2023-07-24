import json

def getLabels(question, selectedAnswer, data):
    questionLabels = []
    selectedAnswerLabels = []
    for item in data:
        if item['Component'] == question:
            questionLabels = item['Labels']
        if item['Component'] == selectedAnswer:
            selectedAnswerLabels = item['Labels']
    qLabels = ""
    for i in range(len(questionLabels)):
        qLabels += questionLabels[i]
        if i != len(questionLabels) - 1:
            qLabels += ", "
    saLabels = ""
    for i in range(len(selectedAnswerLabels)):
        saLabels += selectedAnswerLabels[i]
        if i != len(selectedAnswerLabels) - 1:
            saLabels += ", "
    print("The labels relevant to '"+ question + "' are: " + qLabels)
    if len(selectedAnswerLabels):
        print("The labels relevant to '"+ selectedAnswer + "' are: " + saLabels)
    print()

file = open('Questionnaire.json')
jsonData = json.load(file)
questions = [["What is the type of application?", "Web Application", "Mobile Application", "Batch Processing", "ETL"], #0
             ["Do you have restful APIs in your application?", "Yes", "No"], #1
             ["Does your application support SSO?", "Yes", "No"], #2
             ["Does your application require any SQL database?", "Yes", "No"], #3
             ["What is the type of SQL database?", "Microsoft SQL Server", "MySQL", "Postgress", "SQLite"], #4
             ["Are you using any unstructured database?", "Yes", "No"], #5
             ["What kind of database are you using?", "JSON document", "NoSQL"], #6
             ["Are you doing load balancing for your application?", "Yes", "No"], #7
             ["Do you have any web application firewalls in place", "Yes", "No"], #8
             ["Are your endpoints accessible via HTTPS only?", "Yes", "No"], #9
             ["Where the application is hosted on?", "On-Prem Private Data Center", "Public Cloud Provider", "Shared Hosting"], #10
             ["What cloud provider you are using?", "AWS", "Azure", "GCP", "Other"], #11
             ["What is the architecture of the mobile application?", "Monolithic", "Microservices"], #12
             ["Are you using any Container Orchestration tools?", "Yes", "No"], #13
             ["Which Container Orchestration tool you are using?", "Kubernetes", "EKS", "ECS", "GKE", "AKS"], #14
             ["Does your application send an outbound email?", "Yes", "No"], #15
             ["Are you using a self-hosted SMTP Server?", "Yes", "No"], #16
             ["Does your application use any queue to de-couple components?", "Yes", "No"], #17
             ["Which queue are you using", "RabbitMQ", "AWS SQS", "Apache ActiveMQ"], #18
             ["Is your application accessible from the public internet?", "Yes", "No"], #19
             ["Is your application & database server deployed in a public subnet?", "Yes", "No"], #20
             ["Is your application & database server deployed in the same subnet?", "Yes", "No"] #21
             ]
i = 0
while i < len(questions):
    question = questions[i]
    print(question[0])
    print("Options:")
    for j in range(1, len(question)):
        print(str(j) + ". " + question[j])
    answer = int(input())
    getLabels(question[0], question[answer], jsonData)
    if i == 3 and answer == 2:
        i += 1
    elif i == 4:
        i += 2
    elif i == 5 and answer == 2:
        i += 1
    elif i == 10 and (answer == 1 or answer ==3):
        i += 1
    elif i == 12 and answer == 1:
        i += 1
    elif i == 13 and answer == 2:
        i += 1
    elif i == 15 and answer == 2:
        i += 1
    elif i == 17 and answer == 2:
        i += 1
    i += 1