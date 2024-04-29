from skcriteria.agg import similarity  # here lives TOPSIS
from skcriteria.agg._agg_base import RankResult
from skcriteria.pipeline import mkpipe  # this function is for create pipelines
from skcriteria.preprocessing import invert_objectives, scalers
from skcriteria import mkdm

# Models
from models.municipio_stack import MunicipioStack


class Topsis:

    def __init__(self, municipio_stack: MunicipioStack) -> None:
        self.municipio_stack = municipio_stack
        self.__create_matrix__()
        self.objectives: list = [max, max, min, min]
        self.weights: list = [0.5, 0.05, 0.45, 0.45]
        self.__create_alternatives__()
        self.criteria: list = ["Transporte público eficiente y ecológico", "Red de ciclovías y peatonales",
                               "Accesibilidad y movilidad inclusiva", "Minimización del tráfico"]
        self.__create_decision_matrix__()
        self.pipe: mkpipe = mkpipe(
            invert_objectives.NegateMinimize(),
            scalers.VectorScaler(target="matrix"),  # this scaler transform the matrix
            scalers.SumScaler(target="weights"),  # and this transform the weights
            similarity.TOPSIS(),
        )

    def __create_matrix__(self) -> None:
        self.matrix: list = [[municipio.transportation, municipio.pedestrian_networks, municipio.accessibility,
                              municipio.traffic] for municipio in self.municipio_stack.municipios]

    def __create_alternatives__(self) -> None:
        self.alternatives: list = [municipio.name for municipio in self.municipio_stack.municipios]

    def __create_decision_matrix__(self) -> None:
        self.dm = mkdm(
            self.matrix,
            self.objectives,
            weights=self.weights,
            alternatives=self.alternatives,
            criteria=self.criteria,
        )

    def rank(self) -> RankResult:
        rank = self.pipe.evaluate(self.dm)
        print(rank)
        return rank
