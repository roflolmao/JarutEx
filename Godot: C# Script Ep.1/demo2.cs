//วิ่งจากทางซ้ายล่างขึ้นขวาบน
using Godot;
using System;
public class Icon : Sprite
{
	int num1, num2, direction;
public override void _Ready() {
	num1 = 2;
	num2 = 0;
	direction = 0;
}
public override void _Process(float delta)
{
	float result = (float)Math.Pow(num1, num2);
	Position = new Vector2(num2*30, 500-(float)(result/5000000));
	if (direction == 0) {
		num2 += 1;
		if (num2 > 30) {
			direction = 1;
		}
	} else {
		num2 -= 1;
		if (num2 == 0) {
			direction = 0;
		}
	}
}
}
