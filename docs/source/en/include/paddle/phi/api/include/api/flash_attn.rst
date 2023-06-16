.. _en_api_paddle_experimental_flash_attn:

flash_attn
-------------------------------

.. cpp:function:: std::tuple<Tensor , Tensor> flash_attn ( const Tensor & q , const Tensor & k , const Tensor & v , const paddle::optional<Tensor> & fixed_seed_offset , float dropout = 0.0 , bool causal = false , bool return_softmax = false , bool is_test = false , const std::string & rng_name = "" ) 



Path
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

Parameters
:::::::::::::::::::::
	- **q** (const Tensor&)
	- **k** (const Tensor&)
	- **v** (const Tensor&)
	- **fixed_seed_offset** (const paddle::optional<Tensor>&)
	- **dropout** (float)
	- **causal** (bool)
	- **return_softmax** (bool)
	- **is_test** (bool)
	- **rng_name** (const std::string&)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
