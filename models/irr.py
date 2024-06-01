from matplotlib.figure import Figure, FigureBase

# Models
from topsis import Topsis


class Irr:

    def __init__(self, topsis: Topsis) -> None:
        # Receive topsis rankings
        self.topsis = topsis

        # Yearly income data
        self.years: list = [2025, 2026, 2027, 2028, 2029]
        self.volkswagen_revenue = [282.3, 264.0, 287.2, 309.8, 318.3]
        self.toyota_revenue: list = [275.4, 256.5, 279.3, 278.7, 286.2]
        self.stellantis_revenue: list = [197.8, 180.4, 182.4, 195.6, 200.9]
        self.ford_revenue: list = [155.9, 127.1, 136.3, 148.0, 169.8]
        self.gm_revenue: list = [137.2, 122.5, 130.6, 140.0, 169.7]

        # Calculate combined yearly average
        self.average_revenue: list = [(v + t + s + f + g) / 5 for v, t, s, f, g in zip(
            self.volkswagen_revenue,
            self.toyota_revenue,
            self.stellantis_revenue,
            self.ford_revenue,
            self.gm_revenue
        )]

        # Adjust data to start at 0 on Y axis
        self.average_adjusted: list = [value - self.average_revenue[0] for value in self.average_revenue]

    def create_graph_fig(self) -> Figure:
        # Get no. 1 ranked municipio
        no_1_topsis_score: float = self.topsis.df[self.topsis.df['Rank'] == 1]['Topsis Score']
        # Create a matplotlib fig
        fig: Figure = Figure(figsize=(8, 3), dpi=100)
        ax: FigureBase = fig.add_subplot(111)

        # Plot data
        ax.plot(self.years, [period * no_1_topsis_score for period in self.average_adjusted], marker='o')

        # Set graph params
        ax.set_xlabel('Years')
        ax.set_ylabel('Average Revenue (in billion USD)')
        ax.set_title('Average Annual Revenue of Car Manufacturing Factory (2019-2023)')
        ax.legend()
        ax.grid(True)
        ax.tick_params(axis='x', rotation=45)

        # Adjust layout
        fig.tight_layout()

        return fig
