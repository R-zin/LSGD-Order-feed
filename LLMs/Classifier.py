from langchain_openai import ChatOpenAI

import os
from dotenv import load_dotenv
load_dotenv()
api_cred=os.getenv("OPENAI_API_KEY")
baseurl = os.getenv("OPENAI_BASE_URL")
class Classifier:
    temp = 1
    llm = ChatOpenAI(model="x-ai/grok-4-fast",api_key=api_cred,base_url=baseurl,temperature=temp)
    def __init__(self,temp):
        self.temp = temp
    def test(self):
        res = self.llm.invoke("This is a Test of LLM please respond with Hi this LLM is ready")
        json_res = res.text()
        if json_res == "Hi this LLM is ready":
            return True
        else:
            return False
    def pass_to_LLM(self,lst):
        res = []
        for i in lst:
            message = [
                {"role": "system",
                 "content": "You are Summarizer and classifier of these Orders from LSGD website.Return in json fromat with keys title,summary,link to document,date,and a class in [Resource managment,transfer order,promotion order]"},
                {"role": "user", "content": i}]
            resp = self.llm.invoke(message)
            res.append(resp)
        print(res)
        return resp



