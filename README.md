## CE-4-Readable-RAW 
代码思路来源https://github.com/siyu6974/ChangE_4_data_playground  
此代码读取pds文件  
输出为灰度16bit png  
可保留图像的完整信息供后期使用
#### 注意：处理前需按如下规则剔除原数据中异常的文件，否则会造成处理中断  
(1) .2B文件的正确大小为7938KB或1985KB，如果不是此大小，说明数据损坏，需要和对应的.2BL一起删除  
(2) 有些时候一张图片数据会丢失一个.2B或.2BL文件，需要将余下的不完整文件删除
