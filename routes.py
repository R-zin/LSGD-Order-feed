from fastapi import APIRouter
from LLMs import Classifier
router = APIRouter()

LLM = Classifier



@router.get("/orders")
async  def get_orders():
    pass