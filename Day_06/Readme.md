# Introduction to Operators in Python

Operators in Python are special symbols or keywords that are used to perform operations on variables and values. Python supports a wide range of operators, categorized into several types. These operators allow you to perform tasks such as arithmetic calculations, assign values to variables, compare values, perform logical operations, and more.

Here are the main types of operators in Python:

1. **Arithmetic Operators:** These operators are used for performing basic mathematical operations such as addition, subtraction, multiplication, division, and more.

2. **Assignment Operators:** Assignment operators are used to assign values to variables. They include the equal sign (=) and various compound assignment operators.

3. **Relational Operators:** Relational operators are used to compare values and determine the relationship between them. They return a Boolean result (True or False).

4. **Logical Operators:** Logical operators are used to combine and manipulate Boolean values. They include "and," "or," and "not."

5. **Identity Operators:** Identity operators are used to check if two variables point to the same object in memory. The identity operators in Python are "is" and "is not."

6. **Membership Operators:** Membership operators are used to check if a value is present in a sequence or collection, such as a list, tuple, or string. The membership operators in Python are "in" and "not in."

7. **Bitwise Operators:** Bitwise operators are used to perform operations on individual bits of binary numbers. They include bitwise AND, OR, XOR, and more.

8. **Precedence of Operations:** Operators in Python have different levels of precedence, which determine the order in which operations are performed in an expression.


🛠️ Your Next Lab: The "Logic & Automation" Challenge (15 Problems)
Level 1: Conditionals (The Decision Maker)
Access Control: Write a script that checks if a user_role is "admin". If yes, print "Full Access"; if "editor", print "Limited Access"; otherwise, print "Access Denied".

Server Status: Given status = "active", use an if statement to print "Server is healthy" only if the status is exactly "active".

Port Checker: Write a script that checks if port = 443. If it is, print "Secure connection". If it's 80, print "Insecure connection".

Disk Alert: Create a variable disk_usage = 85. Print "CRITICAL" if usage is above 90, "WARNING" if above 70, and "OK" otherwise.

Level 2: Logical & Membership Operators
Environment Security: Check if env == "prod" AND maintenance == False. If both are true, print "Deployment Allowed".

Multi-Region Check: If a region is either "us-east-1" OR "us-west-2", print "Standard Region".

Blacklist Filter: You have a list blacklisted_ips = ["1.1.1.1", "2.2.2.2"]. Write a script that checks if user_ip = "1.1.1.1" is in that list and prints an alert.

Tag Validator: Check if the key "CostCenter" is NOT in a dictionary of resource tags.

Level 3: Loops (The Automator)
S3 Bucket List: Use a for loop to iterate through buckets = ["logs", "assets", "backups"] and print "Syncing bucket: [name]...".

Countdown: Use a for loop and range() to print a countdown from 5 to 1 before a "deployment" starts.

Filtering: Given a list of numbers [22, 80, 443, 8080], use a loop to print only the ports greater than 100.

The While Wait: Create a variable attempts = 0. Use a while loop to print "Retrying connection..." until attempts reaches 3.

Level 4: Complex Automation Logic
Nested Logic: Loop through a list of servers (dictionaries). For each server, if it is "prod", print its ID and "High Priority".

User Input Loop: Write a while loop that keeps asking the user for a "Service Name" and appends it to a list. The loop should stop only when the user types "exit".

Break/Continue: Loop through numbers 1 to 10. Use continue to skip the number 5 and break to stop the loop entirely when it hits 8.