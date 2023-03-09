The purpose of this script is to generate pie chart for Heroku Support Review.

## Required:
- Python 3.10.7
- pip 22.2.2
- matplotlib (can be installed with pip: `pip install matplotlib`)

## How to:
###### Create The Top 5 Ticket Components Visualisation
- Go to dataclip: https://data.heroku.com/dataclips/ixjnkhpllerynncwjhfjvotceini
- Change the dates and save/run dataclip
- Export csv and re-name it to: `review.csv` - script specificlly looks for file with this name
- Add `review.csv` file to the root folder of script
- Run the script: `python3 main.py`

###### Create The Incident-Related Tickets Breakdown Visualisation
- Go to dataclip: https://data.heroku.com/dataclips/lfhkcolvnwmuqscmpaojxbqvkssh
- Change the dates and save/run dataclip
- Export csv and re-name it to: `incidents.csv`
- Add `incidents.csv` file to the root folder of script
- Run the script: `python3 incidents.py`

###### Create The Regular Tickets vs. Incident-Related Tickets Visualisation

- Go to dataclip: https://data.heroku.com/dataclips/olyzoxhoxvouazjcubbchywnhggo
- Change the dates and save/run dataclip
- Export csv and re-name it to: `comparison.csv`
- Add `comparison.csv` file to the root folder of script
- Run the script `python3 comparison.py`

## Preview:

![Screenshot 2023-02-03 at 11 34 52](https://user-images.githubusercontent.com/98904780/216593628-1498ca8a-3665-4b92-8903-51b72aff5a8a.png)

![Screenshot 2023-02-03 at 11 33 37](https://user-images.githubusercontent.com/98904780/216593462-7196c1f0-782b-42c7-bf1a-937a87dc5697.png)

![Screenshot 2023-02-03 at 11 33 48](https://user-images.githubusercontent.com/98904780/216593468-04ee3d8f-4177-43dd-8644-ba103f10be42.png)
