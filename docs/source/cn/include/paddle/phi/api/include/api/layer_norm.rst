.. _cn_api_paddle_experimental_layer_norm:

layer_norm
-------------------------------

.. cpp:function:: Tensor layer_norm ( const Tensor & x , const paddle::optional<Tensor> & scale , const paddle::optional<Tensor> & bias , float epsilon = 1e - 5 , int begin_norm_axis = 1 ) 



定义目录
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **scale** (const paddle::optional<Tensor>&)
	- **bias** (const paddle::optional<Tensor>&)
	- **epsilon** (float)
	- **begin_norm_axis** (int)

返回
:::::::::::::::::::::
Tensor
