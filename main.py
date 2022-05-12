import pymzml
import matplotlib.pyplot as plt
import numpy as np

mzml_file = 'data/TQ8_201023SJ01_0103.mzML'

msrun = pymzml.run.Reader(mzml_file)
#
# for n, spectrum in enumerate(msrun):
#
#     if n > 10: break
#
#     print("Retention time (min): {}, MS level: {}".format(
#         spectrum.scan_time_in_minutes(), spectrum.ms_level
#     ))
#
# for n, spectrum in enumerate(msrun):
#
#     if n > 0: break
#
#     # an array containing the m/z values of the scan
#     print(spectrum.mz)
#
#     # an array containing the corresponding values of the scan
#     print(spectrum.i)
#
#     # a list of (m/z, intensity) tuples
#     print(spectrum.peaks)

target = 1082.5313
ppmTol = 1

target_ll = target - target / 1000000 * ppmTol
target_hl = target + target / 1000000 * ppmTol

times = []
target_intensities = []

msrun = pymzml.run.Reader(mzml_file)
for n, spectrum in enumerate(msrun):

    if spectrum.ms_level != 1: continue

    target_intensities.append(
        spectrum.reduce(mz_range=(target_ll, target_hl))[:, 1].sum()
    )

    times.append(spectrum.scan_time_in_minutes())

fig, ax = plt.subplots()
ax.plot(times, target_intensities)
ax.set_xlabel('Retention Time (min)')
ax.set_ylabel('Intensity')
ax.set_title('Target Intensity')
plt.savefig('./data/ing.png')

print("ciao")
