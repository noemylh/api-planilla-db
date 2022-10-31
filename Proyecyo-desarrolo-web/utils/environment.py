from json import load

environment = {"Key": "value"}

def load_environment(file_name):
  with open(file_name) as f:
    global environment
    environment = load(f)

def get_environment(key):
  return environment.get(key, None)