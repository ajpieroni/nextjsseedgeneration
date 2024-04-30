# /opt/homebrew/bin/python3.11 "/Users/alexpieroni/Documents/Documents - Alex’s MacBook /Projects/next_seed_generation/main.py"


import pandas as pd

csv_path = '/Users/alexpieroni/Documents/Documents - Alex’s MacBook /Projects/next_seed_generation/Eventbrite Report Apr 01 (4).csv'  # Adjust the path to your actual CSV file
data = pd.read_csv(csv_path)

# Create events from the CSV data, or whatever your csv structure is
# My headers are 'Event Name', 'Check-In Date', 'Attendee Status'   
events = [
    {
        'event_name': row['Event Name'],
        'check_in_date': row['Check-In Date'] if pd.notna(row['Check-In Date']) else 'TBA',
        'attendee_status': row['Attendee Status']
    }
    for index, row in data.iterrows()
]

js_content = f"""const events = {events};

module.exports = {{
  events
}};
"""

# write to a JavaScript
with open('./seed.js', 'w') as file:  # Adjust the path where you want to save the JS file
    file.write(js_content)
