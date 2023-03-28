# Cars overtaking
<p>My programming study project in Tula State University (Russian Federation).</p>

<h2>Description</h2>
<p>A program that calculates the possibility of overtaking. 
Has 3 methods of work: normal, with oncoming traffic and with oncoming overtaking.</p>

<h2>Libraries</h2>
<p>This program using library <code>customtkinter</code> with beautiful design and some features
that was needed for this project and classic <code>tkinter</code> used to display system alerts.</p>

<h2> Methods </h2>
<p>Let's analyze the work of the individual modules.</p>
<h3>Initiation</h3>
<p><code>__init__</code> declares all app's widgets and displays some of them. Another widgets that 
hided instantly will be displayed if you press one or two check buttons. This working by using 
<code>oncoming_traffic</code> and <code>oncoming_overtaking</code> methods. If you choose only second method, 
you will see error, because you need to choose two methods to use oncoming overtaking.</p>

<h3>Start</h3>
<p>This method using to prepare program to next calculations. Looking at pressed check buttons it calls
methods to make calculations.</p>

<h3>First method</h3>
<p>Now we're starting some calculations. This method in <code>App</code> class takes values from input boxes
to <code>first</code> method in <code>methods\first.py</code> and depending on return displays result in
system alert.</p>
<p>For first <code>first</code> method transforming entered values to the desired number system. Next it 
checking the possibility of overtaking(if first car has more boost or speed then second car). Next it 
calculates the way desired to complete overtaking: <code>_way = 2 * between + first_length + second_length</code>.
And finally program can calculate the time of overtaking. If first car don't have a boost <code>
_time = _way / abs(second_speed - first_speed)</code>, in another case <code>_time = _way / abs(second_speed - first_
speed) + (second_speed - first_speed) / first_boost</code>. If this method has a result, it will return them,
if not program return <code>None</code></p>

<h3>Second method</h3>
<p>This method works like first method for first two cars, but for third car it has some changes.
After calculating first and second cars parameters, program finds coordinate X for first and third cars 
<code>_new_first_x = first_x + first_speed * _time + (first_boost * (_time ** 2)) / 2</code>
where <code>first_x = 0</code> and <code>_new_third_x = third_x - third_speed * _time - (third_boost * (_time ** 2)) / 
2</code> where <code>third_x = second_x + third_between</code>.</p>
<p>If first car's coordinate lower than third car's program returns result. If not program returning <code>'smash'</code>
which signals to <code>second_method</code> in <code>App</code> class to display smash alert.</p>

<h3>Third method</h3>
<p>This method working like first and second simultaneously. It calculates the time
to overtaking for first two cars and two another. After finding two times to overtaking,
program takes higher of them like main time and calculates coordinates to first and 
fourth car after main time. All return features working like in second method.</p>