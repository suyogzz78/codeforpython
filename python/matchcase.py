
marks = int(input("Enter your marks: "))

match marks:
    case _ if marks >= 40:
        print("You are passed")
    case _ if marks < 40:
        print("You are failed")
    case _ if marks > 90:
        print("You are great")
    case _:
        print("Marks don't match predefined cases")
