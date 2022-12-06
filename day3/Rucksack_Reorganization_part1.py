file='reorganizacion_mochilas.input'
with open(file) as f:
    elf_bags = [line.rstrip('\n') for line in f]

#ord('a')-96 ##convert priority of letters

repeated_element=[]
repeated_element_list=[]
for count,bag in enumerate(elf_bags):
    for element in bag[:int(len(bag)/2)]:
        #print(f"{element} in {bag[int(len(bag)/2):]}")
        if element in bag[int(len(bag)/2):]:
                #repeated_element.append(element)
            if ord(element) in range(ord('a'), ord('z')+1):
                repeated_element.append(int(ord(element)-96))
            if ord(element) in range(ord('A'), ord('Z')+1):
                repeated_element.append(int(ord(element)-38))
    repeated_element=list(dict.fromkeys(repeated_element))
    for item in repeated_element:
        repeated_element_list.append(item)
    #print(f"{count} - {len(repeated_element)}")
    repeated_element=[]

print(sum(repeated_element_list))