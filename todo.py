
import sys , os

import datetime

curr_dt = datetime.datetime.now()


def help_func():
         
    help_val1 = "Usage :-"
    help_val2 = """$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics"""
    print(help_val1)
    print(help_val2)
    # print(help_val2)

def add_new_item( item):
    file1 = open("todo.txt","a") 
    file1.write(f"{item}\n") 
    file1.close()
    print(f'Added todo: "{item}"')
    return


def show_all_todos():

    # reading the txt file 
    file1 = open("todo.txt","r")

    all_todos = list(file1.readlines() )
    if(len(all_todos)== 0):
        print("There are no pending todos!")
        return

    all_todos =  all_todos[::-1] 
    # reversing the array
    counter_decrement= len(all_todos)

    show_in_console = ""
    for i in range(len(all_todos)):
                
        show_in_console += f"[{counter_decrement}] {all_todos[i]}"
        counter_decrement -=1
    
    # removing the last \n
    show_in_console = show_in_console[:-1]

    print(show_in_console)
    return


def del_todo( item ):

    try:
        file_original = open('todo.txt' , "r")
        
    except:
        print(f"Error: todo #{item} does not exist. Nothing deleted.")
        return

    all_todos = list(file_original.readlines() )

    # checkpoint
    if(int(item) == 0 or int(item) > len(all_todos)):
        print(f"Error: todo #{item} does not exist. Nothing deleted.")
        return

    all_todos.remove(all_todos[int(item) - 1])
    

    file_original = open('todo.txt' , "a")
    file_original.seek(0)  
    # to erase all data  
    file_original.truncate()  

    for i in all_todos:
        file_original.write(i)
    print(f"Deleted todo #{item}")
    
    return


def done_todo(item):

    try:
        item = int(item)
    except:
        print("Error")
        return

    try:
        file_original = open('todo.txt' , "r")
    except:
        return
    
    all_todos = list(file_original.readlines() )

    # checkpoint
    if(int(item) == 0 or int(item) > len(all_todos)):
        print(f"Error: todo #{item} does not exist.")
        return
    
    to_move_data = all_todos[int(item) - 1]
    all_todos.remove(to_move_data)

    # reopening the file to write
    file_original = open('todo.txt' , "a")
    file_original.seek(0)  
    # to erase all data  
    file_original.truncate()  

    for i in all_todos:
        file_original.write(i)
    
    file_new = open('done.txt' , "a")
    file_new.write("x" + " " + str(curr_dt.year) + "-" +  str(curr_dt.month) + "-" +  str(curr_dt.day) + " " + to_move_data)
    
    file_new.close()
    file_original.close()
    print(f"Marked todo #{item} as done.")


    return


def generate_report():

    try:
        f_todo = open('todo.txt' , "r")
        counter_todos = list(f_todo.readlines() )
    except:
        return

    try:
        f_done = open('done.txt' , "r")
        counter_done = list(f_done.readlines())
        
    except:
        counter_done = []
        
    print( f"{curr_dt.year}-{curr_dt.month}-{curr_dt.day}  Pending : {len(counter_todos)}  Completed : {len(counter_done)}")

    return




if __name__ == '__main__':

    temp1 = open('todo.txt' , 'a')
    temp1.close()
    temp2  = open('done.txt' , "a")
    temp2.close()

    if( len(sys.argv) == 1):
        help_func()

    elif (sys.argv[1] == "help" and len(sys.argv) == 2):
        help_func()
    
    elif (sys.argv[1] == "add" and len(sys.argv) == 2 ):
        print("Error: Missing todo string. Nothing added!")
    
    elif (sys.argv[1] == "add" and len(sys.argv) == 3 and type(sys.argv[2])  == str ):
        add_new_item(sys.argv[2])
    
    elif(sys.argv[1] == "ls" and len(sys.argv) == 2):
        show_all_todos()

    elif(sys.argv[1] == "del" and len(sys.argv)== 2):
        print("Error: Missing NUMBER for deleting todo.")

    elif(sys.argv[1] == "del" and len(sys.argv) == 3  ):

        if(type(sys.argv[2]) != int):
            print("Error: Missing NUMBER for deleting todo.")
            
        else:
            del_todo(sys.argv[2])

    elif(sys.argv[1] == "done" and len(sys.argv)== 2):
        print("Error: Missing NUMBER for marking todo as done.")

    elif(sys.argv[1] == "done" and len(sys.argv) == 3 ):
                
        if(type(sys.argv[2]) != int):
            print("Error: Missing NUMBER for marking todo as done.")
        else:
            done_todo(sys.argv[2])
    
    elif(sys.argv[1] == "report" and len(sys.argv) == 2 ):
        generate_report()

    else:
        print("Error")
