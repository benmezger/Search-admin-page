#!/usr/bin/python2

"""
Author: Ephexeve M
Date: Mon May 21 11:48:10 CEST 2012
System: Unix
"""

import pages
from sys import argv, exit
import httplib
from optparse import OptionParser


parser = OptionParser()
parser.add_option("-l", "--language", help = "Choose a specific language {php/brf/cgi/cfm/js/asp}")
(options, args) = parser.parse_args()

        
class GetPages:
    
    def __init__(self):
        try:
            self.site = argv[1]
        except IndexError as error:
            print "\nError, where is the link? -- %s" % error
            exit(1)

        self.language = argv[3] if len(argv) >= 3 else False
        self.start = self.start()
        
    def connectSite(self, language = None):
        
        if not language:
            for pagelinks in pages.links:
                pagelinks = pagelinks.replace("\n", "") ; pagelinks =  "/" + pagelinks
                host = self.site + pagelinks
                site_connection = httplib.HTTPConnection(self.site)
                site_connection.request("GET", host)
                response = site_connection.getresponse()
                print "%s Status: %s" % (host, response.status)
        else:
            if self.language in pages.languages:
                for pagelinks in pages.languages.get(self.language):
                    pagelinks = pagelinks.replace("\n", "") ; pagelinks =  "/" + pagelinks
                    host = self.site + pagelinks
                    site_connection = httplib.HTTPConnection(self.site)
                    site_connection.request("GET", host)
                    response = site_connection.getresponse()
                    print "%s Status: %s" % (host, response.status)
            else:
                print "Language not found!"

    def start(self):
        
        if not self.site.startswith("www.") or self.site.startswith("http"):
            self.site = "www." + self.site
        try:
            if self.language:
                self.connectSite(self.language)
            else:
                self.connectSite()
        except Exception as error: 
            print "Error occured: %s" % error                  
        
if __name__ == "__main__":
    GetPages()