import pickle as pickle

filename = 'erase.pkl'

pickle_file = open(filename, "rb")
objects = []
while True:
   try:
      objects.append(pickle.load(pickle_file))
   except EOFError:
      break

pickle_file.close()

angles = objects[0]

print(angles)