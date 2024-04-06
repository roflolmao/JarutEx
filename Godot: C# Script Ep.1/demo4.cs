using Godot;
using System;

public class Lift : StaticBody2D
{
float y;
int direction;
public override void _Ready()
{       
	direction = 0;
	y = 200;
}
public override void _PhysicsProcess(float delta)
{
	Position = new Vector2(Position.x, y);
	if (direction == 0) {
		y+=2;
		if (y > 400) {
			direction = 1;
		}
	} else {
		y -= 2;
		if (y < 200) {
			direction = 0;
		}
	}
}
}
