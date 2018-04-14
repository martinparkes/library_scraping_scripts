import urllib
from bs4 import BeautifulSoup

# Create/open a file called address.csv (which will be a comma-delimited file)
f = open('address_torbay.csv', 'w')
f.write("Name," + "Full address," + "Postcode," + "\n")


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
    
    # Get values from page
    soup = BeautifulSoup(page, 'lxml')
    
    # set up the empty list
    lib_name = lib_dict.get(library)
    addr_bits = [lib_name]
    
    # Find the section with the address in which is different almost every time so ...
    # find the relevant sections
    for address in soup.findAll(attrs={"class":"offscreen"}):
        foo = address.get_text(strip=True).strip()
        if foo == "Address:":
            bits = address.nextSibling
            bits_split = bits.split(",")
            street = bits_split[0]
            town = bits_split[1]
            pcode = bits_split[2].strip()
            addr_bits = lib_name, bits, pcode
            addr_bits_string = str(addr_bits)
            print (addr_bits_string)
        
    #Write details to file
    f.write(addr_bits_string + '\n')
    
# Done getting data! Close file.
f.close()