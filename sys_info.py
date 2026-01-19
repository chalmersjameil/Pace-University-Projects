def main():
    import sys 
    import os 

    print(f"python: {sys.version}")
    print(f"Operating system:{sys.platform}")
    print(f"user:{os.getlogin}")
    print(f"Working dictionary:{os.getcwd} ")
    print(f"Current dictioanry:{os.listdir}")



    
    return

if __name__ == '__main__':
    main()
