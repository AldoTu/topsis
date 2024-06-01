from utils.utils import normalize_array

# Models
from models.municipio import Municipio
from models.irr import Irr

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
        self.irr: Irr = Irr(self.topsis)

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

        self.topsis.df.loc[len(self.topsis.df)] = [v for k, v in municipio.items()] + [None, None, None, None]

    # Update municipio in stack and in topsis df
    def update_municipio(self, row: int, values: list) -> None:
        # Normalize array values
        values: list = normalize_array(values)
        # Store updated municipio in same list space
        self.municipios[row] = Municipio(
            values[0],
            values[1],
            values[2],
            values[3],
            values[4],
            values[5],
            values[6],
            values[7],
            values[8],
            values[9]
        )
        self.topsis.df.loc[row] = values + [None, None, None, None]
