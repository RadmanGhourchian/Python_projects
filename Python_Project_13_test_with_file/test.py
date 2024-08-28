# elif In_Out.get() == "Out" and len(list_tuple) < 1:
# list_tuple.clear()
# msg.showerror("error", "aaaa")

# elif (int(i[2]) < int(count.get())) and In_Out.get() == "Out":
# list_tuple.remove(i)
# msg.showerror("Error", "You don't you that much data")

# elif int(i[2]) > int(count.get()):
# i[2] = int(i[2]) - int(count.get())
# if i[2] == 0:
#     list_tuple.remove(i)
#     return None
import pickle

x = [1,2,3,4,5, [1,2,3]]

file = open("test.txt", "ab")
pickle.dump(x, file)
file.close()

file_2 = open("test.txt", "rb")
b = pickle.load(file_2)
file_2.close()
a = list(b)
print(a)

print(x[5][1])
