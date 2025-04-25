# nerf_target_controller
game controller using an arduino and a nerf elite digital light-up target
https://www.amazon.co.uk/NER0156-Elite-Digital-Target-Multi/dp/B06XGC9964?source=ps-sl-shoppingads-lpcontext&ref_=fplfs&smid=A1R64IUNVWPSMR&th=1

using the circuit baord inside the target, you can take the input from the buttons and simulate key presses to play games. i played geometry dash with a nerf gun a minute ago

to make the arduino properly detect signals from the target's circuit board, you have to take the wires onto a breadboard, then to arduino. these connections are also connected to the arduino's ground through 10k resistors. the circuit board takes in vdd (i did 5v), so the ground for the arduino and circuit board were different and te arduino didn't know what was high or low for the cirucit board. having a shared ground fixed the problem, but made the circuit a whole lot bigger and more annoying
