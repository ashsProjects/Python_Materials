import time
import datetime
import calendar
#Use strptime to convert from string to a time object
#Use strftime to convert from a time object to a string
#Write a Python script to display the various Date Time formats
def display_time():
    print("Current date and time: {}".format(datetime.datetime.now()))#can also use time.strftime(time.ctime())
    print("Current year: {}".format(datetime.date.today().strftime("%Y")))
    print("Current Month: {} or abbrv. {}".format(datetime.date.today().strftime("%B"), datetime.date.today().strftime("%b")))
    print("Current week number of the year: {}".format(datetime.date.today().strftime("%W")))
    print("Current day of the week in num: {}".format(datetime.date.today().strftime("%w")))
    print("Current day of the week in str: {}".format(datetime.date.today().strftime("%A")))
    print("Current day of the year: {}".format(datetime.date.today().strftime("%j")))
    print("Current day of the month: {}".format(datetime.date.today().strftime("%d")))
#display_time()
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to convert a string to datetime
def str_to_dt(str1):
    date_obj = datetime.datetime.strptime(str1, "%b %d %Y %I:%M%p")
    print(date_obj)
#str_to_dt("Jan 1 2014 2:43PM")
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to subtract five days from the current date
#Use timdelta(n)
def subtract_from_current_day():
    dt = datetime.date.today() - datetime.timedelta(5)
    print(dt)  
#subtract_from_current_day()
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to print yesterday, today, tomorrow
def print_dates():
    print("Yesterday's date: ", datetime.date.today() - datetime.timedelta(1))
    print("Today's date: ", datetime.date.today())
    print("Tomorrow's date: ", datetime.date.today() + datetime.timedelta(1))    
#print_dates()
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to print the next 5 days starting today.
def print_5_days():
    for i in range(0,5):
        print(datetime.date.today() + datetime.timedelta(i + 1))
#print_5_days()
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to add 5 seconds to the current time.
def add_to_seconds():
    print("Current time: ", datetime.datetime.now() + datetime.timedelta(0,5))
#add_to_seconds()
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to find the date of the first Monday of a given week.
#print(time.asctime(time.strptime('2023 12 1', '%Y %W %w')))
#--------------------------------------------------------------------------------------------------------------------------------

#Write a Python program to select all the Sundays in a specified year.
def select_all_sundays(year):
    lst = []
    first_date = time.strptime(str(year) + " 0 0", "%Y %W %w").tm_yday
    last_date = time.strptime(str(year) + " 51 0", "%Y %W %w").tm_yday
    
    for i in range(first_date, last_date + 1, 7):
        lst.append(time.strftime("%d %B %Y",(time.strptime(str(year) + str(i), '%Y%j'))))
    for i in lst: print(i)
        
# select_all_sundays(2020)
#--------------------------------------------------------------------------------------------------------------------------------

# Calculate the number of months it takes to pay off a credit card
def credit_card_debt(bal, ir, mp):
    balance = bal
    interest_rate = ir
    monthly_payment = mp

    today = datetime.date.today()
    days_in_current_month = calendar.monthrange(today.year, today.month)[1]
    days_until_EOM = days_in_current_month - today.day

    start_date = today + datetime.timedelta(days=days_until_EOM + 1)
    end_date = start_date

    while balance > 0:
        monthly_interset = (interest_rate / 12) * balance
        balance += monthly_interset
        balance -= monthly_payment
        
        balance = 0 if balance < 0 else round(balance, 2)
        
        print(end_date, balance)
        
        days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
        end_date = end_date + datetime.timedelta(days=days_in_current_month)

credit_card_debt(5000, 0.13, 500)


