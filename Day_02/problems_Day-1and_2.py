import time
# 🛠️ Day 2: DevOps Python Lab (10 Problems)
# Level 1: String & Variable Manipulation
# 1. The Log Formatter: You have a variable log_level = "error" and message = "database connection failed". Print a single string that looks like this: [ERROR]: DATABASE CONNECTION FAILED. (Hint: Use string methods like .upper()).

log_level = "error"
message = "database connection failed"

print(f"[{log_level.upper()}]: {message.upper()}")

# 2. The URL Builder: Define three variables: protocol = "https", server = "api.aws.com", and endpoint = "v1/clusters". Join them together to create a full URL: https://api.aws.com/v1/clusters.

protocol = "https"
server = "api.aws.com"
endpoint = "v1/clusters"

print(f"{protocol}://{server}/{endpoint}")

# 3. Version Extractor: You have a string from a command output: version_info = "python-3.10.12-final". Use string slicing or splitting to extract only the version number 3.10.12.

version_info = "python-3.10.12-final"
print(version_info.split("-")[1])


# Level 2: Working with Lists (The Inventory)
# 4. Package Manager: Create a list called required_packages containing "vim", "curl", and "git".
required_packages = ["vim", "curl", "git"]

# Add "docker" to the list.
required_packages.append("Docker")

# Remove "vim".
required_packages.remove("vim")

# Print the final list.
print(required_packages)

# 5. Instance Search: Given a list instance_ids = ["i-123", "i-456", "i-789", "i-101"], print the total number of instances in the list and the ID of the very first instance.
instance_ids = ["i-123", "i-456", "i-789", "i-101"]
print(f"Total instances are {len(instance_ids)}")
print(f"The very first instance's id is {instance_ids[0]}")

# 6. Deployment Check: You have two lists: current_pods = ["nginx", "redis"] and new_pods = ["db", "api"]. Create a single list called all_pods that combines them both.
current_pods = ["nginx", "redis"]
new_pods = ["db", "api"]
all_pods = [*new_pods, *current_pods]
print(all_pods)


# Level 3: Dictionaries (Metadata Management)
# 7. Server Specs: Create a dictionary called server with the following keys: hostname, ip, and cpu_cores. Assign them any values. Then, print only the ip address from that dictionary.

server_dict = {
    "hostname": "k8sCluster",
    "ip": "127.0.0.2",
    "cpu_cores": 8,
}
print(server_dict["ip"])

# 8. Update Status: You have a service dictionary: service = {"name": "app-server", "status": "active"}. Change the status to "restarting" and add a new key called last_updated with today's date.
service = {"name": "app-server", "status": "active"}
service["status"] = "restarting"
service["last_updated"] = time.strftime("%Y-%m-%d %H:%M:%S")
print(service)

# 9. Cloud Billing: Create a dictionary where keys are AWS regions (e.g., "us-east-1") and values are the hourly cost (e.g., 0.02). Write a line of code that calculates the cost for 24 hours in a specific region of your choice.
billing = {
    "us-east-1": 0.02,
    "ap-south-1": 0.12,
}
region = input("what is your region in format us-east-2: ")
for reg in billing.keys():
    if reg == region:
        bill = billing[region] *24 
        print(f"bill for {region} for 24 hours is ${bill}")

# Level 4: The "DevOps Logic" Challenge
# 10. The Health Checker: You have a list of dictionaries representing microservices:

# Python
services = [
    {"name": "auth", "status": "up"},
    {"name": "gateway", "status": "down"},
    {"name": "payments", "status": "up"}
]
# Task: Access the second service in the list (the gateway) and print: "Alert: gateway is down!" by accessing the values within the dictionary.

for serv in services:
    if serv["status"] == "down":
        print(f"Alert: {serv["name"]} is down!")

