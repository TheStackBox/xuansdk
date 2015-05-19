##############################################################################################
# Copyright 2014-2015 Cloud Media Sdn. Bhd.
#
# This file is part of Xuan Application Development SDK.
#
# Xuan Application Development SDK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Xuan Application Development SDK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Xuan Application Development SDK.  If not, see <http://www.gnu.org/licenses/>.
##############################################################################################

from com.cloudMedia.theKuroBox.sdk.app.appinfo import AppInfo
from com.cloudMedia.theKuroBox.sdk.app.sharedMethod import SharedMethod

class SybSerialService():
    '''
    Opto (GPIO)
    '''

    @staticmethod
    def opto_gpio_write(pin, value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Opto GPIO Read.
        pin:Number - 
        value:String - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def opto_gpio_read(pin, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Opto GPIO Read.
        pin:Number - 
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def rs232_open(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        RS232 Open.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def rs232_list_baud_rate(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        RS232 List Baud Rate.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def rs232_set_baud_rate(baud, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        RS232 Set Baud Rate.
        baud:Number - baud rate
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def rs232_get_baud_rate(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        RS232 Get Baud Rate.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def rs232_write(data, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        RS232 Write.
        data:String - data to write
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def rs232_write_hex(data, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        RS232 Write Hex.
        data:String - hex data to write
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def rs232_read(length, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        RS232 Read.
        length:Number - 
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def rs232_read_hex(length, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        RS232 Read Hex.
        length:Number - 
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def rs232_flush(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        RS232 Flush.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def rs232_close(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        RS232 Close.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_set_mode(mode, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus Set Mode.
        mode:String -
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_get_mode(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus Get Mode.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_gpio_write(pin, value, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus GPIO Write.
        pin:Number - 
        value:String -
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_gpio_read(pin, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus GPIO Read.
        pin:Number - 
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_list_speed(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C List Speed.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_open(address, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C Open.
        address:String - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_set_attr(speed, delay, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C Set Attr.
        speed:Number - 
        delay:Number - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_get_attr(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C Get Attr.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_set_speed(speed, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C Set Speed.
        speed:Number - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_set_delay(delay, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C Set Delay.
        delay:Number - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_write(data, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C Write.
        data:String - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_write_hex(data, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C Write Hex.
        data:String - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_read(length, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C Read.
        length:Number - 
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_read_hex(length, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C Read Hex.
        length:Number - 
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_i2c_close(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus I2C List Speed.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_spi_set_attr(ssActive, speed, mode, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus SPI Set Attr.
        ssActive:String - 
        speed:Number - 
        mode:String - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_spi_get_attr(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus SPI Get Attr.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_spi_open(cs, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus SPI Open.
        cs:String - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_spi_write(data, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus SPI Write.
        data:String - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_spi_write_hex(data, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus SPI Write Hex.
        data:String - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_spi_read(address, length, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus SPI Read.
        address:String - 
        length:Number - 
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_spi_read_hex(address, length, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus SPI .
        address:String -
        length:Number - 
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_spi_close(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus SPI Close.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_uart_open(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus UART Open.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_uart_list_baud_rate(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus UART List Baud Rate.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_uart_set_baud_rate(baud, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus UART Set Baud Rate.
        baud:Number - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_uart_get_baud_rate(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus UART Get Baud Rate.
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_uart_write(data, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus UART Write.
        data:String - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_uart_write_hex(data, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus UART Write Hex.
        data:String - 
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_uart_read(length, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus UART Read.
        length:Number - 
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_uart_read_hex(length, language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus UART Read Hex.
        length:Number - 
        return:Dictionary :eg- {}
        '''
        pass

    @staticmethod
    def pi_bus_uart_flush(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus UART Flush.
        return:Dictionary :eg- {"success":true}
        '''
        pass

    @staticmethod
    def pi_bus_uart_close(language=AppInfo.DEFAULT_API_LANGUAGE):
        '''
        Pi Bus UART Close.
        return:Dictionary :eg- {"success":true}
        '''
        pass

