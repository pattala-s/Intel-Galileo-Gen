import time
from datetime import datetime
#import <your_galileo_library>  # Import the library for your Galileo board
#import <your_metal_sensor_library>  # Import the library for your metal sensor

# Function to read data from the metal sensor
def read_metal_sensor():
    # Replace this with the actual logic to read data from your metal sensor
    # It might involve initializing the sensor and reading its values
    return 0  # Replace 0 with the actual reading

# Create a text file for recording data
file_path = 'metal_sensor_data.txt'

try:
    with open(file_path, 'w') as file:
        while True:
            # Read data from the metal sensor
            metal_sensor_data = read_metal_sensor()

            # Get the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Write data to the file
            data_line = f'{timestamp}, {metal_sensor_data}\n'
            file.write(data_line)

            # Wait for some time before the next iteration (adjust as needed)
            time.sleep(1)

except KeyboardInterrupt:
    print("Recording stopped by user. Data saved to 'metal_sensor_data.txt'.")
