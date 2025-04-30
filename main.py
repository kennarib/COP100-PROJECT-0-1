import os

# File path for the Allowed Vehicles list
FILE_PATH = "allowed_vehicles.txt"

def load_vehicles():
    """Load vehicles from the file into a list."""
    if not os.path.exists(FILE_PATH):
        # Create the file with default vehicles if it doesn't exist
        with open(FILE_PATH, "w") as file:
            file.write("\n".join([
                'Ford F-150',
                'Chevrolet Silverado',
                'Tesla CyberTruck',
                'Toyota Tundra',
                'Rivian R1T',
                'Ram 1500'
            ]))
    with open(FILE_PATH, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_vehicles(vehicles):
    """Save the list of vehicles back to the file."""
    with open(FILE_PATH, "w") as file:
        file.write("\n".join(vehicles))
                   
class CarFinder:
   def __init__(self):
       self.allowed_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500']
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
       print("4. DELETE Authorized Vehicle")
       print("5. Exit")
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
               delete_vehicle = input("Please Enter the full Vehicle name you would like to REMOVE: ")
               if delete_vehicle in self.allowed_vehicles:
                  confirm = input(f'Are you sure you want to remove "{delete_vehicle}" from the Authorized Vehicles List? (yes/no): ')
                  if confirm.lower() == 'yes':
                    self.allowed_vehicles.remove(delete_vehicle)
                    print(f'You have REMOVED "{delete_vehicle}" as an authorized vehicle')
                  else:
                    print(f'"{delete_vehicle}" was not removed from the Authorized Vehicles List')
               else:
                print(f"{delete_vehicle} is not in the Authorized Vehicles List")
               print("********************************")
           elif choice == '5':
                print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
                break
           else:
                print("Invalid input. Please enter a number between 1 and 5") 

if __name__ == "__main__":
   car_finder = CarFinder()
   car_finder.run()