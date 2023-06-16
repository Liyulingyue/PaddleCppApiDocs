.. _en_api_paddle_experimental_class_center_sample:

class_center_sample
-------------------------------

.. cpp:function:: std::tuple<Tensor , Tensor> class_center_sample ( const Tensor & label , int num_classes , int num_samples , int ring_id = 0 , int rank = 0 , int nranks = 1 , bool fix_seed = false , int seed = 0 ) 



Path
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

Parameters
:::::::::::::::::::::
	- **label** (const Tensor&)
	- **num_classes** (int)
	- **num_samples** (int)
	- **ring_id** (int)
	- **rank** (int)
	- **nranks** (int)
	- **fix_seed** (bool)
	- **seed** (int)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
