import pickle

print('hi')
dict1 = {'key': 'value'}
key = 'akfnuing'
value= 5
dict1[key]= value
encoded_dict1 = pickle.dumps(dict1).encode('base64', 'strict')
print(type(encoded_dict1))
print(encoded_dict1)
decoded_dict1 = pickle.loads(encoded_dict1.decode('base64', 'strict'))
print(decoded_dict1)
