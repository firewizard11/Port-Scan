import unittest
import port_scan


class TestHostValidation(unittest.TestCase):

    def test_valid_hosts(self):
        valid_hosts = ['192.168.0.1', '127.0.0.1', '10.0.0.2', '172.16.254.1', '8.8.8.8', '255.255.255.255', '0.0.0.0']

        for host in valid_hosts:
            self.assertTrue(port_scan.validate_host(host), f'Valid Host: {host}')

    def test_invalid_hosts(self):
        invalid_hosts = ["256.256.256.256", "192.168.0.999", "192.168.1.", "192.168..1", "192.168.1.1.1", "192.168.1.-1", "192.168.01.1", "abc.def.ghi.jkl", "192.168.1.1/24" ]

        for host in invalid_hosts:
            self.assertFalse(port_scan.validate_host(host), f'Invalid Host: {host}')


class TestPortValidation(unittest.TestCase):

    def test_valid_ports(self):
        for port in range(1, 65535 + 1):
            self.assertTrue(port_scan.validate_port(port), f'Valid Port: {port}')

    def test_invalid_ports(self):
        self.assertFalse(port_scan.validate_port(-1), 'Invalid Port: -1')
        self.assertFalse(port_scan.validate_port(0), 'Invalid Port: 0')

        self.assertFalse(port_scan.validate_port(65536), 'Invalid Port: 65536')
        self.assertFalse(port_scan.validate_port(70000), 'Invalid Port: 70000')


class TestFormatPorts(unittest.TestCase):

    def test_valid_single_port(self):
        self.assertEqual(port_scan.format_ports('40'), [40])
        self.assertEqual(port_scan.format_ports('40000'), [40000])
        self.assertEqual(port_scan.format_ports('1'), [1])
        self.assertEqual(port_scan.format_ports('65535'), [65535])

    def test_invalid_single_port(self):
        invalid_inputs = ['0', '-1', '65536', 'abc']

        for input in invalid_inputs:
            with self.assertRaises(ValueError, msg=f'Input: {input}'):
                port_scan.format_ports(input)

    def test_valid_range_of_ports(self):
        valid_inputs = ["40-2000", "1-65535", "1000-2000"]

        for input in valid_inputs:
            start = int(input.split('-')[0])
            stop = int(input.split('-')[1]) + 1

            self.assertEqual(port_scan.format_ports(input), list(range(start, stop)))

    def test_invalid_range_of_ports(self):
        invalid_inputs = ["40-200000", "2000-40", "1--2000", "abc-2000", "40-def"]

        for input in invalid_inputs:
            with self.assertRaises(ValueError, msg=f'Input: {input}'):
                port_scan.format_ports(input)

    def test_valid_list_of_ports(self):
        self.assertEqual(port_scan.format_ports("21,22,80,139,443,445"), [21,22,80,139,443,445])
        self.assertEqual(port_scan.format_ports("1,2,3,4,5"), [1,2,3,4,5])
        self.assertEqual(port_scan.format_ports("1024,2048,4096"), [1024,2048,4096])

    def test_invalid_list_of_ports(self):
        invalid_inputs = ["21,22,abc,80", "65536,22,80", "21,22,,80", "21;22;80"]

        for input in invalid_inputs:
            with self.assertRaises(ValueError, msg=f'Input: {input}'):
                port_scan.format_ports(input)


if __name__ == '__main__':
    unittest.main(verbosity=2)