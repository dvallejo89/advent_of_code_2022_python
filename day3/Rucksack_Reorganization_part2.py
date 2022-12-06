file='reorganizacion_mochilas.input'
with open(file) as f:
    elf_bags = [line.rstrip('\n') for line in f]

#ord('a')-96 ##convert priority of letters

repeated_element=[]
repeated_element_list=[]

#creacion en sublistas de 3
elf_group_bags = [elf_bags[x:x+3] for x in range(0, len(elf_bags), 3)]

for count,group in enumerate(elf_group_bags):
    for element in group[0]:
        if element in group[1] and element in group[2]:
            #print(f"{count} - {element}")
            if ord(element) in range(ord('a'), ord('z')+1):
                repeated_element.append(int(ord(element)-96))
            if ord(element) in range(ord('A'), ord('Z')+1):
                repeated_element.append(int(ord(element)-38))
    #print(f"{count} - {repeated_element}")
    repeated_element_list.append(repeated_element[0])
    repeated_element=[]

print(sum(repeated_element_list))


            
            
