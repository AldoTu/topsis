class Municipio:
    def __init__(self,
                 name: str = '',
                 transportation: float = 0.,
                 pedestrian_networks: float = 0.,
                 accessibility: float = 0.,
                 traffic: float = 0.
                 ) -> None:
        self.name: str = name
        self.transportation: float = transportation
        self.pedestrian_networks: float = pedestrian_networks
        self.accessibility: float = accessibility
        self.traffic: float = traffic

    # Function to transform object to tuple
    def get_municipio_as_tuple(self) -> tuple:
        return (self.name, self.transportation, self.pedestrian_networks, self.accessibility, self.traffic)
