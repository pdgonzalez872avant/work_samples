from urllib.request import urlopen
from bs4 import BeautifulSoup

# This gets data from the page below
url = r'http://mslgroupcreativeplus.com/work/SMG/starcomusa_api/v2/getAdvertisementsByPage.php'
page = urlopen(url)
soup = BeautifulSoup(page)  #initiates bs4
table = soup.find('table')

#Data structures
job_list = []
interesting_job_list = []

#fetches every job title and adds to a list
for row in table.find_all('tr')[1:]: #[1:] skips the header
    row_as_list = row.findAll('td')
    if row_as_list: # Had to test if this existed because there is an empty line in between table rows
        job_title = str(str(row_as_list[1]).split('>')[2]).replace('</a', '').replace(r'&amp;','and')
        job_list.append(job_title)
    else:
        continue

#adds interesting jobs - ones with 'Analyst' in title - to a list
for interesting_job in job_list:
    if 'Analyst' in interesting_job:
        interesting_job_list.append(interesting_job)
    else:
        continue

# Here is a summary of positions at Starcom
print('Here is a list of interesting jobs for Paulo')
for job_number, job in enumerate(interesting_job_list):
    print(job_number + 1, job)