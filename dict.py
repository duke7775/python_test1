
dict_a = {1 : "1","1" : 1,"3":"hello","hello":True,1.233:"firth"}

print(dict_a)
len(dict_a)
print(len(dict_a)) 

for site in dict_a:
    print(site)    
if  1000 in dict_a:  
    print(True)
else :
    print(False)

del dict_a["1"]
print(dict_a)

dict_a["1"]=[1,2,3,4,5]
print(dict_a)

dict_a["1"]=[1,2,3,4,5]
print(dict_a)

del dict_a
print(dict_a)