import json
file = open("dictionary.txt", "r")
cont = file.read()
dicti = json.loads(cont)
file.close()
freq={}
def get_all_keys(dictio):
    for k, value in dictio.items():
        if type(value) is dict:
            get_all_keys(value)
            if (k in freq):
                freq[k] += 1
            else:
                freq[k]=1
        elif (k in freq):
            freq[k] += 1
        else:
            freq[k]=1
        if type(value) is list:
            for i in range(len(value)):
                if type(value[i]) is dict:
                    get_all_keys(value[i])
get_all_keys(dicti)
keyWithMaxValue = max(freq.items(), key=lambda x: x[1])
listOfKeysWithMaxFreq = list()
for key, value in freq.items():
    if value == keyWithMaxValue[1]:
        listOfKeysWithMaxFreq.append(key)
print(listOfKeysWithMaxFreq)
