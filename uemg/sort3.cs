using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp4
{
    class Program
    {
        static void Main(string[] args)
        {
            int I, J, Valor, VAR; int[] lista = new int[5] {42, 1532, 53503, 290, 5};

            for (I = 0; I < 5; ++I)
            {
                Valor = I;

                for (J = I + 1; J < 5; J++)
                {
                    if (lista[J] < lista[Valor])
                    {
                        Valor = J;
                    }

                    VAR = lista[Valor];
                    lista[Valor] = lista[I];
                    lista[I] = VAR;
                }
            }
        }
    }
}