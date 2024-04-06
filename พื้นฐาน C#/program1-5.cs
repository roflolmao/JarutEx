using System;
namespace level_if
{
    class Program
    {
        public static float score;
        static void Main(string[] args)
        {
            score = 35.0f;
            if (score <10) {
                Console.WriteLine("Level 0");
            } else if (score < 20) {
                Console.WriteLine("Level 1");
            } else if (score < 30) {
                Console.WriteLine("Level 2");
            } else if (score < 40) {
                Console.WriteLine("Level 3");
            } else {
                Console.WriteLine("Level 4");
            }
        }
    }
}
