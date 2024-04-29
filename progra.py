import tkinter as tk
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
        transportation: float = float(self.transportation_entry.get())
        pedestrian_networks: float = float(self.pedestrian_networks_entry.get())
        accessibility: float = float(self.accessibility_entry.get())
        traffic: float = float(self.traffic_entry.get())

        # Create 'Municipio' object
        new_municipio: Municipio = Municipio(
            municipio_name,
            transportation,
            pedestrian_networks,
            accessibility,
            traffic
        )

        # Add new 'municipio' to MunicipioStack
        self.municipio_stack.append_municipio(new_municipio)
        self.municipio_stack.print_municipios()

        # Refresh table view
        self.__init_view__()

        # Aquí puedes guardar los datos a un archivo, base de datos, o cualquier otro lugar
        # Por ahora, simplemente los mostraré en una ventana de mensaje (messagebox)
        messagebox.showinfo("¡Datos Guardados!",
                            f"Nombre del Municipio: {municipio_name}\nTransporte público eficiente y ecológico: {transportation}\nRed de ciclovías y peatonales: {pedestrian_networks}\nAccesibilidad y movilidad inclusiva: {accessibility}\nMinimización del tráfico: {traffic}")

    def __init_inputs__(self) -> None:
        # Create the form elements
        # Name input
        ttk.Label(self.add_municipio, text="Nombre del Municipio:").grid(row=0, column=0, sticky="w")
        self.municipio_name_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.municipio_name_entry.grid(row=0, column=1, sticky="we")

        # Transportation input
        ttk.Label(self.add_municipio, text="Transporte público eficiente y ecológico:").grid(row=1, column=0, sticky="w")
        self.transportation_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.transportation_entry.grid(row=1, column=1, sticky="we")

        # Pedestrian networks input
        ttk.Label(self.add_municipio, text="Red de ciclovías y peatonales:").grid(row=2, column=0, sticky="w")
        self.pedestrian_networks_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.pedestrian_networks_entry.grid(row=2, column=1, sticky="we")

        # Accessibility input
        ttk.Label(self.add_municipio, text="Accesibilidad y movilidad inclusiva:").grid(row=3, column=0, sticky="w")
        self.accessibility_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.accessibility_entry.grid(row=3, column=1, sticky="we")

        # Traffic input
        ttk.Label(self.add_municipio, text="Minimización del tráfico:").grid(row=4, column=0, sticky="w")
        self.traffic_entry: ttk.Entry = ttk.Entry(self.add_municipio)
        self.traffic_entry.grid(row=4, column=1, sticky="we")

        # Save button
        save_button: ttk.Button = ttk.Button(self.add_municipio, text="Guardar Alternativa", command=self.__save_data__)
        save_button.grid(row=5, column=1, sticky="e")

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
        # Code for creating table
        for row, municipio in enumerate(self.municipio_stack.municipios):
            # We have always 5 columns
            for column in range(5):
                entry: ttk.Entry = ttk.Entry(self.view_municipios, width=20, font=('Arial', 16, 'bold'))
                entry.grid(row=row, column=column)
                entry.insert(tk.END, municipio.get_municipio_as_tuple()[column])


if __name__ == "__main__":
    filename = 'municipios'
    # Use 'with' to make sure file is closed after read
    with open(filename + '.json') as my_file:
        # Load 'municipio' stack to memory from 'json' file
        municipio_stack: MunicipioStack = MunicipioStack(json.load(my_file)[filename])

    MainApplication(municipio_stack)
