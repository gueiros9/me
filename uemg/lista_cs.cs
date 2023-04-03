static void Main(string[] args)
        {
            /* Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B. 
             * A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo 
             * com que o valor que está em A passe para B e vice-versa. 
             * Ao final, escrever os valores que ficaram armazenados nas variáveis.*/
            
            int ValorA = 10; int ValorB = 20; int VarAux = 0;
            Console.WriteLine("O valor de A é {0}, e o valor de B é {1}", ValorA, ValorB);

            VarAux = ValorA;
            ValorA = ValorB;
            ValorB = VarAux;

            Console.WriteLine("O valor de A será {0} e o valor de B é {1}", ValorA, ValorB);
            Console.ReadKey();
	}

static void Main(string[] args)
        {
            /* Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), 
             * calcular e escrever a área do retângulo.*/

	    Console.WriteLine ("Informe a Altura do retangulo");
            float Altura = float.Parse(Console.ReadLine());

	    Console.WriteLine ("Informe a Base do retangulo");
            float Base = float.Parse (Console.ReadLine());

            float Area = (Base * Altura) / 2;
 
            Console.ReadKey();
       }

static void Main(string[] args)
	{
            /* Escreva um algoritmo para ler o salário mensal atual de um funcionário
             * e o percentual de reajuste. Calcular e escrever o valor do novo salário. */

            Console.WriteLine("Informe o salario");
            float Salario = float.Parse(Console.ReadLine());

            Console.WriteLine("Informe o Reajuste");
            float Reajuste = float.Parse(Console.ReadLine());

            float SalNovo = Salario + (Salario * (Reajuste / 100));
            Console.WriteLine("O novo salario sera de {0}", SalNovo);
 
            Console.ReadKey();
       }

static void Main(string[] args)
        {
            /* Uma revendedora de carros usados paga a seus funcionários vendedores 
             * um salário fixo por mês, mais uma comissão também fixa para cada
             * carro vendido e mais 5% do valor das vendas por ele efetuadas. 
             * Escrever um algoritmo que leia o número de carros por ele vendidos, 
             * o valor total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. 
             * Calcule e escreva o salário final do vendedor. */

            Console.WriteLine("Informe o numero de carros vendidos");
            float CarrosVend = float.Parse(Console.ReadLine());

            Console.WriteLine("Informe o total de vendas");
            float TotalVend = float.Parse(Console.ReadLine());

            Console.WriteLine("Informe o salario fixo");
            float SalarioFix = float.Parse(Console.ReadLine());

            Console.WriteLine("Informe o valor por carro vendido");
            float ValCar = float.Parse(Console.ReadLine());

            TotalVend = (float)(TotalVend * 0.05);
            float SalarioFinal = SalarioFix + (CarrosVend * ValCar) + (TotalVend);

            Console.ReadKey();
        }

static void Main(string[] args)
        {
            /* Ler um valor e escrever se é positivo, negativo ou zero.*/

            Console.WriteLine("Informe um valor");
            float Valor = float.Parse(Console.ReadLine());

            if (Valor > 0)
            {
                Console.WriteLine("O valor e possitivo");
            }
            else if (Valor < 0)
            {
                Console.WriteLine("O valor é negativo");
            }
            else
            {
                Console.WriteLine("O valor é igual a zero");
            }
            Console.ReadKey();
        }

static void Main(string[] args)
        {
            /* Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos maiores. */

            float Valor = 0;

            Console.WriteLine("Informe um valor");
            float Valor1 = float.Parse(Console.ReadLine());

            Console.WriteLine("Informe um valor");
            float Valor2 = float.Parse(Console.ReadLine());

            Console.WriteLine("Informe um valor");
            float Valor3 = float.Parse(Console.ReadLine());

            if ((Valor1 > Valor2) && (Valor2 > Valor3))
            {
                 Valor = Valor1 + Valor2;
            }

            if ((Valor1 > Valor2) && (Valor2 < Valor3))
            {
                 Valor = Valor1 + Valor2;
            }

            if ((Valor3 < Valor2) && (Valor2 > Valor1))
            {
                 Valor = Valor2 + Valor1;
            }

            if ((Valor1 < Valor2) && (Valor2 > Valor3))
            {
                 Valor = Valor2 + Valor3;
            }

            if ((Valor2 < Valor3) && (Valor1 < Valor3))
            {
                 Valor = Valor3 + Valor1;
            }

            if ((Valor1 < Valor2) && (Valor2 < Valor3))
            {
                 Valor = Valor3 + Valor2;
            }
            Console.WriteLine("O resultado é {0}", Valor);
            Console.ReadKey();
        }

static void Main(string[] args)
        {
            /*  Escreva um algoritmo para imprimir os números de 1 (inclusive)
             *  a 10 (inclusive) em ordem crescente por meio de um laço de repetição.*/

            foreach (int I in Enumerable.Range(1, 10))
            {
                Console.Write(I + 1);
            }
        }

static void Main(string[] args)
        {
            /*  Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] 
             *  (incluindo os valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo.*/

            float Valor; int A = 0; ; int B = 0;
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine("Informe um valor");
                Valor = float.Parse(Console.ReadLine());

                if ((Valor >= 10) && (Valor <= 20))
                {
                    A = A + 1;
                }
                else
                {
                    B = B + 1;
                }
            }
            Console.WriteLine("{0} estão dentro do intervalo, e {1} estão fora do intervalo", A, B);
            Console.ReadKey();
        }