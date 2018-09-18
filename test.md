Doctest file for testing a backend

These tests assure, that certain endpoints work as expected.

>>> import testutils
>>> import config


###################################################
# check endpoints that need a valid, logged in user
###################################################

Check login.html; should redirect to /index.html if not logged in:

>>> browser = testutils.loadPage("http://localhost:8080/login.html")
>>> browser.url
u'http://localhost:8080/index.html'


Destroy spynner browser
>>> testutils.destroyBrowser(browser)


######################################
# test backend methods
######################################

The methods tested here are part of the functionality of the endpoints.

Set test param to True to use the test db
>>> config.TEST = True

Import test/dummy data
>>> testutils.importData() 
True

Test something else
>>> browser = testutils.loadPage("http://localhost:8080/logout.html")
>>> browser.url
u'http://localhost:8080/index.html'

Drop test db again
>>> testutils.dropTestDb()
>>> config.TEST = False
