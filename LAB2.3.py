from sys import argv

def newtask(task_list):
    string=input()
    task_list.append(string)

def remove_task(task_list):
    string=input("Type task you want to remove!")
    if string in task_list:
        task_list.remove(string)
    else:
        print("Task is not in your list! ")


def remove_substring_in_task(task_list):

    remove_list=[]
    substring = input("Inset task you want remove")

    for single_task in task_list:
        if (substring in single_task):
            remove_list.append(single_task)

    if (len(remove_list)>0):
        for task_to_remove in remove_list:
            if(task_to_remove in task_list):
                task_list.remove(task_to_remove)


def printsorted_task(task_list):
    print(sorted(task_list))


if __name__ == '__main__':

    given_list = []
    ended=False

    filename=argv[1]
    txt=open(filename)
    given_list=txt.read().splitlines()

    txt.close()



    while not ended:

        print("Insert the number corresponding to the action you want to perform")
        print("1: insert a new task")
        print("2: remove a task (by typing all its content)")
        print("5: remove all the existing tasks that contain a provided string")
        print("3: show all existing tasks sorted in alphabetic order")
        print("4: close the program")


        print("Insert a command:")
        string = input()

        while string.isdigit()!= True:
            string=input("Wrong input! Try again")

        choice=int(string)

        if (choice == 1):
            newtask(given_list)

        elif (choice == 2):
            remove_task(given_list)

        elif (choice == 3):
            printsorted_task(given_list)

        elif (choice==5):
            remove_substring_in_task(given_list)

        elif (choice == 4):
            flag = True

        else:
            print("Insert a number between 1 and 4")

    if ended:
        txt=open(filename,"w")

        for task in given_list:
            txt.write(task + "\n")

        txt.close()

