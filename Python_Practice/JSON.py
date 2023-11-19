#import the json module
#json values are stored as key value pairs, which can be converted to items in dictionaries in py
#use json.loads(json_obj_name) to load a json object as a py dict
#use json.dumps(py_obj_name) to dump a py pbject as a json
import json

#Write a Python program to convert JSON data to Python object.
def json_to_py(json_obj):
    py_obj = json.loads(json_obj)
    print(py_obj)
    print("\nName: ", py_obj["Name"])
#json_to_py("{ \"Name\":\"Ash\", \"Age\":\"21\"}")
#--------------------------------------------------------------------------------------------------------------------------------
#Write a Python program to convert Python object to JSON data.
def py_to_json(py_obj):
    json_obj = json.dumps(py_obj)
    print(json_obj)
#py_to_json({"Name":"Ash", "Age":21})
#--------------------------------------------------------------------------------------------------------------------------------
#Write a Python program to create a new JSON file from an existing JSON file.
#with open('states.json') as f:
  #state_data= json.load(f)

#for state in state_data['states']:
  #del state['area_codes']

#with open('new_states.json', 'w') as f:
  #json.dump(state_data, f, indent=2)
#--------------------------------------------------------------------------------------------------------------------------------
