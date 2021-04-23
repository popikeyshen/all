# Dissasemble RGB to gray and color component

Look at this beautiful image of a cat.

<!--![cat.jpg](http://github.com/popikeyshen/all/disassemble_rgb/cat.jpg)-->
<p align="center"> <img src="https://github.com/popikeyshen/all/blob/main/disassemble_rgb/cat.jpg" width = 40% /> </p>

In some tasks, such as composition or neural networks, you would like to know its color or brightness in order to work separately with color and ignore the darkness and saturation of individual areas. Since the very common RGB format contains 3 components, this can interfere. I offer several ways to highlight only the color component.

<!--![color](https://github.com/popikeyshen/all/blob/main/disassemble_rgb/rgb.jpg)![gray](https://github.com/popikeyshen/all/blob/main/disassemble_rgb/gray.jpg)-->
<p align="center"> 
<img src="https://github.com/popikeyshen/all/blob/main/disassemble_rgb/rgb.jpg" width = 40% />  <img src="https://github.com/popikeyshen/all/blob/main/disassemble_rgb/gray.jpg" width = 40% /> 
</p>

Where one way is to use Opencv HSV convertation and another is to convert RGB cube space to spherical, where the value(gray) component will be distance, and color component - teta and phi angles. 

<p align="center"> 
<img src="https://github.com/popikeyshen/all/blob/main/disassemble_rgb/spherical.jpg" width = 40% />



<p align="center"> 
<img src="https://github.com/popikeyshen/all/blob/main/disassemble_rgb/rgbToHSV.jpg" width = 40% />
</p>
