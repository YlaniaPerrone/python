'''
arrayColor = {
    "red":"🔴",
    "green":"🟢",
    "yellow":"🟡",
    "orange": "🟠",
    "blue":"🔵",
    "purple":"🟣",
    "white":"⚪",
    "black":"⚫",
    "brun":"🟤"
}

array = []


if len(array) > 0 :
    print("tableau initial \n " + str(array))

QuestionColorAd = str(input("What color do you want to insert  : "))

while QuestionColorAd != "stop":

    if (QuestionColorAd not in arrayColor):
        
        print("Color not exist, Choose other color !!!! ")

    elif (arrayColor[QuestionColorAd]  in array):
        print("Exist !!!! ")

    else:
        array.extend(arrayColor[QuestionColorAd])
        print(arrayColor[QuestionColorAd])
        #array.append(QuestionColorAd)

    print(array)

    QuestionColorAd = str(input("What color do you want to insert  (stop to quit) : "))

  
'''
#*************************************************************#
#                          Do while                           #
#*************************************************************#
arrayColor = {
    "red":"🔴",
    "green":"🟢",
    "yellow":"🟡",
    "orange": "🟠",
    "blue":"🔵",
    "purple":"🟣",
    "white":"⚪",
    "black":"⚫",
    "brun":"🟤"
}

array = []


if len(array) > 0 :
    print("tableau initial \n " + str(array))


while True:

    QuestionColorAd = str(input("What color do you want to insert  (stop to quit) : "))

    if(QuestionColorAd == "stop"):
        break
    else:
        if (QuestionColorAd not in arrayColor):
            
            print("Color not exist, Choose other color !!!! ")

        elif (arrayColor[QuestionColorAd]  in array):
            print("Exist !!!! ")

        else:
            array.append(arrayColor[QuestionColorAd])
            print(arrayColor[QuestionColorAd])
            #array.append(QuestionColorAd)

        print(array)


    

