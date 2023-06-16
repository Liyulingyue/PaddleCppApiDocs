.. _cn_api_paddle_experimental_depthwise_conv2d:

depthwise_conv2d
-------------------------------

.. cpp:function:: Tensor depthwise_conv2d ( const Tensor & input , const Tensor & filter , const std::vector<int> & strides = { 1 , 1 } , const std::vector<int> & paddings = { 0 , 0 } , const std::string & padding_algorithm = "EXPLICIT" , int groups = 1 , const std::vector<int> & dilations = { 1 , 1 } , const std::string & data_format = "NCHW" ) 



定义目录
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

参数
:::::::::::::::::::::
	- **input** (const Tensor&)
	- **filter** (const Tensor&)
	- **strides** (const std::vector<int>&)
	- **paddings** (const std::vector<int>&)
	- **padding_algorithm** (const std::string&)
	- **groups** (int)
	- **dilations** (const std::vector<int>&)
	- **data_format** (const std::string&)

返回
:::::::::::::::::::::
Tensor
