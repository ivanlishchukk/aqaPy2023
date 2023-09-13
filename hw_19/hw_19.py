from xml.etree import ElementTree

tree = ElementTree.parse("films.xml")
root = tree.getroot()
for movie in root.iter("movie"):
    print(movie.attrib["title"])
    for movie_child in movie.findall("*"):
        print(movie_child.text)
    #movie_child = movie.findall("*")
    #print(movie_child)
    #print(movie.items())
    #print(movie.attrib)
print(root)
