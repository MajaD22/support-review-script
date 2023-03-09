import csv
import matplotlib.pyplot as plt
import numpy as np

colors = ["#41b658", "#D83A00"]
ticket_type = []
ticket_numbers = []
percentage = []
ticket_labels = []

# Get values from csv file
file = open("comparison.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()

# Extend Ticket types and numbers and also convert to integer
ticket_type.extend([data[0][0], data[0][1]])
ticket_numbers.extend([int(float(data[1][0])), int(float(data[1][1]))])

# # Calculate percentage
total_tickets = sum(ticket_numbers)
for ticket_number in ticket_numbers:
    percentage.append(round(ticket_number / total_tickets * 100, 2))

# Combine values of ticket type (incident/regular) and percentage
combined = list(zip(ticket_type, percentage))
for ticket_type,percentage in combined:
    ticket_labels.append("{} {}%".format(ticket_type,percentage))

# # Create Pie Chart
y = np.array(ticket_numbers)
plt.title('Regular Tickets vs. Incident-Related Tickets', fontsize = 20)
pie = plt.pie(y,startangle=90, labels=ticket_numbers, colors=colors)

# Add legend
plt.legend(bbox_to_anchor=(1.2, 1), borderaxespad=0, mode="expand", labels=ticket_labels)

# Display chart
plt.show()
