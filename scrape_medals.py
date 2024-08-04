import requests
from bs4 import BeautifulSoup
import re

def fetch_medal_data():
    print("Fetching data...")
    url = "https://www.bbc.co.uk/sport/olympics/paris-2024/medals"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        html = response.content
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

    print("Data fetched successfully.")
    print("Parsing data...")

    soup = BeautifulSoup(html, 'html.parser')
    
    # Update this line with the correct class or ID
    table = soup.find('table', {'class':'ssrcss-jsg8ev-TableWrapper e1xoxfm62'})

    if table is None:
        print("Error: Could not find the table with the correct class.")
        return

    rows = table.find_all('tr')
    countries = []

    for row in rows[1:]:  # Skip the header row
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

    print("Data parsed successfully.")
    print("Generating HTML...")

    # Sort countries by total score
    countries.sort(key=lambda x: x[4], reverse=True)

    # Handle tied rankings
    ranked_countries = []
    current_rank = 1
    previous_score = None
    for index, (country_name, gold, silver, bronze, total_score) in enumerate(countries):
        if total_score != previous_score:
            rank_to_use = current_rank
        else:
            rank_to_use = previous_rank
        
        ranked_countries.append((rank_to_use, country_name, gold, silver, bronze, total_score))
        previous_score = total_score
        previous_rank = rank_to_use
        current_rank += 1

 # Mapping of country names to ISO 3166-1 alpha-2 country codes
    country_codes = {

    "united states": "us",
    "china": "cn",
    "japan": "jp",
    "germany": "de",
    "france": "fr",
    "south africa": "za",
    "hong kong": "hk",
    "great britain": "gb",
    "italy": "it",
    "spain": "es",
    "canada": "ca",
    "brazil": "br",
    "australia": "au",
    "india": "in",
    "south korea": "kr",
    "russia": "ru",
    "netherlands": "nl",
    "sweden": "se",
    "norway": "no",
    "denmark": "dk",
    "finland": "fi",
    "switzerland": "ch",
    "belgium": "be",
    "poland": "pl",
    "mexico": "mx",
    "new zealand": "nz",
    "portugal": "pt",
    "argentina": "ar",
    "colombia": "co",
    "greece": "gr",
    "turkey": "tr",
    "saudi arabia": "sa",
    "united arab emirates": "ae",
    "singapore": "sg",
    "malaysia": "my",
    "thailand": "th",
    "vietnam": "vn",
    "pakistan": "pk",
    "bangladesh": "bd",
    "iran": "ir",
    "israel": "il",
    "austria": "at",
    "czech republic": "cz",
    "slovakia": "sk",
    "hungary": "hu",
    "romania": "ro",
    "bulgaria": "bg",
    "ukraine": "ua",
    "serbia": "rs",
    "croatia": "hr",
    "slovenia": "si",
    "estonia": "ee",
    "latvia": "lv",
    "lithuania": "lt",
    "cyprus": "cy",
    "malta": "mt",
    "liechtenstein": "li",
    "andorra": "ad",
    "monaco": "mc",
    "san marino": "sm",
    "luxembourg": "lu",
    "moldova": "md",
    "georgia": "ge",
    "armenia": "am",
    "azerbaijan": "az",
    "qatar": "qa",
    "kuwait": "kw",
    "oman": "om",
    "bahrain": "bh",
    "yemen": "ye",
    "afghanistan": "af",
    "nepal": "np",
    "sri lanka": "lk",
    "malawi": "mw",
    "zambia": "zm",
    "zimbabwe": "zw",
    "uganda": "ug",
    "ethiopia": "et",
    "kenya": "ke",
    "tanzania": "tz",
    "namibia": "na",
    "botswana": "bw",
    "eswatini": "sz",
    "lesotho": "ls",
    "central african republic": "cf",
    "ivory coast": "ci",
    "ghana": "gh",
    "nigeria": "ng",
    "liberia": "lr",
    "sierra leone": "sl",
    "algeria": "dz",
    "morocco": "ma",
    "tunisia": "tn",
    "libya": "ly",
    "sudan": "sd",
    "south sudan": "ss",
    "chad": "td",
    "niger": "ne",
    "burkina faso": "bf",
    "mali": "ml",
    "mauritania": "mr",
    "senegal": "sn",
    "gambia": "gm",
    "guinea": "gn",
    "burundi": "bi",
    "rwanda": "rw",
    "djibouti": "dj",
    "eritrea": "er",
    "somalia": "so",
    "western sahara": "eh",
    "ireland": "ie",
    "kazakhstan": "kz",
    "uzbekistan": "uz",
    "guatemala": "gt",
    "north korea": "kp",
    "ecuador": "ec",
    "kosovo": "xk",
    "fiji": "fj",
    "mongolia": "mn",
    "tajikistan": "tj",
    "egypt": "eg",
    "barbados": "bb",
    "belize": "bz",
    "benin": "bj",
    "bermuda": "bm",
    "bhutan": "bt",
    "bolivia": "bo",
    "bosnia-herzegovina": "ba",
    "angola": "ao",
    "antigua and barbuda": "ag",
    "american samoa": "as",
    "albania": "al",
    "brunei": "bn",
    "cape verde": "cv",
    "cambodia": "kh",
    "cameroon": "cm",
    "cayman islands": "ky",
    "chile": "cl",
    "chinese taipei": "tw",  # Note: "TW" is used for Taiwan
    "comoros": "km",
    "congo": "cg",  # Congo-Brazzaville
    "cook islands": "ck",
    "costa rica": "cr",
    "cuba": "cu",
    "dominica": "dm",
    "dominican republic": "do",
    "dr congo": "cd",  # Democratic Republic of the Congo
    "el salvador": "sv",
    "refugee olympic team": "olympic",
    "equatorial guinea": "gq",
    "gabon": "ga",
    "grenada": "gd",
    "guam": "gu",
    "guinea-bissau": "gw",
    "guyana": "gy",
    "haiti": "ht",
    "honduras": "hn",
    "iceland": "is",
    "indonesia": "id",
    "iraq": "iq",
    "jamaica": "jm",
    "jordan": "jo",
    "kiribati": "ki",
    "kyrgyzstan": "kg",
    "laos": "la",
    "lebanon": "lb",
    "madagascar": "mg",
    "maldives": "mv",
    "marshall islands": "mh",
    "mauritius": "mu",
    "micronesia": "fm",
    "montenegro": "me",
    "mozambique": "mz",
    "myanmar": "mm",
    "nauru": "nr",
    "nicaragua": "ni",
    "north macedonia": "mk",
    "palau": "pw",
    "palestine": "ps",
    "panama": "pa",
    "papua new guinea": "pg",
    "paraguay": "py",
    "peru": "pe",
    "philippines": "ph",
    "puerto rico": "pr",
    "st lucia": "lc",
    "samoa": "ws",
    "sao tome and principe": "st",
    "seychelles": "sc",
    "solomon islands": "sb",
    "st kitts and nevis": "kn",
    "st vincent and the grenadines": "vc",
    "suriname": "sr",
    "syria": "sy",
    "east timor": "tl",  # Timor-Leste
    "togo": "tg",
    "tonga": "to",
    "trinidad and tobago": "tt",
    "turkmenistan": "tm",
    "tuvalu": "tv",
    "uruguay": "uy",
    "vanuatu": "vu",
    "venezuela": "ve",
    "british virgin islands": "vg",
    "american virgin islands": "vi",
    "aruba": "aw",
    "bahamas": "bs",
    "coddr congo": "cg",  # Congo-Brazzaville
    # Add more countries as needed
}

    olympics_logo_url = 'olympics-medals\images\logo.png'

    # HTML content
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Olympics Medal Standings</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: white;
            font-weight: bold;
            display: flex;
            flex-direction: column;
            align-items: center; /* Center all content in the body */
        }

        .header-container {
            text-align: center;
            width: 100%;
            max-width: 800px; /* Limit header width to match table */
            margin-bottom: 20px; /* Space between header and table */
        }

        .header-title {
            margin: 0;
            font-family: 'Playfair Display', serif;
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .header-subtitle {
            margin: 15px 0 20px 0;
            font-family: 'Arial', sans-serif;
            font-size: 1.2em;
            color: #555;
        }

        .olympics-logo {
            height: 50px; /* Adjust size as needed */
            margin: 30px auto;
            display: block; /* Center image in the header container */
        }

        .table-container {
            width: 100%;
            max-width: 800px; /* Limit table width to match header */
            overflow-x: auto; /* Enable horizontal scroll on small screens */
        }

        table {
            width: 100%;
            border-collapse: collapse;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        img.flag {
            width: 30px; /* Adjust size as needed */
            vertical-align: middle;
            margin-right: 8px;
        }

        th, td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }

        th {
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }

        .gold-header {
            background-color: #FFD700;
        }

        .silver-header {
            background-color: #C0C0C0;
        }

        .bronze-header {
            background-color: #cd7f32;
        }

        td {
            background-color: #f9f9f9;
        }

        .medal-icon {
            width: 20px; /* Adjust size as needed */
            vertical-align: middle;
            margin-right: 5px;
        }

        .gold-icon {
            content: url('https://example.com/gold-medal-icon.png');
        }

        .silver-icon {
            content: url('https://example.com/silver-medal-icon.png');
        }

        .bronze-icon {
            content: url('https://example.com/bronze-medal-icon.png');
        }

        .total-icons {
            display: flex;
            align-items: center;
        }

        /* Media query for mobile devices */
        @media (max-width: 768px) {
            .header-title {
                font-size: 2em; /* Slightly smaller font size for mobile */
            }

            .header-subtitle {
                font-size: 1em; /* Slightly smaller font size for mobile */
            }

            .olympics-logo {
                height: 40px; /* Adjust size for mobile */
            }

            .header-container {
                max-width: 100%; /* Full width on mobile */
            }

            .table-container {
                max-width: 100%; /* Full width on mobile */
            }
        }
    </style>
</head>
<body>
    <div class="header-container">
        <h1 class="header-title">Fairer Olympic Scoring:<br>Balanced Model Rankings</h1>
        <p class="header-subtitle">This table uses a weighted scoring system to rank countries, giving more value to gold medals and less to silver and bronze. This approach aims to provide a more balanced comparison of Olympic achievements.</p>
        <img src="images/logo.png" alt="Olympics Logo" class="olympics-logo">
    </div>

    <div class="table-container">
        <table>
            <thead>
                <tr>
                    <th>Rank</th>
                    <th>Country</th>
                    <th class="gold-header">Gold</th>
                    <th class="silver-header">Silver</th>
                    <th class="bronze-header">Bronze</th>
                    <th>Total Score</th>
                </tr>
            </thead>
            <tbody>
    """

    # Add rows to the HTML table with tied rankings
    for rank, country_name, gold, silver, bronze, total_score in ranked_countries:
        country_code = country_codes.get(country_name.lower(), "xx")
        flag_url = f"https://flagcdn.com/h40/{country_code}.png"
        
        html_content += f"""
            <tr>
                <td>{rank}</td>
                <td>
                    <img src="{flag_url}" alt="{country_name} flag" class="flag">
                    {country_name}
                </td>
                <td>{gold}</td>
                <td>{silver}</td>
                <td>{bronze}</td>
                <td>{total_score}</td>
            </tr>
        """

    # Close the HTML tags
    html_content += """
            </tbody>
        </table>
    </body>
    </html>
    """

    # Write to an HTML file
    with open('medal_standings.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("HTML file generated: medal_standings.html")

# Execute the function
fetch_medal_data()
