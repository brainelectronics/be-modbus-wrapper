#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Unittest for Modbus Wrapper package"""

from be_helpers import ModuleHelper
import logging
import unittest
import sys

# custom imports
from be_modbus_wrapper import ModbusWrapper


class TestModbusWrapper(unittest.TestCase):
    """This class describes a ModbusWrapper unittest."""

    def setUp(self) -> None:
        """Run before every test method"""
        # define a format
        custom_format = "[%(asctime)s][%(levelname)-8s][%(filename)-20s @" \
                        " %(funcName)-15s:%(lineno)4s] %(message)s"

        # set basic config and level for all loggers
        logging.basicConfig(level=logging.INFO,
                            format=custom_format,
                            stream=sys.stdout)

        # create a logger for this TestSuite
        self.test_logger = logging.getLogger(__name__)

        # set the test logger level
        self.test_logger.setLevel(logging.DEBUG)

        # enable/disable the log output of the device logger for the tests
        # if enabled log data inside this test will be printed
        self.test_logger.disabled = False

    def test_init(self) -> None:
        """Test initalisation of ModuleHelper"""
        logger_name = "Test Logger"
        logger_with_name = ModuleHelper.create_logger(logger_name=logger_name)

        with self.assertLogs(logger_name, level="DEBUG") as logger:
            obj = ModbusWrapper(logger=logger_with_name)
            self.assertIsInstance(obj, ModbusWrapper)

        self.assertEqual(len(logger.output), 1)
        self.assertIn('ModbusWrapper init finished', logger.output[0])

    @unittest.skip("Not yet implemented")
    def test_load_modbus_registers_file(self) -> None:
        """Test initalisation of ModuleHelper"""
        pass

    @unittest.skip("Not yet implemented")
    def test_restore_human_readable_content(self) -> None:
        """Test restoring received data to human readable content"""
        pass

    @unittest.skip("Not yet implemented")
    def test_setup_connection(self) -> None:
        """Test setting up connection to Modbus device"""
        pass

    @unittest.skip("Not yet implemented")
    def test_connection(self) -> None:
        """Test connection property"""
        pass

    @unittest.skip("Not yet implemented")
    def test_connect(self) -> None:
        """Test connect property"""
        pass

    @unittest.skip("Not yet implemented")
    def test_disconnect(self) -> None:
        """Test disconnecting from Device"""
        pass

    @unittest.skip("Not yet implemented")
    def test_client(self) -> None:
        """Test client property"""
        pass

    @unittest.skip("Not yet implemented")
    def test_unit(self) -> None:
        """Test unit property"""
        pass

    @unittest.skip("Not yet implemented")
    def test_read_all_registers(self) -> None:
        """Test reading all Modbus registers"""
        pass

    @unittest.skip("Not yet implemented")
    def test_read_content(self) -> None:
        """Test read_content property"""
        pass

    @unittest.skip("Not yet implemented")
    def test_write_all_registers(self) -> None:
        """Test writing all Modbus registers"""
        pass

    @unittest.skip("Not yet implemented")
    def test_read_coil_registers(self) -> None:
        """Test reading all coil registers"""
        pass

    @unittest.skip("Not yet implemented")
    def test_write_coil_registers(self) -> None:
        """Test writing all coil registers"""
        pass

    @unittest.skip("Not yet implemented")
    def test_read_hregs_registers(self) -> None:
        """Test reading all holding registers"""
        pass

    @unittest.skip("Not yet implemented")
    def test_write_hregs_registers(self) -> None:
        """Test writing all holding registers"""
        pass

    @unittest.skip("Not yet implemented")
    def test_read_ists_registers(self) -> None:
        """Test reading all discrete input registers"""
        pass

    @unittest.skip("Not yet implemented")
    def test_read_iregs_registers(self) -> None:
        """Test reading all input registers"""
        pass

    def tearDown(self) -> None:
        """Run after every test method"""
        pass


if __name__ == '__main__':
    unittest.main()
