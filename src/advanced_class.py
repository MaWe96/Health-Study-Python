import pandas as pd, numpy as np, matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA

class ComplexHandler:
    """
    Här definieras en mer detaljerad klass, kapabel av mera analys med hälsodatans kolumner, som är:
    [df.age, df.height, df.weight, df.systolic_bp, df.cholesterol, df.disease]
    
    Lista med Attribut:
    - data (pd.DataFrame)       - Bearbeta numerisk data presentabelt.
    - explanatory variables []  - Analysens förklarande variabler.
    - target variable (str)     - Systoliskt blodtryck.
    - metod 1                   - Multipel linjär regression med scikit.
    - metod 2                   - Principal Component Analysis med numpy och scikit.

    Lista av ComplexHandler kapaciteter:
    - Summera & presentera DataFrame med vanliga statistiska mått.
    - Multipel linjär regression med scikit, och PCA med både numpy och scikit.
    - Facilitera, lagra och visa grafer.
    """

    def __init__(self, df):
        """
        Standard initialisering av objektet, skapar tomma variabler för andra funktioner i klassen,
        och behöver att klassens initialisering kallas med hälsodatans df.
        """
        self.df = df                        # tilldelar df till objektet
        self.normal_statistics = None       # tom variabel
        self.choice_of_regression = None
        self.results_of_regression = {}     # tom dictionary
        self.results_of_PCA = {}


    def assign_metric_calculations(self):
        """
        Gör aggregering med flera typer av beräkningar på flera kolumner, och tilldela objektet 
        dataframe form av output. Istället som i del1 med DataFrame och manuella calculated entries,
        görs här en DataFrame med .agg().
        """
        calculations = ['mean', 'median', 'min', 'max']
        self.normal_statistics = np.round(
            self.df[['age', 'weight', 'height', 'systolic_bp', 'cholesterol']]
            .agg(calculations), 2)
        return self.normal_statistics # lagra in i objektet


    def assign_multiple_regression(self):
        """
        Utför multipel regression som ska förutspå blodtryck via ålder och vikt, och output inkluderar:
        - skärningspunkt på y-axeln
        - koefficienter för ålder och vikt
        - förklarad varians R^2
        - rester
        """
        X_regr = self.df[["age","weight"]].values
        y = self.df["systolic_bp"].values
        method = LinearRegression()
        method.fit(X_regr, y)
        y_prediction = method.predict(X_regr)

        self.choice_of_regression = method
        self.results_of_regression = {
            "intercept": method.intercept_,
            "coefficients": method.coef_,
            "R2_score": method.score(X_regr, y),
            "y_prediction": y_prediction,
            r"residuals $y-\hat{y}$": y - y_prediction
        }
        return self.results_of_regression # lagra in i objektet


    def draw_multregression_after_assigned(self):
        """
        Plottar scatterplots av äkta vs förutspådda värden via multipel regression via scikit, även rester.
        Denna plot funktionen returnerar även fig & axes[0] + axes[1] ifall graferna önskas presenteras i 
        notebooken på övriga sätt.
        """
        y_prediction = self.results_of_regression["y_prediction"]
        residuals = self.results_of_regression[r"residuals $y-\hat{y}$"]
        y = self.df["systolic_bp"].values

        fig, axes = plt.subplots(1,2, figsize=(13,5))
        axes[0].scatter(y, y_prediction, alpha=0.6)
        axes[0].plot([y.min(), y.max()], [y.min(), y.max()], color="black", linestyle="-")
        axes[0].set_xlabel("Äkta blodtryck data")
        axes[0].set_ylabel("Förutspådda blodtryck data")
        axes[0].set_title("Äkta vs. förutspådda datapunkter")

        axes[1].scatter(y_prediction, residuals, alpha=0.6, color="purple")
        axes[1].axhline(0, color='black', linestyle='-.')
        axes[1].set_xlabel("Predicerade värden")
        axes[1].set_ylabel(r"Residualer ($y - \hat{y}$)")
        axes[1].set_title("Residualanalys")
        axes[1].grid(True, linestyle="--")
        
        fig.tight_layout()
        
        return fig, axes # gör att man kallar denna funktionen i notebooken såhär:
        #                fig, axes = <instance>.draw_multiregression_after_assigned()



    def assign_PCA(self, n_components=3):
        """
        Utför PCA utefter df som initialiserats på age, weight, height, systolic_bp, cholesterol.
        Beräknar både scikit-learn och numpy version.
        Denna funktionen ger komponenter, R^2, egenvektorer + värden gällande numpy.
        """
        PCA_X = self.df[['age', 'weight', 'height', 'systolic_bp', 'cholesterol']].values
        PCA_X_centered = PCA_X - PCA_X.mean(axis=0)
        method = PCA(n_components=n_components)
        PCA_parts = method.fit_transform(PCA_X)

        covariance_matrix = np.cov(PCA_X_centered, rowvar=False)
        eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)
        parts_numpy = PCA_X_centered @ eigen_vectors[:, :n_components]

        self.results_of_PCA = {
            "scikit": {
                "components": method.components_, "explained_variance": method.explained_variance_, "parts_scikit": PCA_parts},
            "numpy": {
                "eigen_vectors": eigen_vectors[:, :n_components], "eigen_values": eigen_values, "parts_numpy": parts_numpy}
        }
        return self.results_of_PCA


    def draw_PCA_after_assigned(self, component_x=0, component_y=1):
        """
        Visar upp en punktdata graf efter objektet har tilldelats PCA beräkningar.
        x och y-axlarna på grafen visar två olika huvudkomponenter.
        """
        scikit_parts = self.results_of_PCA["scikit"]["parts_scikit"]
        sick_colors = self.df.disease.map({0:"teal",1:"darkred"})
        plt.figure()
        plt.scatter(scikit_parts[:,component_x], scikit_parts[:,component_y], c=sick_colors, alpha=0.6)
        plt.xlabel(f"Varians för sörsta komponenten")
        plt.ylabel("Varians för näst största komponenten")
        plt.title("Störst komponent varians riktning (blågrön) vs näst störst (mörkröd)")
        plt.grid(True, linestyle="--")
        plt.tight_layout()
        plt.show() # Visar graf i notebooken utan att behöva return figure som i draw_multregression_after_assigned.