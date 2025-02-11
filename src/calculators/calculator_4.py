from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError

class Calculator4: 
  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler

  def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
    body = request.json

    input_data = self.__validate_body(body)

    mean = self.__calculate_mean(input_data)

    self.__verify_results(mean)

    formatted_response = self.__format_response(mean)

    return formatted_response
    
  def __validate_body(self, body: Dict) -> List[float]:
    if 'numbers' not in body:
      raise HttpUnprocessableEntityError('body not formatted')
    
    input_data = body['numbers']
    return input_data
    
  def __calculate_mean(self, numbers: List[float]) -> float:
    if not all(isinstance(num, (int, float)) for num in numbers):
      raise ValueError("The result must be a number (int ou float).")
    
    total_sum = sum(numbers)
    mean = total_sum / len(numbers)
    return mean
  
  def __verify_results(self, num: int) -> None:
    if not isinstance(num, (int, float)):
      raise ValueError('The result must be a number (int ou float).')
    
  def __format_response(self, mean: float) -> Dict:
    rounded_mean = round(mean, 2)
    return {
      'data': {
        'Calculator': 4, 
        'mean': rounded_mean,
        'success': True
      }
    }