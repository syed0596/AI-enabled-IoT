# AI-enabled-IoT
The proposed product, in general, is aimed to apply artificial intelligence concept equipped with computer vision capabilities for outdoor security/surveillance that focuses on innovative technique to detect the number plates of vehicles and recognize characters from it in real-time and, additionally, include the typical facial recognition system that also works in real-time using an IoT device.

![AI-enabled-IoT](Demo-Video.gif)

The proposed system processes the data and produce the result in the real-time as soon as it receives the information from IoT device unlike traditional approach where the data is stored first and then processing begins. In order to achieve best results for detecting the type of vehicle (i.e. car or motorcycle) and recognizing characters from number plates, YOLO based Convolutional Neural Network models are trained at all stages on over 6000 images that required manual labelling of each of the image to extract its annotations.

Raspberry Pi and a Pi Camera are responsible to stream live video over the network and act as client-side/IoT device, whereas the server-side software running on a PC 64-bit dual core processor with 8GB RAM is capable to detect vehicles (i.e. motorcycles and cars) and detect/recognize number plates of five different regions namely American, Brazilian, Chinese, European and Taiwanese and simultaneously recognize license plate characters and face in real-time.

# Citations
Hsu, G.S., Chen, J.C. and Chung, Y.Z., "Application-Oriented License Plate Recognition," Vehicular Technology, IEEE Trans., vol.62, no.2, pp.552-561, Feb. 2013
