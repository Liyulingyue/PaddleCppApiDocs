.. _cn_api_CPUContext:

CPUContext `源代码 <https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\include\paddle\phi\backends\cpu\cpu_context.h>`_
-------------------------------

.. cpp:class:: CPUContext



定义目录
:::::::::::::::::::::
paddle\include\paddle\phi\backends\cpu\cpu_context.h

方法
:::::::::::::::::::::

CPUContext ( ) ;
'''''''''''



CPUContext ( CPUContext & & ) ;
'''''''''''



CPUContext & operator = ( CPUContext & & ) ;
'''''''''''



**返回**
'''''''''''
CPUContext &

explicit CPUContext ( const Place & ) ;
'''''''''''



virtual ~CPUContext ( ) ;
'''''''''''



Eigen::DefaultDevice * eigen_device ( ) const ;
'''''''''''



**返回**
'''''''''''
Eigen::DefaultDevice *

const Place & GetPlace ( ) const override ;
'''''''''''



**返回**
'''''''''''
const Place &

static const char * name ( ) {
'''''''''''



**返回**
'''''''''''
const char *

