from edifice import component, VBoxView, Label, TabView

from ui.features.graph.graph_screen import GraphScreen
from ui.features.table.table_screen import TableScreen


@component
def MainWindow(self):
    label_style = {
        "margin-top": 24,
        "margin-bottom": 24,
        "margin-left": 16,
        "margin-right": 16,
    }
    tab_view_style = {"padding": 16}

    with VBoxView():
        Label("Some text", style=label_style)
        with TabView(labels=["Table", "Graph"], style=tab_view_style):
            TableScreen()
            GraphScreen()
