from .unit_seperator import is_unit_convertible, get_unit_value

def _component_filter_type(component: str, type) -> bool:
    try:
        type(component)
        return True
    except ValueError:
        return False
    
_ends_with_numerical = ["0","1","2","3","4","5","6","7","8","9"]

_component_filter = {   "IsInteger" : lambda component: _component_filter_type(component, int),
                        "PositiveInteger": lambda component: _component_filter_type(component, int) and int(component) > 0,
                        "NegativeInteger": lambda component: _component_filter_type(component, int) and int(component) < 0,
                        "IsFloat" : lambda component: _component_filter_type(component, float),
                        "PositiveFloat": lambda component: _component_filter_type(component, float) and float(component) > 0,
                        "NegativeFloat": lambda component: _component_filter_type(component, float) and float(component) < 0,
                        "IsUnitConvertible" : lambda component: is_unit_convertible(component),
                        "PositiveUnitConvertible" : lambda component: is_unit_convertible(component) and get_unit_value(component) > 0,
                        "NegativeUnitConvertible" : lambda component: is_unit_convertible(component) and get_unit_value(component) < 0,
                        "MustBeEnergy" : lambda component: any([component.endswith(a) for a in ["eV","meV","ueV","Hz"]+_ends_with_numerical]),
                        "MustBeTime" : lambda component: any([component.endswith(a) for a in ["s","ms","mus","ns","ps","fs"]+_ends_with_numerical]),
                        "NotEmpty" : lambda component: len(component) > 0,
                     }

def component_filter(component: str, default: str, callback = None, *args) -> str:
    for arg in args:
        if arg not in _component_filter:
            raise ValueError(f"Unknown component filter: {arg}")
        f = _component_filter[arg]
        if not f(component):
            if callback is not None:
                callback()
            return default
    return component

if __name__ == "__main__":
    print("Available Filters:")
    print(_component_filter.keys())
    print(f"This file ({__file__}) is part of the QDaCC GUI and should be imported, not executed.")