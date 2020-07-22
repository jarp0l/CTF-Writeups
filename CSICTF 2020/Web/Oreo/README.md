<h1>Oreo</h1>

<h2>Description:</h2>
My nephew is a fussy eater and is only willing to eat chocolate oreo. Any other flavour and he throws a tantrum.

<h5>Given link:</h5> http://chall.csivit.com:30243<br />
<hr>
<h2>Solution:</h2>
<p>Since the challenge had Oreo in title as well as description, I became sure that it was related to cookies. So, I headed over to Local Storage to have a look at the cookies. There was a cookie with the name <code>flavour</code> and value <code>c3RyYXdiZXJyeQ</code> which is the Base64(B64) encoding of <code>strawberry</code>. Silly me, I used the B64 decoded <code>strawberry</code> in the value of <code>flavour</code> and hit refresh several times, but there was no flag. I even fired up Burpsuite to change the value..xD. Later I used <code>curl</code>, again with B64 encoded and decoded values of <code>strawberry</code>. After getting no flag I read the description again and put <code>chocolate</code> in the value of <code>flavour</code>. But it did not work. Then I converted <code>chocolate</code> into B64, which is <code>Y2hvY29sYXRl</code> and assigned this B64 encoded value to <code>flavour</code>, and executed <code>curl</code> again, which returned the flag! The full <code>curl</code> command was:

```bash
curl --cookie "flavour=Y2hvY29sYXRl" http://chall.csivit.com:30243
```
And the flag:
</p>

```
csictf{1ick_twi5t_dunk}
```
