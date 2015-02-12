# csv-to-latlong  

Given a spreadsheet containing city, state, and optionally address:  

| Name | Description | Address | Notes | City | State | Zip |  
| ---- | ----------- | ------- | ----- | ---- | ----- | --- |  

The program runs as follows:  

``$ python csv-to-latlong.py example_input.py``  
``Enter 1 for city / state lookup. Enter 2 for address / city / state lookup:``  
``>>> 2``  
``Does your spreadsheet have a header row (y/n)?:``  
``>>> y``  
``Enter 0-based column number of address1 (address2 not supported - DIY):``  
``>>> 2``  
``Enter 0-based column number of city:``  
``>>> 4``  
``Enter 0-based column number of state:``  
``>>> 5``  
``Processing your shit.``  
``Done. Check output.csv for results.``  

... and outputs something like below:  

| Address | City | State | Latitude | Longitude |  
| ------- | ---- | ----- | -------- | --------- |  

Make sure to install geopy (in reqs.txt)
