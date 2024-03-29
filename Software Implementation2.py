from enum import Enum  # Importing Enum class for creating enumerated constants

# Defining an Enum class for ticket types
class TicketType(Enum):
    ONLINE = 1  # Enum constant for online tickets
    IN_PERSON = 2  # Enum constant for in-person tickets

# Defining an Enum class for locations
class Location(Enum):
    PERMANENT_GALLERIES = "Permanent Galleries"  # Enum constant for permanent galleries
    EXHIBITION_HALLS = "Exhibition Halls"  # Enum constant for exhibition halls
    OUTDOOR_SPACES = "Outdoor Spaces"  # Enum constant for outdoor spaces

# Defining a class for the ticketing system
class TicketingSystem:
    def __init__(self):
        self.visitor_demographics = None  # Initializing visitor demographics

    # Method to set visitor demographics
    def get_visitor_demographics(self, name, age, gender):
        self.visitor_demographics = VisitorDemographics(name, age, gender)  # Creating VisitorDemographics object

    # Method to purchase ticket
    def purchase_ticket(self, event_name, event_type, location, duration, price, ticket_type, event_details):
        ticket = Ticket(event_name, event_type, location, duration, price, ticket_type, self.visitor_demographics,
                        event_details)  # Creating Ticket object
        ticket.print_receipt()  # Printing ticket receipt

# Defining a class for tickets
class Ticket:
    def __init__(self, event_name, event_type, location, duration, price, ticket_type, visitor_demographics,
                 event_details):
        # Constructor method
        self.event_name = event_name  # Initializing event name
        self.event_type = event_type  # Initializing event type
        self.location = location  # Initializing location
        self.duration = duration  # Initializing duration
        self.price = price  # Initializing price
        self.ticket_type = ticket_type  # Initializing ticket type
        self.visitor_demographics = visitor_demographics  # Initializing visitor demographics
        self.event_details = event_details  # Initializing event details

    # Method to calculate ticket price
    def calculate_price(self):
        if self.ticket_type == TicketType.ONLINE:  # Checking if ticket type is online
            return self.price  # Returning the price for online tickets
        else:  # If ticket type is in-person
            if self.visitor_demographics.age < 18 or self.visitor_demographics.age >= 60:  # Checking age for discounts
                id_verification = input("Please present your national ID card (15-digit ID number): ")  # Asking for ID verification
                if id_verification:  # Checking if ID verification is provided
                    return 0  # Returning free ticket price
                else:  # If no ID verification provided
                    ticket_price = self.price + (self.price * 0.05)  # Calculating ticket price with VAT
                    return ticket_price  # Returning regular ticket price
            elif 18 <= self.visitor_demographics.age < 60:  # Checking age for regular price
                student_teacher = input("Are you a student or teacher of an institute? (yes/no): ").lower()  # Asking if visitor is a student/teacher
                if student_teacher == "yes":  # If visitor is a student/teacher
                     id_verification = input("Please present your national ID card (15-digit ID number): ")  # Asking for ID verification
                    if id_verification:  # Checking if ID verification is provided
                        return 0  # Returning free ticket price
                    return 0  # Returning free ticket price
                else:  # If not a student/teacher
                    group = input("Are you part of a group? (yes/no): ").lower()  # Asking if visitor is part of a group
                    if group == "yes":  # If visitor is part of a group
                        discounted_price = self.price * 0.5  # Calculating discounted price for groups
                        ticket_price = discounted_price + (discounted_price * 0.05)  # Calculating ticket price with VAT
                        return ticket_price  # Returning discounted ticket price
                    else:  # If visitor is not part of a group
                        ticket_price = self.price + (self.price * 0.05)  # Calculating ticket price with VAT
                        return ticket_price  # Returning regular ticket price

    # Method to print ticket receipt
    def print_receipt(self):
        ticket_price = self.calculate_price()  # Calculating ticket price
        if ticket_price == 0:  # Checking if ticket is free
            print("Ticket is free.")  # Printing ticket is free
        else:  # If ticket is not free
            print(f"Ticket Price: {ticket_price} AED")  # Printing ticket price
        print("Ticket Details:")  # Printing ticket details
        print(f"Event Name: {self.event_name}")  # Printing event name
        print(f"Event Type: {self.event_type}")  # Printing event type
        print(f"Location: {self.location.value}")  # Printing event location
        print(f"Duration: {self.duration}")  # Printing event duration
        for detail in self.event_details:  # Looping through event details
            print(detail)  # Printing each event detail
        print("Visitor Demographics:")  # Printing visitor demographics
        print(f"Name: {self.visitor_demographics.name}")  # Printing visitor name
        print(f"Age: {self.visitor_demographics.age}")  # Printing visitor age
        print(f"Gender: {self.visitor_demographics.gender}")  # Printing visitor gender

# Defining a class for visitor demographics
class VisitorDemographics:
    def __init__(self, name, age, gender):  # Constructor method
        self.name = name  # Initializing visitor name
        self.age = age  # Initializing visitor age
        self.gender = gender  # Initializing visitor gender

