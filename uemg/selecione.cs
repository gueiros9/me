        static void Main(string[] args)
        {
            int I, J, Valor, VAR; int[] lista = new int[5] { 42, 1532, 53503, 290, 5 };
            int bubble = 0, insertion = 0, selection = 0;

            Console.WriteLine("Selecione metódo de ordenação desejado");
            Console.WriteLine("(b) Bubble | (i) Insertion | (s) Selection");

            char Ordenar = char.Parse(Console.ReadLine());
            
            switch (Ordenar)
            {
                case 'b':
                    for (J = 0; J <= lista.Length - 2; J++)
                    {
                        for (I = 0; I <= lista.Length - 2; I++)
                        {
                            if (lista[I + 1] < lista[I])
                            {
                                Valor = lista[I + 1];
                                lista[I + 1] = lista[I];
                                lista[I] = Valor;
                            }
                            bubble++;
                        }
                    }
                    Console.WriteLine("O numero de ordenações foram {0}", bubble);
                    Console.ReadKey();
                    break;

                case 'i':
                    for (I = 1; I < 5; ++I)
                    {
                        Valor = lista[I];
                        J = I - 1;
                        while (J >= 0 && lista[J] > Valor)
                        {
                            lista[J + 1] = lista[J];
                            J = J - 1;
                        }           
                        insertion++;
                        lista[J + 1] = Valor;
                    }
                    Console.WriteLine("O numero de ordenações foram {0}", insertion);
                    Console.ReadKey();  
                    break;

                case 's':
                    for (I = 0; I < 5; ++I)
                    {
                        Valor = I;
                        for (J = I + 1; J < 5; J++)
                        {
                            if (lista[J] < lista[Valor])
                            {
                                Valor = J;
                            }
                            selection++;
                            VAR = lista[Valor];
                            lista[Valor] = lista[I];
                            lista[I] = VAR;
                        }
                    }
                    Console.WriteLine("O numero de ordenações foram {0}", selection);
                    Console.ReadKey();
                    break;
            }
            Console.ReadKey();
        }
    }
}
