import requests
import

# Get data from the URL, with the specific codes associated to the Portuguese party and election
url = "https://manifesto-project.wzb.eu/api/v1/texts_and_annotations?api_key=258634ad17dbfac09eb812c3f8ec10cf&keys[]=35110_201106&keys[]=35211_201106&keys[]=35220_201106&keys[]=35311_201106&keys[]=35313_201106&keys[]=35520_201106&version=2023-1"

# Fetch data from the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse JSON data
    data = response.json()

    # Save the data to a local JSON file
    with open("manifesto_portugal_data.json", "w", encoding="utf-8") as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)

    print("Data saved to manifesto_data.json")

else:
    print("Failed to retrieve data from the URL.")
