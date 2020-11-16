﻿using System;
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
        List<string> presets;
        List<string> paths;

        int currentIndex = 0;
        int days = 10;

        public MainWindow()
        {
            InitializeComponent();
            
            presets = new List<string> {"School", "Work", "Home"};
            paths = new List<string> {"path1", "path2"};

            Presets_MouseDown_Call();
            
            Presets_TextBlock.MouseEnter += BackgroundEnterHandler2;
            Presets_TextBlock.MouseLeave += BackgroundLeaveHandler2;
            
            Paths_TextBlock.MouseEnter += BackgroundEnterHandler2;
            Paths_TextBlock.MouseLeave += BackgroundLeaveHandler2;
            
            Cleanup_TextBlock.MouseEnter += BackgroundEnterHandler2;
            Cleanup_TextBlock.MouseLeave += BackgroundLeaveHandler2;
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
            Presets_MouseDown_Call();
        }

        private void Presets_MouseDown_Call() {
            Headline_Text.Text = "Presets";
            Viewing_Grid.Children.Clear();
            for (int i = 0; i < presets.Count(); i++) {
                TextBlock txtBlock = new TextBlock();
                txtBlock.Text = presets[i];
                txtBlock.Height = 20;
                //txtBlock.Width = 100;
                txtBlock.TextWrapping = TextWrapping.Wrap;
                txtBlock.Background=new SolidColorBrush(Colors.White);
                txtBlock.Margin = new Thickness(10,10 + (20*i),10,0);
                txtBlock.VerticalAlignment = VerticalAlignment.Top;
                txtBlock.HorizontalAlignment = HorizontalAlignment.Left;
                txtBlock.MouseDown += EditPresetHandler;
                txtBlock.MouseEnter += BackgroundEnterHandler;
                txtBlock.MouseLeave += BackgroundLeaveHandler;
                Grid.SetRow(txtBlock, 0);
                Grid.SetColumn(txtBlock, 0);
                Viewing_Grid.Children.Add(txtBlock);
                
                TextBlock startBlock = new TextBlock();
                startBlock.Text = "Start";
                startBlock.Height = 20;
                //startBlock.Width = 100;
                startBlock.TextWrapping = TextWrapping.Wrap;
                startBlock.Background=new SolidColorBrush(Colors.White);
                startBlock.Margin = new Thickness(110,10 + (20*i),10,0);
                startBlock.VerticalAlignment = VerticalAlignment.Top;
                startBlock.HorizontalAlignment = HorizontalAlignment.Right;
                startBlock.MouseDown += StartPresetHandler;
                startBlock.MouseEnter += BackgroundEnterHandler;
                startBlock.MouseLeave += BackgroundLeaveHandler;
                startBlock.Name = presets[i];
                Grid.SetRow(startBlock, 0);
                Grid.SetColumn(startBlock, 0);
                Viewing_Grid.Children.Add(startBlock);
            }
            TextBlock addtext = new TextBlock();
            addtext.Text = "+";
            addtext.Height = 20;
            addtext.Width = 100;
            addtext.TextWrapping = TextWrapping.Wrap;
            addtext.Margin = new Thickness(10,10 + (20*(presets.Count())),10,0);
            addtext.VerticalAlignment = VerticalAlignment.Top;
            addtext.HorizontalAlignment = HorizontalAlignment.Left;
            addtext.MouseDown += AddPresetHandler;
            Grid.SetRow(addtext, 0);
            Grid.SetColumn(addtext, 0);
            Viewing_Grid.Children.Add(addtext);
        }
        
        private void BackgroundEnterHandler(object sender, MouseEventArgs e) {
            ((TextBlock)sender).Background = new SolidColorBrush(Colors.LightGray);
        }

        private void BackgroundLeaveHandler(object sender, MouseEventArgs e) {
            ((TextBlock)sender).Background = new SolidColorBrush(Colors.White);
        }

        private void BackgroundEnterHandler2(object sender, MouseEventArgs e) {
            ((TextBlock)sender).Background = new SolidColorBrush(Colors.DeepSkyBlue);
        }

        private void BackgroundLeaveHandler2(object sender, MouseEventArgs e) {
            ((TextBlock)sender).Background = new SolidColorBrush((Color)ColorConverter.ConvertFromString("#FFA6BAFF"));
        }

        private void Paths_TextBlock_MouseDown(object sender, MouseButtonEventArgs e)
        {
            Headline_Text.Text = "Paths";
            Viewing_Grid.Children.Clear();

        }

        private void Cleanup_TextBlock_MouseDown(object sender, MouseButtonEventArgs e)
        {
            Headline_Text.Text = "Cleanup";
            Viewing_Grid.Children.Clear();
            TextBlock txtBlock = new TextBlock();
            txtBlock.Text = "How many days after a download would you like it to expire?";
            txtBlock.Height = 20;
            txtBlock.TextWrapping = TextWrapping.Wrap;
            txtBlock.Background=new SolidColorBrush(Colors.White);
            txtBlock.Margin = new Thickness(10,10,10,0);
            txtBlock.VerticalAlignment = VerticalAlignment.Top;
            txtBlock.HorizontalAlignment = HorizontalAlignment.Left;
            Grid.SetRow(txtBlock, 0);
            Grid.SetColumn(txtBlock, 0);
            Viewing_Grid.Children.Add(txtBlock);

            TextBox editBox = new TextBox();
            editBox.Text = days.ToString();
            editBox.Height = 20;
            editBox.Width = 250;
            editBox.TextWrapping = TextWrapping.Wrap;
            editBox.Background=new SolidColorBrush(Colors.White);
            editBox.Margin = new Thickness(10,30,10,0);
            editBox.VerticalAlignment = VerticalAlignment.Top;
            editBox.HorizontalAlignment = HorizontalAlignment.Left;
            editBox.TextChanged += CleanupTimeChangedHandler;
            Grid.SetRow(editBox, 0);
            Grid.SetColumn(editBox, 0);
            Viewing_Grid.Children.Add(editBox);
        }

        private void CleanupTimeChangedHandler(object sender, TextChangedEventArgs e) {
            TextBox timeBox = (TextBox)sender;
            int newTime = 0;
            if (Int32.TryParse(timeBox.Text, out newTime)) {
                days = newTime;
            }
        }

        private void AddPresetHandler(object sender, MouseButtonEventArgs e) {
            Headline_Text.Text = "New";
            Viewing_Grid.Children.Clear();
            currentIndex = presets.Count();
            presets.Add("New");
            TextBlock txtBlock = new TextBlock();
            txtBlock.Text = "Edit the list of websites for which you want for this preset.";
            txtBlock.Height = 20;
            txtBlock.TextWrapping = TextWrapping.Wrap;
            txtBlock.Background=new SolidColorBrush(Colors.White);
            txtBlock.Margin = new Thickness(10,10,10,0);
            txtBlock.VerticalAlignment = VerticalAlignment.Top;
            txtBlock.HorizontalAlignment = HorizontalAlignment.Left;
            Grid.SetRow(txtBlock, 0);
            Grid.SetColumn(txtBlock, 0);
            Viewing_Grid.Children.Add(txtBlock);

            TextBox nameBox = new TextBox();
            nameBox.Text = "New";
            nameBox.Height = 20;
            nameBox.Width = 250;
            nameBox.TextWrapping = TextWrapping.Wrap;
            nameBox.Background=new SolidColorBrush(Colors.White);
            nameBox.Margin = new Thickness(10,30,10,0);
            nameBox.VerticalAlignment = VerticalAlignment.Top;
            nameBox.HorizontalAlignment = HorizontalAlignment.Left;
            nameBox.TextChanged += EditPresetName;
            Grid.SetRow(nameBox, 0);
            Grid.SetColumn(nameBox, 0);
            Viewing_Grid.Children.Add(nameBox);

            TextBox editBox = new TextBox();
            editBox.Text = "editBox";
            editBox.Height = 20;
            editBox.Width = 250;
            editBox.TextWrapping = TextWrapping.Wrap;
            editBox.Background=new SolidColorBrush(Colors.White);
            editBox.Margin = new Thickness(10,60,10,0);
            editBox.VerticalAlignment = VerticalAlignment.Top;
            editBox.HorizontalAlignment = HorizontalAlignment.Left;
            Grid.SetRow(editBox, 0);
            Grid.SetColumn(editBox, 0);
            Viewing_Grid.Children.Add(editBox);
        }

        private void EditPresetHandler(object sender, MouseButtonEventArgs e) {
            Headline_Text.Text = ((TextBlock)sender).Text;
            Viewing_Grid.Children.Clear();
            currentIndex = presets.IndexOf(((TextBlock)sender).Text);
            TextBlock txtBlock = new TextBlock();
            txtBlock.Text = "Edit the list of websites for which you want for this preset.";
            txtBlock.Height = 20;
            txtBlock.TextWrapping = TextWrapping.Wrap;
            txtBlock.Background=new SolidColorBrush(Colors.White);
            txtBlock.Margin = new Thickness(10,10,10,0);
            txtBlock.VerticalAlignment = VerticalAlignment.Top;
            txtBlock.HorizontalAlignment = HorizontalAlignment.Left;
            Grid.SetRow(txtBlock, 0);
            Grid.SetColumn(txtBlock, 0);
            Viewing_Grid.Children.Add(txtBlock);

            TextBox nameBox = new TextBox();
            nameBox.Text = ((TextBlock)sender).Text;
            nameBox.Height = 20;
            nameBox.Width = 250;
            nameBox.TextWrapping = TextWrapping.Wrap;
            nameBox.Background=new SolidColorBrush(Colors.White);
            nameBox.Margin = new Thickness(10,30,10,0);
            nameBox.VerticalAlignment = VerticalAlignment.Top;
            nameBox.HorizontalAlignment = HorizontalAlignment.Left;
            nameBox.TextChanged += EditPresetName;
            Grid.SetRow(nameBox, 0);
            Grid.SetColumn(nameBox, 0);
            Viewing_Grid.Children.Add(nameBox);

            TextBox editBox = new TextBox();
            editBox.Text = "editBox";
            editBox.Height = 20;
            editBox.Width = 250;
            editBox.TextWrapping = TextWrapping.Wrap;
            editBox.Background=new SolidColorBrush(Colors.White);
            editBox.Margin = new Thickness(10,60,10,0);
            editBox.VerticalAlignment = VerticalAlignment.Top;
            editBox.HorizontalAlignment = HorizontalAlignment.Left;
            Grid.SetRow(editBox, 0);
            Grid.SetColumn(editBox, 0);
            Viewing_Grid.Children.Add(editBox);

            TextBlock remBlock = new TextBlock();
            remBlock.Text = "Remove";
            remBlock.Height = 20;
            remBlock.TextWrapping = TextWrapping.Wrap;
            remBlock.Background=new SolidColorBrush(Colors.White);
            remBlock.Margin = new Thickness(10,90,10,0);
            remBlock.VerticalAlignment = VerticalAlignment.Top;
            remBlock.HorizontalAlignment = HorizontalAlignment.Left;
            remBlock.MouseDown += RemoveBlock;
            Grid.SetRow(remBlock, 0);
            Grid.SetColumn(remBlock, 0);
            Viewing_Grid.Children.Add(remBlock);
        }

        private void StartPresetHandler(object sender, MouseButtonEventArgs e) {
            currentIndex = presets.IndexOf(((TextBlock)sender).Name);
        }

        private void EditPresetName(object sender, TextChangedEventArgs e) {
            presets[currentIndex] = ((TextBox)sender).Text;
            Headline_Text.Text = ((TextBox)sender).Text;
        }

        private void RemoveBlock(object sender, MouseButtonEventArgs e) {
            presets.RemoveAt(currentIndex);
            Presets_MouseDown_Call();
        }
    }
}
