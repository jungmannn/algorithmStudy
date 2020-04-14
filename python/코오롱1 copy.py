# a = '09:10'
# b = '10:11'
# a = a.split(':')
# print(a)

# time = int(a[0]) * 60 + int(a[1])



# print(time)

booked = [['09:10', "lee"]]
unbooked = [['09:00', "kim"], ["09:05", "bae"]]

def soulution(booked, unbooked):
    answer = list()
    dict_booked = dict()
    for n in booked:
        hhmm = n[0].split(':')
        time = int(hhmm[0]) * 60 + int(hhmm[1])
        dict_booked[time] = [n[1], 'booked']
    
    for i in unbooked:
        hhmm = i[0].split(':')
        time = int(hhmm[0]) * 60 + int(hhmm[1])
        dict_booked[time] = [i[1], 'unbooked']

    list_b = dict_booked.items()
    sorted_list_b = sorted(list_b, key=lambda x: x[0])
    print(sorted_list_b)
    

    for k in range(0, len(sorted_list_b)):
        print(sorted_list_b[k])
        for i in range(1, 11):
           if sorted_list_b[sorted_list_b[k][0]+i]:
               print(존재)
            
            
        
    return answer

soulution(booked, unbooked)