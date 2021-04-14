logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# Start
print(logo)
print('Welcome to the secret auction program.')

flag = True
bids = {}
top_bid_amt = 0
top_bid_name = ''

while flag:
  # Take input from user and assign it to bids
  name = input('What is your name?: ')
  bid = int(input('What\'s your bid?: $'))
  bids[name] = bid

  # find highest bidder amt and name
  if bid > top_bid_amt:
    top_bid_amt = bid
    top_bid_name = name

  # ask user if they want to continue
  continu_e = input('Are there any other bidders? Type \'yes\' or \'no\': ')
  if continu_e == 'yes':
    print('\n'*100)
  else:
    flag = False

print(f'The winner is {top_bid_name} with a bid of ${top_bid_amt}')
