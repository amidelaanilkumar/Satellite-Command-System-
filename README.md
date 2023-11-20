# Satellite-Command-System

The provided Python code implements a simple Satellite Command System simulation with user authentication. The system allows users to interactively input commands, controlling the orientation, solar panel status, and data collection of a simulated satellite.

Key Components:

1. **Command Hierarchy:**
   - Abstract `Command` class defines the structure for command execution.
   - Concrete command classes (`RotateCommand`, `ActivatePanelsCommand`, `DeactivatePanelsCommand`, `CollectDataCommand`) implement specific functionalities.

2. **Satellite Class:**
   - Represents the satellite state with attributes for orientation, solar panel status, and data collected.
   - Executes commands on the satellite and handles exceptions.

3. **User Authentication:**
   - Before accepting commands, the system prompts the user for a username and password.
   - Sample user credentials (`valid_users` dictionary) are used for authentication.

4. **Command Execution Loop:**
   - The system continuously prompts the user for commands until 'exit' is entered.
   - Commands are executed based on user input, and the satellite's state is displayed after each command.

5. **Logging:**
   - Logging is configured to record messages in both a file (`satellite_log.txt`) and the console.
   - Log messages include timestamps, log levels, and descriptive information.

6. **Exception Handling:**
   - Exceptions during command execution or authentication are caught and logged with appropriate error messages.

Usage:
- Run the script.
- Enter a valid username and password for authentication.
  Sample user credentials:
  username='admin'
  password='password123'
- Input commands such as 'rotate', 'activatepanels', 'deactivatepanels', 'collectdata', or 'exit' to control the simulated satellite.

