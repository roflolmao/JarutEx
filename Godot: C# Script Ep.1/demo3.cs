using Godot;
using System;
public class Player6 : Sprite
{
	int x;
	public override void _Ready()
	{
		x = 0;
	}
	public override void _Process(float delta)
	{
		float y = (float)Math.Log(x)*80;
		x += 1;
		Position = new Vector2(x*10, 500-y);
		if (x > 90) {
			x = 0;
		}
	}
}
