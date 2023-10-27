# Team work makes dream work
# create a list with a range deceasing every tickets by 1
# another list for the parking space which decrease the amount of parking space by 1

class Parking_garage:
    def __init__(self, parking_tickets):
        self.tickets = list(range(1, parking_tickets - 1))
        self.spaces = list(range(1, parking_tickets - 1))
    
    def takeTickets(self):
        if self.tickets = self.tickets.pop(1)

