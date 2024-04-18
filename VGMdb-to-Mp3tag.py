import numpy as np
import os

# INPUT
albumname = "tags"

# separator between artist and tracks
separator = ""

#Composers
comp_in = """replace with composers"""

#Arrangers
arr_in = """replace with arrangers"""

#Lyricists:
lyr_in="""replace with lyricists"""

#Legacy credited artist
legacy_credit = ""

#directory to save .txt
directory = ""


# PROCESS AND READ INPUT
# reads multiline input to list (1 index per line)
def read_input(text):
    out = []
    for line in text.split("\n"):
        data = line.strip()
        out.append(data)
    return out


# splits artist name and track numbers in two fields of list
def split_by_separator(text):
    if separator == "()":
        out = text.replace(")", "")
        out2 = out.split(" (")
        out3 = [i.strip() for i in out2]
        return out3
    else:
        return text.split(separator)


# split 01~03 into [1,2,3] etc.
def rangesplit(numbers):
    if "~" in numbers:
        splitted = numbers.split("~")
    else:
        splitted = numbers.split("-")
    if len(splitted) == 2:
        a,b = int(splitted[0]),int(splitted[1])
        range = np.linspace(a,b,b-a+1,dtype=int).tolist()
    else:
        range = [int(numbers)]
    return range


# track string to list
def splitter(tracks):
    tracks = tracks.replace(", ",",")
    return tracks.split(",")


# converts string of tracks into list
def tracksplitter(tracks):
    tracks_out = splitter(tracks)
    for i in range(len(tracks_out)):
        tracks_out[i] = rangesplit(tracks_out[i])
    return [x for xs in tracks_out for x in xs]


# comp/arr input to artist list
def text_to_numbers(text):
    artist_and_numbers = read_input(text)
    numbers = []
    for i in range(len(artist_and_numbers)):
        numbers.append(tracksplitter(split_by_separator(artist_and_numbers[i])[1]))
    return numbers


# comp/arr input to number list
def text_to_artist(text):
    artist_and_numbers = read_input(text)
    artist = []
    for i in range(len(artist_and_numbers)):
        artist.append(split_by_separator(artist_and_numbers[i])[0])
    return artist


# creates empty list with variable length
def empty_list(length):
    l = []
    for i in range(length):
        l.append([])
    return l


# find maximum in a list of lists
def nested_max(nested_list):
    list = [x for xs in nested_list for x in xs]
    return int(max(list))


# creates list with artists at the corresponding index
def expand_artists(text):
    artists = text_to_artist(text)
    numbers = text_to_numbers(text)
    num_of_tracks = nested_max(numbers)
    expanded_artists = empty_list(num_of_tracks)
    for i in range(num_of_tracks+1):
        for l in range(len(numbers)):
            if i in numbers[l]:
                if expanded_artists[i-1]==[]:
                    expanded_artists[i-1] = artists[l].replace(", "," & ").split(" & ")
                else:
                    expanded_artists[i-1].extend(artists[l].replace(", "," & ").split(" & "))
    return expanded_artists


# remove duplicates in a list of lists
def remove_dups(nested_list):
    new_list = []
    for sublist in nested_list:
        new_sublist = []
        for name in sublist:
            if name not in new_sublist:
                new_sublist.append(name)
        new_list.append(new_sublist)
    return new_list


# converts a list to string list[0], list[1],..., list[n-1] & list[n]
def artist_separators(sublist):
    num_of_artists = len(sublist)
    artist = ""
    if num_of_artists==0:
        artist = ""
    elif num_of_artists==1:
        artist = sublist[0]
    elif num_of_artists==2:
        artist = sublist[0]+" & "+sublist[1]
    else:
        artist = sublist[0]
        for i in range(1,num_of_artists-1):
            artist+=", "+sublist[i]
        artist+=" & "+sublist[num_of_artists-1]
    return artist


# converts list of list to list of strings with legacy artist credited in parentheses
def legacy_artist_separators(nested_list):
    artist_out=[]
    for sublist in nested_list:
        if legacy_credit != "":
            if legacy_credit in sublist:
                sublist.remove(legacy_credit)
                artist=artist_separators(sublist)+" ("+legacy_credit+")"
            else:
                artist=artist_separators(sublist)
        else:
            artist = artist_separators(sublist)
        artist_out.append(artist.strip())
    return artist_out


# join two lists of lists
def join_lists(list1,list2):
    l = len(list1)
    joined=[]
    for i in range(l):
        joined.append(list1[i]+list2[i])
    return joined



# WRITE TO FILE
list_arranger=expand_artists(arr_in)
list_composer=expand_artists(comp_in)

len_arr = len(list_arranger)
len_comp = len(list_composer)

if len_arr <= len_comp:
    list_arranger.extend([[]] * (len_comp - len_arr))
else:
    list_composer.extend([] * (len_arr - len_comp))

list_artist = join_lists(list_composer,list_arranger)

arranger = legacy_artist_separators(remove_dups(list_arranger))
composer = legacy_artist_separators(remove_dups(list_composer))
artist = legacy_artist_separators(remove_dups(list_artist))

filename = os.path.join(directory,albumname+".txt")
s = "  -  "

if lyr_in != "":
    list_lyricist=expand_artists(lyr_in)

    len_lyr = len(list_lyricist)

    if len_lyr < len_comp:
        list_lyricist.extend([[]] * (len_comp - len_lyr))

    lyricist = legacy_artist_separators(remove_dups(list_lyricist))

    f = open(filename, "w")

    for i in range(len(artist)):
        f.write(artist[i] + s + composer[i] + s + arranger[i] + s + lyricist[i] + "\n")
    f.close()

    print("File name:\n"+filename)
    print("\nFormat String: \n%artist%  -  %composer%  -  %arranger%  -  %lyricist%")
else:
    f = open(filename, "w")

    for i in range(len(artist)):
        f.write(artist[i] + s + composer[i] + s + arranger[i] + "\n")
    f.close()

    print("File name:\n" + filename)
    print("\nFormat String: \n%artist%  -  %composer%  -  %arranger%")
