class operators3
{
    public static void main(String args[])
    {
        /*
        Bitwise Operator
        ---------------------
        1. Bitwise and (&)
        2. Bitwise or (|)
        3. Bitwise xor (^)
        4. Left shift (<<)
        5. Right shift (>>)
        6. Complement (~)
        */
        /*
         1 1 0 1 -> 13
        0 1 1 0 -> 6
        -------------- [(& (and) operation)]
        0 1 0 0 -> 4 (output)
 
        1 1 0 1 -> 13
        0 1 1 0 -> 6
        ------------- [(| (or) operation)]
        1 1 1 1 -> 15

        1 1 0 1 -> 13
        0 1 1 0 -> 6
        -------------- [(^ (xor operation) OR same = 0 else 1)].
        1 0 1 1 -> 11

        32 16 8 4 2 1
        0  0  0 1 0 1 -> 5
        --------------- [(<<3 (left shift 3)) = Number*2^(no of shifts)];
        1  0  1 0 0 0 -> 40
        15 << 2 = 15 * 2^2 = 15 * 4 = 60 (answer)/

        32  16  8  4  2  1
        0   1   0  1  0  1 = 21;
        -------------------------  [(>>2 (right shift 2)) = Number/(2^(Number of shifts))]
        0   0   0  1  0  1 =  5;  = 21/(2^2) = 21 / 4 = 5;

        32  16  8  4  2  1
        0   0   0  1  0  1 =  5;
        ------------------------- (~ (complement)) = [~n = (-1)(n + 1)]
        ~5 = (-1) (5 + 1) = (-1)(6) = -6;

        ~(-6) = (-1)(-6 + 1) = (-1)(-5) = 5;
        */
       int a = -9;
       System.out.println(~a);
    }
}