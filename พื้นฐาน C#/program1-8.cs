using System;
namespace loop_for
{
    class Program
    {
        static Int32 x;
        static void Main(string[] args)
        {
            for (x=0; x <= 12; x+=3)
            {
                Console.WriteLine(x);
            }
        }
    }
}
