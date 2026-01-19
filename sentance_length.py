def main():
    sentence = input("Enter a sentence:")

    sentence_lenth = len(sentence)

    approx_length = (sentence_lenth // 10 ) * 10

    print(f"The sentence is{sentence_lenth}characters long.")
    print(f"Approximate length (in 10s): {approx_length}")


    return

if __name__ == '__main__':
    main()