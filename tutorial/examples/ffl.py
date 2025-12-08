from planet import * 

# define primary variable of interest
interface = ExperimentVariable(
    name = "interface",
    options = ["ffl", "latex"]
)

# define task type (control) variable
task = ExperimentVariable(
    name = "task",
    options = ["creation", "editing"]
)

# define task number (control) variable
number = ExperimentVariable(
    name = "number",
    options = ["1", "2"]
)

# sample 16 units
units = Units(16)

# design specifying viable orders of the task variable
task_des = (
    Design()
        .within_subjects(task)
        .start_with(task, "creation")
)

# design specifying orders with counterbalanced interface conditions
interface_des = (
    Design()
        .within_subjects(interface)
        .counterbalance(interface)
)

# design specifying orders with counterbalanced task number conditions
number_des = (
    Design()
        .within_subjects(number)
        .counterbalance(number)
)

# crossing interface and task number design is 
# similar to a graeco latin square
num_interface_des = cross(interface_des, number_des)
# finally, we nest designs. This insures that we see all 
# conditions of the num-interface orders before switching to 
# a new task-type
des = nest(outer=task_des, inner=num_interface_des)

assignment = assign(units, des)
print(assignment)
assignment.to_latex()