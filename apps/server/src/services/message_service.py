class MessageService:
  def __init__(self, session):
    self.session = session

  async def create_message(self, thread_id, data):
    ...

  async def list_messages(self, thread_id):
    ...