import plotly.graph_objects as go
import numpy as np
import pymzml

np.random.seed(1)

N = 70

file = "data/TQ8_201023SJ01_0103.mzML"
run = pymzml.run.Reader(
    file,
    MS1_Precision=5e-6,
    MSn_Precision=20e-6
)

intensities = []
mass_ratios = []
times = []

for i, spec in enumerate(run):
    if i > 0 and i % 100 == 0: print("Done {} elements so far".format(i))

    intensities += spec.i.tolist()
    mass_ratios += spec.mz.tolist()
    times += [spec.scan_time_in_minutes()] * len(spec.i)

# fig = go.Figure(data=[go.Mesh3d(x=mass_ratios,
#                                 y=times,
#                                 z=intensities,
#                                 opacity=0.5,
#                                 color='rgba(244,22,100,0.6)'
#                                 )])
#
# fig.update_layout(
#     scene=dict(
#         xaxis=dict(nticks=4, range=[-100, 100], ),
#         yaxis=dict(nticks=4, range=[-50, 100], ),
#         zaxis=dict(nticks=4, range=[-100, 100], ), ),
#     width=700,
#     margin=dict(r=20, l=10, b=10, t=10))


# fig = go.Figure(data=[go.Surface(x=mass_ratios,
#                                  y=times,
#                                  z=intensities,
#                                  opacity=0.5
#                                  )])
#
# fig.update_layout(title='Mt Bruno Elevation', autosize=False,
#                   width=500, height=500,
#                   margin=dict(l=65, r=50, b=65, t=90))
#
# fig.show()

# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Creating figure
fig = plt.figure(figsize=(14, 9))
ax = plt.axes(projection='3d')

# Creating plot
ax.plot_trisurf(np.array(mass_ratios), np.array(times), np.array(intensities))

ax.set_xlabel("m/z")
ax.set_ylabel("time")
ax.set_zlabel("i")

# show plot
plt.savefig("./img/3d_plot.png")
