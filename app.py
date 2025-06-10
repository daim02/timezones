from flask import Flask, render_template
import datetime
import pytz

# Initialize the Flask application
app = Flask(__name__)

# Define the timezones you want to display on the website
WORLD_TIMEZONES = {
    "Americas": [
        ("Pacific", "US/Pacific"),
        ("Mountain", "US/Mountain"),
        ("Central", "US/Central"),
        ("Eastern", "US/Eastern"),
    ],
    "Europe & Africa": [
        ("London", "Europe/London"),
        ("Paris", "Europe/Paris"),
        ("Johannesburg", "Africa/Johannesburg"),
    ],
    "Asia & Oceania": [
        ("Dubai", "Asia/Dubai"),
        ("India", "Asia/Kolkata"),
        ("Tokyo", "Asia/Tokyo"),
        ("Sydney", "Australia/Sydney"),
    ]
}

@app.route("/")
def index():
    """This function runs when a user visits the main page."""
    # Get the current universal time (UTC)
    now_utc = datetime.datetime.now(pytz.utc)
    
    # Create a dictionary to hold the formatted times
    world_times = {}
    for region, zones in WORLD_TIMEZONES.items():
        region_times = []
        for name, tz_id in zones:
            # Convert UTC time to the local time for that zone
            local_time = now_utc.astimezone(pytz.timezone(tz_id))
            # UPDATED: Placed %Z in brackets to format the timezone abbreviation
            formatted_time = local_time.strftime("%I:%M %p (%Z)")
            region_times.append((name, formatted_time))
        world_times[region] = region_times
            
    # Render the HTML page and send the world_times data to it
    return render_template('index.html', world_times=world_times)

# This allows you to run the app directly
if __name__ == "__main__":
    app.run(debug=True)
