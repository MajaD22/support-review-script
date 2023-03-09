import csv
import matplotlib.pyplot as plt
import numpy as np

colors = ["#293462", "#fff1c1", "#a64942", "#fe5f55"]
incidents = []
tickets = []
percentage = []
ticket_labels = []

# Get values from csv file
with open('incidents.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        incidents.append(row[0])
        tickets.append(row[1])


# Remove first values in lists as they are titles of columns
tickets.pop(0)
incidents.pop(0)

# Format tickets 
formated_tickets = ([int(formated_tickets) for formated_tickets in tickets])

# Calculate percentage
total_tickets = sum(formated_tickets)
for formated_ticket in formated_tickets:
    percentage.append(round(formated_ticket / total_tickets * 100, 2))

# Combine values of incidents and percentage
combined = list(zip(incidents, percentage))
for incidents,percentage in combined:
    ticket_labels.append("{} {}%".format(incidents,percentage))

# # Create Pie Chart
y = np.array(tickets)
plt.title('Incident-Related Tickets Breakdown', fontsize = 20)
pie = plt.pie(y,startangle=90, labels=tickets, colors=colors)

# Add legend
plt.legend(bbox_to_anchor=(1.2, 1), borderaxespad=0, mode="expand", labels=ticket_labels)

# Display chart
plt.show()
