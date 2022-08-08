from ran import pick_random_word

def play_game(attempts=5):
    # it will contain main logic of my game
    selected_word = pick_random_word()

    current_word_state = ""
    for i in selected_word:
        if i == ''or i=='a'or i =='o' or i=='e' or i=='u':
            current_word_state+=i
        else:
            current_word_state+="_"
# attempts_remaining = attempts
# print_current_state(current_word_state, attempts)

#   if __name__ =="__main__":
#     play_game()     
