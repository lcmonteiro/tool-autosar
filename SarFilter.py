# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------------------------
# dependencies
# -------------------------------------------------------------------------------------------------
from SarBase      import SarBase
from SarParser    import SarParser
from Log          import Log
# -------------------------------------------------------------------------------------------------
# Sar Parser
# -------------------------------------------------------------------------------------------------
class SarFilter(SarBase):
# -----------------------------------------------------------------------------
# public
# -----------------------------------------------------------------------------
    # initialization
    # -------------------------------------------------------------------------
    def __init__(self, start=None, suppress=None):
        self.__start    = start
        self.__suppress = suppress
    # ------------------------------------------------------------------------- 
    # process
    # -------------------------------------------------------------------------
    def __call__(self, data):
        result = data
        return result
    #
# -----------------------------------------------------------------------------
# private
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
def main(params):
    # start
    Log.info('Start')
    # xml to python
    data = SarFilter(SarParser(params.path)())()
    # finish
    Log.info('Finish')
    return 0
# -------------------------------------------------------------------------------------------------
# end
# -------------------------------------------------------------------------------------------------