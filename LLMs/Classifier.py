from langchain_openai import ChatOpenAI
class Classifier:
    temp = 1
    llm = ChatOpenAI(model="",temperature=temp)
    def __init__(self,temp=1):
        self.temp = temp
        res = self.llm.invoke("This is a Test of LLM please respond with Hi this LLM is ready")
        print(res)
    def pass_to_LLM(self,lst):
