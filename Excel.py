import random
import time
import openpyxl
from openpyxl import Workbook

# Simulated Galileo Board Data (Replace this with actual data retrieval code)
def read_galileo_data():
    # Simulating data, replace with actual data retrieval logic
    temperature = random.uniform(20, 30)
    humidity = random.uniform(40, 60)
    return temperature, humidity

# Create a new Excel workbook and add a sheet
workbook = Workbook()
sheet = workbook.active
sheet.title = 'GalileoData'

# Add headers to the sheet
headers = ['Timestamp', 'Temperature (Celsius)', 'Humidity (%)']
sheet.append(headers)

# Record data in Excel every 5 seconds for demonstration (adjust as needed)
for _ in range(5):
    # Get Galileo board data
    temperature, humidity = read_galileo_data()

    # Record data in Excel
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    sheet.append([timestamp, temperature, humidity])

    # Sleep for 5 seconds before the next iteration
    time.sleep(5)

# Save the workbook to a file
workbook.save('galileo_data.xlsx')
