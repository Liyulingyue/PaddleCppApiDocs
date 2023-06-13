.. _en_api_paddle_experimental_roi_align:

roi_align
-------------------------------

.. cpp:function:: Tensor roi_align ( const Tensor & x , const Tensor & boxes , const paddle::optional<Tensor> & boxes_num , int pooled_height , int pooled_width , float spatial_scale , int sampling_ratio , bool aligned ) ;


Path
:::::::::::::::::::::
paddle/include/paddle/phi/api/include/api.h

Parameters
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **boxes** (const Tensor&)
	- **boxes_num** (const paddle::optional<Tensor>&)
	- **pooled_height** (int)
	- **pooled_width** (int)
	- **spatial_scale** (float)
	- **sampling_ratio** (int)
	- **aligned** (bool)

Returns
:::::::::::::::::::::
Tensor
