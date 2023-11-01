class Passenger:
    def __init__(self, name, ticket_number, destination, place):
        self.name = name  # Імя пасажира
        self.ticket_number = ticket_number  # Номер білета пасажира
        self.destination = destination  # Назва станції призначення
        self.place = place  # Номер місця в вагоні

    def __str__(self):
        return f"{self.name} ({self.ticket_number}), Destination: {self.destination}, Place: {self.place}"


# Створюємо пасажирів для вагонів
passengers_for_car1 = [
    Passenger("John Dow", "12345", "Station A", 1),
    Passenger("Alex Dowson", "67890", "Station B", 2),
    Passenger("Lisa Smith", "54321", "Station C", 3),
    Passenger("Eva Johnson", "98765", "Station A", 4),
    Passenger("Mike Brown", "23456", "Station B", 5),
    Passenger("Sophia Williams", "78901", "Station C", 6),
    Passenger("David Lee", "34567", "Station A", 7),
    Passenger("Olivia Davis", "89012", "Station B", 8),
    Passenger("Daniel Miller", "45678", "Station C", 9),
    Passenger("Emily Wilson", "90123", "Station A", 10),
]

passengers_for_car2 = [
    Passenger("Tom Johnson", "11111", "Station A", 11),
    Passenger("Sophie Davis", "22222", "Station B", 12),
    Passenger("Liam Brown", "33333", "Station C", 13),
    Passenger("Olivia Smith", "44444", "Station A", 14),
    Passenger("Lucas Lee", "55555", "Station B", 15),
    Passenger("Emma Wilson", "66666", "Station C", 16),
    Passenger("William Martin", "77777", "Station A", 17),
    Passenger("Ava Miller", "88888", "Station B", 18),
    Passenger("Mia Jones", "99999", "Station C", 19),
    Passenger("James White", "00000", "Station A", 20),
]
