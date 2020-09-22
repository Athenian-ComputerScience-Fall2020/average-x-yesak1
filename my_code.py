# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# office hours with Megan

def avg(user_list):
    number=int(len(user_list))
    total=sum(user_list)
    average = total/number
    return average

   


if __name__ == '__main__':
   
        

    # test your fucntion with this print statement before writing the input loop    
    #print(avg([5,6,7]))   # Put the values you want to test in for x,y and z

    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section
    user_list = [] # start with an empty list
    # Write a loop to allow the user to input the values to be averaged
    number2=input("Enter a number")
    
    while number2 != ("done"):
        user_list.append(float(number2))
        number2=input("enter a number")
    print (avg(user_list))
    
        
            
       

        
    
    