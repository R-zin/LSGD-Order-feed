from fastapi import APIRouter
from LLMs import Classifier
from RSSFeedHandler import RSS
RSSHandler = RSS.RSSFeed()
router = APIRouter()
from RSSFeedHandler import Order
St = Order.Storage()
ll = Classifier.Classifier(1)


@router.get("/orders")
async  def get_orders():
    data = RSSHandler.get_orders()
    return {"Res":data,
            "type":str(type(data))}

@router.get("/jsontest")
async def get_json():
    data = RSSHandler.get_orders()
    res = ll.pass_to_LLM(data)
    return {"Result":res}