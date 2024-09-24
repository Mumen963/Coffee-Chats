from typing import Iterator
from datetime import datetime



"""
    Represents a Senior Executive in the platform.

    Attributes:
    - name: Name of the Senior Executive.
    - industry: Industry the Senior Executive belongs to.
    - company: Company where the Senior Executive works.
    - title: Job title of the Senior Executive.
    - price: Price for booking a coffee chat with the Senior Executive.
    - region: Region where the Senior Executive operates.
    - interests: Interests related to the Senior Executive's industry.

    Methods:
    - display_info(): Returns a formatted string with the Senior Executive's information.
"""

class SeniorExecutive:
    def __init__(self, name, industry, company, title, price, region, interests):
        self.name = name
        self.industry = industry
        self.company = company
        self.title = title
        self.price = price
        self.region = region
        self.interests = interests


    
    # Returns a formatted string with the Senior Executive's information.
    def display_info(self):
        info = ""
        info += f"Name: {self.get_name()}\n"
        info += f"Industry: {self.get_industry()}\n"
        info += f"Company: {self.get_company()}\n"
        info += f"Title: {self.get_title()}\n"
        info += f"Price: {self.get_price()}\n"
        info += f"Region: {self.get_region()}\n"
        info += f"Interests: {self.get_interests()}\n"
        return info

    # Getter methods
    def get_name(self):
        return self.name

    def get_industry(self):
        return self.industry

    def get_company(self):
        return self.company

    def get_title(self):
        return self.title

    def get_price(self):
        return self.price

    def get_region(self):
        return self.region

    def get_interests(self):
        return self.interests

    # Setter methods
    def set_name(self, name):
        self.name = name

    def set_industry(self, industry):
        self.industry = industry

    def set_company(self, company):
        self.company = company

    def set_title(self, title):
        self.title = title

    def set_price(self, price):
        self.price = price

    def set_region(self, region):
        self.region = region

    def set_interests(self, interests):
        self.interests = interests


#______________________________________________________________________________________

"""
    Represents an Aspiring Professional in the platform.

    Attributes:
    - name: Name of the Aspiring Professional.
    - industry: Industry the Aspiring Professional belongs to.
    - interests: Interests related to the Aspiring Professional's industry.
    - frequency: Number of times the Aspiring Professional has made bookings.
"""

class AspiringProfessional:
    def __init__(self, name, industry, interests):
        self.name = name
        self.industry = industry
        self.interests = interests
        self.frequency = 0

    # Getter methods
    def get_name(self):
        return self.name

    def get_industry(self):
        return self.industry

    def get_interests(self):
        return self.interests

    def get_frequency(self):
        return self.frequency

    # Increases the booking frequency of the Aspiring Professional.
    def increase_frequency(self):
        self.frequency += 1

    # Decreases the booking frequency of the Aspiring Professional.
    def decrease_frequency(self):
        if self.frequency > 0:
            self.frequency -= 1


    # Returns a formatted string with the Aspiring Professional's information
    def display_info(self):
        info = ""
        info += f"Name: {self.get_name()}\n"
        info += f"Industry: {self.get_industry()}\n"
        info += f"Interests: {', '.join(self.get_interests())}\n"
        info += f"Frequency: {self.get_frequency()}\n"
        return info

#______________________________________________________________________________________

"""
    Represents an event logged in the platform.

    Attributes:
    - date_logged: Date and time when the event was logged.
    - description: Description of the event.
"""

class Event:
    HASH_CONSTANT = 13

    def __init__(self, description):
        self.date_logged = datetime.now()
        self.description = description

    def get_date(self):
        return self.date_logged

    def get_description(self):
        return self.description

    def __eq__(self, other):
        if not isinstance(other, Event):
            return False
        return (self.date_logged == other.date_logged
                and self.description == other.description)

    def __hash__(self):
        return hash(self.date_logged) * Event.HASH_CONSTANT + hash(self.description)

    # Returns a string representation of the event.
    def __str__(self):
        return str(self.date_logged) + "\n" + self.description + "\n"



#______________________________________________________________________________________

"""
    Represents a log of events in the platform.

    Singleton class ensuring only one instance of EventLog exists.

    Attributes:
    - events: List of events logged in the system.
"""
class EventLog:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(EventLog, cls).__new__(cls)
            cls._instance.events = []
        return cls._instance

    # Logs a new event in the event log.
    def log_event(self, event):
        self.events.append(event)

    # Clears all events in the event log and logs a clearing event
    def clear(self):
        self.events.clear()
        self.log_event(Event("Event log cleared."))

    # Returns all events logged in the event log.
    def get_events(self):
        return self.events

    # Returns an iterator over the events in the event log.
    def __iter__(self):
        return iter(self.events)

