#make a quiz game use  2d collections to make it easy
answer = ("B" , "A" ,"" ,"" , "")
questions = ("what is captial of india ?",
            "what is longeat river ?",
            "what is the smallest prime number",
            "what is smallest perfect number",
            "what is best sorting algorithm for almost sorted sata set")
options = (("A: kolkata" , "B: New delhi" , "C: mumbai" , "D: chennai"),
           ("A: ganga " , "B: yamuna","C : kaveri" ,"D: gandak"),
           ("A: 10" ,"B: 5" ,"C: 2" , "D: 13"),
           ("A: 3" , "B: 2",  "C: 8" , "D: 6"),
           ("A: quick sort" , "B: inseartion sort" ,"C: merger sort" ,"D: selection sort"))
selection= []
score = 0
question_no = 0

for question in questions :
    print(question)
    for option in options[question_no]:
        print(option)
    while True :
        select = input("ENTER A VALID OPTION (A , B , C , D) : ").upper()
        if select in ("A","B","C","D"):
            break 
        else :
            print("invalid choice !")
        
    selection.append(select)
    if select == answer[question_no] :
        score +=1 
        print("CORRECT")
    else :
        print("INCORRECT")

    question_no += 1
print(f"------YOUR FINAL SCORE IS : {score}  -------")   

        

        
              


 