.. _cn_api_paddle_experimental_unpool3d:

unpool3d
-------------------------------

..cpp: function::Tensor unpool3d ( const Tensor & x , const Tensor & indices , const std::vector<int> & ksize , const std::vector<int> & strides = { 1 , 1 , 1 } , const std::vector<int> & paddings = { 0 , 0 , 0 } , const std::vector<int> & output_size = { 0 , 0 , 0 } , const std::string & data_format = "NCDHW" ) ;


定义目录
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **indices** (const Tensor&)
	- **ksize** (const std::vector<int>&)
	- **strides** (const std::vector<int>&)
	- **paddings** (const std::vector<int>&)
	- **output_size** (const std::vector<int>&)
	- **data_format** (const std::string&)

返回
:::::::::::::::::::::
Tensor
