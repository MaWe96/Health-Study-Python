# En klass som beräknar statistik och ritar grafer (med plotter.py och summary.py i src paketet)

# importera dataclass, lite mindre robust men lättare skriven.
from dataclasses import dataclass
import pandas as pd

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
        make_plots(self.df)

    def assign_summary(self):
        return summary(self.df)
