using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BTree
{
    class Program
    {
        static void Main(string[] args)
        {
            // Criar uma Árvore
            Arvore tree = new Arvore();
            // Criar Nó
            Node root = new Node();

            // Inserir elementos a Árvore
            tree.Inserir(31);
            tree.Inserir(21);
            tree.Inserir(90);
            tree.Inserir(12);
            tree.Inserir(42);
            tree.Exibir();
        }
    }
    // Classe Nó
    public class Node
    {
        public int Valor { get; set; }
        // Direcionar valor para esquerda
        public Node Esquerda { get; set; }
        // Direcionar valor para direita
        public Node Direita { get; set; }

        public Node()
        {
        }

        public Node(int valor)
        {
            this.Valor = valor;
        }
    }

    public class Arvore
    {
        private Node raiz;

        public Arvore()
        {
            raiz = null;
        }
        // Função para adicionar números
        public void Inserir(int valor)
        {
            // Caso a árvore esteja vazia, o primeiro numero será considerado como raiz
            if (raiz == null)
            {
                raiz = new Node(valor);
                return;
            }
            // se não estiver, utilizará do "Insert" para direcionar os elementos
            Insert(raiz, new Node(valor));
        }

        private void Insert(Node root, Node newNode)
        {
            // Criar novo nó caso estiver vaizo
            if (root == null)
                root = newNode;

            // Se o novo elemento for menor que o presente no nó, será adicionado para esquerda
            if (newNode.Valor < root.Valor)
            {
                if (root.Esquerda == null)
                    root.Esquerda = newNode;
                else
                    Insert(root.Esquerda, newNode);
            }
            // Se maior, será adicionado para direita
            else
            {
                if (root.Direita == null)
                    root.Direita = newNode;
                else
                    Insert(root.Direita, newNode);
            }
        }

        private void Exibir(Node root)
        {
            if (root == null) return;
            Exibir(root.Esquerda);
            System.Console.Write(root.Valor + " ");
            Exibir(root.Direita);
        }

        public void Exibir()
        {
            Exibir(raiz);
        }
    }
}