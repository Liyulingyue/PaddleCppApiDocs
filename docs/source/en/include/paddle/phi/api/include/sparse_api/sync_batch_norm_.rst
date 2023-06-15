.. _en_api_paddle_experimental_sparse_sync_batch_norm_:

sync_batch_norm_
-------------------------------

.. cpp:function:: std::tuple<Tensor , Tensor & , Tensor & , Tensor , Tensor , Tensor> sync_batch_norm_ ( const Tensor & x , Tensor & mean , Tensor & variance , const Tensor & scale , const Tensor & bias , bool is_test , float momentum , float epsilon , const std::string & data_layout , bool use_global_stats , bool trainable_statistics ) ;


Path
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/sparse_api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **mean** (Tensor&)
	- **variance** (Tensor&)
	- **scale** (const Tensor&)
	- **bias** (const Tensor&)
	- **is_test** (bool)
	- **momentum** (float)
	- **epsilon** (float)
	- **data_layout** (const std::string&)
	- **use_global_stats** (bool)
	- **trainable_statistics** (bool)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor , Tensor , Tensor , Tensor>
