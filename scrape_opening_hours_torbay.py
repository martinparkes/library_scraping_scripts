import urllib
from bs4 import BeautifulSoup, NavigableString, Tag

# Create/open a file called opening_hours.csv (which will be a comma-delimited file)
f = open('opening_hours_torbay.csv', 'w')
f.write("Name," + "Monday," + "Tuesday," + "Wednesday," + "Thursday," + "Friday," + "Saturday" + "\n")


# Iterate through libraries
for library in (
'brixham-library/',
'churston-library/',
'plaic/',
'torquay-library/'
):
    lib_dict = {
        'brixham-library/': 'Brixham Library',
        'churston-library/': 'Churston Library',
        'plaic/': 'Paignton Library',
        'torquay-library/': 'Torquay Library'
    }

    # Open library url
    url = "http://www.torbay.gov.uk/libraries/find-a-library/" + library 
    #url = "https://devonlibraries.org.uk/web/arena/" + library
    page = urllib.request.urlopen(url)
    
    # Get values from page
    soup = BeautifulSoup(page, 'lxml')
    tables = soup.findChildren('table')
    
    # Fetch the first table - Opening Hours
    my_table = tables[0]

    # Get table rows
    # Find children with multiple tags by passing a list of strings
    rows = my_table.findChildren(['th', 'tr'])
    lib_name = lib_dict.get(library)
    times_str = [lib_name]
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.string
            times_str.append(value)    
        hours = str(times_str)
        #print (hours)
    tidy_hours = times_str[0] + ',' + times_str[2] + ',' + times_str[4] + ',' + times_str[6] + ',' + times_str[8] + ',' + times_str[10] + ',' + times_str[12]
    #print (tidy_hours)
    
    #Write details to file
    f.write(tidy_hours + '\n')
    
# Done getting data! Close file.
f.close()