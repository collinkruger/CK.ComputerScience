using System;
using System.Diagnostics;
using System.Linq;

public static class MergeSort
{
    // Prep Arrays To Sort
    public static void Prep(int[] a, int[] b, int[] c)
    {
        // Sorted
        for (int i = 0; i < a.Length; i++)
            a[i] = i;

        // Sorted In Reverse Order
        for (int i = 0; i < b.Length; i++)
            b[i] = b.Length - 1 - i;

        // Interleaved Sorted And Reverse Order
        for (int i = 0; i < c.Length; i++)
            c[i] = i % 2 == 0 ? i : b.Length - i;
    }

    // Niave Implementation
    public static int[] Niave(int[] arr)
    {
        static (int[], int[]) Split(int[] arr)
        {
            var i = arr.Length / 2;
            return (arr.Take(i).ToArray(),
                    arr.Skip(i).ToArray());
        }
        
        static int[] Merge(int[] arr1, int[] arr2)
        {
            var arr = new int[arr1.Length + arr2.Length];
            
            int i = 0;
            int j = 0;
            int o = 0;
            
            for (; o < arr.Length && i < arr1.Length && j < arr2.Length; o++)
            {
                var a = arr1[i];
                var b = arr2[j];
                
                if (a < b)
                {
                    i += 1;
                    arr[o] = a;
                }
                else
                {
                    j += 1;
                    arr[o] = b;
                }
            }
            
            while (i < arr1.Length)
            {
                arr[o] = arr1[i];
                i += 1;
                o += 1;
            }
            
            while (j < arr2.Length)
            {
                arr[o] = arr2[j];
                j += 1;
                o += 1;
            }
            
            return arr;
        }
        
        if (arr.Length < 2)
        {
            return arr;
        }
        else
        {
            var (arr1, arr2) = Split(arr);
            var arr1Sorted = Niave(arr1);
            var arr2Sorted = Niave(arr2);
            return Merge(arr1Sorted, arr2Sorted);
        }
    }

    // Use Spans To Proxy Into The Source Array Instead Of Creating New Arrays During Split
    public static int[] Spanified(int[] arr)
    {
        static void Merge(Span<int> arr, int split)
        {
            int i = 0;
            int j = split;

            while (i < arr.Length && j < arr.Length && i < j)
            {
                var a = arr[i];
                var b = arr[j];

                if (a <= b)
                {
                    i += 1;
                }
                else
                {
                    arr[i] = b;
                    arr[j] = a;
                    j += 1;
                }
            }

            for (; i < arr.Length; i++)
            {
                var a = arr[i];
                var b = arr[arr.Length - 1];

                if (a > b)
                {
                    arr[i] = b;
                    arr[arr.Length - 1] = a;
                }
            }
        }

        static void Spanified(Span<int> arr)
        {
            if (arr.Length > 1)
            {
                var i = arr.Length / 2;

                var left = arr.Slice(0, i);
                var right = arr.Slice(i);

                Spanified(left);
                Spanified(right);

                Merge(arr, i);
            }
        }
        
        Spanified(arr.AsSpan());
        
        return arr;
    }

    // Similar To Spanified But Without Spans
    public static int[] DeSpanified(int[] arr)
    {
        static void Recurse(int[] arr, int iSpanLeft, int iSpanRight)
        {
            // Split
            
            var iMid = (iSpanRight - iSpanLeft) / 2 + iSpanLeft;
            
            if (iMid - iSpanLeft > 1)
                Recurse(arr, iSpanLeft, iMid);
            
            if (iSpanRight - iMid > 1)
                Recurse(arr, iMid, iSpanRight);

            // Sort/Merge

            int i = iSpanLeft;
            int j = iMid;

            while (i < iSpanRight && j < iSpanRight && i < j)
            {
                var a = arr[i];
                var b = arr[j];

                if (a <= b)
                {
                    i += 1;
                }
                else
                {
                    arr[i] = b;
                    arr[j] = a;
                    j += 1;
                }
            }

            for (; i < iSpanRight; i++)
            {
                var a = arr[i];
                var b = arr[arr.Length - 1];

                if (a > b)
                {
                    arr[i] = b;
                    arr[arr.Length - 1] = a;
                }
            }
        }
        
        Recurse(arr, 0, arr.Length);
        
        return arr;
    }

    public static int[] BuiltIn(int[] arr)
    {
        Array.Sort(arr);
        return arr;
    }

    public static void Main()
    {
        const int iterations = 1000;
        const int array_length = 10_000;
        var known = Enumerable.Range(0, array_length).Select((_, i) => i); 


        // Implementations
        var sorters = new (Func<int[], int[]>, string)[]
        { 
            (Niave, nameof(Niave)),
            (Spanified, nameof(Spanified)),
            (DeSpanified, nameof(DeSpanified)),
            (BuiltIn, nameof(BuiltIn))
        };


        // Cases
        var a = Enumerable.Range(0, array_length).ToArray();
        var b = Enumerable.Range(0, array_length).ToArray();
        var c = Enumerable.Range(0, array_length).ToArray();


        // Check That Implementations Are Correct
        foreach (var (sorter, name) in sorters)
        foreach (var arr in new[] { a, b, c })
        {
            var sorted = sorter(arr);

            foreach (var (k, s) in known.Zip(sorted))
                if (k != s)
                    throw new Exception($"Invalid implementation for {name}");
        }


        // Speed Test
        foreach (var (sorter, name) in sorters)
        {
            var sw = Stopwatch.StartNew();

            for (int i = 0; i < iterations; i++)
            {
                Prep(a, b, c);

                sorter(a);
                sorter(b);
                sorter(c);
            }

            sw.Stop();

            Console.WriteLine($"Sorted: {name} | Elapsed Milliseconds For {sw.ElapsedMilliseconds} Iterations: {iterations}");
        }
    }
}