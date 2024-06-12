from matplotlib.figure import Figure, FigureBase
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

import pandas as pd

# Models
from topsis import Topsis


class Irr:

    def __init__(self, topsis: Topsis) -> None:
        # Receive topsis rankings
        self.topsis = topsis

        # Yearly income data
        self.initial_years: list = [2019, 2020, 2021, 2022, 2023]
        self.years: list = [2024, 2025]
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

    def __train_irr_regression_model__(self, no_topsis_score: float) -> tuple:
        # Create dummy df to train model
        df_irr: pd.DataFrame = pd.DataFrame({
            'average_adjusted': [period * no_topsis_score for period in self.average_adjusted],
            'years': self.initial_years
        })

        X: pd.DataFrame = df_irr[['years']]
        y: pd.Series = df_irr['average_adjusted']

        # Create polynomial characteristics of 3 degree
        poly: PolynomialFeatures = PolynomialFeatures(degree=3)
        X_poly: pd.Series = poly.fit_transform(X)

        # Create the linear regression model
        model: LinearRegression = LinearRegression()

        # Train the model with the polynomial characteristics
        model.fit(X_poly, y)

        # Create new predictions
        y_predict: list = [[float(model.predict(poly.transform([[year]]))[0]) for year in self.years]][0]

        return list(df_irr['average_adjusted']), y_predict

    def create_graph_fig(self, topsis_rank: int) -> Figure:
        # Get ranked municipio
        no_topsis_score: float = float(self.topsis.df[self.topsis.df['Rank'] == topsis_rank]['Topsis Score'])
        new_average_adjusted, y_predict = self.__train_irr_regression_model__(no_topsis_score)
        # Create a matplotlib fig
        fig: Figure = Figure(figsize=(8, 3), dpi=100)
        ax: FigureBase = fig.add_subplot(111)

        # Plot data
        ax.plot(self.initial_years, new_average_adjusted, marker='o')
        ax.plot(self.initial_years[-1:] + self.years, new_average_adjusted[-1:] + y_predict, marker='o')

        # Set graph params
        ax.set_xlabel('Years')
        ax.set_ylabel('Average Revenue (in billion USD)')
        ax.set_title('Estimated Average Annual Revenue of Car Manufacturing Factory')
        ax.legend()
        ax.grid(True)
        ax.tick_params(axis='x', rotation=45)

        # Adjust layout
        fig.tight_layout()

        return fig
