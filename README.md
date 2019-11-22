# ASCII-armor-enhancer

The problem with printing ASCII armored data on a paper is that some characters are looking similarly and this is a prerequisite for OCR errors.

This script is changing some characters with cyrillic and greek characters.

It's recommended to use OCR-friendly fonts like [OCR-A](https://en.wikipedia.org/wiki/OCR-A) and [OCR-B](https://en.wikipedia.org/wiki/OCR-B). The font DejaVu Sans Mono is also good.

You can install them on a Debian-based distribution easy:
```
$ sudo apt-get install fonts-ocr-a fonts-ocr-b fonts-dejavu
```

I don't like that "0" and "O" in the OCR-B font are looking too similar. In DejaVu Sans Mono they can be differantiated by the dot in the zero.

Fonts like "Courier" have too similar characters - "l" is looking like "1".

Translation table:

```
Q ⇨ Я
0 ⇨ θ
l ⇨ л
I ⇨ Д
G ⇨ Ж
```

```
$ enhance-ascii-armor.py --action=encode < test.txt.asc  > test.txt.asc.enhanced
$ gedit test.txt.asc.enhanced 
$ cat test.txt.asc
-----BEGIN PGP MESSAGE-----

jA0ECQMKKEnwbwZvywT/0kQBvTttT+fvKRQk0qz1MRUb3sLM8lisu90LCe8jOgQd
MT1oFmbh4k+1ViD0zqjUd76kMuSCEP+bxx92ykCe3laoIZRquA==
=C3bh
-----END PGP MESSAGE-----
$ cat test.txt.asc.enhanced 
-----BEЖДN PЖP MESSAЖE-----

jAθECЯMKKEnwbwZvywT/θkЯBvTttT+fvKRЯkθqz1MRUb3sLM8лisu9θLCe8jOgЯd
MT1oFmbh4k+1ViDθzqjUd76kMuSCEP+bxx92ykCe3лaoДZRquA==
=C3bh
-----END PЖP MESSAЖE-----
$ enhance-ascii-armor.py --action=decode  < test.txt.asc.enhanced > decoded.asc
$ diff test.txt.asc decoded.asc
$
```
