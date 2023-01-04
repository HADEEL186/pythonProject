with open("originalfile.txt", "w+")as file:
    file.write("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'\n")
    file.write("J.U.U.U Kmltin.\n")
    file.write("mmps iks nmk eio; ---> hkmu\n")
    file.seek(0)
    readtxt = file.read()



def countappear(a):
    dict1 = {}
    for char in a:
        if char.isalpha():
            char = char.lower()
            if char in dict1:
                dict1[char] +=1
            else:
                dict1[char] = 1
    return dict1
print(countappear(readtxt))
dict1 = dict(sorted(countappear(readtxt).items(), key= lambda x:x[1], reverse=True)[:4])
print(dict1)
solution_list = ['e','t','o','r']
dict_Keys = list(dict1.keys())
print(dict_Keys)
res_dict = {}
for key, value in zip(solution_list,dict_Keys):
    res_dict[key] = value
    res_dict[value] = key
print("Resultant dictionary is : " + str(res_dict))






