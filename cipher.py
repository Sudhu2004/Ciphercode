alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end_of_game=False
while not end_of_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    def caeser(start_text,shift_amount,cipher_direction):
        if cipher_direction=="decode":
            shift_amount*=-1
        end_text=""
        for char in start_text:
            if char in alphabet:
                position=alphabet.index(char)
                new_position=position+shift_amount
                end_text+=alphabet[new_position]
            else:
                end_text+=char
        print(f"The {cipher_direction}d message is {end_text}")
    caeser(start_text=text,shift_amount=shift,cipher_direction=direction)
    a=input(" Type 'yes' if you want to go again .Otherwise type 'no'")
    if a=="yes":
        end_of_game=False
    else:
        end_of_game=True
        print("Good Bye")


