import urllib
from bs4 import BeautifulSoup

# Create/open a file called opening_hours.csv (which will be a comma-delimited file)
f = open('opening_hours.csv', 'w')
f.write("Name," + "Monday," + "Tuesday," + "Wednesday," + "Thursday," + "Friday," + "Saturday" + "\n")


# Iterate through libraries
for library in (
'appledorelibrary',
'ashburtonlibrary',
'axminsterlibrary', 
'bamptonlibrary', 
'barnstaplelibrary',
'bidefordlibrary', 
'boveytraceylibrary', 
'brauntonlibrary', 
'buckfastleighlibrary', 
'budleighsaltertonlibrary', 
'chagfordlibrary', 
'chudleighlibrary', 
#'chulmleighlibrary', 
'clystvalelibrary', 
'colytonlibrary', 
'combemartinlibrary',
'creditonlibrary',
'cullomptonlibrary',
'dartmouthlibrary',
'dawlishlibrary',
'exeterlibrary',
'exmouthlibrary',
'holsworthylibrary',
'honitonlibrary',
'ilfracombelibrary',
'ivybridgelibrary',
'kingsbridgelibrary',
'kingskerswelllibrary',
'kingsteigntonlibrary',
'lyntonlibrary',
'moretonhampsteadlibrary',
'newtonabbotlibrary',
'northamlibrary',
'okehamptonlibrary',
'otterystmarylibrary',
'pinhoelibrary',
'princetownlibrary',
'salcombelibrary',
'seatonlibrary',
'sidmouthlibrary',
'southmoltonlibrary',
'stthomaslibrary',
'stokefleminglibrary', 
'tavistocklibrary',
'teignmouthlibrary',
'tivertonlibrary',
'topshamlibrary',
'torringtonlibrary',
'totneslibrary',
'uffculmelibrary'  
):
    lib_dict = {
        'appledorelibrary':'Appledore Library',
        'ashburtonlibrary':'Ashburton Library',
        'axminsterlibrary':'Axminster Library',
        'bamptonlibrary':'Bampton Library',
        'barnstaplelibrary':'Barnstaple Library',
        'bidefordlibrary':'Bideford Library',
        'boveytraceylibrary':'Bovey Tracey Library',
        'brauntonlibrary':'Braunton Library',
        'buckfastleighlibrary':'Buckfastleigh Library',
        'budleighsaltertonlibrary':'Budleigh Salterton Library',
        'chagfordlibrary':'Chagford Library',
        'chudleighlibrary':'Chudleigh Library',
        'chulmleighlibrary':'Chulmleigh Library',
        'clystvalelibrary':'Clyst Vale Library',
        'colytonlibrary':'Colyton Library',
        'combemartinlibrary':'Combe Martin Library',
        'creditonlibrary':'Crediton Library',
        'cullomptonlibrary':'Cullompton Library',
        'dartmouthlibrary':'Dartmouth Library',
        'dawlishlibrary':'Dawlish Library',
        'exeterlibrary':'Exeter Library',
        'exmouthlibrary':'Exmouth Library',
        'holsworthylibrary':'Holsworthy Library',
        'honitonlibrary':'Honiton Library',
        'ilfracombelibrary':'Ilfracombe Library',
        'ivybridgelibrary':'Ivybridge Library',
        'kingsbridgelibrary':'Kingsbridge Library',
        'kingskerswelllibrary':'Kingskerswell Library',
        'kingsteigntonlibrary':'Kingsteignton Library',
        'lyntonlibrary':'Lynton Library',
        'moretonhampsteadlibrary':'Moretonhampstead Library',
        'newtonabbotlibrary':'Newton Abbot Library',
        'northamlibrary':'Northam Library',
        'okehamptonlibrary':'Okehampton Library',
        'otterystmarylibrary':'Ottery St Mary Library',
        'pinhoelibrary':'Pinhoe Library',
        'princetownlibrary':'Princetown Library',
        'salcombelibrary':'Salcombe Library',
        'seatonlibrary':'Seaton Library',
        'sidmouthlibrary':'Sidmouth Library',
        'southmoltonlibrary':'South Molton Library',
        'stthomaslibrary':'St Thomas Library',
        'stokefleminglibrary':'Stoke Fleming Library',
        'tavistocklibrary':'Tavistock Library',
        'teignmouthlibrary':'Teignmouth Library',
        'tivertonlibrary':'Tiverton Library',
        'topshamlibrary':'Topsham Library',
        'torringtonlibrary':'Torrington Library',
        'totneslibrary':'Totnes Library',
        'uffculmelibrary':'Uffculme Library'
    }

    # Open library url
    url = "https://devonlibraries.org.uk/web/arena/" + library
    page = urllib.request.urlopen(url)
    
    # Get values from page
    soup = BeautifulSoup(page, 'lxml')
    tables = soup.findChildren('table')
    
    # Fetch the first table - Opening Hours
    my_table = tables[0]

    # Find children with multiple tags by passing a list of strings
    rows = my_table.findChildren(['th', 'tr'])
    lib_name = lib_dict.get(library)
    times_str = [lib_name]
    for row in rows:
        cells = row.findChildren('td')
        for cell in cells:
            value = cell.string
            times_str.append(value)    
        #hours = str(times_str)
        #print (hours)
    tidy_hours = times_str[0] + ',' + times_str[2] + ',' + times_str[4] + ',' + times_str[6] + ',' + times_str[8] + ',' + times_str[10] + ',' + times_str[12]
    print (tidy_hours)
    
    #Write details to file
    f.write(tidy_hours + '\n')
    
# Done getting data! Close file.
f.close()
