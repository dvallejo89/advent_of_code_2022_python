file='camp_cleanup.input'
with open(file) as f:
    elf_sections = [line.rstrip('\n') for line in f]

count_list=[]
count_superpouse=0
for section in elf_sections:
    superpouse_list=[]
    for item in range(int(section.split(',')[0].split('-')[0]),int(section.split(',')[0].split('-')[1])+1):
        if item in range(int(section.split(',')[1].split('-')[0]),int(section.split(',')[1].split('-')[1])+1):
            count=1
            superpouse_list.append(count)
            #print(f"{item} in {int(section.split(',')[1].split('-')[0])} - {int(section.split(',')[1].split('-')[1])+1}")
            #print('step1')
        else:
            count=0
            superpouse_list.append(count) 
    if count == 0:
        for item in range(int(section.split(',')[1].split('-')[0]),int(section.split(',')[1].split('-')[1])+1):
            if item in range(int(section.split(',')[0].split('-')[0]),int(section.split(',')[0].split('-')[1])+1):
                count=1
                superpouse_list.append(count) 
                #print(f"{item} in {int(section.split(',')[1].split('-')[0])} - {int(section.split(',')[1].split('-')[1])+1}")
                #print('step2')
            else:
                count=0
                superpouse_list.append(count)
    #print(sum(superpouse_list))
    if sum(superpouse_list) > 0:
        count_superpouse+=1

print(count_superpouse) 




