static void Main(string[] args)
            {
                // Declaração de Variáveis e do Vetor "lista" 
                int valor, I, J; int[] lista = new int[8] { 42, 1532, 53503, 290, 5, 2, 11, 60 };

                // Primeiro laço de repetição, para passar por todo o vetor
                for (J = 0; J <= lista.Length - 2; J++)
                {
                    // Segundo laço de repetição, para realizar comparações
                    for (I = 0; I <= lista.Length - 2; I++)
                    {

                        // "lista[I + 1] é o proximo valor referente ao I, se o proximo for menor que o I (número atual), será realizada a troca entre os dois
                        if (lista[I + 1] < lista[I])
                        {
                            // valor = variável auxiliar, copia o valor do proximo
                            valor = lista[I + 1];
                            // O proximo se torna o atual
                            lista[I + 1] = lista[I];
                            // O "atual" copia o valor contido na variável auxiliar
                            lista[I] = valor;
                        }
                        // Caso a condição seja falsa, não ocorrera troca, pois o valor atual é menor que o proximo, assim retornando para o laço anterior, que irá passar para o proximo número do vetor
                    }
                }
            }