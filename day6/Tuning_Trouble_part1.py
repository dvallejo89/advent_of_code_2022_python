import tuning_trouble_input
input_str=tuning_trouble_input.input_str

for count,letter in enumerate(input_str):
    if input_str[count] in (input_str[count+1:count+4]):
        #pass
        print(f'{input_str[count]} in {input_str[count+1:count+4]}')
        list_check=[1]
    else:
        list_check=[0]
    if input_str[count+1] == input_str[count] or input_str[count+1] in input_str[count+2:count+4]:
        print(f'{input_str[count+1]} == {input_str[count]} or in {input_str[count+2:count+4]}')
        list_check.append(1)
    else:
        list_check.append(0)
    if input_str[count+2] in input_str[count:count+1] or input_str[count+2] in input_str[count+3:count+4]:
        print(f'{input_str[count+1]} in {input_str[count:count+1]} or in {input_str[count+3:count+4]}')
        list_check.append(1)
    else:
        list_check.append(0)
    if input_str[count+3] == input_str[count+4] or input_str[count+3] in input_str[count:count+2]:
        print(f'{input_str[count+4]} == {input_str[count]} or in {input_str[count:count+2]}')
        list_check.append(1)
    else:
        list_check.append(1)
    
    print(list_check)
    break