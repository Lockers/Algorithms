#!/usr/bin/python

import math
import time

def recipe_batches(recipe, ingredients):
      batches = 0
      lista = []
      if len(recipe) > len(ingredients):
            return batches
      for i in recipe:
          lista.append(int(ingredients[i] / recipe[i]))
      return min(lista)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 52, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
