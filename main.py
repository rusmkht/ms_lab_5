import random

# Function to generate random network traffic type
def generate_traffic_type():
    traffic_types = ['normal', 'suspicious', 'highly suspicious']
    return random.choice(traffic_types)

# Function to detect intrusion based on network traffic type
def detect_intrusion(traffic):
    if traffic == 'suspicious':
        return "Suspicious activity detected!"
    elif traffic == 'highly suspicious':
        return "Highly suspicious activity detected!"
    else:
        return "No suspicious activity was detected."

# Function to report the result of intrusion detection
def report_detection_result(intrusion_detected):
    print(intrusion_detected)

# Main function to run the simulation
def simulate_network_intrusion():
    for i in range(10):
        traffic = generate_traffic_type()
        intrusion = detect_intrusion(traffic)
        report_detection_result(intrusion)

# Check if the script is being run directly
if __name__ == '__main__':
    simulate_network_intrusion()
