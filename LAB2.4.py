
task1 = {"todo": "call John for AmI project organization", "urgent": True}
task2 = {"todo": "buy a new mouse", "urgent": True}
task3 = {"todo": "find a present for Angelina’s birthday", "urgent": False}
task4 = {"todo": "organize mega party (last week of April)", "urgent": False}
task5 = {"todo": "book summer holidays", "urgent": False}
task6 = {"todo": "whatsapp Mary for a coffee", "urgent": False}

newtask=[]
i=0
tasks=[task1,task2,task3,task4,task5,task6]
for search in tasks:
    if search["urgent"]==True:
        newtask.append(search)
        print ("Task {} = {}".format(i+1,newtask[i]))
        i+=1
