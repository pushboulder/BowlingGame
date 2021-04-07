from django import template

register = template.Library()


@register.filter
def pins_dict(available_pins):
    """ Alters the basic pins dictionary into a list of
        dictionaries included context for disabling their buttons.

    :param available_pins: Dictionary from GameStyle context
    :type available_pins: dict[int, bool]
    :return: Dictionary with the data split into lists for styling
    :rtype: dict[int, list[dict[str, int or str]]]
    """
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
    """ Forms the dictionary for a single pin button

    :param pin_id: The id and value of a pin
    :type pin_id: int
    :param available: Determination of button disablement
    :type available: bool
    :return: Dictionary with id and disabled
    :rtype: dict[str, int or str]
    """
    pin_dict = {
        'id': pin_id,
        'disabled': '' if available else 'disabled'
    }
    return pin_dict
