def main():
    import datetime

    today = datetime.date.today()
    print(f"Today's date: {today}")

    now = datetime.datetime.now()
    print(f"Current date and time: {now}")

    formatted_date = today.strftime("%d/%m/%y")
    print(f"Formatted date (short): {formatted_date}")

    formatted_datetime = now.strftime("%d/%m/%Y %H:%M")
    print(f"Formatted date with time: {formatted_datetime}")

    timezone = now.astimezone().tzinfo
    print(f"Time zone: {timezone}")


    
    return

if __name__ == '__main__':
    main()