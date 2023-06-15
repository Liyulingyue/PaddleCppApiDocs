.. _en_api_paddle_experimental_conv2d:

conv2d
-------------------------------

.. cpp:function:: Tensor conv2d ( const Tensor & input , const Tensor & filter , const std::vector<int> & strides = { 1 , 1 } , const std::vector<int> & paddings = { 0 , 0 } , const std::string & padding_algorithm = "EXPLICIT" , const std::vector<int> & dilations = { 1 , 1 } , int groups = 1 , const std::string & data_format = "NCHW" ) ;


Path
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

Parameters
:::::::::::::::::::::
	- **input** (const Tensor&)
	- **filter** (const Tensor&)
	- **strides** (const std::vector<int>&)
	- **paddings** (const std::vector<int>&)
	- **padding_algorithm** (const std::string&)
	- **dilations** (const std::vector<int>&)
	- **groups** (int)
	- **data_format** (const std::string&)

Returns
:::::::::::::::::::::
Tensor
