# Get Started

Brutforce a zip file protected with a password.

Ex:
wordlist.txt
```
foo
bar
baz
qux
```
=> Possibilities : foo, bar, baz, qux, foofoo, foobar, foobaz, fooqux, barfoo, barbar...

---

## Prerequisites
```
$ pip3 install tqdm
```

## Run 
```
$ python3 brutforce.py example.zip wordlist.txt 2
```
The last parameter indicate the maximum of word to concatenate.