import unittest
import port_scan


class TestHostValidation(unittest.TestCase):

    def test_valid_hosts(self):
        valid_hosts = ['192.168.0.1', '127.0.0.1', '10.0.0.2', '172.16.254.1', '8.8.8.8', '255.255.255.255', '0.0.0.0']

        for host in valid_hosts:
            self.assertTrue(port_scan.validate_host(host))

    def test_invalid_hosts(self):
        invalid_hosts = ["256.256.256.256", "192.168.0.999", "192.168.1.", "192.168..1", "192.168.1.1.1", "192.168.1.-1", "192.168.01.1", "abc.def.ghi.jkl", "192.168.1.1/24" ]

        for host in invalid_hosts:
            self.assertFalse(host)

if __name__ == '__main__':
    unittest.main()