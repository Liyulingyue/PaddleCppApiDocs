.. _en_api_paddle_experimental_cross_entropy_with_softmax_:

cross_entropy_with_softmax_
-------------------------------

.. cpp:function:: std::tuple<Tensor & , Tensor> cross_entropy_with_softmax_ ( Tensor & input , const Tensor & label , bool soft_label = false , bool use_softmax = true , bool numeric_stable_mode = true , int ignore_index = - 100 , int axis = - 1 ) 



Path
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

Parameters
:::::::::::::::::::::
	- **input** (Tensor&)
	- **label** (const Tensor&)
	- **soft_label** (bool)
	- **use_softmax** (bool)
	- **numeric_stable_mode** (bool)
	- **ignore_index** (int)
	- **axis** (int)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
