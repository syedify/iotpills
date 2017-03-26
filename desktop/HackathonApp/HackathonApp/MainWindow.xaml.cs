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
using System.IO;
using System.IO.Ports;
using Newtonsoft.Json;


namespace HackathonApp
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        SerialPort MyPort = new SerialPort();

        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                if (!MyPort.IsOpen)
                MyPort.PortName = "COM7";
                MyPort.BaudRate = 9600;
                MyPort.DtrEnable = true;
                MyPort.RtsEnable = true;
                MyPort.Open();
                
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error opening my port: {0}", ex.Message);
            }
            Console.WriteLine(MyPort.IsOpen);
            try
            {
                string patient_name = textbox1.Text;
                string doctor_name = textbox2.Text;
                string quantity = textbox3.Text;
                string refills = textbox4.Text;
                string supply = textbox5.Text;
                Random rnd = new Random();
                Random rnd2 = new Random();


                Patient patient = new Patient
                {
                    id = rnd.Next(52) ,
                    name = patient_name,
                    timestamp = new DateTime(2017, 03, 26)
                };


                Doctor doctor = new Doctor
                {
                    id = rnd2.Next(52),
                    name = doctor_name,
                    timestamp = new DateTime(2017, 03, 26),
                    doctor_refills = refills,
                    doctor_quantity = quantity,
                    doctor_daysupply = supply
                };



                string json = JsonConvert.SerializeObject(patient);
                string json2 =JsonConvert.SerializeObject(doctor);
                string patient_string = "\"patient\":";
                string doctor_string = "\"doctor :\":";
                string json3 = "{" + patient_string + json +"," + doctor_string + json2 + "}";

                //MyPort.WriteLine(patient_name +"|"+ doctor_name + "|" + refills + "|" + quantity + "|"+ supply);
                Console.WriteLine(json3);
                MyPort.Write(json3);
            }
            catch (Exception ex)
            {
                Console.WriteLine("Error writing:", ex.Message);
            }

            //MyPort.Close();

            Console.WriteLine(MyPort.IsOpen);


        }

        internal class Patient
        {
            public int id { get; set; }
            public string name { get; set; }
            public DateTime timestamp { get; set; }
           
        }

        internal class Doctor
        {
            public int id { get; set; }
            public string name { get; set; }
            public DateTime timestamp { get; set; }
            public string doctor_refills { get; set; }
            public string doctor_quantity { get; set; }
            public string doctor_daysupply { get; set; }


        }

    }
}
