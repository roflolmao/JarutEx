using System;
namespace err_float2
{
    class Program
    {
        const float epsilon = 0.000001f;
        static void Main(string[] args)
        {
            float a = 0.1f;
            float b = 0.2f;
            float c = a + b;
            Console.WriteLine("a = ", a);
            Console.WriteLine("b = ", b);
            Console.WriteLine("a+b = ", (a + b));
            if ((c - 0.3) < epsilon)
                Console.WriteLine("0.3");

            else
                Console.WriteLine("???");
        }
    }
}
