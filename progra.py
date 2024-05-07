import tkinter as tk
import pandas as pd
from tkinter import ttk, messagebox
import json

# Models
from models.municipio_stack import MunicipioStack
from models.municipio import Municipio


class MainApplication:
    def __init__(self, municipio_stack: MunicipioStack) -> None:
        self.municipio_stack: MunicipioStack = municipio_stack
        self.root: tk.Tk = tk.Tk()
        self.root.title('Análisis de Municipios en México')
        self.__create_tabs__()
        self.__init_inputs__()
        self.__init_view__()
        self.root.mainloop()

    def __save_data__(self) -> None:
        municipio_name: str = self.municipio_name_entry.get()
        tech_infra: float = float(self.tech_infra_entry.get())
        green_transportation: float = float(self.green_transportation_entry.get())
        environment: float = float(self.environment_entry.get())
        public_services_quality: float = float(self.public_services_quality_entry.get())
        economy: float = float(self.economy_entry.get())
        citizen_participation: float = float(self.citizen_participation_entry.get())
        security: float = float(self.security_entry.get())
        gen_characterization: float = float(self.gen_characterization_entry.get())
        socioeconomic: float = float(self.socioeconomic_entry.get())

        # Create 'Municipio' object
        new_municipio: dict = {
            "name": municipio_name,
            "tech_infra": tech_infra,
            "green_transportation": green_transportation,
            "environment": environment,
            "public_services_quality": public_services_quality,
            "economy": economy,
            "citizen_participation": citizen_participation,
            "security": security,
            "gen_characterization": gen_characterization,
            "socioeconomic": socioeconomic
        }

        # Add new 'municipio' to MunicipioStack
        self.municipio_stack.append_municipio(new_municipio)

        # Refresh table view
        self.__init_view__()

        # Aquí puedes guardar los datos a un archivo, base de datos, o cualquier otro lugar
        # Por ahora, simplemente los mostraré en una ventana de mensaje (messagebox)
        messagebox.showinfo("¡Datos Guardados!",
                            f"Nombre del Municipio: {municipio_name}\n" +
                            f"Infraestructura Tecnológica: {tech_infra}\n" +
                            f"Movilidad Sostenible: {green_transportation}\n" +
                            f"Sostenibilidad Ambiental: {environment}\n" +
                            f"Calidad de Servicios Públicos: {public_services_quality}"
                            f"Economía y Oportunidades de Mejora Económica en el Tiempo: {economy}\n" +
                            f"Participación Ciudadana: {citizen_participation}\n" +
                            f"Seguridad y Bienestar Social: {security}\n" +
                            f"Caracterización Generacional: {gen_characterization}\n" +
                            f"Variables socioeconómicas asociadas con el Modelo propuesto: {socioeconomic}\n"
                            )

    def __init_inputs__(self) -> None:
        # Create the form elements
        # Name input
        ttk.Label(self.add_municipio, text="Nombre del Municipio:").grid(row=0, column=0, sticky="w")
        self.municipio_name_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.municipio_name_entry.grid(row=0, column=1, sticky="we")

        # Tech infra input
        ttk.Label(self.add_municipio, text="Infraestructura Tecnológica:").grid(row=1, column=0, sticky="w")
        self.tech_infra_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.tech_infra_entry.grid(row=1, column=1, sticky="we")

        # Green transportation input
        ttk.Label(self.add_municipio, text="Movilidad Sostenible:").grid(row=2, column=0, sticky="w")
        self.green_transportation_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.green_transportation_entry.grid(row=2, column=1, sticky="we")

        # Environment input
        ttk.Label(self.add_municipio, text="Sostenibilidad Ambiental:").grid(row=3, column=0, sticky="w")
        self.environment_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.environment_entry.grid(row=3, column=1, sticky="we")

        # Public services quality input
        ttk.Label(self.add_municipio, text="Calidad de Servicios Públicos:").grid(row=4, column=0, sticky="w")
        self.public_services_quality_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.public_services_quality_entry.grid(row=4, column=1, sticky="we")

        # Economy input
        ttk.Label(self.add_municipio, text="Economía y Oportunidades de Mejora Económica en el Tiempo:").grid(
            row=5, column=0, sticky="w")
        self.economy_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.economy_entry.grid(row=5, column=1, sticky="we")

        # Citizen participation input
        ttk.Label(self.add_municipio, text="Participación Ciudadana:").grid(row=6, column=0, sticky="w")
        self.citizen_participation_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.citizen_participation_entry.grid(row=6, column=1, sticky="we")

        # Security input
        ttk.Label(self.add_municipio, text="Seguridad y Bienestar Social:").grid(row=7, column=0, sticky="w")
        self.security_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.security_entry.grid(row=7, column=1, sticky="we")

        # Generational characterization input
        ttk.Label(self.add_municipio, text="Caracterización Generacional:").grid(row=8, column=0, sticky="w")
        self.gen_characterization_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.gen_characterization_entry.grid(row=8, column=1, sticky="we")

        # Socioeconomic input
        ttk.Label(self.add_municipio, text="Variables socioeconómicas asociadas con el Modelo propuesto:").grid(
            row=9, column=0, sticky="w")
        self.socioeconomic_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.socioeconomic_entry.grid(row=9, column=1, sticky="we")

        # Save button
        save_button: ttk.Button = ttk.Button(self.add_municipio, text="Guardar Alternativa", command=self.__save_data__)
        save_button.grid(row=10, column=1, sticky="e")

        # Make the second column stretchable
        self.root.columnconfigure(1, weight=1)

    def __create_tabs__(self) -> None:
        # Creating notebook
        tab_control: ttk.Notebook = ttk.Notebook(self.root)
        # Creating tabs
        self.add_municipio: ttk.Frame = ttk.Frame(tab_control)
        self.view_municipios: ttk.Frame = ttk.Frame(tab_control)
        # Adding tabs to notebook
        tab_control.add(self.add_municipio, text='Agregar Municipio')
        tab_control.add(self.view_municipios, text='Visualizar Municipios')
        # Packing notebook
        tab_control.pack(expand=1, fill="both")

    def __init_view__(self) -> None:
        # Reset frame
        for widget in self.view_municipios.winfo_children():
            widget.destroy()

        # Code for creating table
        for row, municipio in enumerate(self.municipio_stack.municipios):
            # We have always 10 columns
            for column in range(10):
                entry: ttk.Entry = ttk.Entry(self.view_municipios, width=20, font=('Arial', 16, 'bold'))
                entry.grid(row=row, column=column)
                entry.insert(tk.END, municipio.get_municipio_as_tuple()[column])

        # Recalculate button
        recalculate_button_row = len(self.municipio_stack.municipios)
        recalculate_button: ttk.Button = ttk.Button(self.view_municipios, text="Recalcular ranking", command=self.__init_view__)
        recalculate_button.grid(row=recalculate_button_row, column=0, sticky="e")

        # Show table
        rank: pd.DataFrame = self.municipio_stack.topsis.rank()
        rank_row = recalculate_button_row + 1
        ttk.Label(self.view_municipios, text=f"{rank[['name']].to_string(index=False)}").grid(row=rank_row, column=0,
                                                                                              sticky="w")
        ttk.Label(self.view_municipios, text=f"{rank[['Rank']].to_string(index=False)}").grid(row=rank_row, column=1,
                                                                                              sticky="w")


if __name__ == "__main__":
    filename = 'municipios'
    # Use 'with' to make sure file is closed after read
    with open(filename + '.json') as my_file:
        # Load 'municipio' stack to memory from 'json' file
        json_data = json.load(my_file)[filename]
        municipio_stack: MunicipioStack = MunicipioStack(json_data)

    MainApplication(municipio_stack)
