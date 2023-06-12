.. _cn_api_paddle_experimental_depthwise_conv2d_transpose:

depthwise_conv2d_transpose
-------------------------------

..cpp: function::Tensor depthwise_conv2d_transpose ( const Tensor & x , const Tensor & filter , const std::vector<int> & strides = { 1 , 1 } , const std::vector<int> & paddings = { 0 , 0 } , const std::vector<int> & output_padding = { } , const IntArray & output_size = { } , const std::string & padding_algorithm = "EXPLICIT" , int groups = 1 , const std::vector<int> & dilations = { 1 , 1 } , const std::string & data_format = "NCHW" ) ;


定义目录
:::::::::::::::::::::
D:\Codes\PaddleCppApiDocs\venv\lib\site-packages\paddle\include\paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **filter** (const Tensor&)
	- **strides** (const std::vector<int>&)
	- **paddings** (const std::vector<int>&)
	- **output_padding** (const std::vector<int>&)
	- **output_size** (const IntArray&)
	- **padding_algorithm** (const std::string&)
	- **groups** (int)
	- **dilations** (const std::vector<int>&)
	- **data_format** (const std::string&)

返回
:::::::::::::::::::::
Tensor
