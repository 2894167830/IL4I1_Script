#A module to calculte 2D RMSD for Desmond trajectories using threading/multiprocessing.

#To calculate 2D RMSD for Desmond Trajectory call
"""
from schrodinger.trajectory.rmsd2d import calc_rmsd_matrix
from schrodinger.trajectory.desmondsimulation import create_simulation
dsim = create_simulation("foo-out.cms", "foo_trj")
rmsd_matrix = calc_rmsd_matrix(dsim,
                               'BACKBONE',
                               'BACKBONE',
                               frame_list=None,
                               nworkers=8,
                               nframes=50,
                               multiprocessing = True)
"""
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
    A multithreading/multiprocessing function to calculate 2D RMSD matrix

        :type dsim: DesmondSimulation instance
        :param dsim:
                DesmondSimulation instance that contains reference to trajectory.

        :type rmsd_asl_expr: string
        :param rmsd_asl_expr
                The atom selection from which to indetify atom indices to be
                compared.

        :type fit_asl_expr: string
        :param fit_asl_expr:
                The atom selection from which to indetify atom indices to be
                transformed.  if fit_asl_expr is set to None, it will not
                transform the coordinates.

        :type nworkers: integer
        :param nworkers:
                Number of threads/processes used to load frames and calculate rmsd
                matrix.

        :type nframes: integer
        :param nframes:
                Number of frames handled by each worker in one run.

        :type multiprocessing: boolean
        :param multiprocessing:

        :return 2D RMSD numpy array

    """
    if nworkers <= 0:
        raise RuntimeError("nworkers(%d) must be a positive number" % nworkers)
    if nframes <= 0:
        raise RuntimeError("nframes(%d) must be a positive number" % nframes)

    if frame_list is None:
        frame_list = xrange(dsim.total_frame)
    total_frame = len(frame_list)

    if total_frame < 1:
        raise RuntimeError("frame list is empty")

    frame0 = dsim.getFrame(frame_list[0])
    rmsd_fas = FAS(rmsd_asl_expr)
    rmsd_indices = rmsd_fas.getArraySelection(frame0)

    fit_indices = None
    if fit_asl_expr:
        fit_fas = FAS(fit_asl_expr)
        fit_indices = fit_fas.getArraySelection(frame0)

    if multiprocessing:
        model = MultiprocessingModel()
        print("Using multiprocessing module to calculate RMSD")
    else:
        model = ThreadingModel()
        print("Using threading module to calculate RMSD")

    print("Processing %d frames using %d worker(s):" % (total_frame, nworkers))

    block_size = nworkers * nframes

    nblocks = total_frame / block_size
    if total_frame % block_size:
        nblocks += 1

    rmsd_matrix = model.createSharedArray(ctypes.c_double,
                                          total_frame * total_frame)
    for i in xrange(nblocks):
        for j in xrange(i, nblocks):

            # load frames using python threading library
            # although python threading library has the famous Global
            # Interpreter Lock issue, it is suitable for I/O bound operation
            # like trajectory reading.
            # print "Loading trajectory block(%d, %d) ..."%(i, j)
            row_frames, col_frames = load_frame(dsim, i, j, block_size, nframes,
                                                nworkers, frame_list)

            print("Calculating RMSD for trajectory nrows = %d, ncols=%d ..." %
                  (len(row_frames), len(col_frames)))

            # Because of the Global Interpreter Lock, only one thread is active
            # at anytime. Therefore, multiprocessing is more preferable than
            # Threading in RMSD calculation. However, there is overhead in
            # launching extra python interpreter.
            calc_rmsd_matrix_block(model, rmsd_matrix, total_frame, row_frames,
                                   col_frames, rmsd_indices, fit_indices, i, j,
                                   block_size, nworkers)

    rmsd_matrix = numpy.frombuffer(rmsd_matrix)
    #rmsd_matrix =  numpy.array(rmsd_matrix.value)
    rmsd_matrix.shape = total_frame, total_frame

    return rmsd_matrix
'''

