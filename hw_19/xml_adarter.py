import xml.dom.minidom
from xml.etree import ElementTree
import json
import xmltodict


class Movie:
    def __init__(self,
                 title,
                 format,
                 year,
                 rating,
                 description,
                 category):
        self.title = title
        self.format = format
        self.year = year
        self.rating = rating
        self.description = description
        self.category = category

    @classmethod
    def from_xml(cls, path):
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        movies = []
        for genre in collection:
            for decade in genre:
                for movie in decade:
                    movies.append(cls(
                        movie.attrib['title'],
                        movie.find('format').text,
                        movie.find('year').text,
                        movie.find('rating').text,
                        movie.find('description').text,
                        genre.attrib['category']
                    ))
        return movies

    @classmethod
    def xml_to_line(cls, path):
        tree = ElementTree.parse(path)
        collection = tree.getroot()
        xml_to_line = ElementTree.tostring(collection)
        return xml_to_line


    @classmethod
    def line_to_xml(cls, xml_string):
        xml_file = xml.dom.minidom.parseString(xml_string)
        xml_pretty_str = xml_file.toprettyxml()
        return xml_pretty_str


    @classmethod
    def xml_to_json(cls, path_xml, path_json):
        with open(path_xml) as xml_file:
            data_dict = xmltodict.parse(xml_file.read())
            json_data = json.dumps(data_dict)
            with open(path_json, "w") as json_file:
                json_file.write(json_data)
                json_file.close()


movies = Movie.from_xml("films.xml")
for movie in movies:
    print(movie.title)

movies_to_line = Movie.xml_to_line("films.xml")
print(movies_to_line)

xml_file_from_string = Movie.line_to_xml(Movie.xml_to_line("films.xml"))
print('\n')
print(xml_file_from_string)

Movie.xml_to_json("films.xml", "films.json")
