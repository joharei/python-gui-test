import numpy as np
from edifice import component
from edifice.extra.matplotlib_figure import MatplotlibFigure
from matplotlib.axes import Axes


@component
def GraphScreen(self):
    def plot_fun(ax: Axes):
        time_range = np.linspace(-10, 10, num=120)
        ax.plot(time_range, np.sin(time_range))

    MatplotlibFigure(plot_fun=plot_fun)
