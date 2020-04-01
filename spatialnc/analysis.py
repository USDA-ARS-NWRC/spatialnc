from collections import OrderedDict
import logging

def get_stats(data, np_stats=['max','min','mean','std'], use_nan_stat=True):
    '''
    Given a numpy array, calculate all the numpy statistics and return them
    in a dictionary

    data: Numpy array of any size/dimension
    np_stats: Statistic name to use, must be an function of a numpy array
    use_nan_stat: Calculate the same statistics using the nan variant (e.g. nanmean vs mean)
    '''
    log = logging.getLogger(__name__)

    # put together the operations to use
    operations = np_stats

    # Change the ops to nan variants
    if use_nan_stat:
        operations = ['nan{}' for op in operations]

    # Build the output
    out = OrderedDict()

    log.info('Data is {}'.format(' X '.join(data.shape)))

    for op in operations:
        log.info('Calculating {} ...'.format(op))
        stat_fn = getattr(data,op)
        out[op] = stat_fn()
