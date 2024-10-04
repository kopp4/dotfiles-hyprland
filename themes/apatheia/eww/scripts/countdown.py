#!/usr/bin/env python3

import datetime
import sys
import calendar


def print_help():
    help_text = """
Usage: python script.py [options]

Options:
  print(" option: ./x.py DD/MM/YYYY event")
  -h, --help  Show this help message and exit.
"""
    print(help_text)


def date_subtract(ddldate):
    """
    math stuff
    return int daysleft
    """
    daysleft = (ddldate - datetime.date.today())
    return daysleft.days

def get_date(ddldate):
    """
    len(sys.argv) including ./count.py itself & the same to python x.py
    DD/MM/YYYY
    return : int days left
    """
    ddldate = datetime.datetime.strptime(ddldate, "%d/%m/%Y")
    return date_subtract(ddldate.date())

def get_event(event):
    """
    filter event after 1st parament
    return : str event
    """
    ddlevent = ' '.join(event)
    return ddlevent


def format_output(ddl, event):
    """
    How would you like to output
    """
    # print("There is only {} days left for {}".format(ddl, event))

    # print(str(ddl) + " Days ")          # daysleft 
    print(str(ddl))
    # print(str(int(ddl / 7)) + " Weeks ") # weeks left
    print(str(event))        # THE event that is coming towards us



if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if (sys.argv[1].lower() == '-h' or sys.argv[1].lower() == '--help'):
            print_help()
            sys.exit()
        try:
            ddl = get_date(sys.argv[1])
            event = get_event(sys.argv[2:])
            format_output(ddl, event)
        except Exception as e:
            print("DDL is not working it wont fix itself")


    else:
        """
        Print without parameters

        1. days left current month
        2. current month
        """

        today = datetime.date.today()
        current_month = today.month
        current_year = today.year
        # ddl = get_date(sys.argv[1])
        # event = get_event(sys.argv[2:])
        # format_output(ddl, event)


        _, number_of_days = calendar.monthrange(current_year, current_month)
    
        # Calculate remaining days
        remaining_days = number_of_days - today.day
    
        # print(f"Remaining days in {calendar.month_name[current_month]} {current_year}: {remaining_days}")
        print(f"{remaining_days}")
        print(f"{calendar.month_name[current_month]}")


