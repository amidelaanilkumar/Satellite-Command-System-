import logging

# Set up logging with both console and file handlers
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('satellite_log.txt'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Sample user credentials
valid_users = {'admin': 'password123'}

class Command:
    def execute(self, satellite):
        raise NotImplementedError("Subclasses must implement the execute method.")

class RotateCommand(Command):
    def __init__(self, direction):
        self.direction = direction

    def execute(self, satellite):
        valid_directions = ["North", "South", "East", "West"]
        if self.direction in valid_directions:
            satellite.orientation = self.direction
            logger.info(f"Orientation set to {self.direction}.")
        else:
            logger.warning(f"Invalid direction '{self.direction}'. Orientation not changed.")

class ActivatePanelsCommand(Command):
    def execute(self, satellite):
        if satellite.solar_panels_status == "Inactive":
            satellite.solar_panels_status = "Active"
            logger.info("Solar panels activated.")
        else:
            logger.warning("Solar panels are already active.")

class DeactivatePanelsCommand(Command):
    def execute(self, satellite):
        if satellite.solar_panels_status == "Active":
            satellite.solar_panels_status = "Inactive"
            logger.info("Solar panels deactivated.")
        else:
            logger.warning("Solar panels are already inactive.")

class CollectDataCommand(Command):
    def execute(self, satellite):
        if satellite.solar_panels_status == "Active":
            satellite.data_collected += 10
            logger.info("Data collected.")
        else:
            logger.warning("Data collection failed. Solar panels are inactive.")

class Satellite:
    def __init__(self):
        self.orientation = "North"
        self.solar_panels_status = "Inactive"
        self.data_collected = 0

    def execute_command(self, command):
        try:
            command.execute(self)
        except Exception as e:
            logger.error(f"Error executing command: {str(e)}")

def authenticate_user():
    while True:
        username = input("Enter your username: ").strip().lower()
        password = input("Enter your password: ").strip()

        if username in valid_users and valid_users[username] == password:
            logger.info(f"Authentication successful for user '{username}'.")
            return True
        else:
            logger.warning("Authentication failed. Invalid username or password. Try again.")

def execute_commands_from_input(satellite):
    # Authenticate the user before allowing commands
    if not authenticate_user():
        return

    while True:
        user_input = input("Enter a command:\nrotate\nactivatepanels\ndeactivatepanels\ncollectdata\n(or 'exit' to quit): ").strip().lower()


        if user_input == 'exit':
            break

        try:
            if user_input == 'rotate':
                direction = input("Enter rotation direction (North/South/East/West): ").strip()
                command = RotateCommand(direction)
            elif user_input == 'activatepanels':
                command = ActivatePanelsCommand()
            elif user_input == 'deactivatepanels':
                command = DeactivatePanelsCommand()
            elif user_input == 'collectdata':
                command = CollectDataCommand()
            else:
                logger.warning(f"Invalid command '{user_input}'. Try again.")
                continue

            satellite.execute_command(command)

            # Display current state after each command
            logger.info("\nCurrent Satellite State:")
            logger.info(f"Orientation: {satellite.orientation}")
            logger.info(f"Solar Panels: {satellite.solar_panels_status}")
            logger.info(f"Data Collected: {satellite.data_collected}")

        except KeyboardInterrupt:
            logger.warning("User interrupted. Exiting...")
            break
        except Exception as e:
            logger.error(f"An unexpected error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    satellite = Satellite()

    
    execute_commands_from_input(satellite)# Execute commands from authenticated user input
