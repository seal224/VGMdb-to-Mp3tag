# VGMdb-to-Mp3tag
## Description & Features
Converts detailed track-based composer, arranger and lyricist credits as often found in the "Notes" section of [VGMdb](https://vgmdb.net/) to a text file that is readable by music tagging software like [Mp3tag](https://www.mp3tag.de/en/). Additionally, an artist tag is generated in the form composer(s) & arranger(s). The program supports multiple artist input separated by `,` and/or `&` and returns the output in the form `artist1, artist2 & artist3`. 

**Example:**  
The following input:

>Composition:  
>  John & Charlie (1,2,5)  
>  Jane (2-4)  
>  Alice (5)

>Arrangement:  
>  Bob (1,4,5)  
>  John (2,3)

returns the tags:

|Track|Artist|Composer|Arranger|
|----|----|----|----|
|1|John, Charlie & Bob|John & Charlie|Bob|
|2|John, Charlie & Jane|John, Charlie & Jane|John|
|3|Jane & John|Jane|John|
|4|Jane & Bob|Jane|Bob|
|5|John, Charlie, Alice & Bob|John, Charlie & Alice|Bob|

If, for example, this is a soundtrack of a game's sequel and Alice composed the first game's main theme but didn't directly work on the sequel (in this case, track 5 would be using the first game's theme), she may be credited differently in brackets (see legacy credit in Usage):

|Track|Artist|Composer|Arranger|
|----|----|----|----|
|...|...|...|...|
|5|John, Charlie & Bob (Alice)|John & Charlie (Alice)|Bob|


## Usage
Requires installation of Python and the Numpy module.

- In the .py file, insert the respective credits as in the example above (without the header line "Composition:" etc.). As of now, only lyricist (but not composer and arranger\*) may be empty
- Albumname can remain unchanged; this only determines the filename
- Legacy credited artist will be out in brackets as above
- directory must be specified
- Separator can be `()` (brackets must be specified like this!), ` - `, `: `,...

\*One can enter `[separator](1)`, e.g. `: (1)` as arranger; this will produce empty arranger tags on all tracks.
