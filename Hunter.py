#!/usr/bin/python

import requests
import sys
class colors:
    END = '\033[0m'
    RED='\033[31m'
    GREEN='\033[32m'
    ORANGE='\033[33m'
    Purple='\033[35m'
    CYAN='\033[1;96m'

print colors.ORANGE+"                   Hackers Hunter v1.0 "+colors.END	
print colors.ORANGE+"[*] Written by: Mustafa - Twitter: twitter.com/c0brabaghdad1 [*]\n"+colors.END		


def main (user):  
    try:
     print colors.RED + "Your Input : {} ".format(colors.Purple+user+colors.END)+colors.END
#FaceBook   
     url = "https://www.facebook.com/"+ user
     response = requests.get(url)
     if response.status_code == 200:
         response.close()
         print  "[\033[36m+\033[0m]\033[36m FaceBook :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m FaceBook :\033[0m \033[33mNot Found !\033[0m"
#H1   
     url = "https://hackerone.com/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Hackerone :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Hackerone :\033[0m \033[33mNot Found !\033[0m"
# Bugcrowd
     url = "https://bugcrowd.com/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m BugCrowd :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m BugCrowd :\033[0m \033[33mNot Found !\033[0m"
# Bugcrowd Blog
     url = "https://www.bugcrowd.com/blog/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Bugcrowd Blog :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Bugcrowd Blog:\033[0m \033[33mNot Found !\033[0m"
# OpenBugBounty   
     url = "https://www.openbugbounty.org/researchers/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m OpenBugBounty :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m OpenBugBounty :\033[0m \033[33mNot Found !\033[0m"
# Yogosha
     url = "https://yogosha.com/ca_leaderboards/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Yogosha :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Yogosha :\033[0m \033[33mNot Found !\033[0m"
# YesWeHack
     url = "https://yeswehack.com/hunters/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m YesWeHack :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m YesWeHack :\033[0m \033[33mNot Found !\033[0m"
# Intigriti
     url = "https://app.intigriti.com/profile/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Intigriti :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Intigriti :\033[0m \033[33mNot Found !\033[0m"
# Hackenproof
     url = "https://hackenproof.com/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Hackenproof :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Hackenproof :\033[0m \033[33mNot Found !\033[0m"
# Cobalt
     url = "https://app.cobalt.io/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Cobalt :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Cobalt :\033[0m \033[33mNot Found !\033[0m"
