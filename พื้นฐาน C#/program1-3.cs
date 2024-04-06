using System;

namespace temp_conv
{
    class Program
    {
        public static double C;
        public static double F;

        static void Main(string[] args)
        {
            C = 35.0;
            F = C * 9.0 / 5.0 + 32;
            Console.WriteLine(F);
        }
    }
}
