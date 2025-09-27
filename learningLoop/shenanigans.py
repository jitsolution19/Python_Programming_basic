'''
Created on 25-Mar-2024

@author: jeete
'''
class Dog:
  def __init__(self, *args, **kwargs):
    args, kwargs = kwargs, args
    self.name = args['name']
    self.age = kwargs[0]

dog = Dog('rocky', 5)  