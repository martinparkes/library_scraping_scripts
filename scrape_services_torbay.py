import urllib
from bs4 import BeautifulSoup, NavigableString, Tag
import re

# Create/open a file called services_torbay.csv (which will be a comma-delimited file)
f = open('services_torbay.csv', 'w')
f.write('Name,'+"Wifi,"+"Internet access,"+"Printing,"+"Photocopying,"+"Meeting rooms,"+"Hearing loop,"+"Lift\n")

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
    page = urllib.request.urlopen(url)
    #print (url)
    
    # Get values from page
    soup = BeautifulSoup(page, "lxml")
    #print (soup)
    
    for header in soup.find_all('h3'):
        nextNode = header
        foo = header.get_text(strip=True).strip()
        #print (foo)
        serv_list = []
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            if isinstance(nextNode, Tag) and foo == "Facilities":
                if nextNode.name == "h3":
                    break
                serv_list.append(nextNode.get_text(strip=True).strip())
                lib_name = lib_dict.get(library)
                tidy_serv = [lib_name]
                for li in serv_list:
                    tidy_serv.append(li)
        #print ("tidy_serv", tidy_serv)
        wifi = "Free wifi" in tidy_serv
        internet = ("Internet access (free to members)" in tidy_serv) or ("Free public computer and WiFi" in tidy_serv)
        fax = "Fax" in tidy_serv
        printing = ("Printing" in tidy_serv) or ("Printing facilities" in tidy_serv)
        copy = "Photocopying" in tidy_serv
        meeting = "Meeting rooms" in tidy_serv
        loop = "Hearing loop available" in tidy_serv
        lift = "Lift" in tidy_serv

    print (lib_name, "wifi", wifi, "internet", internet, "printing", printing, "copy", copy, "meeting", meeting, "loop", loop, "lift", lift)
    facilities = lib_name + ',' + str(wifi) + ',' + str(internet) + ',' + str(printing) + ',' + str(copy) + ',' + str(meeting) + ',' + str(loop) + ',' + str(lift)

    
    #Write details to file
    f.write(facilities + '\n')
    
# Done getting data! Close file.
f.close()