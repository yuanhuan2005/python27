import urllib2

for line in urllib2.urlopen("http://uinfo.mail.163.com/cgi-bin/hseed/two.pl"):
    print line
