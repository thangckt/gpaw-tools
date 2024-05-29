Outdirname = 'Charged'
# -------------------------------------------------------------
Mode = 'LCAO'             # Use PW, PW-GW, LCAO, FD  (PW is more accurate, LCAO is quicker mostly.)
# -------------------------------------------------------------
Ground_calc = True     # Ground state calculations
Geo_optim = True       # Geometric optimization with LFBGS
Elastic_calc = False    # Elastic calculation
DOS_calc = True         # DOS calculation
Band_calc = True        # Band structure calculation
Density_calc = True    # Calculate the all-electron density?
Optical_calc = False     # Calculate the optical properties

# -------------------------------------------------------------
# Parameters
# -------------------------------------------------------------
# GEOMETRY
Optimizer = 'LBFGS'     # QuasiNewton, GPMin, LBFGS or FIRE
Max_F_tolerance = 0.05 	# Maximum force tolerance in LBFGS geometry optimization. Unit is eV/Ang.
Max_step = 0.1          # How far is a single atom allowed to move. Default is 0.2 Ang.
Alpha = 60.0            # LBFGS only: Initial guess for the Hessian (curvature of energy surface)
Damping = 1.0           # LBFGS only: The calculated step is multiplied with this number before added to the positions
Fix_symmetry = True    # True for preserving the spacegroup symmetry during optimisation
# Which components of strain will be relaxed: EpsX, EpsY, EpsZ, ShearYZ, ShearXZ, ShearXY
# Example: For a x-y 2D nanosheet only first 2 component will be true
Relax_cell = [False, False, False, False, False, False]
Hydrostatic_pressure=0.0 #GPa

# ELECTRONIC
Cut_off_energy = 340 	# eV
#Ground_kpts_density = 2.5     # pts per Å^-1  If the user prefers to use this, kpts_x,y,z will not be used automatically.
Ground_kpts_x = 4 			    # kpoints in x direction
Ground_kpts_y = 4				# kpoints in y direction
Ground_kpts_z = 1				# kpoints in z direction
Ground_gpts_density = 0.2      # (for LCAO) Unit is Å. If the user prefers to use this, gpts_x,y,z will not be used automatically.
Ground_gpts_x = 8              # grid points in x direction (for LCAO)
Ground_gpts_y = 8              # grid points in y direction (for LCAO)
Ground_gpts_z = 8              # grid points in z direction (for LCAO)
Gamma = True
Band_path = 'GKMG'	    # Brillouin zone high symmetry points
Band_npoints = 40		# Number of points between high symmetry points
Setup_params = {}            # Can be used like {'N': ':p,6.0'}, for none use {}

XC_calc = 'LDA'         # Exchange-Correlation, choose one: LDA, PBE, GLLBSCM, HSE06, HSE03, revPBE, RPBE, PBE0, EXX, B3LYP

Ground_convergence = {}   # Convergence items for ground state calculations
Band_convergence = {'bands':8}   # Convergence items for band calculations
Occupation = {'name': 'fermi-dirac', 'width': 0.05}  # Refer to GPAW docs: https://wiki.fysik.dtu.dk/gpaw/documentation/basic.html#occupation-numbers

DOS_npoints = 501        # Number of points
DOS_width = 0.0          # Width of Gaussian smearing.  Use 0.0 for linear tetrahedron interpolation
DOS_convergence = {}  # Convergence items for DOS calculations

Spin_calc = False        # Spin polarized calculation?
Magmom_per_atom = 1.0    # Magnetic moment per atom
Refine_grid = 4             # refine grid for all electron density (1, 2 [=default] and 4)
Total_charge = 1.0       # Total charge. Normally 0.0 for a neutral system.

#GENERAL
MPI_cores = 4            # Number of cores in calculation.
Energy_min = -5 		# eV. It is the minimum energy value for band structure and DOS figures.
Energy_max = 5  		# eV. It is the maximum energy value for band structure and DOS figures.
