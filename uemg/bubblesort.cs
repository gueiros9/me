namespace ConsoleApp3
{
    class Sort
    {
        static void Main(string[] args)
        {
            int valor, I, J; int[] lista = new int[5] {42, 1532, 53503, 290, 5};

            for (J = 0; J <= lista.Length - 2; J++)
            {
                for (I = 0; I <= lista.Length - 2; I++)
                {
                    if (lista[I + 1] < lista[I])
                    {
                        valor = lista[I + 1];
                        lista[I + 1] = lista[I];
                        lista[I] = valor;
                    }
                }
            }
        }
    }
}