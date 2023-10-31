import calendar


def display_calendar( month):
    
    cal = calendar.monthcalendar( month)
    
    
    print(calendar.month_name[month])
    print(" sun Mo Tu We Th Fr Sat ")
    
    for week in cal:
        for day in week:
            if day != 0:
                print(f"{day:2}", end=" ")
            else:
                print("   ", end=" ")
        print()

#year = int(input("Enter the year: "))
month = int(input("Enter the month (1-12): "))


display_calendar( month)