# OSINT
## Dark Social Web
36 solves / 472 points
### Description:

0xDarkArmy has 1 social account and DarkArmy uses the same name everywhere. Hint: The front page of internet

flag format: darkctf{}

---

### Solution:

Searching for the username 0xDarkArmy (for example here: https://whatsmyname.app, and filter by category -> social) returns a result: https://www.reddit.com/user/0xDarkArmy

Scrolling down(if needed), there is a QR code marked as spoiler: https://www.reddit.com/user/0xDarkArmy/comments/iwal85/darkarmy_ctf/

Decoding that QR code gives a url which redirects to onion link: http://cwpi3mxjk7toz7i4.onion<br>
Part of the flag is on /robots.txt: http://cwpi3mxjk7toz7i4.onion/robots.txt<br>
Remaining part is on the response header 'flag' (Developer tools -> Network -> robots.txt -> Response headers).

Complete flag:
`darkctf{S0c1a1_D04k_w3b_051n7}`
