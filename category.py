import os
from langchain.schema import HumanMessage
from langchain.chat_models import ChatOpenAI
import ast
def promptmaker(statement):
    instructions = f"""You are doctor's assistant.your duty is to create a list with following data in the order:
        1. what are health issues faced by the patient now seperated by '*' symbol.
        2. what all health issues and main health events did patient face earlier and when seperated by hyphen and each health issue seperated by comma,
                for instance: heart surgery-2010,tyroid-2005 etc
        3. what all medicines is patient already taking seperated by '*' symbol.
        4. what all new medicines should he take and when to take,for how long seperated by '*' symbol.
                for instance: dolo-morning and evening- 5 days * paracetamol-whenever fever-3 days
                dont include instructions in this
        5. what all things to take care.for instance:drink water,eat less salty food,go for trip etc seperated by '*' symbol.
        6. what is initial conlusion of the symptoms seperated by '*' symbol.
    if any of the details is not present leave it as null 
    return a list.
    example of expected output:[fever,brain surgery-2009,vikz*albumin,dolo-morning-5 days,drink water*eat food]
    return only list no other sentences.
    """
    question=f"returm only list of words in {statement} aligned  in the order mentioned above.only return th list no other sentence"

    prompt = instructions+question

    return askgpt(prompt)

def askgpt(prompt):
    # print("etti")
    openai_api_key =os.environ.get('OPENAI_API_KEY')
    chat_model = ChatOpenAI(temperature=0, model='gpt-4', openai_api_key=openai_api_key,max_tokens=350)
    
    output = chat_model([HumanMessage(content=prompt)])
    response = output.content
    # print(response)
    
    # print("******************",dat)
    # print("***********",dat[1])
    try:
        extracted_list = response.split('[')[-1].strip()
        # print("elist-----",extracted_list)
        extracted_list = '[' +extracted_list
    
        # print("elist-----",extracted_list)
    except ValueError:
        print("Invalid input string")
    
    


    dat=ast.literal_eval(extracted_list)
    # print("********************", dat)
    # print(dat[0])
    # The rest of your code...

    now=dat[0]
    list_now = now.split('*')
    # print("list_now is",list_now)

    past=dat[1]
    if '*' in past:
        list_past=past.split('*')
    else:
        list_past=past
    # print("list_past is",list_past)

    past_med=dat[2]
    if '*' in past_med:
        list_med=past_med.split('*')
    else:
        list_med=past_med
    # print("list_med is",list_med)

    now_med=dat[3]
    if '*' in now_med:
        list_now_med=now_med.split('*')
    else:
        list_now_med=now_med
    # print("now med is",list_now_med)

    precaution=dat[4]
    if '*' in precaution:
        list_pre=precaution.split('*')
    else:
        list_pre=precaution
    # print("list_instruct ",list_pre)

    finding=dat[5]
    # print("-------------------------------",finding)
    if '*' in finding:
        list_find=finding.split('*')
    else:
        list_find=finding
    print(list_find)


    result_dict = {
        'now': list_now,
        'past': list_past,
        'past_medicine': list_med,
        'now_medicine': list_now_med,
        'instructions': list_pre,
        'finding': list_find
    }
    # print(result_dict)
    return(result_dict)






