import urllib
from bs4 import BeautifulSoup

# Create/open a file called address.csv (which will be a comma-delimited file)
f = open('address.csv', 'w')
f.write("Name," + "Full address," + "Postcode," + "\n")


# Iterate through libraries
for library in (
'appledorelibrary',
'axminsterlibrary', 
'ashburtonlibrary',
'bamptonlibrary', 
'barnstaplelibrary',
'bidefordlibrary', 
'boveytraceylibrary', 
'brauntonlibrary', 
'buckfastleighlibrary', 
'budleighsaltertonlibrary', 
'chagfordlibrary', 
'chudleighlibrary', 
'chulmleighlibrary', 
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
        'axminsterlibrary':'Axminster Library',
        'ashburtonlibrary':'Ashburton Library',
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
    
    # set up the empty list
    lib_name = lib_dict.get(library)
    addr_bits = [lib_name]
    # Find the section with the address in which is different almost every time so ...
# find the relevant sections
    sections = soup.findAll(attrs={"class":"journal-content-article"})
    
    i=0
    for item in sections:
        content = item.get_text()
        if 'Find us:' in content:
            ind = i
            git, data = content.rsplit('Find us:')
            #print ('index is ',i, data)
        else:
            whatever = 'index is ',i, 'not found'
            i=i+1            
            
    sidebar = 'soup.findAll(attrs={"class":"journal-content-article"})[' + str(i) + '].get_text()'
        
    # Where 'Devon' isn't in the address, get the last 8 chars e.g. mystr[-8:]
    data = data.rstrip()
    try:
        addr, pcode = data.rsplit('Devon ')
    except:
        pcode = data[-8:]
    #print (lib_name, data, pcode)
    
    addr_bits.append(data)
    addr_bits.append(pcode)
    #addr_bits.append(lib_addr)
    #print (addr_bits)
    
    # list to string
    addr_bits_string = ','.join(addr_bits)
    print (addr_bits_string)
        
    #Write details to file
    f.write(addr_bits_string + '\n')
    
# Done getting data! Close file.
f.close()
