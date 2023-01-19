from HW4.Services.TicketRepository import TicketRepository


class TicketProvider:

    def __init__(self):
        self.ticket_repo = TicketRepository.get_tickets_repository()

    def get_tickets(self, route):
        return self.ticket_repo.read_all(route)

    def update_ticket_status(self, ticket):
        return self.ticket_repo.update(ticket)