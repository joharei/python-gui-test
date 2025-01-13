from edifice import component, use_state
from ui.components.tableview import TableView
from ui.features.table.table_view_model import use_table_view_model


@component
def TableScreen(self):
    get_table_model = use_table_view_model()
    table_model, _ = use_state(get_table_model())

    TableView(model=table_model, hide_columns=[0])
