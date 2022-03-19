import urllib.request
import json
import random

def get_char():

  url ='http://hp-api.herokuapp.com/api/characters'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())

  #print(result)
  char = random.randint(1,30)

  #print(result[char])
  
  return f"The character '{result[char]['name']}' in the Harry Potter movie series was played by {result[char]['actor']}, {result[char]['actor']} is a {result[char]['gender']} with {result[char]['eyeColour']} eyes, {result[char]['hairColour']} hair, and is of the house of {result[char]['house']}."
  

