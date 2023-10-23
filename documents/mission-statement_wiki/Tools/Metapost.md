### meta scriptting- get last state
In case you would like to find the deformation/scalar/vector types and the corresponding number of state for a given solver file you could use the:

results.DeformationTypes , results.ScalarTypes , results.VectorTypes

Please check the provided examples of these functions.

However, I suppose that you have some states already loaded and you would like to read some extra results only on the 1 interval 5 until the last state. If so, there are the following:

You could execute the command "animation last" so that to select the last state of the animation.

Then you could use the META variable CUR_STATE in order to receive the number of the last state. This can be implement in python script as follow:

# PYTHON script
import os
import meta
from meta import utils

def main():
	utils.MetaCommand('animation last')
	last_state_num = utils.MetaGetVariable('CUR_STATE')
	print(last_state_num )
if __name__ == '__main__':
	main()


Alternatively, you could use the Built-in function expression that returns the total states of a specific model ,window.
This can be implement in python code as follow:

# PYTHON script
import meta
from meta import utils


def main():
	expression = '`w[MetaPost]m0s_totalstates`'
	value = utils.EvalBuiltInFunction(expression)
	print(value)


if __name__ == '__main__':
	main()
-----------------------
one additional way that I forgot to mentioned is the following:

Generally, through GUI you can apply a filter so that to select a specific range (defining also the interval) as follow:
![image](uploads/240b115e75be35c0bac59a3671cd6d9b/image.png)


In case you would like to include the last state as well, you can press the cross button(in the following image), so that to enable the last checkbox, and then select last = Yes as it is depicted in the image:

![image](uploads/f72f5d57370e9315e87404ee8fd874de/image.png)

Then switching the filter on the "Advanched" mode, you can change the "and" to "or" so that to keep both range of state as well as the last state.
![image](uploads/d7900404db308e557dc375099a5df380/image.png)


Finally, this expression can be used in the read results command as follow:

e.g.  read dis Dyna3d C:/User/d3plot "%'Serial Id' in range (1, 12, 2) or last = Yes"  Displacements
In other words, advanced filter expression can be defined in META commands using the % symbol and use single quotes (') instead of double quotes (")

