def main():
    cipher_alphabet = "OWQGPKVYEFDXMCHSBNRTIULZA"
    normal_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ciphertext = "EKORY ECVEN UHJRY GHECV ERENU HJRYG HECVS HHJXZ"

    cipher_mapping = dict(zip(cipher_alphabet, normal_alphabet))

    plaintext = "".join(cipher_mapping.get(char, char) for char in ciphertext)

    print(f"Ciphertext: {ciphertext}")
    print(f"Plaintext: {plaintext}")


if __name__ == '__main__':
    main()
