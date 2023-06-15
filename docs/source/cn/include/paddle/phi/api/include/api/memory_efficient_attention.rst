.. _cn_api_paddle_experimental_memory_efficient_attention:

memory_efficient_attention
-------------------------------

.. cpp:function:: std::tuple<Tensor , Tensor , Tensor> memory_efficient_attention ( const Tensor & query , const Tensor & key , const Tensor & value , const paddle::optional<Tensor> & bias , const paddle::optional<Tensor> & cu_seqlens_q , const paddle::optional<Tensor> & cu_seqlens_k , const paddle::optional<Tensor> & causal_diagonal , const paddle::optional<Tensor> & seqlen_k , const Scalar & max_seqlen_q , const Scalar & max_seqlen_k , bool causal , double dropout_p , float scale , bool is_test ) ;


定义目录
:::::::::::::::::::::
paddle\include\paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **query** (const Tensor&)
	- **key** (const Tensor&)
	- **value** (const Tensor&)
	- **bias** (const paddle::optional<Tensor>&)
	- **cu_seqlens_q** (const paddle::optional<Tensor>&)
	- **cu_seqlens_k** (const paddle::optional<Tensor>&)
	- **causal_diagonal** (const paddle::optional<Tensor>&)
	- **seqlen_k** (const paddle::optional<Tensor>&)
	- **max_seqlen_q** (const Scalar&)
	- **max_seqlen_k** (const Scalar&)
	- **causal** (bool)
	- **dropout_p** (double)
	- **scale** (float)
	- **is_test** (bool)

返回
:::::::::::::::::::::
std::tuple<Tensor , Tensor , Tensor>
