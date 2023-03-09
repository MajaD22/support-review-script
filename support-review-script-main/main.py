import csv
import matplotlib.pyplot as plt
import numpy as np

colors = ["#00A3E0", "#772583", "#AC145A", "#396547", "#41b658", "#FCC003", "#FE9339", "#D83A00", "#9be198"]
components = []
tickets = []
percentage = []
ticket_labels = []

# Get values from csv file
with open('review.csv') as csvfile:
    csvReader = csv.reader(csvfile, delimiter=',')
    for row in csvReader:
        components.append(row[0])
        tickets.append(row[1])


# Remove first values in lists as they are titles of columns
tickets.pop(0)
components.pop(0)

# Format tickets 
formated_tickets = ([int(formated_tickets) for formated_tickets in tickets])

# Calculate percentage
total_tickets = sum(formated_tickets)
for formated_ticket in formated_tickets:
    percentage.append(round(formated_ticket / total_tickets * 100, 2))

# Combine values of components and percentage
combined = list(zip(components, percentage))
for component,percentage in combined:
    ticket_labels.append("{} {}%".format(component,percentage))

# # Create Pie Chart
y = np.array(tickets)
plt.title('Top 5 Ticket Components', fontsize = 20)
pie = plt.pie(y,startangle=90, labels=None, colors=colors, wedgeprops = { 'linewidth' : 0.2, 'edgecolor' : 'white' })

# Add legend
plt.legend(bbox_to_anchor=(1.2, 1), borderaxespad=0, mode="expand", labels=ticket_labels)

# Display chart
plt.show()
