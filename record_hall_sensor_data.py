import time
from datetime import datetime
import random

# Function to simulate reading data from the Hall sensor
def read_hall_sensor_data():
    # Simulated data, replace this with your actual data retrieval logic
    return random.uniform(0, 1023)

# Create a text file for recording data
file_path = 'hall_sensor_data.txt'

try:
    with open(file_path, 'w') as file:
        while True:
            # Simulate reading data from the Hall sensor
            hall_sensor_data2 = read_hall_sensor_data()

            # Get the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # Write data to the file
            data_line = f'{timestamp}, {hall_sensor_data2}\n'
            file.write(data_line)

            # Wait for some time before the next iteration (adjust as needed)
            time.sleep(1)

except KeyboardInterrupt:
    print("Recording stopped by user. Data saved to 'hall_sensor_data.txt'.")
