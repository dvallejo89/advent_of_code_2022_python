import tuning_trouble_input
input_str=tuning_trouble_input.input_str

for count,item in enumerate(input_str):
    list_check=[]
    for letter in input_str[count:count+14]:
        if input_str[count:count+14].count(letter) == 1:
            list_check.append(0)
        else:
            list_check.append(1)
    if sum(list_check) == 0:
        print(f"solution is {count+14}")
        break


