import pymzml
import matplotlib.pyplot as plt
from matplotlib import cm

file = "data/TQ8_201023SJ01_0103.mzML"
run = pymzml.run.Reader(
    file,
    MS1_Precision=5e-6,
    MSn_Precision=20e-6
)
viridis = cm.get_cmap('viridis', run.get_spectrum_count())

max_mz = 0
max_i = 0
for spec in run:
    max_mz = max(max_mz, max(spec.mz))
    max_i = max(max_i, max(spec.i))


for i, spec in enumerate(run):
    if i > 0 and i % 100 == 0: print("Done {} elements so far".format(i))

    plt.title("MS Peaks\nMinute: {time:1.4f}".format(time=spec.scan_time_in_minutes()))
    plt.plot(spec.mz, spec.i, lw=1, alpha=1, color=viridis(range(run.get_spectrum_count()))[i])
    plt.xlim(0, max_mz)
    plt.ylim(0, max_i)
    plt.ylabel("intensity")
    plt.xlabel("m/z")

    plt.savefig(fname="./img/spec_sequence/{index}.png".format(index=i))
    plt.cla()
