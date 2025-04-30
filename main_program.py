import json
from random import randint
import datetime

#
event_date = datetime.date(2025, 8, 1)
event_time = datetime.time(14)
today = datetime.date.today()
event_date_and_time = f"{event_date.strftime('%d.%m.%y')}, " \
                      f"{event_time.strftime('%H:%M')}"


class Ticket:
    """The basic ticket"""
    def __init__(self):
        self.price = 15
        if len(sold_tickets) >= 10:
            pass
        else:
            while True:
                self.number = randint(1, 10)
                if self.number not in sold_tickets:
                    break

    def get_number(self):
        return self.number

    def get_price(self):
        return self.price

    def print_ticket(self):
        print(f"\n{'Ticket for a drawing masterclass':-^65s}")
        print(f"\tTicket price: {self.price:.2f}$")
        print(f"\tTicket number: {self.number}")
        print(f"\tDate of purchase: {today}")
        print(f"\tEvent date and time: {event_date_and_time}")
        print("-" * 65)


class PrePurchasedTicket(Ticket):
    """The ticket purchased in advance (90 days or more before the event)"""

    def __init__(self):
        super().__init__()
        self.price = 0.7 * super().get_price()


class StudentTicket(Ticket):
    """The student ticket"""

    def __init__(self):
        super().__init__()
        self.price = 0.5 * super().get_price()


class LateTicket(Ticket):
    """Late purchased ticket (7 days or less before the event)"""

    def __init__(self):
        super().__init__()
        self.price = 1.2 * super().get_price()


# File where the numbers of purchased tickets are stored
file_name = "tickets.json"
try:
    with open(file_name) as file:
        sold_tickets = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    sold_tickets = []


def update_database(number):
    """Add the purchased ticket number to the database"""
    with open(file_name, 'w') as f:
        sold_tickets.append(number)
        json.dump(sold_tickets, f)


def process_ticket(ticket_class):
    """Process the ticket, update database with it
    and assign it to the appropriate class """
    ticket = ticket_class()
    update_database(ticket.get_number())
    print("\nYour ticket is being printed...")
    ticket.print_ticket()


# Implementation of a ticket machine
print(f"\n{'Drawing Masterclass Ticket System':-^65s}")

while True:
    # The maximum number of tickets is 10.
    # If all tickets are sold out, no more tickets can be sold
    if len(sold_tickets) >= 10:
        print(f"\nUnfortunately, all tickets are sold out...")
        break
    else:
        print("\n0 - Exit"
              "\n1 - Buy a ticket")
        try:
            user_input = int(input("\n>>> "))
        except ValueError:
            print("\nPlease enter a valid input value!")
            continue

        if user_input == 0:
            print("\nThe end of the program...")
            break
        elif user_input == 1:
            # There is a discount for students
            print("\nWe have a special discount for students! "
                  "Are you a student?\n0 - no, 1 - yes.")
            try:
                user_student = int(input("\n>>> "))
            except ValueError:
                print("\nPlease enter a valid input value!")
                continue

            if user_student == 1:
                process_ticket(StudentTicket)
                continue

            elif user_student == 0:
                # There is a discount for tickets bought in advance
                if event_date - today >= datetime.timedelta(days=90):
                    print("\nWe have a discount for tickets purchased in advance!")
                    process_ticket(PrePurchasedTicket)
                    continue
                # Tickets bought too late cost more
                elif event_date - today <= datetime.timedelta(days=7):
                    print("\nTickets purchased too late are more expensive!")
                    process_ticket(LateTicket)
                    continue

                else:
                    process_ticket(Ticket)
                    continue
            else:
                print("\nPlease enter a valid input value!")
                continue
        else:
            print("\nPlease enter a valid input value!")
            continue
