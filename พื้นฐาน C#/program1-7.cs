using System;
namespace loop_while
{
    class Program
    {
        static Int32 x;
        static void Main(string[] args)
        {
            x = 0;
            while (x <= 12)
            {
                Console.WriteLine(x);
                x = x + 3;
            }
        }
    }
}
