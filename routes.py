from fastapi import APIRouter
from LLMs import Classifier
from fastapi.exceptions import HTTPException
from RSSFeedHandler import RSS
RSSHandler = RSS.RSSFeed()
router = APIRouter()
from RSSFeedHandler import Order
St = Order.Storage()
ll = Classifier.Classifier(1)


@router.get("/orders/{start}/item/{end}")
async  def get_orders_test(start:int,end:int):
    data = RSSHandler.get_no_of_orders(start,end)
    return {"Res":data,
            "type":str(type(data)),
            "total_length":RSSHandler.get_len()}

@router.get("/jsontest")
async def get_json():
    data = RSSHandler.get_orders()
    res = ll.pass_to_LLM(data)
    return {"Result":res}

@router.get("/orders/{start}/{stop}")
async def get_order(start:int,stop:int):
    if start<0 or start>RSSHandler.get_len():
        raise HTTPException(status_code=404,detail="Out of Bounds Error")
    if stop<0 or stop>RSSHandler.get_len():
        raise HTTPException(status_code=404,detail="Out of Bounds Error")
    try:

