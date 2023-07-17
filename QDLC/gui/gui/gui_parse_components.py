from .unit_seperator import  get_uv_scaled, get_unit, get_unit_value

def _parse_electronic_system(components: dict, escape_symbol: str = "'", callback = None) -> str:
    ret = ""
    for level in sorted(components["EnergyLevels"].values(), key = lambda a: get_uv_scaled(a["Energy"])):
        n,e,d,c,p,to = level["Name"], level["Energy"], level["DephasingScaling"], level["DecayScaling"], level["PhononScaling"], ",".join(level["CoupledTo"]) if level["CoupledTo"] != (None,) and len(level["CoupledTo"]) > 0 else "-"
        ret += f"{n}:{e}:{to}:{c}:{d}:{p};"
    return f"--SE {escape_symbol}{ret[:-1]}{escape_symbol}"

def _parse_cavity_system(components: dict, escape_symbol: str = "", callback = None) -> str:
    ret = ""
    for cavity in sorted(components["CavityLevels"].values(), key = lambda a: get_uv_scaled(a["Energy"])):
        n,e,t,ts,ds,p = cavity["Name"], cavity["Energy"], ",".join(cavity["CoupledTo"]), ",".join([str(a) for a in cavity["CoupledToScalings"]]), cavity["DecayScaling"], cavity["PhotonNumber"]
        ret += f"{n}:{e}:{p}:{t}:{ts}:{ds};"
    if len(ret) > 0:
        return f"--SO {escape_symbol}{ret[:-1]}{escape_symbol}"
    return ret

def _parse_pulse_system(components: dict, escape_symbol: str = "", callback = None) -> str:
    ret = ""
    for pulse in components["Pulse"].values():
        n,ct,a,f,c,w,t = pulse["Name"], pulse["CoupledTo"], pulse["Amplitudes"], pulse["Frequencies"], pulse["Centers"], pulse["Widths"], pulse["Type"]
        a,f,c,w,t = ",".join(a), ",".join(f), ",".join(c), ",".join(w), ",".join(t)
        ret += f"{n}:{','.join(ct)}:{a}:{f}:{w}:{c}:{t};"
    if len(ret) > 0:
        return f"--SP {escape_symbol}{ret[:-1]}{escape_symbol}"
    return ret

def _parse_shift_system(components: dict, escape_symbol: str = "", callback = None) -> str:
    ret = ""
    for shift in components["Shift"].values():
        n,t,a,k,s,sc = shift["Name"], shift["Times"], shift["Amplitudes"], shift["Type"], shift["CoupledTo"], shift["CoupledToScalings"]
        ret += f"{n}:{','.join(s)}:{','.join(sc)}:{','.join(a)}:{','.join(t)}:{k};"
    if len(ret) > 0:
        return f"--SC {escape_symbol}{ret[:-1]}{escape_symbol}"
    return ret

def _parse_config_time(components: dict, escape_symbol: str = "", callback = None) -> str:
    t = components["ConfigTime"]
    if t["Start"] == "0" and t["End"] == "auto" and t["Step"] == "auto":
        return ""
    rtend = t["End"] if t["End"] != "auto" else -1
    rtstep = t["Step"] if t["Step"] != "auto" else -1
    return f"--time {t['Start']} {rtend} {rtstep}"

def _parse_config_tolerances(components: dict, escape_symbol: str = "", callback = None) -> str:
    ret = ""
    if "ConfigTolerances" in components:
        if "Time" in components["ConfigTolerances"] and "Value" in components["ConfigTolerances"]:
            t,v = components["ConfigTolerances"]["Time"],components["ConfigTolerances"]["Value"]
            ret = f"--rktol {';'.join( [ f'{tt}:{vv}' for tt,vv in zip(t,v) ] )}"
        else:
            tol = components['ConfigTolerances']['Resolution']
            if len(tol) > 0:
                ret = f"--rktol {tol}"
    if len(ret) > 0:
        return ret
    return ret

def _parse_config_grid(components: dict, escape_symbol: str = "", callback = None) -> str:
    ret = ""
    if "ConfigGrid" in components:
        if "Time" in components["ConfigGrid"] and "Value" in components["ConfigGrid"]:
            t,v = components["ConfigGrid"]["Time"],components["ConfigGrid"]["Value"]
            ret = f"--grid {';'.join( [ f'{tt}:{vv}' for tt,vv in zip(t,v) ] )}"
        else:
            gridres = components['ConfigGrid']['Resolution']
            if gridres == "auto":
                gridres = "-1"
            if len(gridres) > 0:
                ret = f"--gridres {gridres}"
    if len(ret) > 0:
        return ret
    return ret
    
def _parse_config_solver(components: dict, escape_symbol: str = "", callback = None) -> str:
    s = components["ConfigSolver"]
    ret = ""
    if s["Solver"] < 3:
        # Usual RK Solver
        solvers = ["45","4","5"]
        ret += f"--rkorder {solvers[s['Solver']]}"
    else:
        # Path Integral
        if (components["ConfigPhonons"]["Temperature"] == "No Phonons"):
            callback("If the PathIntegral PSADM IQUAPI Solver is chosen, the temperature must be set to T >= 0!")
        else:
            nc = s["NC"]
            cutoff, unit = get_unit_value(components["ConfigPhonons"]["TimeCutoff"]), get_unit(components["ConfigPhonons"]["TimeCutoff"])
            tstep = float(cutoff) / float(nc)
            ret += f"--phononorder 5 --NC {nc} --tstepPath {tstep}{unit}"
    # Interpolator
    if s['Interpolator'] != 0:
        ret += " -interpolate"
    orders_tau = {0: 0, 1: 2}
    ret += f" --interpolateOrder {escape_symbol}{s['Interpolator']-1},{orders_tau[s['InterpolatorGrid']]}{escape_symbol}"
    return ret

def _parse_config_system(components: dict, escape_symbol: str = "", callback = None) -> str:
    s = components["ConfigSystem"]
    return f"--system {s['Coupling']} {s['CavityLosses']} {s['RadiativeLosses']} {s['DephasingLosses']}"

def _parse_config_phonons(components: dict, escape_symbol: str = "", callback = None) -> str:
    p = components["ConfigPhonons"]
    ret = ""
    if p["Temperature"] == "No Phonons":
        return ret
    ret += f"--temperature {p['Temperature']} --phononAdjust {int(p['ARRad'])} {int(p['ARDep'])} {int(p['Renormalization'])} --phononohm {p['Ohm']}"
    if components["ConfigSolver"]["Solver"] < 3:
        ret += f" --phononorder {p['Approximation']}"
    if p["IteratorStep"] != "auto":
        ret += f" --iteratorStepsize {p['IteratorStep']}"
    # Phonon Parameters OR QD Parameters
    if p["UseQD"]:
        ret += f" --quantumdot {p['QDde']} {p['QDdh']} {p['QDrho']} {p['QDcs']} {p['QDeh']} {p['QDs']}"
    else:
        ret += f" --phononalpha {p['Alpha']} --phononwcutoff {p['SpectralCutoff']} --phononwcutoffdelta {p['SpectralDelta']} --phonontcutoff {p['TimeCutoff']}"
    return ret

def _parse_config_spectra(components: dict, escape_symbol: str = "", callback = None) -> str:
    p = components["Spectrum"]
    if len(p.values()) == 0:
        return ""
    ret = f"--GS {escape_symbol}"
    for spectrum in p.values():
        ret += f"{','.join(spectrum['Modes'])}:{spectrum['Center']}:{spectrum['Range']}:{spectrum['Res']}:{spectrum['Order']+1}:{spectrum['Norm']};"
    ret = ret[:-1] + escape_symbol
    return ret

def _parse_config_initial_state(components: dict, escape_symbol: str = "", callback = None) -> str:
    p = components["InitialState"]
    if "State" not in p or len(p["State"]) == 0:
        callback("Please enter the initial State!")
        return ""
    return f"--R {escape_symbol}:{p['State']};{escape_symbol}"

def _parse_runconfig(components: dict, escape_symbol: str = "", callback = None) -> str:
    p = components["RunConfig"]
    ret = ""
    ret += ["", "-L2 ", "-L3 "][p["LoggingLevel"]]
    if p["CPUCores"] == "all":
        ret += "--Threads -1 "
    elif p["CPUCores"] != 0:
        ret += f"--Threads {p['CPUCores']} "
    return ret

