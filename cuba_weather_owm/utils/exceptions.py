class BadRequestException(Exception):
  def __init__(self, message: str):
    self.message = message

class InvalidSourceException(Exception):
  def __init__(self, message: str):
    self.message = message

class ParseException(Exception):
  def __init__(self, message: str):
    self.message = message
