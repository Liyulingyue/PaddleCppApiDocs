.. _en_api_paddle_experimental_conv3d_transpose:

conv3d_transpose
-------------------------------

.. cpp:function:: Tensor conv3d_transpose ( const Tensor & x , const Tensor & filter , const std::vector<int> & strides = { 1 , 1 , 1 } , const std::vector<int> & paddings = { 0 , 0 , 0 } , const std::vector<int> & output_padding = { } , const std::vector<int> & output_size = { } , const std::string & padding_algorithm = "EXPLICIT" , int groups = 1 , const std::vector<int> & dilations = { 1 , 1 , 1 } , const std::string & data_format = "NCHW" ) ;



Path
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **filter** (const Tensor&)
	- **strides** (const std::vector<int>&)
	- **paddings** (const std::vector<int>&)
	- **output_padding** (const std::vector<int>&)
	- **output_size** (const std::vector<int>&)
	- **padding_algorithm** (const std::string&)
	- **groups** (int)
	- **dilations** (const std::vector<int>&)
	- **data_format** (const std::string&)

Returns
:::::::::::::::::::::
Tensor
