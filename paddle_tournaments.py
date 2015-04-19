from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


# This gets data from the page below: A list of the current players in the ATP
# This is a men's tournaments only search
url1 = (r'http://www.platformtennis.org/Tournaments/Calendar.htm?EventMode=AdvancedSearch&Keyword=&Categories=79266955&DateFrom=41883&DateTo=42124.0409722222')
page = urlopen(url1)
soup = BeautifulSoup(page) #initiates bs4

final_data = []

data1 = soup.findAll('td')

for row in data1:
    col = row.findAll('td')
    if not col:
        pass
    else:
        name = ''.join(str(col[0].getText()))
        href = str(row.find('a', href=True))

        web_address = str(href[href.find('href="')+6:href.find('">')])

        # print(web_address)  # this works

        if 'SourceId' not in web_address and web_address != '':
            page2 = urlopen(web_address)  # initiates bs4
            soup2 = BeautifulSoup(page2)  # initiates bs4

            tour_info_all = soup2.findAll('td')
            tour_info_text = soup2.findAll('tr')[1].getText()

            pretty_tour_info_text = ' '.join(tour_info_text.split())

            # interesting variables : final_data = (t_name, t_date, t_location)
            # 1
            t_date = pretty_tour_info_text[pretty_tour_info_text.find('Date:')+6:pretty_tour_info_text.find(',')+6]
            if t_date == '':
                t_date = 'Unable to parse date'

            # 2
            if 'Location' in pretty_tour_info_text:
                t_location = pretty_tour_info_text[pretty_tour_info_text.find('Location:')+10:pretty_tour_info_text.rfind(',')+4]

                t_state = pretty_tour_info_text[pretty_tour_info_text.rfind(',')+2:pretty_tour_info_text.rfind(',')+4]

                if t_location == '':
                    t_location = 'Unable to parse location'
                    t_state = 'Unable to parse state'

            else:
                t_location = 'Location not listed'
                t_state = 'Unable to parse state'

            # 3
            t_name = pretty_tour_info_text[pretty_tour_info_text.find('Calendar')+9:pretty_tour_info_text.find('Date:')-1]

            # final_data = (t_name, t_date, t_location, web_address)

            fmt = "{}\t{}\t{}\t{}\t{}"

            final_data.append(fmt.format(t_name, t_date, t_location, t_state,web_address))
            print(fmt.format(t_name, t_date, t_location, t_state,web_address))

with open('paddle_tournaments_2014_2015_state.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter='\t')
    writer.writerow(['t_name', 't_date', 't_location', 't_state','web_address'])  # headers
    for line in final_data:
        writer.writerow(line.split('\t'))  # data