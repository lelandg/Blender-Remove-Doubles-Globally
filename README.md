# Blender-Remove-Doubles-Globally
Removes doubles from all meshes in a scene, given minimum distance.

This is my first Blender add-on. Simply open in a text editor in Blender and click "Run Script". (If you don't know how to do that, see below.)

You should immediately see a panel at the bottom of the Tools tab in any 3D View that looks like this:
![Alt text](https://github.com/lelandg/Blender-Remove-Doubles-Globally/blob/master/2018-01-22%20-Blender%20-%20Remove%20Doubles%20Globally%20(1).png)

If you need help beyond this (below), I could create a video tutorial if needed. I'm looking into making this an "official" add-on, but have no idea of the process.

For now, if you hold your mouse cursor over the 3D view and press CTRL-right twice, you should get the code workspace. There you should see the text editor. At the bottom of that window there is a menu, and you want Text->Open Text Block. Then navigate to the.py file that you downloaded and open it. You should then see the "Run Script" button.

Note that at the top of the code work space, there is a console output that will show the status. But if you click the Remove Doubles Globally button, it will also print an information message at the very end and tell you how many meshes it processed and how many verts it removed.

![Alt text](https://github.com/lelandg/Blender-Remove-Doubles-Globally/blob/master/2018-01-22%20-Blender%20-%20Remove%20Doubles%20Globally%20(2).png)

If you tick the 'Register' checkbox at the bottom of your text window, it will automatically run the script the next time you open this blend file.

If you want the script to always load at startup, you can import it as an add-on (I think... I'll look into this later), or open your startup scene, open the textblock and take the "Register" box and then save the startup scene (File -> Save Startup File). This latter method is confirmed by me to work, so I'd recommend that until I look into actual Blender plugins.

