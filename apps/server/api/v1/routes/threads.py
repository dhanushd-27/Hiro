from fastapi import APIRouter

router = APIRouter(prefix="/thread")

@router.get("/:id")
def getThread(id):
  return f"Thread with { id } is fetched"

@router.post("/")
def createThread():
  return f"Thread id is 12"

@router.delete("/:id")
def deleteThread(id):
  return f"Thread with { id } has been deleted"