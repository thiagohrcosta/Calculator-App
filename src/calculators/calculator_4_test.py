from typing import Dict, List
from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from.calculator_4 import Calculator4
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandler():
  def variance(self, numbers: List[float]) -> float:
    return 100000
  
def test_calculate_with_invalid_body():
  mock_request = MockRequest({}) 
  calculator_4 = Calculator4(MockDriverHandler())

  with raises(HttpUnprocessableEntityError) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value) == 'body not formatted'

def test_calculate_with_valid_data():
  mock_request = MockRequest({'numbers': [1, 2, 3, 4, 5]})
  calculator_4 = Calculator4(MockDriverHandler())

  response = calculator_4.calculate(mock_request)

  assert response == {
    'data': {
      'Calculator': 4, 
      'mean': 3.0,
      'success': True
    }
  }

def test_calculate_with_invalid_result_type():
  mock_request = MockRequest({'numbers': [1, 2, 3, 'invalid']})
  calculator_4 = Calculator4(MockDriverHandler())

  with raises(ValueError) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value) == 'The result must be a number (int ou float).'

def test_calculate_with_empty_numbers():
  mock_request = MockRequest({'numbers': []})
  calculator_4 = Calculator4(MockDriverHandler())

  with raises(ZeroDivisionError) as excinfo:
    calculator_4.calculate(mock_request)

  assert str(excinfo.value) == 'division by zero'
