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

li = [rock, paper, scissors]

# Generate a random computer choice
c_choice = random.choice(li)

# Ask the user for their choice
# 1 for rock 2 for paper 3 for scissors
u_choice = int(input('Enter 1 for ROCK, 2 for PAPER, 3 for SCISSORS: '))

# Print user choice and computer choice on the console
print(f'You chose {li[u_choice-1]}')
print(f'Computer chose {c_choice}')

if u_choice == 1 and c_choice == scissors:
  print('You win :)')
elif u_choice == 2 and c_choice == rock:
  print('You win!!')
elif u_choice == 3 and c_choice == paper:
  print('You win :)')
else:
  print('You loose :(')
