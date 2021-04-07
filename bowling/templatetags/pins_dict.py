from django import template

register = template.Library()


@register.filter
def pins_dict(available_pins):
    pins = {}
    index = 0
    for pin_id, available in available_pins.items():
        if pins.get(index, None) is None:
            pins[index] = []
        pins[index].append(
            get_dict(pin_id, available)
        )
        if pin_id % 3 == 0:
            index += 1
    return pins


def get_dict(pin_id, available):
    pin_dict = {
        'id': pin_id,
        'disabled': '' if available else 'disabled'
    }
    return pin_dict