def _parse_output_flags(components: dict, escape_symbol: str = "", callback = None) -> str:
    p = components["OutputFlags"]
    # --output flag
    ret = ";".join([ name for name,checked in p.items() if checked])
    if len(ret) > 0:
        ret =  f"--output {escape_symbol}{ret}{escape_symbol} "
    # dm output and dm frame
    p = components["RunConfig"]
    ret += f"--DMconfig {['none','diagonal','full'][p['DMOutputMode']]}:{['int', 'schroedinger'][p['OutputFrame']]}"
    return ret

def _parse_indistinguishabilities(components: dict, escape_symbol: str = "", callback = None) -> str:
    p = components["Indistinguishability"]
    if not len(p.values()):
        return ""
    ret = f"--GI {escape_symbol}"
    for ind in p.values():
        ret += f"{ind['Mode']};"
    return ret[:-1] + escape_symbol

def _parse_concurrences(components: dict, escape_symbol: str = "", callback = None) -> str:
    p = components["Concurrence"]
    if not len(p.values()):
        return ""
    ret = f"--GC {escape_symbol}"
    for ind in p.values():
        ret += f"{ind['Mode']}"
        if "ConcurrenceSpectrum" in components:
            p2 = components["ConcurrenceSpectrum"]
            if p2["Active"]:
                    ret += f":{p2['Center']}:{p2['Range']}:{p2['Res']}"
        ret +=";"
    ret = ret[:-1]
    return ret + escape_symbol

def _parse_g1g2_func(components: dict, escape_symbol: str = "", callback = None) -> str:
    p = components["G1G2"]
    if not len(p.values()):
        return ""
    ret = f"--GF {escape_symbol}"
    for setting in p.values():
        ret += f"{setting['Mode']}:{setting['Order']+1}:{['time','matrix','both'][int(setting['Method'])]};"
    return ret[:-1] + escape_symbol

def _parse_wigner_function(components: dict, escape_symbol: str = "", callback = None) -> str:
    p = components["Wigner"]
    if not len(p.values()):
        return ""
    ret = f"--GW {escape_symbol}"
    for setting in p.values():
        ret += f"{setting['Mode']}:{setting['XMax']}:{setting['YMax']}:{setting['Resolution']}:{setting['Skip']};"
    return ret[:-1] + escape_symbol

def _parse_detector(components: dict, escape_symbol: str = "", callback = None) -> str:
    p1 = components["DetectorTime"]
    p2 = components["DetectorSpectrum"]
    if not len(p1.values()) and not len(p2.values()):
        return ""
    ret = f"--detector {escape_symbol}"
    for d in p1.values():
        ret += f"{d['t0']}:{d['t1']}:{d['Power']};"
    for d in p2.values():
        ret += f"{d['w0']}:{d['w1']}:{d['Points']}:{d['Power']};"
    return ret[:-1] + escape_symbol

_component_parser = {
    "EnergyLevels" : _parse_electronic_system,
    "CavityLevels" : _parse_cavity_system,
    "Pulse": _parse_pulse_system,
    "Shift" : _parse_shift_system,
    "ConfigTime" : _parse_config_time,
    "ConfigGrid" : _parse_config_grid,
    "ConfigTolerances" : _parse_config_tolerances,
    "ConfigSolver": _parse_config_solver,
    "ConfigSystem": _parse_config_system,
    "ConfigPhonons": _parse_config_phonons,
    "Spectrum": _parse_config_spectra,
    "InitialState": _parse_config_initial_state,
    "RunConfig": _parse_runconfig,
    "OutputFlags": _parse_output_flags,
    "Indistinguishability": _parse_indistinguishabilities,
    "Concurrence": _parse_concurrences,
    "G1G2": _parse_g1g2_func,
    "Wigner": _parse_wigner_function,
    "DetectorTime": _parse_detector,
}

def component_parser(component: str, escaped: bool, components: dict, escape_symbol: str = "'", callback = None) -> str:
    if not escaped:
        escape_symbol = ""
    if component not in components.keys() or component not in _component_parser.keys():
        print(f"Error: Key '{component}' not in Components list!")
        return ""
    return _component_parser[component](components, escape_symbol, callback)

if __name__ == "__main__":
    print("Available Components:")
    print(_component_parser.keys())
    print(f"This file ({__file__}) is part of the QDaCC GUI and should be imported, not executed.")