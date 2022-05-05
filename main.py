import raw2mzml
import pymzml
import matplotlib.pyplot as plt
import numpy as np

raw2mzml.convert_single_file()

mzml_file = 'data/TQ8_201023SJ01_0103.raw'

msrun = pymzml.run.Reader(mzml_file)