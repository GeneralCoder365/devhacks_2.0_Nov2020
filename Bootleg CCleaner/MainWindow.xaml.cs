using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Threading;
using System.Diagnostics;

namespace Bootleg_CCleaner
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            //ProcessStartInfo start = new ProcessStartInfo();
            //start.FileName = "";
            //start.Arguments = args;
            //start.UseShellExecute = true;
            //start.RedirectStandardOutput = true;
            //using (Process process = Process.Start(start))
            //{
            //    using (StreamReader reader = process.StandardOutput)
            //    {
            //        string result = reader.ReadToEnd();
            //        Console.Write(result);
            //    }
            //}
        }

        private void Close_Button_Click(object sender, RoutedEventArgs e)
        {
            this.Close();
        }

        private void Maximize_Button_Click(object sender, RoutedEventArgs e)
        {
            WindowState = WindowState.Maximized;
        }

        private void Minimize_Button_Click(object sender, RoutedEventArgs e)
        {
            WindowState = WindowState.Minimized;
        }

        private void Main_Grid_MouseDown(object sender, MouseButtonEventArgs e)
        {
            if (e.ChangedButton == MouseButton.Left) this.DragMove();
        }

        private void Presets_TextBlock_MouseDown(object sender, MouseButtonEventArgs e)
        {

        }

        private void Paths_TextBlock_MouseDown(object sender, MouseButtonEventArgs e)
        {

        }

        private void Cleanup_TextBlock_MouseDown(object sender, MouseButtonEventArgs e)
        {

        }
    }
}
