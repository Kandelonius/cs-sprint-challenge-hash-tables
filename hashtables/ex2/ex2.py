#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    connections = {}
    route = []
    # print(f"first ticket is {tickets[0]}")
    for ticket in tickets:
        # print(ticket)
        connections[ticket.source] = ticket.destination
        # putting the first element into the list.
        if ticket.source == "NONE":
            route.append(ticket.destination)
    # add the items from connections to the list.
    for i in range(length - 1):
        temp = connections[route[i]]
        route.append(temp)

    print(connections)
    return route
#
# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")
#
# tickets = [ticket_1, ticket_2, ticket_3]
#
# # expected = ["PDX", "DCA", "NONE"]
# print(reconstruct_trip(tickets, 3))