file='supply_stacks_movements.input'
with open(file) as f:
    movements = [line.rstrip('\n') for line in f]

queue1='JHPMSFNV'
queue2='SRLMJDQ'
queue3='NQDHCSWB'
queue4='RSCL'
queue5='MVTPFB'
queue6='TRQNC'
queue7='GVR'
queue8='CZSPDLR'
queue9='DSJVGPBF'

list_of_queue=[queue1,queue2,queue3,queue4,queue5,queue6,queue7,queue8,queue9]

##rearrangement
for count,movement in enumerate(movements):
    qty=int(movement.split(' ')[1])
    list_from_pos=int(movement.split(' ')[3])-1
    list_to_pos=int(movement.split(' ')[5])-1
    if qty == 1:
        list_of_queue[list_to_pos]=list_of_queue[list_to_pos]+list_of_queue[list_from_pos][-1]
        list_of_queue[list_from_pos]=list_of_queue[list_from_pos][:-1]
    elif qty > 1:
        list_of_queue[list_to_pos]=list_of_queue[list_to_pos]+list_of_queue[list_from_pos][-qty:]
        list_of_queue[list_from_pos]=list_of_queue[list_from_pos][:-qty]

solution=''.join([stack[-1] for stack in list_of_queue])
print(solution)

