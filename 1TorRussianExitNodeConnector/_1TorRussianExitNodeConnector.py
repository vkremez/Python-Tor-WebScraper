#  Project TorScraper
#  Read Website Through Tor Exit Node Of Our Choice
#  Step 1: Development of Anonymous Login Session Through Tor Node Of Our Choosing
#  Purpose: establish anonymity and secure connection via Tor
#  Sample Program: Russian Tor Exit Node Through Port 9150 to Website ATAGAR.COM
#  1) Important Note: Added Tor/Data/ files to %USER%/AppData/Roaming/tor
#  2) Important Note: Make sure there is no other instance of tor.exe. Otherwise, we get an Exception Error.

import io 
import StringIO
import socket
import pycurl
import time
import stem.process # Native Onion Network Python Module

from stem.util import term

SOCKS_PORT = 9150 # Grab the port from Tor/torrc config files


def query(url):
  """
  Uses pycurl to fetch a site using the proxy on the SOCKS_PORT.
  """

  output = io.BytesIO()

  query = pycurl.Curl()
  query.setopt(pycurl.URL, url)
  query.setopt(pycurl.PROXY, 'localhost')
  query.setopt(pycurl.PROXYPORT, SOCKS_PORT)
  query.setopt(pycurl.PROXYTYPE, pycurl.PROXYTYPE_SOCKS5_HOSTNAME)
  query.setopt(pycurl.WRITEFUNCTION, output.write)

  try:
    query.perform()
    return output.getvalue()
  except pycurl.error as exc:
    return "Unable to reach %s (%s)" % (url, exc)


# Start an instance of Tor configured to only exit through Russia. This prints
# Tor's bootstrap information as it starts. Note that this likely will not
# work if you have another Tor instance running.
# Important Note: Always Make Sure There Is No Other Tor.EXE Running Otherwise You will Get An Exception Error
def print_bootstrap_lines(line):
  if "Bootstrapped " in line:
    print(term.format(line, term.Color.BLUE))


print(term.format("Starting Tor:\n", term.Attr.BOLD))

tor_process = stem.process.launch_tor_with_config(
    tor_cmd = "C:\Tor\Browser\TorBrowser\Tor\\tor.exe", # point to the local tor.exe file for module stem.process
    config = {
    'SocksPort': str(SOCKS_PORT),
    'ExitNodes': '{ru}', # choose a 2-letter country code such as "ru"
  },
  init_msg_handler = print_bootstrap_lines,
)

print(term.format("\nChecking our endpoint:\n", term.Attr.BOLD))
print(term.format(query("https://www.atagar.com/echo.php"), term.Color.BLUE))

tor_process.kill()  # stops tor.exe. It takes some time to gracefully shutdown the process
