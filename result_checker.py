data={1001:200,1002:210,1003:300,1004:350,1005:400} # database used to store ,marks and roll no of students
try:
    roll_no=int(input("Enter your roll_no:")) #roll_no input
    if roll_no in data:
            print(f"The marks allotted for roll_no {roll_no} is {data[roll_no]} marks")
    elif len(str(roll_no))>4:
        print(f"four digits roll_no are accepted more than four digit roll_no {roll_no} are not accepted")
    else:
        print("The entered roll_no is not present in our database,check the roll_no and try again")
except ValueError:
    print("Only integers value are accepted no decimal or strings or any other values are accepted")

