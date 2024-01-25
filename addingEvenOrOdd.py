while True:
    choice= input("Would you like to add even or odd?: ")
    if choice == 'even':
        target = int(input("Enter a number: ")) # Enter a number between 0 and 1000
        # 🚨 Do not change the code above ☝️

        # Write your code here 👇
        targetInclution = target +1
        number =0
        for n in range(0,targetInclution):
            if n%2 ==0:
                number += n
        print(f"The addition of all even number from 1- {target} is {number}")
    else:
        target = int(input("Enter a number: ")) # Enter a number between 0 and 1000
        # 🚨 Do not change the code above ☝️

        # Write your code here 👇
        targetInclution = target +1
        number =0
        for n in range(0,targetInclution):
            if n%2 !=0:
                number += n
        print(f"The addition of all odd number from 1- {target} is {number}")
        
    finalChoice = input("Would you like to use the calculator again? (Y/N)")
    if finalChoice == 'N' or finalChoice =='n':
        print("Thanks for using our calculator")
        break 
