"""
This interactive script is used to generate test data for QDLC.
"""

import sys
import os
import numpy as np
from subprocess import Popen, PIPE, call
from os.path import join

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
BOLD = "\033[1m"
RESET = "\033[0m"

def run_test(test: dict, file_to_output_folder: str, file_to_reference_folder: str, eps = 1E-6):
    #from string import ascii_letters as comments
    comments = ["t","Omega","omega","Time","time","#","w"]
    process = Popen(test["run"]+test["id"]+"/", stdout=PIPE, universal_newlines=True)
    # Wait for the process to terminate
    process.communicate()
    # Test Logfile
    current_logfile = open(join(file_to_output_folder, test["id"], "logfile.log"),"r")
    last_test_line = current_logfile.readlines()[-2]
    try:
        reference_logfile = open(join(file_to_reference_folder, test["id"], "logfile.log"),"r")
        last_reference_line = reference_logfile.readlines()[-2]
    except FileNotFoundError:
        print(f" . . {BLUE}{BOLD}Logfile not found, assuming new set.{RESET}")
        last_reference_line = last_test_line
    if last_test_line != last_reference_line:
        print(f" . . {RED}{BOLD}LOGFILES DO NOT COINCIDE!! Maybe you changed to runstring?{RESET}")
    # Read the output / Test
    fail = 0
    # Test Data
    for name,(file,function) in test["eval"]:
        print(f" . . Testing {name} ... ", end="")
        current_file = join(file_to_output_folder, test["id"], file)
        test_data = np.loadtxt(current_file, unpack=True, comments = comments)
        test_value = function(test_data)
        current_file_ref = join(file_to_reference_folder, test["id"], file)
        try:
            reference_data = np.loadtxt(current_file_ref, unpack=True, comments = comments)
            reference_value = function(reference_data)
        except FileNotFoundError:
            print(f" . . {BLUE}{BOLD}Reference not found, assuming new set.{RESET}")
            reference_value = test_value
        if test_value == reference_value:
            print(f"{GREEN}{BOLD}EXCELLENT{RESET}")
        elif abs(test_value-reference_value) < eps:
            print(f"{GREEN}{BOLD}OK{RESET}")
        else:
            print(f"{RED}{BOLD}FAIL{RESET} Expected: {reference_value}, got: {test_value}")
            fail = 1
    return len(test["eval"]) - fail, fail
        


