class ThreadService:
  def __init__(self, session):
    self.session = session

  async def create_thread(self, data):
    ...
  
  async def list_threads(self):
    ...

  async def get_thread(self, thread_id):
    ...

  async def update_thread(self, thread_id, data):
    ...

  async def delete_thread(self, thread_id):
    ...