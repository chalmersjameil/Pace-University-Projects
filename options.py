def main():
    options = (('y', 'yes'), ('n', 'no'))
    options = options + (('m', 'maybe'), ('p', 'prefer not to answer'))
    for short, full in options:
        print(f"{short}: {full}")

    new_options = [full for short, full in options]
    for option in new_options:

        print(option)


    
    return

if __name__ == '__main__':
    main()