# Defining a class for artworks
class Artwork:
    def __init__(self, title, artist, date, medium, classification, dimensions, inventory_number, location):  # Constructor method
        self.title = title  # Initializing artwork title
        self.artist = artist  # Initializing artist name
        self.date = date  # Initializing creation date
        self.medium = medium  # Initializing artwork medium
        self.classification = classification  # Initializing artwork classification
        self.dimensions = dimensions  # Initializing artwork dimensions
        self.inventory_number = inventory_number  # Initializing inventory number
        self.location = location  # Initializing artwork location

    # Method to represent artwork as a string
    def __str__(self):
        return f"Title: {self.title}\nArtist: {self.artist}\nDate: {self.date}\nMedium: {self.medium}\n" \
               f"Classification: {self.classification}\nDimensions: {self.dimensions}\n" \
               f"Inventory number: {self.inventory_number}\nLocation: {self.location.value}\n"

# Defining a class for exhibitions
class Exhibition:
    def __init__(self, name, location, duration):  # Constructor method
        self.name = name  # Initializing exhibition name
        self.location = location  # Initializing exhibition location
        self.duration = duration  # Initializing exhibition duration
        self.date = None  # Exhibition date

# Defining a class for special events
class SpecialEvent:
    def __init__(self, name, location, duration, purpose):  # Constructor method
        self.name = name  # Initializing event name
        self.location = location  # Initializing event location
        self.duration = duration  # Initializing event duration
        self.purpose = purpose  # Initializing event purpose
        self.date = None  # Event date

# Defining a class for tours
class Tour:
    def __init__(self, name, location, date, guide, group_size):  # Constructor method
        self.name = name  # Initializing tour name
        self.location = location  # Initializing tour location
        self.date = date  # Initializing tour date
        self.guide = guide  # Initializing tour guide
        self.group_size = group_size  # Initializing group size

# Defining a class for event catalog
class EventCatalog:
    def __init__(self):  # Constructor method
        self.events = []  # Initializing list to store events

    # Method to add event to the catalog
    def add_event(self, event):
        self.events.append(event)  # Appending event to the list

    # Method to display events in the catalog
    def display_events(self):
        print("Events in the Event Catalog:")  # Printing header
        for i, event in enumerate(self.events, 1):  # Looping through events with index
            if isinstance(event, Exhibition):  # Checking if event is an exhibition
                print(f"{i}. {event.name} (Exhibition) - Location: {event.location.value}, Duration: {event.duration}")
            elif isinstance(event, SpecialEvent):  # Checking if event is a special event
                print(f"{i}. {event.name} (Special Event) - Location: {event.location.value}, Duration: {event.duration}")
            elif isinstance(event, Tour):  # Checking if event is a tour
                print(f"{i}. {event.name} (Tour) - Location: {event.location.value}, Date: {event.date}, Guide: {event.guide}, Group Size: {event.group_size}")
        print()  # Printing empty line

# Defining a class for art catalog
class ArtCatalog:
    def __init__(self):  # Constructor method
        self.artworks = []  # Initializing list to store artworks

    # Method to add artwork to the catalog
    def add_artwork(self, artwork):
        self.artworks.append(artwork)  # Appending artwork to the list

    # Method to delete artwork from the catalog
    def delete_artwork(self, inventory_number):
        for artwork in self.artworks:  # Looping through artworks
            if artwork.inventory_number == inventory_number:  # Checking if inventory number matches
                self.artworks.remove(artwork)  # Removing artwork from the list
                return True  # Returning True if artwork is deleted
        return False  # Returning False if artwork is not found

    # Method to display artworks in the catalog
    def display_artworks(self):
        print("Artworks in the Art Catalog:")  # Printing header
        for artwork in self.artworks:  # Looping through artworks
            print(artwork)  # Printing each artwork
        print()  # Printing empty line

# Function to create event catalog
def open_event_catalog():
    event_catalog = EventCatalog()  # Creating EventCatalog object
    exhibition1 = Exhibition("Ancient Art Exhibition", Location.EXHIBITION_HALLS, "2 hours")  # Creating an exhibition object
    exhibition1.date = "2024-04-01"  # Setting exhibition date
    exhibition2 = Exhibition("Modern Art Exhibition", Location.EXHIBITION_HALLS, "3 hours")  # Creating another exhibition object
    exhibition2.date = "2024-04-15"  # Setting exhibition date
    special_event1 = SpecialEvent("Musical Concert", Location.OUTDOOR_SPACES, "2 hours", "Musical Performance")  # Creating a special event object
    special_event1.date = "2024-05-20"  # Setting event date
    special_event2 = SpecialEvent("Fundraising Gala", Location.OUTDOOR_SPACES, "4 hours", "Fundraising Event")  # Creating another special event object
    special_event2.date = "2024-06-10"  # Setting event date
    tour1 = Tour("Art History Tour", Location.PERMANENT_GALLERIES, "2024-04-10", "John Smith", 25)  # Creating a tour object
    tour2 = Tour("Modern Art Tour", Location.EXHIBITION_HALLS, "2024-04-25", "Emily Johnson", 30)  # Creating another tour object
    event_catalog.add_event(exhibition1)  # Adding exhibition to event catalog
    event_catalog.add_event(exhibition2)  # Adding exhibition to event catalog
    event_catalog.add_event(special_event1)  # Adding special event to event catalog
    event_catalog.add_event(special_event2)  # Adding special event to event catalog
    event_catalog.add_event(tour1)  # Adding tour to event catalog
    event_catalog.add_event(tour2)  # Adding tour to event catalog
    return event_catalog  # Returning event catalog

