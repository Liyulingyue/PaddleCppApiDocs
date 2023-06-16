.. _cn_api_paddle_experimental_send_uv:

send_uv
-------------------------------

.. cpp:function:: Tensor send_uv ( const Tensor & x , const Tensor & y , const Tensor & src_index , const Tensor & dst_index , const std::string & message_op = "ADD" ) ;



本 API 与 Python API 对齐，详细用法可参考链接：[paddle.send_uv](https://www.paddlepaddle.org.cn/documentation/docs/zh/api/paddle/send_uv_cn.html)

定义目录
:::::::::::::::::::::
paddle\include\paddle\phi\api\include\api.h

参数
:::::::::::::::::::::
	- **x** (const Tensor&)
	- **y** (const Tensor&)
	- **src_index** (const Tensor&)
	- **dst_index** (const Tensor&)
	- **message_op** (const std::string&)

返回
:::::::::::::::::::::
Tensor