#______________________________________________________________________________________

"""
    Represents the platform managing Aspiring Professionals, Senior Executives, and bookings.

    Attributes:
    - aspiring_professionals: List of AspiringProfessional objects.
    - senior_executives: List of SeniorExecutive objects.
    - bookings: List of Booking objects.
"""

class Platform:
    def __init__(self):
        self.aspiring_professionals = []
        self.senior_executives = []
        self.bookings = []

    # Adds a new Aspiring Professional to the platform.
    def add_aspiring_professional(self, professional):
        self.aspiring_professionals.append(professional)
        EventLog().log_event(Event(f"Aspiring Professional added: {professional.get_name()}"))

    # Removes an Aspiring Professional from the platform.
    def remove_aspiring_professional(self, professional):
        self.aspiring_professionals.remove(professional)
        EventLog().log_event(Event(f"Aspiring Professional removed: {professional.get_name()}"))

    # Returns all Aspiring Professionals in the platform.
    def get_aspiring_professionals(self):
        return self.aspiring_professionals

    # Adds a new Senior Executive to the platform.
    def add_senior_executive(self, executive):
        self.senior_executives.append(executive)
        EventLog().log_event(Event(f"Senior Executive added: {executive.get_name()}"))

    # Removes a Senior Executive from the platform.
    def remove_senior_executive(self, executive):
        self.senior_executives.remove(executive)
        EventLog().log_event(Event(f"Senior Executive removed: {executive.get_name()}"))

    # Returns all Senior Executives in the platform.
    def get_senior_executives(self):
        return self.senior_executives

    # Adds a new booking between an Aspiring Professional and a Senior Executive.
    def add_booking(self, booking):
        self.bookings.append(booking)
        EventLog().log_event(Event(f"Booking added: {booking.get_aspiring_professional().get_name()} with {booking.get_senior_executive().get_name()}"))

    # Removes a booking from the platform.
    def remove_booking(self, booking):
        self.bookings.remove(booking)
        EventLog().log_event(Event(f"Booking removed: {booking.get_aspiring_professional().get_name()} with {booking.get_senior_executive().get_name()}"))

    # Getter for bookings
    def get_bookings(self):
        return self.bookings


#______________________________________________________________________________________

"""
Represents a booking between an Aspiring Professional and a Senior Executive.

Attributes:
- aspiring_professional: The Aspiring Professional involved in the booking.
- senior_executive: The Senior Executive involved in the booking.
- day: The day of the booking.
"""

class Booking:
    def __init__(self, aspiring_professional, senior_executive, day):
        self.aspiring_professional = aspiring_professional
        self.senior_executive = senior_executive
        self.day = day

        # Increase frequency when booking is made
        aspiring_professional.increase_frequency()

    # Getters and Setters
    def get_aspiring_professional(self):
        return self.aspiring_professional

    def set_aspiring_professional(self, aspiring_professional):
        self.aspiring_professional = aspiring_professional

    def get_senior_executive(self):
        return self.senior_executive

    def set_senior_executive(self, senior_executive):
        self.senior_executive = senior_executive

    def get_day(self):
        return self.day

    # Logs event of changing the date of booking
    def set_day(self, day):
        EventLog().log_event(Event(
            f"Booking time changed from {self.get_day()} to {day} for {self.aspiring_professional.get_name()} with {self.senior_executive.get_name()}"
        ))
        self.day = day


    # Method to display booking details
    def display_booking(self):
        return f"Senior Executive {self.senior_executive.get_name()} is booked by Aspiring Professional " \
               f"{self.aspiring_professional.get_name()} on {self.day}\n"


#______________________________________________________________________________________