# Cybertalents
     url = "https://cybertalents.com/members/{}/profile".format(user)
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Cybertalents :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Cybertalents :\033[0m \033[33mNot Found !\033[0m"
# BackdoorSdslabs
     url = "https://backdoor.sdslabs.co/users/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m BackdoorSdslabs :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m BackdoorSdslabs :\033[0m \033[33mNot Found !\033[0m"
# TryHackMe
     url = "https://tryhackme.com/p/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m TryHackMe :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m TryHackMe :\033[0m \033[33mNot Found !\033[0m"
# Crackmes
     url = "https://crackmes.one/user/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Crackmes :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Crackmes :\033[0m \033[33mNot Found !\033[0m"
# CryptoHack
     url = "https://cryptohack.org/user/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m CryptoHack :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m CryptoHack :\033[0m \033[33mNot Found !\033[0m"
# W3Challs
     url = "https://w3challs.com/profile/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m W3Challs :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m W3Challs :\033[0m \033[33mNot Found !\033[0m"
# BugReader
     url = "https://bugreader.com/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m BugReader :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m BugReader :\033[0m \033[33mNot Found !\033[0m"
# HackingArticles
     url = "https://www.hackingarticles.in/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m HackingArticles :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m HackingArticles :\033[0m \033[33mNot Found !\033[0m"
# InfosecInstitute
     url = "https://resources.infosecinstitute.com/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m InfosecInstitute :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m InfosecInstitute :\033[0m \033[33mNot Found !\033[0m"
# Rapid7
     url = "https://blog.rapid7.com/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Rapid7 :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Rapid7 :\033[0m \033[33mNot Found !\033[0m"
# Acunetix
     url = "https://www.acunetix.com/blog/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Acunetix :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Acunetix :\033[0m \033[33mNot Found !\033[0m"
# Portswigger
     url = "https://portswigger.net/daily-swig/by/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Portswigger :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Portswigger :\033[0m \033[33mNot Found !\033[0m"
# Sans
     url = "https://www.sans.org/profiles/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Sans :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Sans :\033[0m \033[33mNot Found !\033[0m"
# HackerNoon
     url = "https://hackernoon.com/u/"+user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m HackerNoon :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m HackerNoon :\033[0m \033[33mNot Found !\033[0m"
# Securitum
     url = "https://research.securitum.com/authors/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Securitum :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Securitum :\033[0m \033[33mNot Found !\033[0m"
# Netsparker
     url = "https://www.netsparker.com/blog/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Netsparker :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Netsparker :\033[0m \033[33mNot Found !\033[0m"
# BugBountyPoc
     url = "https://bugbountypoc.com/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m BugBountyPoc :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m BugBountyPoc :\033[0m \033[33mNot Found !\033[0m"
# AT&T Blog
     url = "https://cybersecurity.att.com/blogs/author/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m AT&T Blog :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m AT&T Blog :\033[0m \033[33mNot Found !\033[0m"
# GeeksforGeeks
     url = "https://auth.geeksforgeeks.org/user/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m GeeksforGeeks :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m GeeksforGeeks :\033[0m \033[33mNot Found !\033[0m"
# eLearnSecurity Blog
     url = "https://blog.elearnsecurity.com/author/mkreisher"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m eLearnSecurity Blog :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m eLearnSecurity Blog :\033[0m \033[33mNot Found !\033[0m"
# EC-Council Blog
     url = "https://blog.eccouncil.org/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m EC-Council Blog :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m EC-Council Blog :\033[0m \033[33mNot Found !\033[0m"
# Wattpad
     url = "https://www.wattpad.com/user/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Wattpad :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Wattpad :\033[0m \033[33mNot Found !\033[0m"
# Secjuice
     url = "https://www.secjuice.com/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Secjuice :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Secjuice :\033[0m \033[33mNot Found !\033[0m"
# Veracode
     url = "https://www.veracode.com/blog/author/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Veracode :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Veracode :\033[0m \033[33mNot Found !\033[0m"
# NotABug
     url = "https://notabug.org/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m NotABug :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m NotABug :\033[0m \033[33mNot Found !\033[0m"
# SecureIdeas
     url = "https://blog.secureideas.com/author/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m SecureIdeas Blog :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m SecureIdeas Blog:\033[0m \033[33mNot Found !\033[0m"
# DEV.TO
     url = "https://dev.to/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m DEV.TO :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m DEV.TO :\033[0m \033[33mNot Found !\033[0m"
# Medium
     url = "https://medium.com/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Medium :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Medium :\033[0m \033[33mNot Found !\033[0m"
# CVEbase
     url = "https://www.cvebase.com/researcher/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m CVEbase :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m CVEbase :\033[0m \033[33mNot Found !\033[0m"
# WonderHowTo
     url = "https://creator.wonderhowto.com/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m WonderHowTo :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m WonderHowTo :\033[0m \033[33mNot Found !\033[0m"
# Quora
     url = "https://www.quora.com/profile/"+user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Quora :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Quora :\033[0m \033[33mNot Found !\033[0m"
# Netspi
     url = "https://blog.netspi.com/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Netspi :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Netspi :\033[0m \033[33mNot Found !\033[0m"
# Gitlab
     url = "https://gitlab.com/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Gitlab :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Gitlab :\033[0m \033[33mNot Found !\033[0m"
# Github
     url = "https://github.com/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Github :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Github :\033[0m \033[33mNot Found !\033[0m"
# Reddit
     url = "https://www.reddit.com/user/"+user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Reddit :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Reddit :\033[0m \033[33mNot Found !\033[0m"
# Hackr
     url = "https://hackr.io/blog/author/"+user+"/"
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Hackr :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Hackr :\033[0m \033[33mNot Found !\033[0m"
# CoderByte
     url = "https://coderbyte.com/profile/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m CoderByte :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m CoderByte :\033[0m \033[33mNot Found !\033[0m"
# TechTarget
     url = "https://www.techtarget.com/contributor/" + user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m TechTarget :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m TechTarget :\033[0m \033[33mNot Found !\033[0m"
# FireEye
     url = "https://www.fireeye.com/blog/threat-research.html/category/etc/tags/fireeye-blog-authors/"+ user
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m FireEye Blog :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m FireEye Blog :\033[0m \033[33mNot Found !\033[0m"
#Subdomains (wordpress,Github,Blogspot)
     url = "https://{}.github.io/".format(user)
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Github Subdomain Found  :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Github Subdomain Not Found :\033[0m \033[33mNot Found !\033[0m"
     url = "https://{}.blogspot.com".format(user)
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m Blogspot Subdomain Found  :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m Blogspot Subdomain Not Found :\033[0m \033[33mNot Found !\033[0m"
     url = "https://{}.wordpress.com".format(user)
     response = requests.get(url)
     if response.status_code == 200:
	    response.close()
	    print  "[\033[36m+\033[0m]\033[36m WordPress Subdomain Found :\033[0m \033[0;37m" + url + "\033[0m"
     else:print "[\033[31m-\033[0m]\033[36m WordPress Subdomain Not Found :\033[0m \033[33mNot Found !\033[0m"
    except : #requests.ConnectionError ##if you have bad network don't enable this option
        print(colors.RED+"Failed To Connect !"+colors.END)
if len(sys.argv) > 1:
	if sys.argv[1] == "--user" or  sys.argv[1] == "-u":
		if len(sys.argv) > 2:
			main(sys.argv[2])
		else:
			print(colors.RED+"Missing Username Try ->  -h"+colors.END)
	if sys.argv[1] == "--help" or sys.argv[1] == "-h":
         print (colors.GREEN+"Usage : --user or -u"+colors.END)
         print (colors.GREEN+"Usage : --help or -h "+colors.END)
	else:
		pass
else:
	username = raw_input ("Enter Username : ")
	main(username)