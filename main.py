class CarFinder:
   def __init__(self):
       self.allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
   def print_allowed_vehicles(self):
       print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
       for vehicle in self.allowed_vehicles:
           print(vehicle)
   def display_menu(self):
       print("\n ******" \
       "AutoCountry Vehicle Finder v0.1" \
       "******")
       print("1. PRINT all Authorized Vehicles")
       print("2. SEARCH for Authorized Vehicle")
       print("3. ADD Authorized Vehicle")
       print("4. Exit")
   def run(self):
       while True:
           self.display_menu()
           choice = input("Please Enter the following number below from the following menu: ")
           if choice == '1':
               self.print_allowed_vehicles()
           elif choice == '2':
               search_vehicle = input("Please Enter the full Vehicle name: ")
               if search_vehicle in self.allowed_vehicles:
                print(f"{search_vehicle} is an authorized vehicle")
               else:
                print(f"{search_vehicle} is not an authorized vehicle, if you received this in error please check the spelling and try again")
                print("********************************")
           elif choice == '3':
                new_vehicle = input("Please Enter the full Vehicle name you would like to add:")
                self.allowed_vehicles.append(new_vehicle)
                print(f'You have added "{new_vehicle}" as an authorized vehicle')
                print("********************************")
           elif choice == '4':
                print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
                break
           else:
                print("Invalid input. Please enter 1, 2, or 3.") 

if __name__ == "__main__":
   car_finder = CarFinder()
   car_finder.run()