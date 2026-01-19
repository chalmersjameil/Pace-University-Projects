def main():
    Current_time = float(input("What time is it Currrently?"))
    set_alarm = float(input("How long would you like to set alarm for"))

    if set_alarm >= Current_time:
        hours_until_alarm = set_alarm - Current_time

    else:
     hours_until_alarm = (24 - Current_time) + set_alarm

    print(f"I have {hours_until_alarm} hours until the alarm goes off.")
if __name__ == '__main__':
    main()