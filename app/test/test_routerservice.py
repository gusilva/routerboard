from app.main.service.routerservice import RouterService
from requests import Session
from unittest.mock import patch
import unittest


class TestRouterService(unittest.TestCase):
    """docstring for TestRouterService"""

    def setUp(self):
        self.service = RouterService("10.100.176.50", 8080)
        self.assertIsInstance(self.service.session, Session)
        self.assertEqual(self.service.url, "http://10.100.176.50:8080")
        self.assertEqual(self.service.auth, "luci_username=root&luci_password=admin")

    def test_get_stock_number_has_sucessful(self):
        code = self.service.getStock()
        self.assertEqual(code, 302)
        self.assertEqual(len(self.service.stock), 52)
        self.assertEqual(self.service.stock[:20], "/cgi-bin/luci/;stok=")

    def test_get_stock_number_connection_failed(self):
        self.service.url = "http://10.100.176.100:8080"
        code = self.service.getStock()
        self.assertEqual(code, 500)
        self.assertEqual(self.service.stock, "Connection Failed")

    def test_get_stock_number_authentication_failed(self):
        self.service.auth = "luci_username=root&luci_password=pass"
        code = self.service.getStock()
        self.assertEqual(code, 403)
        self.assertEqual(self.service.stock, "No Number")

    def test_get_signal_quality(self):
        self.service.getStock()
        code, quality = self.service.getSignalQuality()
        self.assertEqual(code, 200)
        self.assertEqual(len(quality), 2)

    # @patch('app.main.controller.routercontroller.requests.session.post')
    # def test_post(self, mock_hit):
    #     mock_hit.return_value = 200, "/cgi-bin/luci/;stok=91akd9932w39322"
    #     code, resp = self.controller.hit(url="http://10.100.176.30:8080/cgi-bin/luci")
