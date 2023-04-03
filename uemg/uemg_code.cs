using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;

namespace WinFormsApp2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnSalvar_Click(object sender, EventArgs e)
        {
            SqlConnection sqlConexao = new SqlConnection("Data Source=DESKTOP-KQVJL86\\SQLEXPRESS01;Initial Catalog=Pv02;Integrated Security=True");
            SqlCommand cmd = new SqlCommand("INSERT INTO Veiculo(proprietario, placa, marca, categoria, ano_fabric) VALUES('" + txtProp.Text +"','"+ txtPlaca.Text +"','"+ txtMarca.Text + "','"+ cbCategoria.Text +"','"+ txtAnoFab.Text +"')", sqlConexao);

            try
            {
                sqlConexao.Open();
                cmd.ExecuteNonQuery();
                sqlConexao.Close();
                dataGridView1.DataSource = GetData();
                MessageBox.Show("Veículo inserido");
            }
            catch
            {
                MessageBox.Show("Problema durante o cadastro");
            }
        }

        private void btnDel_Click(object sender, EventArgs e)
        {
            {
                SqlConnection sqlConexao = new SqlConnection("Data Source=DESKTOP-KQVJL86\\SQLEXPRESS01;Initial Catalog=Pv02;Integrated Security=True");
                SqlCommand cmd = new SqlCommand("DELETE FROM Veiculo WHERE placa = (@placa)", sqlConexao);
                cmd.Parameters.Add("@placa", SqlDbType.VarChar).Value = txtPlaca.Text;
                try
                {
                    sqlConexao.Open();
                    cmd.ExecuteNonQuery();
                    sqlConexao.Close();
                    dataGridView1.DataSource = GetData();
                    MessageBox.Show("Veículo removido");
                }
                catch
                {
                    MessageBox.Show("Problema durante a remoção");
                }
            }
        }

        private void txtPlaca_TextChanged(object sender, EventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            dataGridView1.DataSource = GetData();
        }
        private DataTable GetData()
        {
            DataTable dtTabela = new DataTable();
            SqlConnection sqlConexao = new SqlConnection("Data Source=DESKTOP-KQVJL86\\SQLEXPRESS01;Initial Catalog=Pv02;Integrated Security=True");
            SqlCommand cmd = new SqlCommand("SELECT * FROM Veiculo", sqlConexao);

            sqlConexao.Open();
            SqlDataReader reader = cmd.ExecuteReader();
            dtTabela.Load(reader);

            return dtTabela;
        }
    }
}