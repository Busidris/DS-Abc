import requests

class Titanic :
    def __init__(self, data) :

        self.data = data


obj = Titanic("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv")

response = requests.get("https://raw.githubusercontent.com/datasciencedojo/datasets/refs/heads/master/titanic.csv")