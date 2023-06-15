.. _cn_api_paddle_experimental_check_numerics:

check_numerics
-------------------------------

.. cpp:function:: std::tuple<Tensor , Tensor> check_numerics ( const Tensor & tensor , const std::string & op_type = "" , const std::string & var_name = "" , int check_nan_inf_level = 0 , int stack_height_limit = - 1 , const std::string & output_dir = "" ) ;



定义目录
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

参数
:::::::::::::::::::::
	- **tensor** (const Tensor&)
	- **op_type** (const std::string&)
	- **var_name** (const std::string&)
	- **check_nan_inf_level** (int)
	- **stack_height_limit** (int)
	- **output_dir** (const std::string&)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
