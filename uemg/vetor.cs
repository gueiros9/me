        static void Main(string[] args)
        {
            /* Criar um vetor do tipo inteiro de 50 posições e atribuir para cada posição, 
             * o valor da posição anterios + 2. A primeira posição do vetor deverá ser 2 e a última 100.*/
            
            int[] Vetor = new int[50]; int Valor = 0;
            for(int I = 0; I < 50; I++)
            {
                Vetor[I] = Valor + 2;
                Valor = Valor + 2;

                // Criar um laço que apresente na tela cada posição do vetor criado anteriormente.
                Console.WriteLine("a posição do Vetor é {0}", I);
            }
	}

        static void Main(string[] args)
        {
            /* Criar uma matriz de duas dimensões do tipo string e preenchê-la automaticamente.*/

            string[,] Matriz = new string[2,3];
            for(int I = 0; I < 2; I++)
            {
                for(int J = 0; J < 3; J++)
                {
                    Console.WriteLine("[{0},{1}]",I,J);
                }
            }
            Console.ReadKey();
        }