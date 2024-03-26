# Thermal MM/GBSA Calculation Guide

## Introduction:
The thermal MM/GBSA method is a valuable tool for estimating the binding free energy of protein-ligand complexes from molecular dynamics (MD) simulations. This method is implemented in the Schrodinger software suite and can be executed on a 64-bit Linux system with the 2017 version of Schrodinger installed.

## System Requirements:
- A 64-bit Linux operating system.
- Schrodinger 2017 software package.

## Basic Command Structure:
To perform the thermal MM/GBSA calculation, the following command structure is used:
/opt/schrodinger2017-4/run 

/opt/schrodinger2017-4/mmshare-v4.0/python/common/thermal_mmgbsa.py 

{out_cms} -start_frame {start_frame} -end_frame {end_frame} -step_size {step_size} -atom_asl ions -HOST localhost:72 -NJOBS {NJOBS}

Replace `{out_cms}`, `{start_frame}`, `{end_frame}`, `{step_size}`, and `{NJOBS}` with the appropriate values for your specific MD simulation.

### Parameters Explanation:
- `{out_cms}`: The output coordinate file (.cms) from the MD simulation.
- `{start_frame}`: The starting frame number for the analysis.
- `{end_frame}`: The ending frame number for the analysis.
- `{step_size}`: The frame step size for the analysis.
- `-atom_asl ions`: Specifies the atom selection list for the analysis (in this case, ions).
- `-HOST localhost:72`: The host and port where the job will be executed (adjust if necessary).
- `-NJOBS {NJOBS}`: The number of concurrent jobs to run.

## Obtaining Help:
For further assistance on the usage of the `thermal_mmgbsa.py` script, you can run the following command to get a list of available options:
/opt/schrodinger2017-4/run /opt/schrodinger2017-4/mmshare-v4.0/python/common/thermal_mmgbsa.py -h


## Example Command:
Here is an example command for running the thermal MM/GBSA calculation:
/opt/schrodinger2017-4/run /opt/schrodinger2017-4/mmshare-v4.0/python/common/thermal_mmgbsa.py md_IFD_35_p1-out.cms -start_frame 10 -step_size 50 -atom_asl ions -HOST localhost:72 -NJOBS 20


## Output Files:
Upon completion of the calculation, two output files will be generated:
- `trajectory-mmgbsa-prime-out.csv`: Contains the MM/GBSA binding free energy values.
- `trajectory-mmgbsa-prime-out.maegz`: Contains the extracted conformations for the protein and ligand.

## Accessing MD Simulation Files:
The MD simulation files (.cms and .trj) used in this example can be found in the Zenodo repository (https://doi.org/10.5281/zenodo.10473570) in the XXX folder.