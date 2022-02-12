service_charge = int(2)
TICKET_PRICE = int(10)
tickets_remaining = int(100)

# create the calculate_price function. It takes number of tickets and returns
# ticket_amount * TICKET_PRICE

def calculate_price(ticket_amount):
  # create new constant for the 2 dollar service charge
  # add service charge to our result
  return (ticket_amount * TICKET_PRICE) + (service_charge * ticket_amount)

#run this code continuously until we run out of tickets
while tickets_remaining > 0:
  
  # output how many tickets are remaining using the tickets_remaining variable
  
  print(f"There are {tickets_remaining} tickets left to purchase.")
  
  # gather user name and assign it to a new variable
  name = input("Good day to you! What is your name?: ")
  print(f"Welcome to Ticketmaster, {name}!")
  
  # prompt the user by name and ask how many tickets they would like
  # expect a ValueError to happen and handle it appropiately
  try:
    ticket_amount = int(input(f"How many tickets would you like to purchase today?: "))
    #raise a ValueError if tickets exceed availability
    if ticket_amount > tickets_remaining:
      raise ValueError("There are not enough tickets.")
  except ValueError as err:
    print(f"Oh no, we ran into an issue.{err} Please try again.")
    
  else:
    # calculate price (number of tickets * price) and assign it to variable 
    price = calculate_price(ticket_amount)
    
    # output price to the screen
    print(f"You've selected {ticket_amount} tickets. Your total is ${price}.")
    
    # prompt user to confirm their selection
    proceed = input("Would you like to proceed? y/n: ").lower().strip()
    
    # if they want to proceed
    if proceed == "y":
      # print out to the screen "SOLD!" to confirm purchase
      print("SOLD!")
      # update tickets_remaining
      tickets_remaining -= ticket_amount
    # otherwise thank them by name
    else:
      print(f"Thank you anyways, {name}")
  
  # notify the user that tickets are sold out
print("Sorry the tickets are all sold out.")
