import datetime

while(True):
    # get the name of the city from the user
    city = input("Enter city: ")
    # get the current time
    current_time = datetime.datetime.now()

    # save hours, minutes and second of the current
    # time in their corresponding varisbles

    hour = current_time.hour
    minute = current_time.minute
    second = current_time.second

    # check for case 1
    if city == 'Boston':
        hour = hour - 4

    # check case 2:
    elif city == 'tokyo':
        hour = hour + 4
    
    # check case 3:

    elif city == 'chicago':
        hour = hour -7

    # check for case 4:
    elif city == 'exit':
        break

    # if all cases fail, show time for GMT

    else:
        print(city, "is not added")
        city = "GMT"
    
    # print the name of the city and its corresponding time
    print(city, str(hour) + ":" + str(minute) + ":" + str(second))
    