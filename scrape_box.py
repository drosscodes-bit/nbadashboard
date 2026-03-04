from bs4 import BeautifulSoup


link = "https://www.espn.com/nba/game/_/gameId/401809939/wizards-bucks"


def format_url(url):
    url = url[0:25] + "boxscore" + url[29:]
    return url


# Read from file instead of requesting
with open('box_score.html', 'r', encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')

# Home Team 
def hometeam(url):
    flex = soup.find_all("div", class_="flex")
    player_name = flex[1].find_all("tr", class_="Table__TR Table__TR--sm Table__even")
    stats = soup.find_all("tbody", class_="Table__TBODY")
    # print(stats[1].prettify())

    for player in range (1, 6):
        data = stats[1].find_all("tr", class_="Table__TR Table__TR--sm Table__even")
        get_name = player_name[player].find_all("span")


        data = data[player].find_all("td")
        minutes = data[0].get_text()
        points = data[1].get_text()
        field_goal_percentage = data[2].get_text()
        three_point_percentage = data[3].get_text()
        free_throw_percentage = data[4].get_text()
        rebounds = data[5].get_text()
        assists = data[6].get_text()
        turnovers = data[7].get_text()
        steals = data[8].get_text()
        blocks = data[9].get_text()
        o_rebounds = data[10].get_text()
        d_rebounds = data[11].get_text()
        fouls = data[12].get_text()
        plus_minus = data[13].get_text()
        name = get_name[0].get_text()
        jersey = get_name[2].get_text()

        print(f"{name} {jersey} {minutes} {points} {field_goal_percentage} {three_point_percentage} {free_throw_percentage} {rebounds} {assists} {turnovers} {steals} {blocks} {o_rebounds} {d_rebounds} {fouls} {plus_minus}")
    
    print("Bench:")
    for player in range(7, 17):
        data = stats[1].find_all("tr", class_="Table__TR Table__TR--sm Table__even")
        get_name = player_name[player].find_all("span")


        data = data[player].find_all("td")
        minutes = data[0].get_text()
        points = data[1].get_text()
        field_goal_percentage = data[2].get_text()
        three_point_percentage = data[3].get_text()
        free_throw_percentage = data[4].get_text()
        rebounds = data[5].get_text()
        assists = data[6].get_text()
        turnovers = data[7].get_text()
        steals = data[8].get_text()
        blocks = data[9].get_text()
        o_rebounds = data[10].get_text()
        d_rebounds = data[11].get_text()
        fouls = data[12].get_text()
        plus_minus = data[13].get_text()
        name = get_name[0].get_text()
        jersey = get_name[2].get_text()

        print(f"{name} {jersey} {minutes} {points} {field_goal_percentage} {three_point_percentage} {free_throw_percentage} {rebounds} {assists} {turnovers} {steals} {blocks} {o_rebounds} {d_rebounds} {fouls} {plus_minus}")

def awayteam(url):
    

hometeam(format_url(link))