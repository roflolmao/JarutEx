using System;
namespace array1
{
    class Program
    {
        static UInt16[] actor_stat;
        static void Main(string[] args)
        {
            actor_stat = new ushort[7];
            String[] stat_info = {"ST","AC","DX","RS","HP","MP","EX"};
            actor_stat[0] = 5; // ST
            actor_stat[1] = 4; // AC
            actor_stat[2] = 5; // DX
            actor_stat[3] = 5; // RS
            actor_stat[4] = 10; // HP
            actor_stat[5] = 10; // MP
            actor_stat[6] = 0; // EX
            for (int idx=0; idx<actor_stat.Length; idx++)
            {
                Console.WriteLine(stat_info[idx].ToString() +
                                  "="+ actor_stat[idx].ToString());
            }
        }
    }
}
