# En klass som beräknar statistik och ritar grafer (med plotter.py och summary.py i src paketet)

# importera dataclass, lite mindre robust men lättare skriven.
from dataclasses import dataclass
import pandas as pd, matplotlib.pyplot as plt

# importera summary och plotter funktionerna inuti src paketet
from .summary import summary
from .plotter import make_plots

@dataclass
class Analysis_class:
    """
    Create an object with attributes numeric summary and making 3 plots.
    """
    df: pd.DataFrame

    def assign_plots(self):
        """
        Uses "plotter.py" functions to assign attribute to Analysis_class object.
        """
        make_plots(self.df)

    def assign_summary(self):
        """
        Uses "summary.py" function to assign a DataFrame attribute to Analysis_class object.
        """
        return summary(self.df)
