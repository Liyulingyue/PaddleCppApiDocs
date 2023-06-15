.. _en_api_paddle_experimental_unpool:

unpool
-------------------------------

.. cpp:function:: Tensor unpool ( const Tensor & x , const Tensor & indices , const std::vector<int> & ksize , const std::vector<int> & strides , const std::vector<int> & padding , const IntArray & output_size , const std::string & data_format ) ;


Path
:::::::::::::::::::::
paddle\include\paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **indices** (const Tensor&)
	- **ksize** (const std::vector<int>&)
	- **strides** (const std::vector<int>&)
	- **padding** (const std::vector<int>&)
	- **output_size** (const IntArray&)
	- **data_format** (const std::string&)

Returns
:::::::::::::::::::::
Tensor
