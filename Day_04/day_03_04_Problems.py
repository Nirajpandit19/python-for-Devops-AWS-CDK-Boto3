import math
import os
from datetime import date
# Level 1: Functions & Scope (Reusability)
# 1. The Health Checker: Write a function check_status(service_name, port) that prints: "Checking service: [service_name] on port [port]...". 
service_name = "K8S_Python_service"
port = 64455
def check_status(service_name, port):
    print(f"Checking service: {service_name} on port {port}...")
check_status(service_name,port)

# 2. CIDR Calculator: Create a function that takes a network name and a default prefix (e.g., prefix=24). If no prefix is provided, it should use 24. 

network_name = "K8S_Network"
prefix = 24

def network(name, default_prefix):
    user_input = input(f"Enter CIDR prefix (default {default_prefix}): ")
    
    # Use user input if they typed something, otherwise use the default
    final_prefix = int(user_input) if user_input else default_prefix
    
    print(f"{name} : {final_prefix}")

network(network_name, prefix)


# 3. Global vs Local: Define a global variable ENV = "dev". Inside a function, try to print it, then create a local variable with the same name and see what happens when you call the function. 
ENV = "dev"
def scope(ENV):
    print(ENV)
    # Using this one local variable inside the function (functional scope)
    ENV = "prod" 
    print(ENV)
# Here using global variable from the global scope
print(ENV)
scope(ENV)
print(ENV)

# 4. The Returner: Write a function get_instance_id() that returns a hardcoded ID string. Assign the result of this function to a variable and print that variable.

def get_instance_id():
    instance_id = "i-205"
    return instance_id
instance_id = get_instance_id()
print(instance_id)

# Level 2: Modules & Packages (Organization)
# 5. Math for Ops: Use the built-in math module to round a float like cpu_usage = 89.6 up to the nearest integer.
cpu_usage = 89.6
print(math.ceil(cpu_usage))

# 6. OS Interaction: Import the os module and write a script to print your current working directory.
print(os.getcwd())

# 7. Custom Module: Create a file named network_utils.py with a function ping_server(ip). In a second file main.py, import that function and use it. 
# network_utils.py

def ping_server(ip):
    print(f"Pinging server {ip}")

# main.py
import network_utils

network_utils.ping_server("127.0.0.1")


# 8. Selective Import: From the datetime module, import only the date class and print today's date.
print(date.today())

# Level 3: Virtual Environments (Isolation)
# 9. The Setup: Write down the command to create a virtual environment named .venv on a Linux system.
# $ python -m venv .venv

# 10. Activation: What command do you run to activate that virtual environment so your terminal starts using it? 

# $ source .venv/bin/activate

# 11. Dependency Export: You’ve installed boto3 and requests. Write the command to save these dependencies into a requirements.txt file. 

# $ pip freeze > ./requirements.txt

# 12. The Clean Slate: How do you deactivate a virtual environment when you are done working? 
# $ deactivate

# Level 4: DevOps Logic (Functions & Packages)
# 13. The Package Checker: Write a function that takes a list of packages (e.g., ["docker", "terraform"]) and prints "Installing [package]..." for each one using a loop. 

packages =  ["docker", "terraform"]
def install_packages(packages):
    for package in packages:
        print(f"Installing {package}...")
install_packages(packages)
# 14. Resource Dictionary: Create a function create_server_config(name, role="web"). It should return a dictionary with the keys server_name and server_role. 
name = "server1"
def create_server_config(name,role):
    server_config = {
        "server_name": name,
        "server_role": role
    }
    return server_config

print(create_server_config(name,role = "web"))
# 15. Error Handling (Bonus): Research the try/except block. Write a function that tries to divide two numbers but prints a friendly error message if the second number is zero (to prevent a crash during a calculation).

num1 = 20
num2 = 2

def divide(num1,num2):
    return num1/num2
try:
    print(divide(num1,num2))
except ZeroDivisionError as e:
    # Handle a specific error
    print(f"Error caught: {e}")
except Exception:
    # Handle any other generic error
    print("Something else went wrong.")
else:
    # Runs ONLY if no error occurred
    print("Success! No errors found.")
finally:
    # Runs ALWAYS (e.g., closing a resource)
    print("Execution complete.")