"""
The `PlatformApp` class is the main entry point for the platform application, 
which manages operations related to Aspiring Professionals, Senior Executives, 
and bookings. It interacts with the `Platform` class to perform various tasks.
"""
class PlatformApp:
    platform = Platform()

    # Dummy data 
    @staticmethod
    def initialize_platform():
        names = [
            "Mohammed", "Ali", "Fatima", "Aisha", "Omar", "Yusuf", "Sana", "Imran",
            "Layla", "Zaynab", "Ibrahim", "Huda", "Ahmad", "Safiya", "Salim",
            "Jamal", "Ayesha", "Yasin", "Nadia", "Hamza", "Zara", "Amir", "Hana",
            "Khalid", "Safia", "Bilal", "Mariam", "Tariq", "Saida", "Jamil"
        ]
        industries = [
            "Technology", "Healthcare", "Education", "Finance", "Engineering",
            "Media", "Consulting", "Retail", "Accounting", "Marketing",
            "Hospitality", "Business", "Engineering", "Arts",
            "Journalism", "Government", "Sciences",
            "Entertainment", "Insurance", "Construction", "Health"
        ]
        companies = [
            "Pioneer Solutions", "Evergreen Enterprises", "Summit Innovations", "Vanguard Holdings",
            "Horizon Group", "Eclipse Ventures", "Prime Partners", "Zenith Global", "Infinity Solutions",
            "Serenity Enterprises", "Catalyst Holdings", "Apex Strategies", "Tranquil Systems",
            "Ascendant Technologies", "Fusion Dynamics", "Elevate Ventures", "Stratosphere Solutions",
            "Equinox Strategies", "Aurora Enterprises", "Synergy Solutions"
        ]
        titles = [
            "Chief Executive Officer", "Managing Director", "Director of Operations", "Executive Vice President",
            "Senior Manager", "Head of Strategy", "Principal Consultant", "General Manager",
            "Chief Financial Officer", "Chief Operating Officer", "Chief Marketing Officer", "Chief Technology Officer",
            "Senior Analyst", "Senior Advisor", "Business Development Manager", "Project Manager",
            "Operations Manager", "Product Manager", "Human Resources Director", "Finance Director"
        ]
        interests = industries

        for i, name in enumerate(names):
            industry = industries[i % len(industries)]
            company = companies[i % len(companies)]
            title = titles[i % len(titles)]
            price = (i % 5 + 1) * 50
            region = "Canada"
            interests = [industries[i % len(industries)]]
            senior_executive = SeniorExecutive(name, industry, company, title, price, region, interests)
            PlatformApp.platform.add_senior_executive(senior_executive)

    @staticmethod
    def display_menu():
        menu = "\nPlatform Menu:\n" \
               "1. Add New Senior Executive\n" \
               "2. Remove Senior Executive\n" \
               "3. Update Senior Executive Details\n" \
               "4. Make New Booking\n" \
               "5. Change Booking Time\n" \
               "6. Delete Booking\n" \
               "7. Show All Aspiring Professionals\n" \
               "8. Show All Senior Executives\n" \
               "9. Show All Bookings\n" \
               "10. Exit\n"
        print(menu)


    """
    Adds a new Senior Executive to the platform.

    This method prompts the user to enter details for a new Senior Executive, including name, industry,
    company, title, price, region, and interests. It then creates a new Senior Executive object and adds it
    to the platform.
    """
    @staticmethod
    def add_new_senior_executive():
        name = input("Enter the name of the Senior Executive: ")
        industry = input("Enter the industry of the Senior Executive: ")
        company = input("Enter the company of the Senior Executive: ")
        title = input("Enter the title of the Senior Executive: ")
        while True:
            try:
                price = float(input("Enter the price for booking a coffee chat with the Senior Executive ($): "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid price.")        
        region = input("Enter the region of the Senior Executive: ")
        interests = input("Enter interests of the Senior Executive (comma-separated): ").split(",")

        senior_executive = SeniorExecutive(name, industry, company, title, price, region, interests)
        PlatformApp.platform.add_senior_executive(senior_executive)
        print(f"Senior Executive {name} added successfuly.")


    """
    Removes a Senior Executive from the platform.

    This method prompts the user to enter the name of the Senior Executive to remove. It then searches
    for the Senior Executive in the platform and removes them if found.
    """
    @staticmethod
    def remove_senior_executive():
        name = input("Enter the name of the Senior Executive to remove: ")
        executives = PlatformApp.platform.get_senior_executives()

        for executive in executives:
            if executive.get_name().lower() == name.lower():
                PlatformApp.platform.remove_senior_executive(executive)
                print(f"Senior Executive {name} removed successfuly.")
                return

        print(f"Senior Executive {name} not found.")


    """
    Updates the details of an existing Senior Executive.

    This method prompts the user to enter the name of the Senior Executive to update. It then allows the user
    to update the industry, company, title, price, region, and interests of the Senior Executive.
    """
    @staticmethod
    def update_senior_executive_details():
        name = input("Enter the name of the Senior Executive to update: ")
        executives = PlatformApp.platform.get_senior_executives()

        found = False
        for executive in executives:
            if executive.get_name().lower() == name.lower():
                found = True
                print("Current details:")
                print(executive.display_info())

                industry = input("Enter the new industry of the Senior Executive (press Enter to keep current): ")
                if industry:
                    executive.set_industry(industry)

                company = input("Enter the new company of the Senior Executive (press Enter to keep current): ")
                if company:
                    executive.set_company(company)

                title = input("Enter the new title of the Senior Executive (press Enter to keep current): ")
                if title:
                    executive.set_title(title)

                while True:
                    try:
                        price = input("Enter the new price for booking a coffee chat with the Senior Executive ($),(press Enter to keep current): ")
                        if price.strip():
                            executive.set_price(float(price))
                            break
                        else:
                            break
                    except ValueError:
                        print("Invalid input. Please enter a valid price.")

                region = input("Enter the new region of the Senior Executive (press Enter to keep current): ")
                if region:
                    executive.set_region(region)

                interests = input("Enter new interests of the Senior Executive (comma-separated, press Enter to keep current): ")
                if interests:
                    executive.set_interests(interests.split(","))

                print(f"Senior Executive {name} details updated successfuly.")
                return

        if not found:
            print(f"Senior Executive {name} not found.")


    """
    Initiates the process for making a new booking.

    This method asks the user whether they are new to the platform. Based on the response, it calls the
    appropriate method to handle the booking process for new or existing Aspiring Professionals.
    """
    def make_new_booking():
        print("Welcome to the booking process.")

        while True:
            isNew = input("Are you new to the platform? (yes/no): ").strip().lower()

            if isNew == "yes":
                PlatformApp.handle_new_aspiring_professional_booking()
                break
            elif isNew == "no":
                PlatformApp.handle_existing_aspiring_professional_booking()
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


    """
    Handles the booking process for new Aspiring Professionals.

    This method prompts the user to provide details for a new Aspiring Professional and adds them to the
    platform. It then displays available Senior Executives in the specified industry and allows the user
    to make a booking.
    """
    @staticmethod
    def handle_new_aspiring_professional_booking():
        print("Welcome! Please provide the following details:")

        name = input("Name: ").strip()
        industry = input("Industry: ").strip()
        interestsInput = input("Interests (comma separated): ").strip()
        interests = [interest.strip() for interest in interestsInput.split(',')]

        professional = AspiringProfessional(name, industry, interests)
        PlatformApp.platform.add_aspiring_professional(professional)

        print()
        print("Thank you for joining us. Here are the available executives in your industry:")
        PlatformApp.display_executives_by_industry(name, industry)


    """
    Handles the booking process for existing Aspiring Professionals.

    This method prompts the user to provide their name and verifies their presence in the platform.
    It then displays available Senior Executives in the specified industry and allows the user to make a booking.
    """
    @staticmethod
    def handle_existing_aspiring_professional_booking():
        print("Welcome back! Please provide your name:")

        name = input("Name: ").strip()

        existingProfessional = PlatformApp.find_aspiring_professional_by_name(name)
        if existingProfessional is None:
            print("Aspiring Professional not found. Please check the name or register as new.")
        else:
            print("Here are the available executives in your industry:")
            PlatformApp.display_executives_by_industry(existingProfessional.name, existingProfessional.industry)


    """
    Displays Senior Executives available in the specified industry.

    This method filters Senior Executives by industry and displays them. It allows the user to select
    an executive and make a booking by specifying a preferred day.
    """
    @staticmethod
    def display_executives_by_industry(name, industry):
        executives = []

        # Filter executives by industry
        for executive in PlatformApp.platform.get_senior_executives():
            if executive.industry.lower() == industry.lower():
                executives.append(executive)

        if not executives:
            print("No executives found in the specified industry.")
        else:
            print("Available executives:")
            for i, executive in enumerate(executives, start=1):
                print(f"{i}. {executive.display_info()}")

            # Loop until valid input for choice
            while True:
                try:
                    choice = int(input("Choose an executive (enter number): ").strip())

                    if 1 <= choice <= len(executives):
                        selected_executive = executives[choice - 1]

                        day = input("Choose a preferred day for the booking(Mon, Tue, Wed): ").strip()

                        booking = Booking(PlatformApp.find_aspiring_professional_by_name(name), selected_executive, day)
                        PlatformApp.platform.add_booking(booking)
                        print("Booking successfully made.")
                        break
                    else:
                        print("Invalid choice. Please select a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")


#  Finds an Aspiring Professional by their name.
    @staticmethod
    def find_aspiring_professional_by_name(name):
        for professional in PlatformApp.platform.get_aspiring_professionals():
            if professional.name.lower() == name.lower():
                return professional
        return None


    """
    Changes the time of an existing booking.

    This method prompts the user to enter the names of the Senior Executive and Aspiring Professional
    involved in the booking. It then allows the user to specify a new day for the booking and updates it.
    """
    @staticmethod
    def change_booking_time():
        senior_name = input("Enter the name of the Senior Executive booked with: ")
        aspiring_name = input("Enter the name of the Aspiring Professional: ")

        bookings = PlatformApp.platform.get_bookings()
        for booking in bookings:
            if booking.get_aspiring_professional().get_name().lower() == aspiring_name.lower() and \
                    booking.get_senior_executive().get_name().lower() == senior_name.lower():
                new_day = input("Enter the new day of the booking (e.g., Monday): ")
                booking.set_day(new_day)
                print("Booking time changed.")
                return

        print("Booking not found.")


    """
    Deletes an existing booking.

    This method prompts the user to enter the names of the Senior Executive and Aspiring Professional
    involved in the booking. It then finds the booking and removes it from the platform.
    """
    @staticmethod
    def delete_booking():
        senior_name = input("Enter the name of the Senior Executive: ")
        aspiring_name = input("Enter the name of the Aspiring Professional: ")

        bookings = PlatformApp.platform.get_bookings()
        for booking in bookings:
            if booking.get_aspiring_professional().get_name().lower() == aspiring_name.lower() and \
                    booking.get_senior_executive().get_name().lower() == senior_name.lower():
                PlatformApp.platform.remove_booking(booking)
                booking.get_aspiring_professional().decrease_frequency()
                print("Booking deleted.")
                return

        print("Booking not found.")


    """
    Displays all Aspiring Professionals on the platform.

    This method retrieves and displays the details of all Aspiring Professionals registered on the platform.
    """
    @staticmethod
    def show_all_aspiring_professionals():
        professionals = PlatformApp.platform.get_aspiring_professionals()
        if not professionals:
            print("No aspiring professional found.")
        else:
            for professional in professionals:
                print(professional.display_info())
        

    """
    Displays all Senior Executives on the platform.

    This method retrieves and displays the details of all Senior Executives registered on the platform.
    """
    @staticmethod
    def show_all_senior_executives():
        executives = PlatformApp.platform.get_senior_executives()
        if not executives:
            print("No senior executives found")
        else:
            for executive in executives:
                print(executive.display_info())


    """
    Displays all bookings on the platform.

    This method retrieves and displays the details of all bookings made on the platform.
     """
    @staticmethod
    def show_all_bookings():
        bookings = PlatformApp.platform.get_bookings()
        if not bookings:
            print("No bookings found.")
        else:
            for booking in bookings:
                print(booking.display_booking())


    """
    Displays all events in the event log.

    This method retrieves and displays all events recorded in the event log.
    """
    @staticmethod
    def show_all_events():
        print("\n--- Event Log ---")
        for event in EventLog._instance.get_events():
            print(f"{event.__str__()} ")


    """
    The main entry point of the application.

    This method initializes the platform with dummy data and starts the main application loop,
    displaying the menu and handling user input to perform various operations.
    """
    @staticmethod
    def main():
        PlatformApp.initialize_platform()

        while True:
            PlatformApp.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                PlatformApp.add_new_senior_executive()
            elif choice == "2":
                PlatformApp.remove_senior_executive()
            elif choice == "3":
                PlatformApp.update_senior_executive_details()
            elif choice == "4":
                PlatformApp.make_new_booking()
            elif choice == "5":
                PlatformApp.change_booking_time()
            elif choice == "6":
                PlatformApp.delete_booking()
            elif choice == "7":
                PlatformApp.show_all_aspiring_professionals()
            elif choice == "8":
                PlatformApp.show_all_senior_executives()
            elif choice == "9":
                PlatformApp.show_all_bookings()
            elif choice == "10":
                PlatformApp.show_all_events()
                print("Exiting platform.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 10.")

if __name__ == "__main__":
    PlatformApp.main()