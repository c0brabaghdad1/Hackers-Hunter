# Hackers Hunter : Hunt down and track CTF Players &amp; Bug Hunters etc accounts  by username across in most places where you can find them :mag_right: :detective:

**Sample Scan ( python Hunter.py --user / -u  username )**
![simple](https://github.com/c0brabaghdad1/Hackers-Hunter/blob/master/image/scan.png)

**Help (python Hunter.py --help / -h )**

# Checking Username on
* bug bounty/CTF platforms and Security blogs and Subdomain by user in github/wordpress (user.github.io ,user.wordpress.com etc) and more 45+ 
* Sites out of scope this tool for example but not limited HackTheBox or more (because it's based in id not user) 

# False Positive
i will show you example with (OpenBugBounty) Save and Run This Code 

* Python
```
import requests
x = requests.get('https://www.openbugbounty.org/researchers/not_exist/')
print(x.status_code)
```
__Response = 200__

* OR Linux CLI

``` curl -LI https://www.openbugbounty.org/researchers/not_exist/ -o /dev/null -w '%{http_code}\n' -s ```

__Response = 200__

* **the user not exist but return 200** :thinking::monocle_face:
* **I am working to find other methods for example but not limited (based in Header as "Location") if you have any suggestions or solutions -> [Twitter](https://twitter.com/c0brabaghdad1)** 

# How to install (* linux)
* git clone https://github.com/c0brabaghdad1/Hackers-Hunter.git
* cd Hackers-Hunter
* python Hunter.py --help / -h
