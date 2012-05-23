#!/usr/bin/python2

"""
Author: Ephexeve M
Date: Mon May 21 11:48:10 CEST 2012
System: Unix
"""

import pages
from sys import argv, exit
import httplib
import socket
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-w", "--write", dest = "filename", help = "write report to file", metavar = "FILE")
(options, args) = parser.parse_args()
        
class GetPages:
    
    def __init__(self):
        try:
            self.site = argv[1]
        except IndexError as error:
            print "\nError, where is the link? --  %s" % error
            exit(0)
            
        self.write = argv[2] if len(argv) >= 3 else False    
        self.filename = argv[3] if len(argv) >= 4 else False
        self.checkSite = self.checkSite()

    def checkSite(self):
        if not self.site.startswith("www."):
            self.site = "www." + self.site
         
        try:
               
            for pagelinks in pages.links:
                pagelinks = pagelinks.replace("\n", "") ; pagelinks =  "/" + pagelinks
                host = self.site + pagelinks
                site_connection = httplib.HTTPConnection(self.site)
                site_connection.request("GET", host)
                response = site_connection.getresponse()
                
                if response.status:
                    if self.write:
                        with open(self.filename, "a") as data:
                            data.writelines("\n" + host + "--" + str(response.status))
                print "%s Status: %s" % (host, response.status)
            
        except Exception as error: return "Error occured: %s" % error                  
        
if __name__ == "__main__":
    GetPages()