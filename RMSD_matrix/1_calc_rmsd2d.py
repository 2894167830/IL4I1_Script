#Copyright (C), Schrodinger, LLC. All rights reserved.
from schrodinger.trajectory.rmsd2d import calc_rmsd_matrix
from schrodinger.trajectory.desmondsimulation import create_simulation
import numpy as np
dsim = create_simulation("md_v4_del_FAD_CIT-out.cms", "md_v4_del_FAD_CIT_trj")
rmsd_matrix = calc_rmsd_matrix(dsim,
                               '(BACKBONE and res.num 156-258)',
                               #'BACKBONE',
                               'BACKBONE',
                               frame_list=list(range(0,1001,1)),
                               nworkers=10,
                               nframes=4,
                               multiprocessing = True)
np.savetxt('matrix_step2_substrate_600ns.csv', rmsd_matrix, fmt='%.5f', delimiter=',')


'''
def calc_rmsd_matrix(dsim,
                     rmsd_asl_expr,
                     fit_asl_expr=None,
                     frame_list=None,
                     nworkers=1,
                     nframes=1,
                     multiprocessing=True):
"""

