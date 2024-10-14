from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

# Global variables to track the battery state
battery_level = 100  # Start with a full battery
charging = False  # Flag to indicate if the robot is charging
last_update_time = time.time()  # Timestamp of the last update

@app.route('/robot/data', methods=['GET'])
def get_robot_data():
    global battery_level, charging, last_update_time

    # Time since the last update
    current_time = time.time()
    time_since_update = current_time - last_update_time

    # Update battery level based on time since the last update
    if charging:
        battery_level += 2 * time_since_update  # Charge at a rate of 2% per second
    else:
        battery_level -= 1 * time_since_update  # Discharge at a rate of 1% per second

    # Ensure battery level stays within bounds
    battery_level = max(0, min(battery_level, 100))

    # Determine if the robot should charge (if battery is below a threshold)
    if battery_level < 20 and not charging:
        charging = True  # Start charging if battery drops below 20%
    elif battery_level >= 100:
        charging = False  # Stop charging if battery is full

    # Update last update time
    last_update_time = current_time

    # Set load weight to zero when charging
    if charging:
        load_weight = 0  # No load while charging
    else:
        load_weight = random.uniform(0, 50)  # Random load weight in kg while discharging

    # Generate random sensor data
    robot_data = {
        'robot_id': 'robot_001',
        'position': {
            'x': random.uniform(0, 100),  # Random x coordinate
            'y': random.uniform(0, 100),  # Random y coordinate
            'z': random.uniform(0, 10)     # Random height
        },
        'battery_level': battery_level,  # Current battery level
        'status': 'charging' if charging else random.choice(['moving', 'idle']),  # Charging or random status
        'load_weight': load_weight,  # Load weight (0 when charging)
        'timestamp': current_time  # Current time in seconds since the epoch
    }
    
    return jsonify(robot_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
