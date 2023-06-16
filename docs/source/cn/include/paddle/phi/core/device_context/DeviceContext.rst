.. _cn_api_DeviceContext:

DeviceContext `源代码 <https://github.com/PaddlePaddle/Paddle/blob/develop/paddle\include\paddle\phi\core\device_context.h>`_
-------------------------------

.. cpp:class:: DeviceContext

 DeviceContext provides device-related interfaces. All kernels must access the interfaces provided by the backend through DeviceContext.


定义目录
:::::::::::::::::::::
paddle\include\paddle\phi\core\device_context.h

方法
:::::::::::::::::::::

DeviceContext ( ) ;
'''''''''''
Default construct.



DeviceContext ( const DeviceContext & ) ;
'''''''''''
Copy construct.



DeviceContext ( DeviceContext & & ) ;
'''''''''''
Move construct.



DeviceContext & operator = ( DeviceContext & & ) ;
'''''''''''
Move assign operator.



**返回**
'''''''''''
DeviceContext &

virtual ~DeviceContext ( ) ;
'''''''''''
Default destruct.



void SetAllocator ( const Allocator * ) ;
'''''''''''
Set the device-related Allocator object. 


void SetHostAllocator ( const Allocator * ) ;
'''''''''''
Set the host Allocator object. 


void SetZeroAllocator ( const Allocator * ) ;
'''''''''''
Set the zero-size Allocator object. 


void SetHostZeroAllocator ( const Allocator * ) ;
'''''''''''
Set the zero-size host Allocator object. 


void SetPinnedAllocator ( const Allocator * ) ;
'''''''''''
Set the zero-size Allocator object. 


const Allocator & GetAllocator ( ) const ;
'''''''''''
Get the const Allocator object. 


**返回**
'''''''''''
Allocator


const Allocator & GetHostAllocator ( ) const ;
'''''''''''
Get the const device-related Allocator object. 


**返回**
'''''''''''
Allocator


const Allocator & GetZeroAllocator ( ) const ;
'''''''''''



**返回**
'''''''''''
const Allocator &

const Allocator & GetHostZeroAllocator ( ) const ;
'''''''''''



**返回**
'''''''''''
const Allocator &

const Allocator & GetPinnedAllocator ( ) const ;
'''''''''''



**返回**
'''''''''''
const Allocator &

void SetCUDAGraphAllocator ( const Allocator * ) ;
'''''''''''
Set the CUDA graph Allocator object. 


const Allocator & GetCUDAGraphAllocator ( ) const ;
'''''''''''
Get the const CUDA graph Allocator object. 


**返回**
'''''''''''
Allocator


bool IsCUDAGraphAllocatorValid ( ) const ;
'''''''''''
Test whether the CUDA graph allocator is valid This method should be called before calling GetCUDAGraphAllocator(). Other unit can calls GetCUDAGraphAllocator() method, only when this method returns True! 


**返回**
'''''''''''
true if cuda_graph_allocator_ is valid, false otherwise


virtual void * Alloc ( TensorBase * , DataType dtype , size_t requested_size = 0 , bool pinned = false , bool fake_alloc = false ) const ;
'''''''''''
Allocate device memory for tensor.


**参数**
'''''''''''
	- **dtype** (DataType)
	- **requested_size** (size_t)
	- **pinned** (bool)
	- **fake_alloc** (bool)

template<typename T>
T * Alloc ( TensorBase * tensor , size_t requested_size = 0 , bool pinned = false ) const ;
'''''''''''


**参数**
'''''''''''
	- **tensor** (TensorBase*)
	- **requested_size** (size_t)
	- **pinned** (bool)

**返回**
'''''''''''
T *

void * HostAlloc ( TensorBase * tensor , DataType dtype , size_t requested_size = 0 , bool fake_alloc = false ) const ;
'''''''''''
Allocate host memory for tensor.


**参数**
'''''''''''
	- **tensor** (TensorBase*)
	- **dtype** (DataType)
	- **requested_size** (size_t)
	- **fake_alloc** (bool)

template<typename T>
T * HostAlloc ( TensorBase * tensor , size_t requested_size = 0 ) const ;
'''''''''''


**参数**
'''''''''''
	- **tensor** (TensorBase*)
	- **requested_size** (size_t)

**返回**
'''''''''''
T *

virtual const Place & GetPlace ( ) const = 0 ;
'''''''''''



**返回**
'''''''''''
const Place &

virtual void Wait ( ) const {
'''''''''''



void SetGenerator ( Generator * ) ;
'''''''''''
Set the generator for special op. 


Generator * GetGenerator ( ) const ;
'''''''''''
Get the generator object. 


**返回**
'''''''''''
Generator


void SetHostGenerator ( Generator * ) ;
'''''''''''
Set the host generator for special op. 


Generator * GetHostGenerator ( ) const ;
'''''''''''
Get the host generator object. 


**返回**
'''''''''''
Generator


TypeInfo<DeviceContext> type_info ( ) const {
'''''''''''
Return the type information of the derived class to supportsafely downcast in non-rtti environment. 


**返回**
'''''''''''
The type information of the derived class.


void SetCommContext ( distributed::CommContext * comm_context ) ;
'''''''''''
Set the comm context point. 

**参数**
'''''''''''
	- **comm_context** (distributed::CommContext*)

distributed::CommContext * GetCommContext ( ) const ;
'''''''''''
Get the comm context point. 


**返回**
'''''''''''
comm context point


