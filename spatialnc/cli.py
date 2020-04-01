#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from netCDF4 import Dataset
import numpy as np
import progressbar as pb
import argparse
from collections import OrderedDict
import sys
from os.path import isfile, isdir, abspath, expanduser
import time

from . import __version__
from .analysis import get_stats
from .utilities import get_logger


def nc_stats():

    parser = argparse.ArgumentParser(description='Calculate Statistics on NetCDF Files.')

    parser.add_argument('filename', metavar='f', type=str,
                        help='Path of a netcdf file (File Extension = .nc).')

    parser.add_argument('variable', metavar='v', type=str,
                        help='Name of the variable in the netcdf file to process.')

    parser.add_argument('-t', dest='time', help="Isolates a timestep from file", default = 'all')
    parser.add_argument('-x', dest='x', help="Specify an x coordinate to run statistics on ", default = 'all')
    parser.add_argument('-y', dest='y', help="Specify an y coordinate to run statistics on ", default = 'all')

    args = parser.parse_args()

    filename = abspath(expanduser(args.filename))

    log = get_logger(__name__,log_file=None)

    # Open data set
    ds = Dataset(filename, 'r')

    # Check the users inpurts
    variable = args.variable

    # track how long this takes.
    start = time.time()

    log.info("\n=========== NC_STATS v{} ==========".format(__version__))
    log.info("\nProcessing netCDF statistics...")
    log.info("\tFilename: {0}".format(filename))
    log.info("\tvariable: {0}".format(variable))

    # Filter the data here according to users
    data = ds.variables[variable][:]
    log.info("\tVariable Shape: {0}".format(" X".join([str(s) for s in data.shape])))

    stats = get_stats(data)
    ds.close()
    msg_str =  " "*3 + "{} statistics".format(variable) + " "*3
    log.info('')
    log.info("="*len(msg_str))
    log.info(msg_str)
    log.info("="*len(msg_str))

    #Output to screen
    for stat, value in stats.items():
        log.info("{0} = {1:0.4f}".format(stat, value))
    log.info('\nComplete! Elapsed {:d}s'.format(int(time.time() - start) ))
def make_projected_nc():
    pass
