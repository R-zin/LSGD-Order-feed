from fastapi import APIRouter
from LLMs import Classifier
from RSSFeedHandler import RSS
RSSHandler = RSS.RSSFeed()
router = APIRouter()
from RSSFeedHandler import Order
St = Order.Storage()



@router.get("/orders")
async  def get_orders():
    return {"Res": RSSHandler.get_orders()}
