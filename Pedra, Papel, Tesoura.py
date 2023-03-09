import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

user_choice = int(input("Escolha! 0 é Pedra, 1 é Papel e 2 é Tesoura: "))
print(f"Você escolheu:\n {game_images[user_choice]}")

computer_choice = random.randint(0, 2)
print(f"O Computador escolheu:\n {game_images[computer_choice]}")

# User escolhe Pedra
if user_choice == 0 and computer_choice == 0:
    print("Empate!")
elif user_choice == 0 and computer_choice == 1:
    print("Você Venceu!")
elif user_choice == 0 and computer_choice == 2:
    print("Você Perdeu!")

# User escolhe Papel
if user_choice == 1 and computer_choice == 0:
    print("Você Venceu!")
elif user_choice == 1 and computer_choice == 1:
    print("Empate!")
elif user_choice == 1 and computer_choice == 2:
    print("Você Perdeu!")

# User escolhe Tesoura
if user_choice == 2 and computer_choice == 0:
    print("Você Perdeu!")
elif user_choice == 2 and computer_choice == 1:
    print("Você Venceu!")
elif user_choice == 2 and computer_choice == 2:
    print("Empate!")

# User escolhe um número invalido
else:
    print("Você escolheu um número inválido, perdeu otário!")

