# Hackers Hunter : Hunt down and track CTF Players &amp; Bug Hunters etc accounts  by username across in most places where you can find them :mag_right: :detective:

**Sample Scan ( python Hunter.py --user / -u  username )**
![simple](https://github.com/c0brabaghdad1/Hackers-Hunter/blob/master/image/scan.png)

**Help (python Hunter.py --help / -h )**

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
