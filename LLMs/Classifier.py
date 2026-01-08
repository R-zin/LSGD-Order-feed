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
        pass
smth = Classifier(1)
print(smth.test())

