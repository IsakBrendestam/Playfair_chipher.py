alphabet_no_j = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def key_generation(keyword):
    """Generating key used to de-/en-crypt msessage"""
    table = []
    new_keyword = keyword.replace(" ", "")
    keyword_list = list(new_keyword.upper())
    found_character = False
    exist = 0
    for i in range(5):
        new_table = []
        for j in range(5):
            added = False
            while not added:
                if i*5 + j + exist < len(keyword_list): 
                    if not any(keyword_list[i*5+j + exist] in sublist for sublist in table) and keyword_list[i*5+j + exist] not in new_table:
                        if keyword_list[i*5+j + exist] == "J":
                            new_table.append("I")
                        else:
                            new_table.append(keyword_list[i*5+j + exist])
                        added = True
                    else:
                        exist += 1
                else:
                    found_character = False
                    for character in alphabet_no_j:
                        if not found_character and not any(character in sublist for sublist in table) and character not in new_table:
                            new_table.append(character)
                            added = True
                            found_character = True
              
        table.append(new_table)
    return table

def list_to_string(l):
    """Converts list to string"""
    string = ""
    for a in l:
        string += a
    return string

def the_playfair_cipher_encrypt(msg, key):
    """Encrypt method"""
    #Ignore spaces, and convert all letters to upper case.
    new_msg = msg.upper()
    new_msg = new_msg.replace(" ", "")
  
    #Convert all instances of the letter “J” in your message to “I”.
    new_msg = new_msg.replace("J", "I")

    new_list = list(new_msg)

    
    #If both letters in the digraph are the same, add an "X" after the first letter, rearranging the subsequent digraphs if necessary
    done = False
    while not done:
        found = False
        for i in range(int(len(new_list)/2)):
            if new_list[2*i] == new_list[2*i + 1] and found == False and (new_list[2*i] != "X" and new_list[2*i + 1] != "X"):
                new_list.insert(2*i + 1, "X")
                found = True
        if found == False:
            done = True
    
    #If a letter is left without a partner, add an “X” at the end.
    number_of_spaces = int((len(new_list))/2)
    if (len(new_list))/2 != number_of_spaces:
        new_list.append("X")
        number_of_spaces += 1
    
    #Break it into digraphs 
    for i in range(number_of_spaces-1):
        new_list.insert((i+1)*2 + i, " ")
    
    #Positions in key
    digraphs_pos_in_key = []
    temp_pos = []
    for letter in new_list:
        if letter != " ":
            for row in range(len(key)):
                for col, j in enumerate(key[row]):
                    if j == letter:
                        temp_pos.append(row)
                        temp_pos.append(col)
        else:
            digraphs_pos_in_key.append(temp_pos)
            temp_pos = []
    digraphs_pos_in_key.append(temp_pos)

    final_result_list = []
    for index, row in enumerate(digraphs_pos_in_key):
        letter1_x = digraphs_pos_in_key[index][0]
        letter1_y = digraphs_pos_in_key[index][1]
        letter2_x = digraphs_pos_in_key[index][2]
        letter2_y = digraphs_pos_in_key[index][3]
        if key[letter1_x][letter1_y] == "X" and key[letter2_x][letter2_y] == "X":
            final_result_list.append("Y")
            final_result_list.append("Y")
        elif letter1_x != letter2_x and letter1_y != letter2_y:
            final_result_list.append(key[letter1_x][letter2_y])
            final_result_list.append(key[letter2_x][letter1_y])
        elif letter1_x != letter2_x and letter1_y == letter2_y:  
            if letter1_x != len(key)-1:
                final_result_list.append(key[letter1_x+1][letter1_y])
            else:
                final_result_list.append(key[0][letter1_y])

            if letter2_x != len(key)-1:
                final_result_list.append(key[letter2_x+1][letter2_y])
            else:
                final_result_list.append(key[0][letter2_y])
        elif letter1_x == letter2_x and letter1_y != letter2_y:
            if letter1_y != len(key[0])-1:
                final_result_list.append(key[letter1_x][letter1_y+1])
            else:
                final_result_list.append(key[letter1_x][0])

            if letter2_y != len(key[0])-1:
                final_result_list.append(key[letter2_x][letter2_y+1])
            else:
                final_result_list.append(key[letter2_x][0])
        
    return list_to_string(final_result_list)

def main_playfair_cipher():
    """Main mathod"""
    done = False
    while not done:
        num_lines = int(input())
        if num_lines > 0:             
            key_word = input()
            key = key_generation(key_word)     
            text = []
            for _ in range(num_lines):
                text_input = input()
                text.append(text_input)

            for t in text:
                print(the_playfair_cipher_encrypt(t, key))
            print()
        else:
            done = True     

main_playfair_cipher()
