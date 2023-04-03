	static void Main(string[] args)
        {
            // Valor VAR auxiliar
            int I, J, Valor; int[] lista = new int[5] {42, 1532, 53503, 290, 5};
            for (I = 1; I < 5; ++I)
            {
                // Auxiliar copia valor a ser comparado
                Valor = lista[I];

                // J será igual o indice anterior
                J = I - 1;

                // Compara o valor anterior (J), com a variavel auxiliar
                while (J >= 0 && lista[J] > Valor)
                {
                    lista[J + 1] = lista[J];
                    J = J - 1;
                }

                // Auxiliar copia o proximo valor referente ao J
                lista[J + 1] = Valor;
                Console.ReadKey();
            }