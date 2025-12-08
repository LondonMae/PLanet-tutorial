from planet import *

# define primary variable of interest
interface = ExperimentVariable(
    name = "treatment",
    options = ["AR", "VR", "reality"]
)

# sample 8 units for the study
units = Units(8)

"""
defines a fully counterbalanced design by including interface as a 
within-subjects variable and counterbalancing its conditions
"""
des = (
    Design()
        .within_subjects(interface)
        .counterbalance(interface)
)

assignment = assign(units, des)
print(assignment)
assignment.to_latex()