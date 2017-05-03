import pickle
pickle_file=open('my_list.pkl','rb')
my_list=pickle.load(pickle_file)
pickle_file.close()
print(my_list)