if __name__ == "__main__":
    """
    Make sure to run this script from the QDLC Main Directory.
    """

    file_to_reference_folder = "data/unit_tests/references/"
    file_to_output_folder = "data/unit_tests/tests/"
    file_to_qdlc = "QDLC.exe"

    qdlc_threads = 2

    from numpy import nansum, abs

    # Data Test Lines
    tests = {
        "basics_exciton": {
            # Basic Exciton Tests:
            "Radiative Decay": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --R |X>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 15mueV 0mueV {file_to_output_folder}",
                                            "id": "test_exciton_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Dephasing": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --R |X>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 10mueV {file_to_output_folder}",
                                            "id": "test_exciton_basics_2",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Cavity": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SO c:1eV:10:G=X:1:1 --R |G|10c>  --rktol 1E-6 --time 0 200ps 1ps -interpolate -L2 --system 0mueV 100mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_cavity_basics_1",
                                            "eval": (
                                                    ( "States", ("photonic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Pulse": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SP p:G=X:1pi:1eV:10ps:5ps:gauss --R |G>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_pulse_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Chirp": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SC s:X:1:0,0,0.2meV,1meV:0,10ps,100ps,200ps:monotone --output eigenvalues --R |X>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_chirp_basics_1",
                                            "eval": (
                                                    ( "States", ("eigenvalues.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
        },
        "basics_biexciton": {
            # Basic BiExciton Tests:
            "Radiative Decay": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X1,X2:0:1:0;X1:1eV:XX:1:1:1;X2:1eV:XX:1:1:1;XX:1.995eV:-:1:1:2 --R |XX>  --rktol 1E-6 --time 0 500ps 1ps -interpolate --system 0mueV 0mueV 15mueV 0mueV {file_to_output_folder}",
                                            "id": "test_biexciton_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Dephasing": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X1,X2:0:1:0;X1:1eV:XX:1:1:1;X2:1eV:XX:1:1:1;XX:1.995eV:-:1:1:2 --R |XX>  --rktol 1E-6 --time 0 500ps 1ps -interpolate --system 0mueV 0mueV 0mueV 10mueV {file_to_output_folder}",
                                            "id": "test_biexciton_basics_2",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Cavity": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X1,X2:0:1:0;X1:1eV:XX:1:1:1;X2:1eV:XX:1:1:1;XX:1.995eV:-:1:1:2 --SO h:1eV:2:G=X1,X1=XX:1,1:1;v:1eV:2:G=X2,X2=XX:1,1:1 --R |XX|1h|0v>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 66mueV 100mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_biexciton_cavity_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Cavity", ("photonic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Pulse": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X1,X2:0:1:0;X1:1eV:XX:1:1:1;X2:1eV:XX:1.2:1:1;XX:1.995eV:-:1:1:2 --SP p:G=X1,X1=XX:1pi:1eV:10ps:5ps:gauss --R |G>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_biexciton_pulse_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Pulse", ("pulse_p.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Pulse+Cavity": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X1,X2:0:1:0;X1:1eV:XX:1:1:1;X2:1eV:XX:1.2:1:1;XX:1.995eV:-:1:1:2 --SP p:G=X1,X1=XX:1pi:1eV:10ps:5ps:gauss --SO h:1eV:2:G=X1,X1=XX:1,1:1;v:1eV:2:G=X2,X2=XX:1,1:1 --R |G|1h|2v>  --rktol 1E-6 --time 0 50ps 1ps -interpolate --system 66mueV 100mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_biexciton_pulse_cavity_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Cavity", ("photonic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Pulse", ("pulse_p.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Chirp": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X1,X2:0:1:0;X1:1eV:XX:1:1:1;X2:1eV:XX:1:1:1;XX:1.995eV:-:1:1:2 --SC s:X1,X2,XX:1,1,2:0,0,0.2meV,1meV:0,10ps,100ps,200ps:monotone --output eigenvalues --R |XX>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_biexciton_chirp_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Chirp", ("chirp_s.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Eigenvalues", ("eigenvalues.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
        },
        "pulse_mechanics" : {
            "Adding Pulses": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --R |X> --SP p1:G=X:1pi,3pi:1eV,0.997eV:30ps,50ps:5ps,2ps:gauss,gauss;p2:G=X:0.1meV:1eV:0:0:cw --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_pulse_adding_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Pulse 1", ("pulse_p1.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Pulse 2", ("pulse_p2.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Pulse Exponent": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --R |X> --SP p:G=X:1pi:1eV:30ps:5ps:gauss+exponent(12) --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_pulse_exponent_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Pulse", ("pulse_p.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Pulse S.U.P.E.R.": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --R |X> --SP p:G=X:1.234meV:0.995eV:100ps:10ps:gauss+super(5meV_4meV) --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_pulse_super_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Pulse", ("pulse_p.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Pulse Chirp": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --R |X> --SP p:G=X:7pi:1eV:100ps:10ps:gauss+chirp(4E-24) --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_pulse_chirp_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Pulse", ("pulse_p.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
        },
        "pme_phonons" : {
            # Basics on X: cutoff energy, temp, cutoff time, alpha, QD params, order
            # ...
            # Biexciton Test cases:
            "Cavity O1": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X1,X2:0:1:0;X1:1eV:XX:1:1:1;X2:1eV:XX:1:1:1;XX:1.995eV:-:1:1:2 --SO h:1eV:2:G=X1,X1=XX:1,1:1;v:1eV:2:G=X2,X2=XX:1,1:1 --R |G|1h|2v> --temperature 5 --phononorder 1 --output greenf;phononJ;phononcoefficients --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 66mueV 100mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_pme_biexciton_cavity_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Cavity", ("photonic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Cavity", ("photonic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "PME Green Functions", ("phonon_greenfunctions.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "PME Spectral Functions", ("phonon_spectral.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Pulse O1": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X1,X2:0:1:0;X1:1eV:XX:1:1:1;X2:1eV:XX:1:1:1;XX:1.995eV:-:1:1:2 --SP p:G=X1,X1=XX:1pi:1eV:10ps:5ps:gauss --R |G> --temperature 5 --phononorder 1 --output greenf;phononJ;phononcoefficients --rktol 1E-6 --time 0 50ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_pme_biexciton_pulse_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Pulse", ("pulse_p.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "PME Green Functions", ("phonon_greenfunctions.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "PME Spectral Functions", ("phonon_spectral.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Pulse+Cavity O1": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X1,X2:0:1:0;X1:1eV:XX:1:1:1;X2:1eV:XX:1:1:1;XX:1.995eV:-:1:1:2 --SP p:G=X1,X1=XX:1pi:1eV:10ps:5ps:gauss --SO h:1eV:2:G=X1,X1=XX:1,1:1;v:1eV:2:G=X2,X2=XX:1,1:1 --R |G|2h|1v> --temperature 5 --phononorder 1 --output greenf;phononJ;phononcoefficients --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 66mueV 100mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_pme_biexciton_pulse_cavity_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Cavity", ("photonic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Pulse", ("pulse_p.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "PME Green Functions", ("phonon_greenfunctions.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "PME Spectral Functions", ("phonon_spectral.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
        },
        # adding pulses, super, amp, etc
        # , initial states sum, coherent, squeezed, thermal, etc.
        # different couplings
        "advanced" : {
            # Exciton Excitation Tests
            "Exciton, Resonant Excitation": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SP p:G=X:1pi:1eV:8ps:50ps:gauss --R |G>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 5mueV 0mueV --gridres 100 --GI G=X --GF G=X:1:both --GS G=X:1.005eV:1meV:100 {file_to_output_folder}",
                                            "id": "test_advanced_exciton_excitation_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Indistinguishability", ("indist_X=G-G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G1 Integrated", ("G1-X=G-G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G1 Matrix", ("G1-X=G-G=X_m.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Spectrum", ("spectrum_G1-X=G-G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Exciton, Off-Resonant Excitation": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SP p:G=X:1pi:1.01eV:8ps:50ps:gauss --R |G>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 5mueV 0mueV --gridres 100 --GI G=X --GF G=X:1:both --GS G=X:1.005eV:1meV:100 {file_to_output_folder}",
                                            "id": "test_advanced_exciton_excitation_2",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Indistinguishability", ("indist_X=G-G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G1 Integrated", ("G1-X=G-G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G1 Matrix", ("G1-X=G-G=X_m.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Spectrum", ("spectrum_G1-X=G-G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Exciton, Resonant Excitation, Chirp": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SP p:G=X:3pi:1.01eV:8ps:50ps:gauss --SC s:X:1:0,0,1meV,1meV:0,10ps,100ps,200ps:monotone --R |G>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 5mueV 0mueV --gridres 100 --GI G=X --GF G=X:1:both --GS G=X:0.9999eV:1meV:100 {file_to_output_folder}",
                                            "id": "test_advanced_exciton_excitation_chirp",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Indistinguishability", ("indist_X=G-G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G1 Integrated", ("G1-X=G-G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G1 Matrix", ("G1-X=G-G=X_m.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Spectrum", ("spectrum_G1-X=G-G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            # Exciton and Cavity
            "Exciton Cavity": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SO c:1eV:3:G=X:1:1 --R |X|0c>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 66mueV 100mueV 0mueV 0mueV --gridres 100 --GI c --GF c,c:1,2:both,both --GS c,c+G=X:1eV,0.999eV:1.5meV,1.337meV:100,123:1,2  {file_to_output_folder}",
                                            "id": "test_advanced_exciton_cavity",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Cavity", ("photonic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Indistinguishability", ("indist_cbd-cb.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G1 Integrated", ("G1-cbd-cb.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G1 Matrix", ("G1-cbd-cb_m.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G2 Integrated", ("G2-cbd-cbd-cb-cb.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G2 Matrix", ("G2-cbd-cbd-cb-cb_m.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Spectrum G1", ("spectrum_G1-cbd-cb.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Spectrum G2", ("spectrum_G2-cbd+X=G-cbd+X=G-cb+G=X-cb+G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
            "Exciton Cavity, CW Pulse, Decay, Dephasing": {"run": f"{file_to_qdlc} --Threads {qdlc_threads} --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SO c:1eV:3:G=X:1:1 --SP p:G=X:0.5meV:1.01eV:10ps:5ps:cw --R |G|0c>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 66mueV 100mueV 5mueV 1mueV --gridres 100 --GI c --GF c,c:1,2:both,both --GS c,c+G=X:1eV,0.999eV:1.5meV,1.337meV:100,123:1,2  {file_to_output_folder}",
                                            "id": "test_advanced_exciton_excitation_cw_pulse_decay_dephasing",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Cavity", ("photonic.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Indistinguishability", ("indist_cbd-cb.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G1 Integrated", ("G1-cbd-cb.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G1 Matrix", ("G1-cbd-cb_m.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G2 Integrated", ("G2-cbd-cbd-cb-cb.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "G2 Matrix", ("G2-cbd-cbd-cb-cb_m.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Spectrum G1", ("spectrum_G1-cbd-cb.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                                    ( "Spectrum G2", ("spectrum_G2-cbd+X=G-cbd+X=G-cb+G=X-cb+G=X.txt", lambda data: nansum([nansum(abs(col)) for col in data[1:]])) ),
                                            )
            },
        }
    }

    # Run tests

    succesfull, failure = 0,0
    for name, set_of_tests in tests.items():
        print(f"Running set: {name}")
        for test_name,test in set_of_tests.items():
            print(f" . Running '{test_name}'")
            s,f = run_test(test, file_to_output_folder, file_to_reference_folder)
            succesfull += s
            failure += f
    print(f"Tests finished with {BOLD}{GREEN}{succesfull}{RESET} succesfull and {BOLD}{RED}{failure}{RESET} failed tests, {BOLD}{succesfull/(succesfull+failure)*100}% succesfull.{RESET}")
    print("Do you want to keep the new dataset as the new reference? (y/n)")
    if input() == "y":
        from shutil import copytree
        print("Copying new dataset to reference folder")
        copytree(file_to_output_folder, file_to_reference_folder, dir_exist_ok=True)
        print("Done")