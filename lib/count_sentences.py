#!/usr/bin/env python3

class MyString:
  def __init__(self,value=""):
   self.value=value

  def value_string(self):
    if not isinstance(self.value,str):
      print("The value must be a string.")
    
  def is_sentence(self):
        return self.value.endswith(".")

  def is_question(self):
        return self.value.endswith("?")

  def is_exclamation(self):
        return self.value.endswith("!")
 
