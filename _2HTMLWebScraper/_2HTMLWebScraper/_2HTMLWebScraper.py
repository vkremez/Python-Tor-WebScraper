# Step 2 - HTML Source Code Scraper
# Developed by Vitali Kremez
# Project: TorScraper
# This program allows us to automate scraping of the cookie-enabled website that contains HTML code using Regular Expressions.
# It must parse the data and write it to a file "result.html."

# Subsection A: 
# a. Set up a website connector by using Py modules urllib and urllib2;
# b. Import Py module re as "Regular Expressions" to the program;
# c. Make sure to edit 'cookie', 'fusion_visited', 'fusion_user', 'PHPSESSID' and '__atuvc' values. [Extract this information from a browser session that would use a springboard for the scarping function.]; 
# d. Select the values that need to be scraped from HTML source code; and
# e. Write the results to file "%USER%/result.html".

# ============================================================================================================================================================================================================

# Work In Progress:
# a. Add time values to the file name such as "result_8_22_15_5_23_PM.html";
# b. Add the recursive function that would walk the website "next page" and continue writing files; and
# c. Finish writing files as the next button reaches the end and terminates the process.

import urllib2, re
import urllib
opener = urllib2.build_opener()
opener.addheaders.append(('cookie', 'fusion_visited=yes;PHPSESSID=b76c27c31bf5b962fa4aea08dba863ba;fusion_user=18389.4c937e11d5117f0f16e60ef16a1c7c92;__atuvc=my__atuvc'))
response = opener.open('--','')
data = response.read()
regex = r"<code style='white-space:nowrap'>.*<code style='white-space:nowrap'>(.*)</code>"
result = re.search(regex, data, re.DOTALL)
result = result.group(1)
result = result.replace('\n', '')
result = result.replace('\t', '')
lines = result.split('<br />')
lines = lines[:len(lines)-1]
print lines

''' result = '' # Designate the necessary scraping function
for i in xrange(0,len(lines)):
    for j in xrange(0,len(lines[i])):
        if lines[i][j] == '@':
            result = result + str(i+1) + '-' + str(j) + ', '
result = result[:len(result)-2]
print result
'''

values = {'string':result,'submitbutton':'12 seconds to Submit',"CSRF_TOKEN":"<?php echo $_SESSION['CSRF_TOKEN'];?>"}
post_data = urllib.urlencode(values)
response = opener.open('http://rescator.cm/index.php', post_data)
file_handle = open('result.html', 'w')
while 1:
    data = response.read()
    if not data:
        break
    file_handle.write(data)
file_handle.close
