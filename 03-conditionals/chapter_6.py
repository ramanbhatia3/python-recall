# match case

course = input("Enter your course (FSD/AI/CC): ").lower()

match course:
    case "fsd":
        print("Full Stack Development")
    case "ai":
        print("Artificial Intelligence")
    case "cc":
        print("Cloud Computing")
    case "sleeper":
        print("Sleeper - No AC")
    case _:
        print("Invalid Course")