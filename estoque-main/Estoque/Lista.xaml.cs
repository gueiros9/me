using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using Xamarin.Forms;
using Xamarin.Forms.Xaml;

namespace Estoque
{
    [XamlCompilation(XamlCompilationOptions.Compile)]
    public partial class Lista : ContentPage
    {
        public ObservableCollection<Produto> Produtos { get; set; }
        public Lista()
        {
            InitializeComponent();

            Produtos = new ObservableCollection<Produto>
            {
                new Produto{Name="RedBull",Price=7},
                new Produto{Name="Coca Cola",Price=6},
                new Produto{Name="Eisenbahn",Price=4},
                new Produto{Name="Heineken",Price=5},
            };

            ProdutoListView.ItemsSource = Produtos;
        }

        private void ProdutoListView_ItemTapped(object sender, ItemTappedEventArgs e)
        {
            if(e.Item==null)
            {
                return;
            }
            ((ListView)sender).SelectedItem = null;
            Navigation.PushModalAsync(new ProdutoPage(e.Item as Produto));
            
        }
    }
}