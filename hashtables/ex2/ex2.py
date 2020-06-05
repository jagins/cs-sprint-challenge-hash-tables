#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination
    def __str__(self):
        return f'Ticket: {self.source}, {self.destination}'

def reconstruct_trip(tickets, length):
    routeMap = {}
    route = []
    for ticket in tickets:
        key = ticket.source
        routeMap[key] = ticket.destination
    
    key = 'NONE'
    while len(route) < length:
        route.append(routeMap[key])
        key = routeMap[key]
    
    return route