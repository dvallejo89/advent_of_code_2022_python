
file='input_advent_code1.input'
with open(file) as f:
    elf_cals = [line.rstrip('\n') for line in f]
num=0
list_sum_cals=[]
for cals in elf_cals:
    if cals != '':
        num+=int(cals)
    if cals == '':
        list_sum_cals.append(num)
        num=0
list_sum_cals
list_sum_cals.sort()
print(f"Dia1 - El elfo que tiene mas calorias lleva {list_sum_cals[-1]} cal")
print(f"Dia2 - Los tres elfos que tiene mas calorias llevan {sum(list_sum_cals[-3:])} cal")


