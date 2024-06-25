from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
  def calculate(self, request: FlaskRequest) -> Dict:
    body = request.json
    input_data = self.__validade_body(body)
    splited_number = input_data / 3

    first_process_result = self.__first_process(splited_number)

  def __validade_body(self, body: Dict) -> float:
    if 'number' not in body:
      raise Exception('body not formatted')
    
    input_data = body['number']
    return input_data
  
  def __first_process(self, first_number: float) -> float:
    first_part = (first_number / 4 ) + 7
    secont_part = (first_part ** 2) * 0.257
    return secont_part
        