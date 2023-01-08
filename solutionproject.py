# def writefile(filename):
#     with open(filename, "w+")as file:
#         file.write("'Puackich, hvhnkrally oaths phufhck. All ymr nhhd is Pykemn.'\n")
#         file.write("J.U.U.U Kmltin.\n")
#         file.write("mmps iks nmk eio; ---> hkmu\n")
#         file.seek(0)
#         return file.read()
# readtxt = writefile("originalfile.txt")



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

def creatdict(readtxt):
    dict1 = dict(sorted(countappear(readtxt).items(), key= lambda x:x[1], reverse=True)[:4])
    print(dict1)
    solution_list = ['e','t','o','r']
    dict_Keys = list(dict1.keys())
    print(dict_Keys)
    res_dict = {}
    for key, value in zip(solution_list,dict_Keys):
        res_dict[key] = value
        res_dict[key.upper()] = value.upper()
        res_dict[value] = key
        res_dict[value.upper()] = key.upper()
    print("Resultant dictionary is : " + str(res_dict))
    return res_dict
def switchar(res_dict,readtxt):
    transletedtxt=""
    for char in readtxt:
        if char in res_dict:
            char = res_dict[char]
        transletedtxt += char

    print(transletedtxt)
    return transletedtxt

def decrypt(filename):
    with open(filename,"r+") as file:
        readtxt = file.read()
        d = creatdict(readtxt)
        transletestxt = switchar(d, readtxt)
        file.write("The encryption for the above text is:\n")
        file.write(transletestxt)
    with open( "results.txt","w") as file:
        file.write(transletestxt)
    file.close()

decrypt("originalfile.txt")










