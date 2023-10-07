class Star_cinema:
    hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls.hall_list.append(hall)


class Hall:
    def __init__(self, rows, cols, hall_no):
        self._seats = {}
        self._show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)      # show info 

        seats = [["Free" for _ in range(self._cols)] for _ in range(self._rows)]       #  seats as a 2d list 
        self._seats[id] = seats

    def book_seats(self, id, seat_list):
        if id not in self._seats:
            print("Invalid show ID.")
            return

        seats = self._seats[id]
        for row, col in seat_list:
            if row < 1 or row > self._rows or col < 1 or col > self._cols:
                print(f"Invalid seat ({row}, {col}).")
                continue

            if seats[row - 1][col - 1] == "Free":
                seats[row - 1][col - 1] = "Booked"
                print(f"Seat ({row}, {col}) has been booked successfully.")
            else:
                print(f"Seat ({row}, {col}) is already booked.")

    def show_list(self):
        print("Shows running in Theater", self._hall_no)
        for id, movie_name, time in self._show_list:
            print(f"Show ID: {id}, Movie: {movie_name}, Time: {time}")

    def available_seats(self, id):
        if id not in self._seats:
            print("Invalid show ID.")
            return

        seats = self._seats[id]
        print(f"Available seats for show {id}:")
        for row in range(self._rows):
            for col in range(self._cols):
                if seats[row][col] == "Free":
                    print(f" {row + 1}, {col + 1}")


hall1 = Hall(rows=7, cols=7, hall_no=1)
hall1.entry_show("S1", "Movie : Jawan maji", "1:00 AM")
hall1.entry_show("S2", "Movie : Sujan maji", "2:00 PM")

while True:
    print("\nOption:")
    print("1: All shows today")
    print("2: Available seats")
    print("3: Book tickets")
    print("4: Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        hall1.show_list()
    elif choice == "2":
        show_id = input("Enter show ID: ")
        hall1.available_seats(show_id)
    elif choice == "3":
        show_id = input("Enter show ID: ")
        num_seats = int(input("Enter the number of seats to book: "))
        seat_list = []
        for _ in range(num_seats):
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            seat_list.append((row, col))
        hall1.book_seats(show_id, seat_list)
    elif choice == "4":
        break
    else:
        print("Invalid Option. Please try again.")
