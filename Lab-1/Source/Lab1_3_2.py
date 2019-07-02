#Airline reservation system
#5 classes
#Flight, Person, Flights, Passenger, Pilot

#Person class for including Passenger, Flight booking agent, Piolot
class Person():      # class

    def __init__(self, name, flight): # method to map person and flight
        self.name = name #Usage of self
        self.flight = flight

    def __perdetails(self):        # private method to display person details
        print("Name of the Agent: %s" % self.name)
        print("Name of the Flight is: %s" % self.flight)


class Flights():     # class to display flights in the airport

    def __init__(self):      # methods
        self.upcomingflights = 90
        self.departedflights = 70
        self.arrivingflights = 70

    def airlinedetails(self):
        print("Total number of flights available are: %s" % self.upcomingflights)
        print("Total count of flights departed are: %s" % self.departedflights)
        print("Total count of flights arrived are: %s" % self.arrivingflights)


class Passenger():   # class

    def __init__(self, name, passport):   #methods
        self.name = name
        self.passport = passport

    def passengerdetails(self):
        print("Name of the passenger: %s" % self.name)
        print("Passport Number: %d" % self.passport)

#Multiple Inheritance - Creation of Pilot to inherit both Person and Passenger
class Pilot(Person, Passenger):   #class

    def __init__(self, name, salary):   #methods
        self.name = name
        self.salary = salary

    def flightdetails(self):
        print("Pilot name:", self.name)
        print("Salary of pilot:", self.salary)

class Flight(Pilot):           # class which relates Pilot class to Flight
    def __init__(self, airportname, flightnumber):
        self.airportname = airportname
        self.flightnumber = flightnumber

    def pr(self):                  # method
        print(self.name)
        #Super class constructor calling
        super.__init__("Vidyu","$80000")

# object creations and calling

person =Person("Vidyu Kaza","Air India")
#Private method call to display person details
person._Person__perdetails()

#Methods to display passenger details
passenger=Passenger("Vignan Bala",8162860165)
passenger.passengerdetails()

#Pilot details
pilot = Pilot("Latha,",8000)
pilot.flightdetails()

#Airport details
airport = Flight("Rajiv Gandhi International Airport", 230)
print("Name of the airport is: %s" % airport.airportname)
print("Total number of flights for departure and arrival in airport is : %d" % airport.flightnumber)