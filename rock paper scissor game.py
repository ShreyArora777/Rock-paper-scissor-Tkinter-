# #asking the user the choice:
# import random
# choices = ('r', 'p', 's')
# emojis = { 'r': '🪨' , 'p': "📃" , 's': '✂️' }

# def get_user_choice():
#     while True:
#         user_choice = input("Rock , Paper, Scissors? ( r/p/s): ").lower()
#         if user_choice not in choices:
#             print("invalid choice!")
#             continue
#         else:
#             return user_choice
        
# def display_choices(user_choice, comp_choice):
#     print (f"you choose { emojis[user_choice]}")
#     print (f"computer choose { emojis[comp_choice]}")
    
# def determine_winner(user_choice, comp_choice):
#     if user_choice == comp_choice:
#         print("tie")
#     elif ((user_choice == 'r' and comp_choice == 's') or 
#         (user_choice == "s" and comp_choice == 'p') or 
#         (user_choice == 'p' and comp_choice == 'r')):
#         print("You Win!")
#     else:
#         print("You Loose!")

    
# def play_game():
#     while True:
#         user_choice =  get_user_choice()
        
#         comp_choice = random.choice(choices)

#         display_choices(user_choice, comp_choice)
#         determine_winner(user_choice, comp_choice)

#         should_continue = input('Contnue? (y/n): ').lower()
#         if should_continue == 'n':
#             break
        
# play_game()



import tkinter as tk
import random

# Choices and emojis
choices = ['r', 'p', 's']
emojis = {'r': '🪨 Rock', 'p': '📃 Paper', 's': '✂️ Scissors'}

# Initialize scores
player_score = 0
computer_score = 0

def play(user_choice):
    global player_score, computer_score

    comp_choice = random.choice(choices)

    user_label.config(text=f"You chose: {emojis[user_choice]}")
    comp_label.config(text=f"Computer chose: {emojis[comp_choice]}")

    if user_choice == comp_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == 'r' and comp_choice == 's') or \
         (user_choice == 's' and comp_choice == 'p') or \
         (user_choice == 'p' and comp_choice == 'r'):
        result_label.config(text="You Win!")
        player_score += 1
    else:
        result_label.config(text="You Lose!")
        computer_score += 1

    player_score_label.config(text=f"Player: {player_score}")
    comp_score_label.config(text=f"Computer: {computer_score}")


root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.configure(bg="#1e1e1e")
root.geometry("400x300")

font = ("Segoe UI Emoji", 14)

player_score_label = tk.Label(root, text="Player: 0", font=font, fg="white", bg="#1e1e1e")
player_score_label.pack(anchor='nw', padx=20, pady=10)

comp_score_label = tk.Label(root, text="Computer: 0", font=font, fg="white", bg="#1e1e1e")
comp_score_label.pack(anchor='ne', padx=20, pady=10)

user_label = tk.Label(root, text="You chose: ", font=font, fg="white", bg="#1e1e1e")
user_label.pack(pady=5)

comp_label = tk.Label(root, text="Computer chose: ", font=font, fg="white", bg="#1e1e1e")
comp_label.pack(pady=5)

result_label = tk.Label(root, text="", font=font, fg="white", bg="#1e1e1e")
result_label.pack(pady=10)


btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Rock", width=10, font=font, command=lambda: play('r')).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Paper", width=10, font=font, command=lambda: play('p')).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Scissors", width=10, font=font, command=lambda: play('s')).grid(row=0, column=2, padx=5)

root.mainloop()
