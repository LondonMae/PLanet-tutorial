from planet import *

# define primary variable of interest
interface = ExperimentVariable(
    name = "interface",
    options = ["AR", "VR", "Reality"]
)

# sample 8 units for the study
units = Units(8)

"""
defines a latin square by including interface as a within-subjects 
variable, counterbalancing its conditions, and limiting the number 
of plans to the number of total conditions
"""
design = (
    Design()
        .within_subjects(interface)
        .counterbalance(interface)
        .limit_plans(len(interface))
)

# assign viable orders to sampled units
assignment = assign(units, design)
print(assignment)
# saves tex table of viable orders to an outputs folder
assignment.to_latex()

