# Coded and Developed By Vitali Kremez
# inSession_HTMLWebTableScraper 0.2
# This program is developed to address the law enforcement needs to examine economics of carding shop RESCATOR.CM.

# Here are the following objects that are met by the program:
# 1. Scrape the content silently without triggering any bot alerts and any other DDOS protection alerts;
# 2. Save the HTML table in the local directory with timestamps;
# 3. Extract and pull any other useful data from the website tables; and
# 4. Run through all available pages of the website credit card data HTML data.

# Requirements:
# 1. Set up a username for the website;
# 2. Use the session key to automate scraping of the website; and
# 3. Scope the content and zone in on specific filters;

# Setup:
# 1. Feel free to change the default scraping directory from C:\%USERPROFILE%\iMacros\Download
# 2. Adjust the URL and website needs fields "URL GOTO" and "TAG POS"" 

# Operation:
# 1. Adds time values to the file name such as "result_8_22_15_5_23_PM.html";
# b. Adds the recursive function that would walk the website "next page" and continue writing files; and
# c. Finishs writing files as the next button reaches the end and terminates the process.


# Developer's Notes:
# 1. It appears the website uses the 33-page max layout;
# 2. Cloud DNS provides DDOS protection and throttles any non-cookie sessions thereby eliminating Py bsoup scraping.
