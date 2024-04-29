from models.municipio import Municipio


class MunicipioStack:
    def __init__(self, data: list[any]):
        self.municipios: list[Municipio] = [Municipio(
            item['name'],
            item['transportation'],
            item['pedestrian_networks'],
            item['accessibility'],
            item['traffic']
        ) for item in data]

    # Function to append new 'municipio' to stack
    def append_municipio(self, municipio: Municipio):
        self.municipios.append(municipio)

    # Read 'municipio stack
    def print_municipios(self):
        for municipio in self.municipios:
            print(municipio)
