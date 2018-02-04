import urllib
from bs4 import BeautifulSoup

# Create/open a file called services.csv (which will be a comma-delimited file)
f = open('services.csv', 'w')
f.write('Name,'+"Children's events,"+"Book groups and events,"+"Free public computers and WiFi,"+"Printing copying and scanning facilities,"+"Self service machines,"+"Meeting rooms for hire,"+"Events,"+"FabLab and maker space,"+"Business and IP Centre,"+"Cafe,"+"Exhibition and display space,"+"Learning Disability Service Day Centre,"+"Friends group\n")

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
    #print (url)
    
    # Get values from page
    soup = BeautifulSoup(page, "lxml")
    #print (soup)
    
    # get detail
    #serv = soup.findAll(attrs={"class":"journal-content-article"})[1].get_text()
    #services = str(serv)
    #pos = services.rfind('Services')

    #blurb, data = services.rsplit('Services')
    #data = str(data)
    #print ('data', data)
    
    serv_list = soup.findAll(attrs={"class":"journal-content-article"})[1]
    lib_name = lib_dict.get(library)
    tidy_serv = [lib_name]
    for li in serv_list.findAll('li'):
        tidy_serv.append(li.get_text())
    #print ("tidy_serv", tidy_serv)
    #print ("repr", repr(tidy_serv))
    child = "Children’s events" in tidy_serv
    book = "Book groups and events" in tidy_serv
    wifi = ("Free public computers and WiFi" in tidy_serv) or ("Free public computer and WiFi" in tidy_serv)
    printing = ("Printing, copying and scanning facilities" in tidy_serv) or ("Printing facilities" in tidy_serv)
    selfserve = "Self-service machines" in tidy_serv
    meeting = "Meeting rooms for hire" in tidy_serv
    events = "Variety of events for all audiences" in tidy_serv
    fablab = "FabLab maker space" in tidy_serv
    business = ("Business and IP Centre" in tidy_serv)or("Business and Intellectual Property (IP) Centre" in tidy_serv)
    cafe_detail = "Real Food Exeter Cafe with garden terrace" in tidy_serv
    display = "Exhibition and display space" in tidy_serv
    day_centre = "Learning Disability Service Day Centre" in tidy_serv
    friends = "Friends group" in tidy_serv

    print (lib_name, "child", child, "book", book, "wifi", wifi, "printing", printing, "selfserve", selfserve, "meeting", meeting, "events", events, "fablab", fablab, "business", business, "cafe", cafeYN, "display", display, "day centre", day_centre)
    facilities = lib_name + ',' + str(child) + ',' + str(book) + ',' + str(wifi) + ',' + str(printing) + ',' + str(selfserve) + ',' + str(meeting) + ',' + str(events) + ',' + str(fablab) + ',' + str(business) + ',' + str(cafeYN) + ',' + str(display) + ',' + str(day_centre) + ',' + str(friends)

        
    # next - list to string
    serv_string = ','.join(tidy_serv)
    cafe_all = serv_string.rfind("Cafe")
    cafeYN = (cafe_all > -1)
    print ("cafe?", cafe_all, cafeYN)

    #print (serv_string)
    
    # don't forget to create CSV header row at the beginning
    
    #Write details to file
    f.write(facilities + '\n')
    
# Done getting data! Close file.
f.close()
