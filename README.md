# VGMdb-to-Mp3tag
## Description & Features
Converts detailed track-based composer, arranger and lyricist credits as often found in the "Notes" section of [VGMdb](https://vgmdb.net/) to a text file that is readable by music tagging software like [Mp3tag](https://www.mp3tag.de/en/).

**Example:**  
The following input (taken from the [FFVII Rebirth Vinyl Soundtrack](https://vgmdb.net/album/132684)):

>Composition:  
>  Nobuo Uematsu (1, 2, 4, 5, 9)  
>  Shotaro Shima (3, 9)  
>  Yoshinori Nakamura (6-8)  
>
>Arrangement:  
>  Shotaro Shima (1-5, 9)  
>  Yoshinori Nakamura (6-8)

returns the tags:

|Track|Artist|Composer|Arranger|
|----|----|----|----|
|1|Shotaro Shima (Nobuo Uematsu)|(Nobuo Uematsu)|Shotaro Shima|
|2|Shotaro Shima (Nobuo Uematsu)|(Nobuo Uematsu)|Shotaro Shima|
|3|Shotaro Shima|Shotaro Shima|Shotaro Shima|
|...|...|...|...|

that is, using `artist = composer & arranger` (multiple artists supported with correct separation `artist1, artist2 & artist3`) and putting one specified artist in brackets at the end (this may be used when, as in the example, said artist didn't directly contribute to the music but only wrote themes that the tracks are based on).

## Usage
Requires installation of Python and Numpy.

- In the .py file, insert the respective credits as in the example above (without the header line "Composition:" etc.). As of now, only lyricist (but not composer and arranger) may be empty
- Albumname can remain unchanged; this only determines the filename
- Legacy credited artist will be out in brackets as above
- directory must be specified
- Separator can be `()` (brackets must be specified like this!), ` - `, `: `,...
