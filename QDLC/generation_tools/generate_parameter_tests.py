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
    from string import ascii_letters as comments
    process = Popen(test["run"]+test["id"]+"/", stdout=PIPE, universal_newlines=True)
    # Wait for the process to terminate
    process.communicate()
    # Read the output / Test
    fail = 0
    for name,(file,function) in test["eval"]:
        print(f" . . Testing {name} ... ", end="")
        current_file = join(file_to_output_folder, test["id"], file)
        test_data = np.loadtxt(current_file, unpack=True, comments = list(comments))
        current_file_ref = join(file_to_reference_folder, test["id"], file)
        reference_data = np.loadtxt(current_file_ref, unpack=True, comments = list(comments))
        test_value = function(test_data)
        reference_value = function(reference_data)
        if test_value == reference_value:
            print(GREEN,BOLD,"EXCELLENT",RESET,sep="")
        elif abs(test_value-reference_value) < eps:
            print(GREEN,BOLD,"OK",RESET,sep="")
        else:
            print(RED,BOLD,"FAIL",RESET,f" Expected: {reference_value}, got: {test_value}",sep="")
            fail -= 1
    return len(test["eval"]) - fail, fail
        


if __name__ == "__main__":
    """
    Make sure to run this script from the QDLC Main Directory.
    """

    file_to_reference_folder = "data/unit_tests/references/"
    file_to_output_folder = "data/unit_tests/tests/"
    file_to_qdlc = "QDLC.exe"

    from numpy import nansum

    # Data Test Lines
    tests = {
        "basics": {
            # Basic Exciton Tests:
            "Exciton, Radiative Decay": {"run": f"{file_to_qdlc} --Threads -1 --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --R |X>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 15mueV 0mueV {file_to_output_folder}",
                                            "id": "test_exciton_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                            )
            },
            "Exciton, Dephasing": {"run": f"{file_to_qdlc} --Threads -1 --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --R |X>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 10mueV {file_to_output_folder}",
                                            "id": "test_exciton_basics_2",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                            )
            },
            "Cavity": {"run": f"{file_to_qdlc} --Threads -1 --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SO c:1eV:10:G=X:1:1 --R |G|10c>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 100mueV 0mueV 10mueV {file_to_output_folder}",
                                            "id": "test_cavity_basics_1",
                                            "eval": (
                                                    ( "States", ("photonic.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                            )
            },
            "Pulse": {"run": f"{file_to_qdlc} --Threads -1 --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SP p:G=X:1pi:1eV:10ps:5ps:gauss --R |G>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_pulse_basics_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                            )
            },
            "Chirp": {"run": f"{file_to_qdlc} --Threads -1 --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SC s:X:1:0,0,0.2meV,1meV:0,10ps,100ps,200ps:monotone --output eigenvalues --R |X>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 0mueV 0mueV {file_to_output_folder}",
                                            "id": "test_chirp_basics_1",
                                            "eval": (
                                                    ( "States", ("eigenvalues.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                            )
            },
        },
        "advanced" : {
            # Exciton Excitation Tests
            "Exciton, Resonant Excitation": {"run": f"{file_to_qdlc} --Threads -1 --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SP p:G=X:1pi:1eV:8ps:50ps:gauss --R |G>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 5mueV 0mueV --gridres 100 --GI G=X --GF G=X:1:both --GS G=X:1.005eV:1meV:100 {file_to_output_folder}",
                                            "id": "test_advanced_exciton_excitation_1",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Indistinguishability", ("indist_X=G-G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G1 Integrated", ("G1-X=G-G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G1 Matrix", ("G1-X=G-G=X_m.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Spectrum", ("spectrum_G1-X=G-G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                            )
            },
            "Exciton, Off-Resonant Excitation": {"run": f"{file_to_qdlc} --Threads -1 --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SP p:G=X:1pi:1.01eV:8ps:50ps:gauss --R |G>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 5mueV 0mueV --gridres 100 --GI G=X --GF G=X:1:both --GS G=X:1.005eV:1meV:100 {file_to_output_folder}",
                                            "id": "test_advanced_exciton_excitation_2",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Indistinguishability", ("indist_X=G-G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G1 Integrated", ("G1-X=G-G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G1 Matrix", ("G1-X=G-G=X_m.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Spectrum", ("spectrum_G1-X=G-G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                            )
            },
            "Exciton, Resonant Excitation, Chirp": {"run": f"{file_to_qdlc} --Threads -1 --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SP p:G=X:3pi:1.01eV:8ps:50ps:gauss --SC s:X:1:0,0,1meV,1meV:0,10ps,100ps,200ps:monotone --R |G>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 0mueV 0mueV 5mueV 0mueV --gridres 100 --GI G=X --GF G=X:1:both --GS G=X:0.9999eV:1meV:100 {file_to_output_folder}",
                                            "id": "test_advanced_exciton_excitation_chirp",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Indistinguishability", ("indist_X=G-G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G1 Integrated", ("G1-X=G-G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G1 Matrix", ("G1-X=G-G=X_m.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Spectrum", ("spectrum_G1-X=G-G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                            )
            },
            # Exciton and Cavity
            "Exciton Cavity": {"run": f"{file_to_qdlc} --Threads -1 --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SO c:1eV:3:G=X:1:1 --R |X|0c>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 66mueV 100mueV 0mueV 0mueV --gridres 100 --GI c --GF c,c:1,2:both,both --GS c,c+G=X:1eV,0.999eV:1.5meV,1.337meV:100,123:1,2  {file_to_output_folder}",
                                            "id": "test_advanced_exciton_cavity",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Indistinguishability", ("indist_cbd-cb.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G1 Integrated", ("G1-cbd-cb.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G1 Matrix", ("G1-cbd-cb_m.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G2 Integrated", ("G2-cbd-cbd-cb-cb.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G2 Matrix", ("G2-cbd-cbd-cb-cb_m.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Spectrum G1", ("spectrum_G1-cbd-cb.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Spectrum G2", ("spectrum_G2-cbd+X=G-cbd+X=G-cb+G=X-cb+G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                            )
            },
            "Exciton Cavity, CW Pulse, Decay, Dephasing": {"run": f"{file_to_qdlc} --Threads -1 --SE G:0:X:0:1:0;X:1eV:-:1:1:1 --SO c:1eV:3:G=X:1:1 --SP p:G=X:0.5meV:1.01eV:10ps:5ps:cw --R |G|0c>  --rktol 1E-6 --time 0 200ps 1ps -interpolate --system 66mueV 100mueV 5mueV 1mueV --gridres 100 --GI c --GF c,c:1,2:both,both --GS c,c+G=X:1eV,0.999eV:1.5meV,1.337meV:100,123:1,2  {file_to_output_folder}",
                                            "id": "test_advanced_exciton_excitation_cw_pulse_decay_dephasing",
                                            "eval": (
                                                    ( "States", ("electronic.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Indistinguishability", ("indist_cbd-cb.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G1 Integrated", ("G1-cbd-cb.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G1 Matrix", ("G1-cbd-cb_m.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G2 Integrated", ("G2-cbd-cbd-cb-cb.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "G2 Matrix", ("G2-cbd-cbd-cb-cb_m.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Spectrum G1", ("spectrum_G1-cbd-cb.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
                                                    ( "Spectrum G2", ("spectrum_G2-cbd+X=G-cbd+X=G-cb+G=X-cb+G=X.txt", lambda data: nansum([nansum(col) for col in data[1:]])) ),
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
        from distutils.dir_util import copy_tree as copytree
        print("Copying new dataset to reference folder")
        copytree(file_to_output_folder, file_to_reference_folder)
        print("Done")