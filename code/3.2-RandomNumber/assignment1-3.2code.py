import matplotlib.pyplot as plt
import numpy as np
import sobol_seq

fig, axs = plt.subplots(2, 5)

axs[0, 0].scatter(np.random.rand(100), (np.random.rand(100)), s=1, marker=".")
axs[0, 0].set_ylabel("Pseudo-Random")
axs[0, 0].set_title("N=100")
axs[0, 1].scatter(np.random.rand(500), (np.random.rand(500)), s=1, marker=".")
axs[0, 1].set_title("N=500")
axs[0, 2].scatter(np.random.rand(1000), (np.random.rand(1000)), s=1, marker=".")
axs[0, 2].set_title("N=1000")
axs[0, 3].scatter(np.random.rand(2000), (np.random.rand(2000)), s=1, marker=".")
axs[0, 3].set_title("N=2000")
axs[0, 4].scatter(np.random.rand(5000), (np.random.rand(5000)), s=1, marker=".")
axs[0, 4].set_title("N=5000")
axs[1, 0].scatter(sobol_seq.i4_sobol_generate(2, 100)[:, 0], sobol_seq.i4_sobol_generate(2, 100)[:, 1], s=1, marker=".")
axs[1, 0].set_ylabel("Quasi-Random")
axs[1, 0].set_title("N=100")
axs[1, 1].scatter(sobol_seq.i4_sobol_generate(2, 500)[:, 0], sobol_seq.i4_sobol_generate(2, 500)[:, 1], s=1, marker=".")
axs[1, 1].set_title("N=500")
axs[1, 2].scatter(sobol_seq.i4_sobol_generate(2, 1000)[:, 0], sobol_seq.i4_sobol_generate(2, 1000)[:, 1], s=1, marker=".")
axs[1, 2].set_title("N=1000")
axs[1, 3].scatter(sobol_seq.i4_sobol_generate(2, 2000)[:, 0], sobol_seq.i4_sobol_generate(2, 2000)[:, 1], s=1, marker=".")
axs[1, 3].set_title("N=2000")
axs[1, 4].scatter(sobol_seq.i4_sobol_generate(2, 5000)[:, 0], sobol_seq.i4_sobol_generate(2, 5000)[:, 1], s=1, marker=".")
axs[1, 4].set_title("N=5000")

plt.show()