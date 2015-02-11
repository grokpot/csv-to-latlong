import csv
import time
import sys
from geopy.geocoders import GoogleV3

# Let's use Google because they have a nice brand
geolocator = GoogleV3()

def main(argv):
    try:
        with open(argv[1], 'rU') as address_file:
            reader = csv.reader(address_file)

            # Get input mode
            input_mode, valid_input = False, False
            while not valid_input:
                input_mode = raw_input("Enter 1 for city / state lookup. Enter 2 for address / city / state lookup:  ")
                valid_input = True if input_mode == '1' or input_mode == '2' else False

            # Get input header
            input_header, valid_input = False, False
            while not valid_input:
                input_header = raw_input("Does your spreadsheet have a header row (y/n)?:  ")
                valid_input = True if input_header == 'y' or input_header == 'n' else False

            # Get address1 column if applicable
            address1, valid_input = False, False
            if input_mode == '2':
                valid_input = False
                while not valid_input:
                    try:
                        address1 = int(raw_input("Enter 0-based column number of address1 (address2 not supported - DIY):  "))
                        valid_input = True
                    except:
                        pass

            # Get city column
            city_col, valid_input = False, False
            while not valid_input:
                try:
                    city_col = int(raw_input("Enter 0-based column number of city:  "))
                    valid_input = True
                except:
                    pass

            # Get state column
            state_col, valid_input = False, False
            while not valid_input:
                try:
                    state_col = int(raw_input("Enter 0-based column number of state:  "))
                    valid_input = True
                except:
                    pass

            print "Processing your shit."

            with open('output.csv', 'w') as output_file:
                csv_writer = csv.writer(output_file)
                header_row = ['address1'] if address1 else []
                header_row += ['city', 'state', 'latitude', 'longitude']
                csv_writer.writerow(header_row)
                n = 0
                for i, row in enumerate(reader):
                    if i == 0 and input_header == 'y':
                        continue
                    query_string = row[address1] if address1 else ''
                    query_string += ', ' + row[city_col] + ', ' + row[state_col]
                    location = geolocator.geocode(query_string)
                    time.sleep(0.15)    # Google lookup limits: 2,500 requests / 24 hours, 5 requests / 1 sec
                    print 'lat: ' + str(location.latitude) + ', long: ' + str(location.longitude)
                    output_row = [row[address1]] if address1 else []
                    output_row += [row[city_col], row[state_col], location.latitude, location.longitude]
                    csv_writer.writerow(output_row)
    except Exception as e:
        print "Uh-oh. You messed something up. Here's a hint:"
        print e

if __name__ == '__main__':
    main(sys.argv)