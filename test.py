import unittest

import main
from File import File
from Folder import Folder
from Device import Device
from Interface import Interface
from main import Monitor


class MyTestCase(unittest.TestCase):
    def test_file(self):
        test_filename = "bb.txt"
        test_path = "correct/"
        test_file = File(test_filename)
        test_file.set_lines(test_path)

        test_dab_id = test_file.get_dab_id()
        test_message_type = test_file.get_message_type()
        test_latitude, test_longitude = test_file.get_coordinates()

        self.assertEqual(67, test_dab_id)
        self.assertEqual(4, test_message_type)
        self.assertEqual(52.6525, test_latitude)
        self.assertEqual(4.7448, test_longitude)

    def test_folder(self):
        test_path = "correct/"
        test_folder = Folder(test_path)

        result_path = test_folder.get_path()
        test_folder.set_path("newpath/")
        result_new_path = test_folder.get_path()

        test_filename = "bb.txt"
        test_file = File(test_filename)
        test_folder.files.append(test_file)
        result_files = test_folder.get_list_files()

        self.assertEqual("correct/", result_path)
        self.assertEqual("newpath/", result_new_path)
        self.assertEqual(test_file, result_files[0])

    def test_device(self):
        test_device = Device("AIS Transponder1", "True Heading", "AIS Base Station", 0)
        result_name = test_device.get_name()
        result_branch = test_device.get_branch()
        result_model = test_device.get_model()
        result_interface = test_device.get_interface()

        self.assertEqual("AIS Transponder1", result_name)
        self.assertEqual("True Heading", result_branch)
        self.assertEqual("AIS Base Station", result_model)
        self.assertEqual(0, result_interface)

        test_device.set_name("test_name")
        test_device.set_branch("python_unit")
        test_device.set_model("PU-00")
        test_device.set_interface(1)

        new_result_name = test_device.get_name()
        new_result_branch = test_device.get_branch()
        new_result_model = test_device.get_model()
        new_result_interface = test_device.get_interface()

        self.assertEqual("test_name", new_result_name)
        self.assertEqual("python_unit", new_result_branch)
        self.assertEqual("PU-00", new_result_model)
        self.assertEqual(1, new_result_interface)

    def test_interface(self):
        test_interface = Interface.Interface(0)
        self.assertEqual(0, test_interface.interface_type)
        test_interface.get_rs232_settings()
        with self.assertRaises(AttributeError):
            test_interface.get_ethernet_settings()

    def test_rs232(self):
        test_rs232 = Interface.RS232()
        #test_rs232.init_serial("/dev/ttyUSB0", 115200)
        test_rs232.set_port("/dev/ttyUSB0")
        test_rs232.set_baudrate(38400)
        result_port = test_rs232.get_port()
        result_baudrate = test_rs232.get_baudrate()

        self.assertEqual("/dev/ttyUSB0", result_port)
        self.assertEqual(38400, result_baudrate)

        self.assertEqual(False, test_rs232.close_rs232())

    def test_i2c(self):
        test_i2c = Interface.I2C()
        #test_i2c.init_i2c(4)
        test_i2c.set_address(4)
        self.assertEqual(4, test_i2c.get_address())

    def test_ethernet(self):
        test_ethernet = Interface.Ethernet()
        test_ethernet.init_socket("192.168.0.101", 1234)

        self.assertEqual("192.168.0.101", test_ethernet.get_ip_address())
        self.assertEqual(1234, test_ethernet.get_port())
        test_ethernet.close_socket()


    def test_spi(self):
        test_spi = Interface.SPI()
        #test_spi.init_spi(0, 1)
        test_spi.set_spi_bus(0)
        test_spi.set_spi_device(1)

        self.assertEqual(0, test_spi.get_spi_bus())
        self.assertEqual(1, test_spi.get_spi_device())

    def test_acknowledge(self):
        test_monitor = Monitor("./correct")
        main.attach_devices("devices.csv")
        #test_monitor.acknowledge(67, 1)


if __name__ == '__main__':
    unittest.main()
