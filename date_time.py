from datetime import datetime, timedelta
def display_current_date():
    curr_date = datetime.now()
    date_format = curr_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"the current date is : {date_format}")
    return curr_date
def display_future_date():
    currently = datetime.now()
    num_of_days = int(input("Enter number of days:"))
    try:
        future_date = currently + timedelta(days = num_of_days)
        future_format = future_date.strftime("%Y-%m-%d %H:%M:%S")
        print(future_format)
    except ValueError:
        print("Invalid num of days")
display_current_date()
display_future_date()