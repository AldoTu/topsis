import pandas as pd

# Models
from models.municipio import Municipio

# TOPSIS
from topsis import Topsis


class MunicipioStack:
    def __init__(self, data: dict) -> None:
        self.municipios: list[Municipio] = [Municipio(
            item['name'],
            item['tech_infra'],
            item['green_transportation'],
            item['environment'],
            item['public_services_quality'],
            item['economy'],
            item['citizen_participation'],
            item['security'],
            item['gen_characterization'],
            item['socioeconomic']
        ) for item in data]
        self.topsis: Topsis = Topsis(data)

    # Function to append new 'municipio' to stack
    def append_municipio(self, municipio: dict) -> None:
        self.municipios.append(Municipio(
            municipio['name'],
            municipio['tech_infra'],
            municipio['green_transportation'],
            municipio['environment'],
            municipio['public_services_quality'],
            municipio['economy'],
            municipio['citizen_participation'],
            municipio['security'],
            municipio['gen_characterization'],
            municipio['socioeconomic']
        ))
        #self.topsis.df = self.topsis.df.join(pd.DataFrame(municipio.values(), columns=self.topsis.df.columns))
        self.topsis.df.loc[len(self.topsis.df)] = [v for k, v in municipio.items()] + [None, None, None, None]
        print(self.topsis.df)

    # Read 'municipio' stack
    def print_municipios(self) -> None:
        for municipio in self.municipios:
            print(municipio)
