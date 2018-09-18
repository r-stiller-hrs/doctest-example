#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################
# utility methods for doctests in test.md
############################################

import spynner
import config


############################################
# return browser object
############################################
def loadPage(url):
    # get browser object
    #browser = spynner.Browser(debug_level = spynner.DEBUG)
    browser = spynner.Browser()

    # create browser window
    browser.create_webview()
    browser.show()

    # load login page
    try:
        browser.load_jquery(True)
        browser.load(url)
        return browser
    except SpynnerTimeout:
        print("could not load page")
        return


############################################
# destroy given webbrowser object
############################################
def destroyBrowser(browser):
    browser.destroy_webview()
    browser.close()


##################################################
# import dummy data in test db
##################################################
def importData():
    # ...
    return True


##################################################
# drop test db
##################################################
def dropTestDb():
    # ...
    return True
