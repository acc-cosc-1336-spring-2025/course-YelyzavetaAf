def add_inventory(widgets, widget_name, quantity):
    if widget_name in widgets:
        widgets[widget_name] += quantity
    else:
        widgets[widget_name] = quantity


def remove_inventory_widget(widgets, widget_name):
    if widget_name in widgets:
        del widgets[widget_name]
        return 'Record deleted'
    else:
        return 'Item not found'