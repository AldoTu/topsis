class Municipio:
    def __init__(self,
                 name: str = '',
                 tech_infra: float = 0.,
                 green_transportation: float = 0.,
                 environment: float = 0.,
                 public_services_quality: float = 0.,
                 economy: float = 0.,
                 citizen_participation: float = 0.,
                 security: float = 0.,
                 gen_characterization: float = 0.,
                 socioeconomic: float = 0.
                 ) -> None:
        self.name: str = name
        self.tech_infra: float = tech_infra
        self.green_transportation: float = green_transportation
        self.environment: float = environment
        self.public_services_quality: float = public_services_quality
        self.economy: float = economy
        self.citizen_participation: float = citizen_participation
        self.security: float = security
        self.gen_characterization: float = gen_characterization
        self.socioeconomic: float = socioeconomic

    # Function to transform object to tuple
    def get_municipio_as_tuple(self) -> tuple:
        return (self.name, self.tech_infra, self.green_transportation, self.environment, self.public_services_quality,
                self.economy, self.citizen_participation, self.security, self.gen_characterization, self.socioeconomic)
