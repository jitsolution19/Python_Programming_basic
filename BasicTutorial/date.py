from datetime import datetime

# Get the current datetime
current_datetime = datetime.now()

# Format the datetime as a string without microseconds
formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

print(datetime.now().strftimestrftime('%Y-%m-%d %H:%M:%S'))