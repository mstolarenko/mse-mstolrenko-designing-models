import matplotlib.pyplot as plt
import sobol_seq

fig, axs = plt.subplots(2, 5)

axs[0, 0].hist(sobol_seq.i4_sobol_generate_std_normal(1, 10))
axs[0, 0].set_ylabel("Normal Distributions")
axs[0, 0].set_title("N=10")
axs[0, 1].hist(sobol_seq.i4_sobol_generate_std_normal(1, 50))
axs[0, 1].set_title("N=50")
axs[0, 2].hist(sobol_seq.i4_sobol_generate_std_normal(1, 100))
axs[0, 2].set_title("N=100")
axs[0, 3].hist(sobol_seq.i4_sobol_generate_std_normal(1, 200))
axs[0, 3].set_title("N=200")
axs[0, 4].hist(sobol_seq.i4_sobol_generate_std_normal(1, 500))
axs[0, 4].set_title("N=500")
axs[1, 0].hist(sobol_seq.i4_sobol_generate(1, 10))
axs[1, 0].set_ylabel("Uniform Distribution")
axs[1, 0].set_title("N=10")
axs[1, 1].hist(sobol_seq.i4_sobol_generate(1, 50))
axs[1, 1].set_title("N=50")
axs[1, 2].hist(sobol_seq.i4_sobol_generate(1, 100))
axs[1, 2].set_title("N=100")
axs[1, 3].hist(sobol_seq.i4_sobol_generate(1, 200))
axs[1, 3].set_title("N=200")
axs[1, 4].hist(sobol_seq.i4_sobol_generate(1, 500))
axs[1, 4].set_title("N=500")
plt.show()
