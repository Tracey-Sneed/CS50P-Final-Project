
class cities:
    def __init__(self):
        self._cities = []
        #the list of cities being accessed by graph_menu

    def __str__(self):
        chosen = ""
        for city in self._cities:
            chosen += "\n" + city
        return f"You have selected the following: {chosen.strip(', ')}"


    def length(self):
        return len(self)

    @property
    def cities(self):
        return self._cities