# Function to create art catalog
def open_art_catalog():
    art_catalog = ArtCatalog()  # Creating ArtCatalog object
    # Adding artworks to the catalog
    # Example:
    artwork1 = Artwork("Mona Lisa", "Leonardo da Vinci", "1503–1506", "Oil on poplar", "Portrait", "77 cm × 53 cm",
                       "INV12345", Location.PERMANENT_GALLERIES)  # Creating artwork object
    artwork2 = Artwork("Starry Night", "Vincent van Gogh", "1889", "Oil on canvas", "Landscape", "73.7 cm × 92.1 cm",
                       "INV67890", Location.PERMANENT_GALLERIES)  # Creating another artwork object
    art_catalog.add_artwork(artwork1)  # Adding artwork to art catalog
    art_catalog.add_artwork(artwork2)  # Adding artwork to art catalog
    return art_catalog  # Returning art catalog

# Function to manage visitor interaction
def open_visitor_management(event_catalog, art_catalog):
    ticketing_system = TicketingSystem()  # Creating TicketingSystem object
    ticket_type = int(input("Choose Ticket Type:\n1. Online\n2. In-Person\nEnter your choice (1/2): "))  # Asking for ticket type choice
    if ticket_type == 1:  # Checking if ticket type is online
        ticket_type = TicketType.ONLINE  # Setting ticket type
    elif ticket_type == 2:  # Checking if ticket type is in-person
        ticket_type = TicketType.IN_PERSON  # Setting ticket type
    else:  # If invalid choice
        print("Invalid choice. Defaulting to In-Person ticket.")  # Printing default message
        ticket_type = TicketType.IN_PERSON  # Setting default ticket type
    submit_demographics(ticketing_system, ticket_type, event_catalog, art_catalog)  # Calling function to submit visitor demographics

# Function to submit visitor demographics
def submit_demographics(ticketing_system, ticket_type, event_catalog, art_catalog):
    name = input("Enter your name: ")  # Asking for visitor name
    age = int(input("Enter your age: "))  # Asking for visitor age
    gender = input("Enter your gender: ")  # Asking for visitor gender
    ticketing_system.get_visitor_demographics(name, age, gender)  # Setting visitor demographics
    # Display available events
    event_catalog.display_events()  # Displaying events in the catalog
    event_choice = int(input("Enter the number corresponding to the event you want to attend: "))  # Asking for event choice
    # Assuming events are indexed starting from 1
    selected_event = event_catalog.events[event_choice - 1]  # Selecting event based on user choice
    event_name = selected_event.name  # Getting event name
    location = selected_event.location  # Getting event location
    duration = selected_event.duration  # Getting event duration
    date = selected_event.date  # Getting event date
    # Get the base price for the ticket
    price = 63  # Base price for adults between 18 to 60
    # Check if the selected event is a special event or an exhibition
    if isinstance(selected_event, SpecialEvent):  # Checking if selected event is a special event
        event_type = "Special Event"  # Setting event type
    elif isinstance(selected_event, Exhibition):  # Checking if selected event is an exhibition
        event_type = "Exhibition"  # Setting event type
    elif isinstance(selected_event, Tour):  # Checking if selected event is a tour
        event_type = "Tour"  # Setting event type
    # If the event type is an Exhibition, offer the regular ticket options
    if event_type == "Exhibition":  # Checking if event type is an exhibition
        # Offer options for individual or group ticket
        individual_or_group = input(
            "Are you purchasing tickets for an individual or a group? (individual/group): ").lower()  # Asking for individual or group ticket
        if individual_or_group == "individual":  # Checking if individual ticket is chosen
            ticket_type = TicketType.IN_PERSON  # Setting ticket type to in-person
        elif individual_or_group == "group":  # Checking if group ticket is chosen
            ticket_type = TicketType.IN_PERSON  # Setting ticket type to in-person
            price = price * 0.5  # Applying 50% discount for groups
        else:  # If invalid choice
            print("Invalid choice. Defaulting to individual ticket.")  # Printing default message
    # Purchase the ticket
    event_details = []  # Initializing event details
    ticketing_system.purchase_ticket(event_name, event_type, location, duration, price, ticket_type, event_details)  # Purchasing ticket
    # Display artworks catalog
    art_catalog.display_artworks()  # Displaying artworks in the catalog

# Now, let's call the function to create the catalogs
event_catalog = open_event_catalog()  # Creating event catalog
art_catalog = open_art_catalog()  # Creating art catalog
# Now, let's call the function to demonstrate the usage
open_visitor_management(event_catalog, art_catalog)
