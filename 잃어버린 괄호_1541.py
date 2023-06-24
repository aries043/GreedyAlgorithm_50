question = input()
store = 0
signs = []
nums = []

for i in question:
    try:
        ques = int(i)
        if store != 0 or ques != 0:
            store = store*10 + ques
    except:
        signs.append(i)
        nums.append(store)
        store = 0
nums.append(store)

order = []
for nth, sign in enumerate(signs):
    if sign == '-':
        order.append(nth)
        
    if sign == '+':
        order.insert(0, nth)

while(len(order)):
    noword = order[0]
    if noword == len(signs)-1:
        del order[0]
    else:
        del order[0]
        for nth, ord in enumerate(order):
            if ord > noword:
                order[nth] -= 1
        
    nowsign = signs[noword]
    del signs[noword]
    
    if nowsign == '+':
        tmp = nums[noword] + nums[noword + 1]
        del nums[noword]
        del nums[noword]
        nums.insert(noword, tmp)
        
    else:
        tmp = nums[noword] - nums[noword + 1]
        del nums[noword]
        del nums[noword]
        nums.insert(noword, tmp)
    
print(nums[0])