import requests
from bs4 import BeautifulSoup
import re

def fetch_medal_data():
    url = 'https://www.bbc.co.uk/sport/olympics/paris-2024/medals'
    print("Fetching data...")

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        print("Data fetched successfully.")
        soup = BeautifulSoup(response.text, 'html.parser')
        print("Parsing data...")

        # Locate the table in the page's HTML
        table = soup.find('table')  # Adjust if necessary
        countries = []

        if table:
            rows = table.find('tbody').find_all('tr')  # Ensure you're getting the correct rows
            for row in rows:
                columns = row.find_all('td')
                if len(columns) >= 4:  # Ensure there are enough columns to parse
                    country_name = columns[1].get_text(strip=True)

                    # Remove the abbreviation by finding the first lowercase letter
                    match = re.search(r'[A-Z]+(?=[A-Z][a-z])', country_name)
                    if match:
                        country_name = country_name[match.end():].strip()

                    # Extract and clean medal counts
                    gold_text = columns[2].get_text(strip=True)
                    silver_text = columns[3].get_text(strip=True)
                    bronze_text = columns[4].get_text(strip=True)

                    gold = int(''.join(filter(str.isdigit, gold_text)))
                    silver = int(''.join(filter(str.isdigit, silver_text)))
                    bronze = int(''.join(filter(str.isdigit, bronze_text)))

                    # Calculate total score
                    total_score = gold * 3 + silver * 2 + bronze
                    countries.append((country_name, gold, silver, bronze, total_score))

            # Sort countries by total score
            countries.sort(key=lambda x: x[4], reverse=True)

            # Generate HTML content
            html_content = """
            <html>
            <head>
                <title>Olympic Medal Standings</title>
                <style>
                    table {
                        width: 50%;
                        border-collapse: collapse;
                        margin: 25px 0;
                        font-size: 1em;
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        min-width: 400px;
                        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
                    }
                    thead tr {
                        background-color: #009879;
                        color: #ffffff;
                        text-align: left;
                        font-weight: bold;
                    }
                    th, td {
                        padding: 12px 15px;
                        border: 1px solid #dddddd;
                    }
                    tbody tr {
                        border-bottom: 1px solid #dddddd;
                    }
                    tbody tr:nth-of-type(even) {
                        background-color: #f3f3f3;
                    }
                    tbody tr:last-of-type {
                        border-bottom: 2px solid #009879;
                    }
                </style>
            </head>
            <body>
                <h1>Olympic Medal Standings</h1>
                <table>
                    <thead>
                        <tr>
                            <th>Country</th>
                            <th>Gold</th>
                            <th>Silver</th>
                            <th>Bronze</th>
                            <th>Total Score</th>
                        </tr>
                    </thead>
                    <tbody>
            """

            for country in countries:
                html_content += f"""
                <tr>
                    <td>{country[0]}</td>
                    <td>{country[1]}</td>
                    <td>{country[2]}</td>
                    <td>{country[3]}</td>
                    <td>{country[4]}</td>
                </tr>
                """

            html_content += """
                    </tbody>
                </table>
            </body>
            </html>
            """

            # Write to an HTML file
            with open('medal_standings.html', 'w', encoding='utf-8') as file:
                file.write(html_content)

            print("HTML file 'medal_standings.html' generated successfully.")

        print("Data parsing complete.")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    fetch_medal_data()
