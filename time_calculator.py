user_start = input("Start Time(HH:MM)pm/am: ")
user_end = input("End Time(HH:MM)pm/am: ")

opt = False
if opt == True:
    optional_day = input("Day: ")

def add_time(user_start,user_end):
    #start time.
    start_hour = int(user_start.split(':')[0])
    start_min = int(user_start.split(':')[1])
    #end time.
    end_hour = int(user_end.split(':')[0])
    end_min = int(user_end.split(':')[1])

    #calculate the day
    day = (start_hour+end_hour) // 24
    

    #calculate the minute
    if ((start_min+end_min)%60>=1):
        remain_min = (start_min+end_min)%60
        #output the total hours and minutes .
        print(f"and total of {start_hour+end_hour} hours and {remain_min%60} minutes.")

    #get the time minutes.
    minutes = end_min + start_min
    count = int(0)
    while minutes >= 60:
        minutes = minutes - 60
        count = count + 1

    #get hours for the day.
    hours = ((start_hour + end_hour)%24)+count
    if(hours < 12) and (minutes < 0):
        print(f"({hours}:{minutes}am) ({day} days later)")
    else:
        #convert the hours after 12 am to pm format.
        x = hours
        match x:
            case 13:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            case 14:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            case 15:
                print(f"({x-12}:{minutes}pm) ({day} days later")
            case 16:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            case 17:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            case 18:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            case 19:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            case 20:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            case 21:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            case 22:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            case 23:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            case 24:
                print(f"({x-12}:{minutes}pm) ({day} days later)")
            

add_time(user_start,user_end)