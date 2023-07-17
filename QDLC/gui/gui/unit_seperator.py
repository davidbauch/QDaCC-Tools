# Seperates a value from its unit
# Units trailable include:
# s,ms,mus,ns,ps,fs
# Hz, eV, meV, mueV
# pi


def seperate_unit(value: str):
    hbar = 1.0545718E-34
    electron_charge = 1.60217662E-19
    one_over_hbare = 1/6.582119516885722624e-16
    units_trail = ["ms","mus","ns","ps","fs","Hz","meV","mueV","pi","eV","s","nm","mum","hbar"]
    scalings_unit = {"s" : 1, "ms" : 1E-3, "mus" : 1E-6, "ns" : 1E-9, "ps" : 1E-12, "fs" : 1E-15, "Hz" : 1, "eV" : one_over_hbare, "meV" : one_over_hbare*1E-3, "mueV" : one_over_hbare*1E-6, "pi" : 1, "nm" : 1E-9, "mum" : 1E-6, "hbar" : hbar}
    if not any( [a in value for a in units_trail] ):
        return value,"",1
    index = [i for i,a in enumerate(units_trail) if value.endswith(a)]
    if len(index) == 0:
        return value,"",1
    index = index[0]
    unit = units_trail[index]
    value = value.replace( unit, "" )
    return value, unit, scalings_unit[unit]

def get_unit_value(value: str):
    v,_,_ = seperate_unit(value)
    return float(v)
def get_unit(value: str):
    _,u,_ = seperate_unit(value)
    return u
def get_unit_scaling(value: str):
    _,_,s = seperate_unit(value)
    return float(s)
def get_uv_scaled(value: str):
    v,_,s = seperate_unit(value)
    return float(v)*float(s)

def is_unit_convertible(value: str):
    try:
        s = get_uv_scaled(value)
        float(s)
        return True
    except ValueError:
        print(f"Input {value} is not unit convertible.")
        return False

if __name__ == "__main__":
    print(f"This file ({__file__}) is part of the QDaCC GUI and should be imported, not executed.")