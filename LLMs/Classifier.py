import json

from fastapi import HTTPException

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
        self.test()
    def test(self):
        res = self.llm.invoke("This is a Test of LLM please respond with Hi this LLM is ready")
        json_res = res.text()
        if json_res == "Hi this LLM is ready":
            print("LLM Test Successful")
            return True
        else:
            return False
    def LLM_Comp_tester(self):
        lst = [
    {
      "title": "G.O.(Rt) 3007/2025/LSGD Dated 19/12/2025",
      "link": "https://go.lsgkerala.gov.in/pages/fileOpen.php?fname=go20251219_40314.pdf& id=40314",
      "Summary": "Management of the waste generated as a result\nof natural and man made disasters - Disaster Waste management Protocol -Approved - orders issued .",
      "Date": "19/12/2025"
    },
    {
      "title": "സ.ഉ(ആര്‍.ടി) 2994/2025/LSGD Dated 19/12/2025",
      "link": "https://go.lsgkerala.gov.in/pages/fileOpen.php?fname=go20251219_40313.pdf& id=40313",
      "Summary": "മാലിന്യമുക്തം നവകേരളം ക്യാമ്പെയിൻ-കൊല്ലം-സംബന്ധിച്ച ഉത്തരവ്",
      "Date": "19/12/2025"
    },
    {
      "title": "G.O.(Rt) 3005/2025/LSGD Dated 19/12/2025",
      "link": "https://go.lsgkerala.gov.in/pages/fileOpen.php?fname=go20251219_40312.pdf& id=40312",
      "Summary": "Local Self Government Department – Mid Term Review Meeting to assess the implementation\nof Mahatma Gandhi NREGS in the State and to assess the eligibility for the release of 2nd tranche of funds for the FY 2025-26 on 24.09.2025 (for Kerala) at New Delhi- Ex post facto Sanction accorded - Orders issued.",
      "Date": "19/12/2025"
    }]
        res =[]
        for i in lst:
            message = [
                {"role": "system",
                 "content": "You are Summarizer and classifier of these Orders from LSGD website.Return in json fromat with keys title,summary,link to document,date,and a class in [Resource managment,transfer order,promotion order]"},
                {"role": "user", "content": json.dumps(i,ensure_ascii=False)}]
            resp = self.llm.invoke(message)
            res.append(resp.text())
        print(res)

    def pass_to_LLM(self,lst):
        res = []
        print(type(lst))
        try:
            for i in lst:
                message = [
                    {"role": "system",
                     "content": "You are Summarizer and classifier of these Orders from LSGD website and ensure title is translated to english.Return in json format with keys title,summary,link to document,date,and a class in [Resource managment,transfer order,promotion order,others]"},
                    {"role": "user", "content": json.dumps(i,ensure_ascii=False)}]
                resp = self.llm.invoke(message)
                res.append(resp.text())
            fin_res = [json.loads(s) for s in res]
            return fin_res
        except Exception as e:
            raise HTTPException(status_code=404,detail="Internal Error")



