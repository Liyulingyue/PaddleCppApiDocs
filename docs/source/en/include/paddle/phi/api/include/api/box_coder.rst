.. _en_api_paddle_experimental_box_coder:

box_coder
-------------------------------

.. cpp:function:: Tensor box_coder ( const Tensor & prior_box , const paddle::optional<Tensor> & prior_box_var , const Tensor & target_box , const std::string & code_type = "encode_center_size" , bool box_normalized = true , int axis = 0 , const std::vector<float> & variance = { } ) 



Path
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

Parameters
:::::::::::::::::::::
	- **prior_box** (const Tensor&)
	- **prior_box_var** (const paddle::optional<Tensor>&)
	- **target_box** (const Tensor&)
	- **code_type** (const std::string&)
	- **box_normalized** (bool)
	- **axis** (int)
	- **variance** (const std::vector<float>&)

Returns
:::::::::::::::::::::
Tensor
