def char_count(stri):
    man_str=stri.replace(" ","")
    list_of_chars=[]
    list_of_inst=[]
    answer=[]
    man_str=[*man_str]
    for ltr in man_str:
        if ltr in list_of_chars:
            pass
        else:
            list_of_chars.append(ltr)
            list_of_inst.append(man_str.count(ltr))
    list_of_chars=sorted(list_of_chars)
    list_of_inst=sorted(list_of_inst, reverse=True)
    for inst in range(len(list_of_inst)):
        for ltr in range(len(list_of_chars)):
            if man_str.count(list_of_chars[ltr])==list_of_inst[inst] and list_of_chars[ltr] !=" ":
                answer.append([list_of_chars[ltr], list_of_inst[inst]])
                list_of_chars[ltr] =" "
                list_of_inst[inst] = 0
    return answer