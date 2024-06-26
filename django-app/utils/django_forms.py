def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()


def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


def add_class(field, class_val):
    add_attr(field, 'class', class_val)


def add_id(field, id_val):
    add_attr(field, 'id', id_val)
