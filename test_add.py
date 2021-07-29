import pytest

def add_test():
  from firsttest import add_two
  
  assert add_two(5, 12) == 17
  assert add_two(8, 12) == 17