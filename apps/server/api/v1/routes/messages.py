from fastapi import APIRouter

router = APIRouter()

@router.post("/message")
def message(message):
  return "message sent"