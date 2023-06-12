.. _en_api_paddle_experimental_flash_attn_unpadded:

flash_attn_unpadded
-------------------------------

..cpp: function::std::tuple<Tensor , Tensor> flash_attn_unpadded ( const Tensor & q , const Tensor & k , const Tensor & v , const Tensor & cu_seqlens_q , const Tensor & cu_seqlens_k , const paddle::optional<Tensor> & fixed_seed_offset , int64_t max_seqlen_q , int64_t max_seqlen_k , float scale , float dropout = 0.0 , bool causal = false , bool return_softmax = false , bool is_test = false , const std::string & rng_name = "" ) ;


Path
:::::::::::::::::::::
D:\Codes\PaddleCppApiDocs\venv\lib\site-packages\paddle\include\paddle\phi\api\include\api.h

Parameters
:::::::::::::::::::::
	- **q** (const Tensor&)
	- **k** (const Tensor&)
	- **v** (const Tensor&)
	- **cu_seqlens_q** (const Tensor&)
	- **cu_seqlens_k** (const Tensor&)
	- **fixed_seed_offset** (const paddle::optional<Tensor>&)
	- **max_seqlen_q** (int64_t)
	- **max_seqlen_k** (int64_t)
	- **scale** (float)
	- **dropout** (float)
	- **causal** (bool)
	- **return_softmax** (bool)
	- **is_test** (bool)
	- **rng_name** (const std::string&)

Returns
:::::::::::::::::::::
std::tuple<Tensor , Tensor>
