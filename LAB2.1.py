
def newtask(task_list):
    string=input()
    task_list.append(string)

def remove_task(task_list):
    string=input("Type task you want remove!")
    if string in task_list:
        task_list.remove(string)
    else:
        print("Task is not in your list! ")

def printsorted_task(task_list):
    print(sorted(task_list))


if __name__ == '__main__':

    given_list = []
    ended=False

    while not ended:

        print("Insert the number corresponding to the action you want to perform")
        print("1: insert a new task")
        print("2: remove a task (by typing all its content)")
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

        elif (choice == 4):
            flag = True

        else:
            print("Insert a number between 1 and 4")
