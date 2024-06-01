import pandas as pd


class Topsis:

    def __init__(self, data: dict) -> None:
        self.df = pd.DataFrame.from_dict(data)
        self.weights: list = [0.21, 0.22, 0.18, 0.05, 0.04, 0.21, 0.01, 0.06, 0.02]
        self.__normalize__()
        self.p_sln, self.n_sln = self.__calculate_ideals__()

    # Get number of columns (fixed to 10)
    def __get_number_of_columns__(self) -> int:
        return 10

    # Normalize dataset
    def __normalize__(self) -> None:
        for i in range(1, self.__get_number_of_columns__()):
            rss = 0
            df_len = len(self.df)
            # Calculating Root of Sum of Squares for a particular column
            for j in range(df_len):
                rss += self.df.iloc[j, i] ** 2
            rss = rss ** 0.5
            # Weighted Normalizing a element
            for j in range(df_len):
                self.df.iat[j, i] = (self.df.iloc[j, i] / rss) * self.weights[i - 1]

    # Calculate ideal best and ideal worst
    def __calculate_ideals__(self) -> tuple:
        p_sln = self.df.max().values[1:]
        n_sln = self.df.min().values[1:]
        return p_sln, n_sln

    # Calculating Topsis score
    def rank(self) -> pd.DataFrame:
        score = []  # Topsis score
        pp = []  # distance positive
        nn = []  # distance negative

        # Recalculate ideals
        self.p_sln, self.n_sln = self.__calculate_ideals__()

        # Calculating distances and Topsis score for each row
        for i in range(len(self.df)):
            temp_p, temp_n = 0, 0
            for j in range(1, self.__get_number_of_columns__()):
                temp_p += (self.p_sln[j - 1] - self.df.iloc[i, j]) ** 2
                temp_n += (self.n_sln[j - 1] - self.df.iloc[i, j]) ** 2
            temp_p, temp_n = temp_p ** 0.5, temp_n ** 0.5
            score.append(temp_n / (temp_p + temp_n))
            nn.append(temp_n)
            pp.append(temp_p)

        # Appending new columns in dataset
        self.df['distance positive'] = pp
        self.df['distance negative'] = nn
        self.df['Topsis Score'] = score

        # Calculating the rank according to topsis score
        self.df['Rank'] = (self.df['Topsis Score'].rank(method='max', ascending=False))
        self.df = self.df.astype({"Rank": int})

        return self.df
