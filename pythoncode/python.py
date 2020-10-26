#Pythoncomment: python code , using pathon 3
#read all before

pizza = open("pizzalist.txt", "a") 
print("where bought:") 
wjerebought= input() 
print("pizza price") 
price= input() 
if int(str(price)) < 1500:
    print("alert00")
pizza.write("\n"+""+ " "+wjerebought+'" "'+price); 
pizza.close()
