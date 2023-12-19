# Initial gradebook list for Computer Science class
gradebook = [100, "Variables Test", 75, "Variables HW"]
# function to print grades
def print_grades():
    print("Current Gradebook: " + str(gradebook))
# Function to amend the gradebook
def amend_gradebook(operation, grade_input, assignment_input):
    if(operation == "add"):
        gradebook.append(assignment_input)
        gradebook.append(int(grade_input))
    elif(operation == "remove"):
        if(assignment_input in gradebook and int(grade_input) in gradebook):
            gradebook.remove(assignment_input)
            gradebook.remove(int(grade_input))
        else:
            print("Assignment or Grade not found in the gradebook")
    else:
        print_grades()
# Main function
def main():
    print("Welcome to my CS gradebook. ")
    while True:
        user_input = input("What would you like to do? [Add] or [Remove] grade or [Print] or type [exit] to exit: ").lower()
        if(user_input == "add"):
            assignment_input = input("please enter the assignment name: ")
            grade_input = input("please enter the grade: ")
            amend_gradebook("add", grade_input, assignment_input)  
        elif(user_input == "remove"):
            assignment_input = input("please enter the assignment name you want to remove: ")
            grade_input = input("please enter the grade you want to remove: ")
            amend_gradebook("remove", grade_input, assignment_input)  
        elif(user_input == "print"):
            print_grades()
        elif(user_input == "exit"):
            print("Exiting Gradebook")
            break
# Running the main function
main()