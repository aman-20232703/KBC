questions = [
    ["What is the output of: print(type([])) ?", "str", "list", "dict", "tuple"],
    ["Which keyword is used to define a function in Python ?", "def", "function", "define", "fun"],
    ["What does the len() function do ?", "Returns number of characters", "Returns number of elements", "Returns size in bytes", "Returns data type"],
    ["Which of these is used to import a module ?", "use", "include", "import", "require"],
    ["Which of the following is NOT a valid data type in Python ?", "list", "tuple", "map", "set"],
    ["What is the output of: 2 ** 3 ?", "5", "6", "8", "9"],
    ["Which symbol is used to comment a single line in Python ?", "//", "#", "/*", "<!--"],
    ["What is the default value of a function parameter if not specified ?", "0", "None", "undefined", "error"],
    ["How do you create a variable with a floating point value ?", "x = 10.5", "x = float(10)", "Both A and B", "None of the above"],
    ["What is the output of: bool(0) ?", "True", "False", "0", "Error"],
    ["Which loop is used to iterate over a sequence ?", "if", "switch", "for", "case"],
    ["What is the correct file extension for Python files ?", ".pt", ".pyt", ".py", ".python"],
    ["What is the output of: 'Python'[-1] ?", "P", "n", "o", "Error"],
    ["Which of the following is a mutable data type ?", "tuple", "string", "list", "int"],
    ["What is the output of: type(None) ?", "int", "NoneType", "null", "undefined"],
]

correct_answers = [2, 1, 2, 3, 3, 3, 2, 2, 3, 2, 3, 3, 2, 3, 2]
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0

for i in range(0,len(questions)):
    question=questions[i]
    # print(question)
    
    print(f"\n\nQuestion for ₹{levels[i]},\n{question[0]}")
    print(f"a. {question[1]}            b. {question[2]}")
    print(f"c. {question[3]}            d. {question[4]}")
    
    try:
        reply=int(input("Enter your option: "))
        if reply == correct_answers[i]:
            print(f"✅correct answer, you have won ₹{levels[i]}")
            if (i==1):
                money=1000
            elif (i==5):
                money= 10000
            elif (i==9):
                money= 320000
            elif (i==14):
                money=1000000
        else:
            print("❌ oops! wrong answer")
            break
    except:
        raise SyntaxError("⚠️ plz enter valid syntax'only numner' ")
    
print(f"\n🎉finally total reward is ₹{money}")
    
