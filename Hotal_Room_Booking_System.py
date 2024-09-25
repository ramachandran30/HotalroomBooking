import random
import webbrowser
li=[1,2,3,4,5,6,7,9,11,23,44,56,77]
d=random.choice(li)
def st1():
    p='Booking'
    print(p.center(100," "),"\n")
    global name
    name=input("Enter a name : ")
    mobile=int(input("how many rooms : "))
    Adder=input('Enter your Id Cord Number : ')
    x=Adder[5:-1]
    
    if(mobile>=True):

        print(" ")
        print(f"Hi {name} your room no:{d} is checking Avaiable")
        print(f"your last 4 digits of Adder is XXXXXXXXX{x}")
        print(f"OYO room was Booked for {name}")
        print('')
        print("------------Room Booked Sucessfull----------")
        webbrowser.open("https://www.booking.com/searchresults.html?label=slnb_msn-lTzSInkrq8mCQDFfdFxeJA-80333103645065%3Atikwd-138208586508%3Aloc-90%3Aneo%3Amte%3Alp144034%3Adec%3Aqsoyo+room+booking+online&sid=b53fa0de26b83dc7200794d838605d03&aid=393655&dest_id=-2103041&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0")


    else:
        print("ERROR")
def st2():
    pass

    


def st3():
    webbrowser.open('https://www.online-reservations.com/?hotelid=3029112&msclkid=0cc0fb6b55fd100791659de245a4e82a')
#-----------------------------



    
p=int(input("Enter A choice : "))

if(p==1):
    st1()
elif(p==2):
    st2()
elif(p==3):
    st3()
else:
    print("the end")
