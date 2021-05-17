from xmlrpc.client import ServerProxy
from os import environ
from datetime import date

from tests.data import test_data

import random
import pytest


class TestApiModels:
    """
    Test api models for Yuju's interface
    """

    def test_authentication(self, common: ServerProxy):
        user = environ.get("ODOO_USER")
        db = environ.get("ODOO_DB")
        pwd = environ.get("ODOO_PWD")
        uid = common.authenticate(db, user, pwd, {})
        
        assert uid is not False

    def test_product_count(self, execute_kw: callable):
        """
        Test product_count method is executed successfully
        """
        count = execute_kw('product.product', 'product_count')
        assert isinstance(count, dict)
        assert count.get('success')

    def test_create_product(self, execute_kw: callable):
        """
        Test create product
        """
        response = execute_kw('product.template', 'mdk_create', [],
                              {'product_data': test_data.product})
        assert isinstance(response, dict)
        assert response.get('success')

    def test_create_product_with_variations(self, execute_kw: callable):
        """
        Test create product with variations
        """
        response = execute_kw('product.template', 'mdk_create', [],
                              {'product_data': test_data.product_with_variations})
        assert isinstance(response, dict)
        assert response.get('success')

    def test_activate_deactivate_product(self, execute_kw: callable):
        """
        Test activations and deactivation of product
        """
        # Create product for testing
        data = execute_kw('product.template', 'mdk_create', [],
                               {'product_data': test_data.product})
        assert data.get('success')

        test_product = data.get('data')

        deactivate_response = execute_kw('product.template', 'deactivate_product',
                                         [], {'template_id': test_product.get('template_id')})
        # check new product is successfully deactivated
        assert deactivate_response.get('success')
        assert not deactivate_response.get('data').get('active')

        activate_response = execute_kw('product.template', 'activate_product',
                                       [], {'template_id': test_product.get('template_id')})
        # check new product is successfully deactivated
        assert activate_response.get('success')
        assert activate_response.get('data').get('active')

    def test_get_product(self, execute_kw: callable):
        """
        Test get product
        """
        # Create product for testing
        data = execute_kw('product.template', 'mdk_create', [],
                          {'product_data': test_data.product})
        assert data.get('success')

        test_product = data.get('data')

        response = execute_kw('product.product', 'get_product', [],
                              {'product_id': test_product.get('id')})
        # check new product is successfully deactivated
        assert response.get('success')
        assert response.get('data').get('id') == test_product.get('id')

    def test_update_product(self, execute_kw: callable):
        """
        Test product update success 
        """
        # Create product for testing
        data = execute_kw('product.template', 'mdk_create', [],
                          {'product_data': test_data.product})
        assert data.get('success')

        test_product = data.get('data')
        test_update_data = test_data.product_update_fields
        test_update_data['id_product_madkting'] = str(random.randint(10000, 20000))
        test_update_data['default_code'] = str(random.randint(100, 1000))
        test_update_data['id'] = test_product.get('id')

        response = execute_kw('product.product', 'update_product', [],
                              {'product_data': test_update_data,
                              'product_type': 'product'})
        assert response.get('success')

        updated_data = execute_kw('product.product', 'get_product', [],
                                 {'product_id': test_product.get('id')})
        
        assert updated_data.get('success')
        #  validate each field was updated
        for field, upd_data in test_update_data.items():
            assert updated_data.get('data').get('variations')[0].get(field) == upd_data

    def test_update_variation(self, execute_kw: callable):
        """
        Test update variation
        """
        response = execute_kw('product.template', 'mdk_create', [],
                              {'product_data': test_data.product_with_variations})
        assert isinstance(response, dict)
        assert response.get('success')
        
        idx = random.randint(0, len(response.get('data').get('variations')) -1 )
        test_variation = response.get('data').get('variations')[idx]
        test_update_data = test_data.variation_update_fields
        test_update_data['id'] = test_variation.get('id')

        response = execute_kw('product.product', 'update_product', [],
                              {'product_data': test_update_data,
                               'product_type': 'variation'})
        assert response.get('success')

        updated_variation = execute_kw('product.product', 'get_variation', [],
                                      {'product_id': test_variation.get('id')})

        assert updated_variation.get('success')
        for field, upd_data in test_update_data.items():
            if field == 'standard_price':
                assert updated_variation.get('data').get(field) == pytest.approx(upd_data)
            else:
                assert updated_variation.get('data').get(field) == upd_data

    def test_create_product_with_image(self, execute_kw: callable):
        """
        Test create product
        """
        product_data = test_data.product.copy()
        product_data['image'] = test_data.image_base_64
        response = execute_kw('product.template', 'mdk_create', [],
                              {'product_data': product_data})
        assert isinstance(response, dict)
        assert response.get('success')

    def test_create_product_with_variations_with_image(self, execute_kw: callable):
        """
        Test create product with variations
        """
        product = test_data.product_with_variations.copy()
        for v in product.get('variations'):
            v['image'] = test_data.image_base_64
        response = execute_kw('product.template', 'mdk_create', [],
                              {'product_data': product})
        assert isinstance(response, dict)
        assert response.get('success')

    def test_create_variation(self, execute_kw: callable):
        """
        Test new variation added to a existing producto with variations
        """
        test_product = execute_kw('product.template', 'mdk_create', [],
                                 {'product_data': test_data.product_with_variations})
        assert isinstance(test_product, dict)
        assert test_product.get('success')

        new_variation_data = test_data.variation_color_size
        new_variation_data['product_id'] = test_product.get('data').get('id')
        response = execute_kw('product.product', 'create_variation', [],
                              {'variation_data': new_variation_data})
        assert response.get('success')

        product_after_new_variation = execute_kw('product.product',
                                                 'get_product', [],
                                                {'product_id': test_product.get('data').get('id')})
        assert product_after_new_variation.get('success')
        assert product_after_new_variation.get('data').get('product_variant_count') > test_product.get('data').get('product_variant_count')

        new_variation_data_2 = test_data.variation_color_size_2
        new_variation_data_2['product_id'] = test_product.get('data').get('id')
        response_2 = execute_kw('product.product', 'create_variation', [],
                                {'variation_data': new_variation_data_2})
        assert response_2.get('success')

        product_after_new_variation_2 = execute_kw('product.product',
                                                   'get_product', [],
                                                   {'product_id': test_product.get('data').get('id')})
        assert product_after_new_variation_2.get('success')
        assert product_after_new_variation_2.get('data').get('product_variant_count') == test_product.get('data').get('product_variant_count') + 2

    def test_create_customer(self, execute_kw: callable):
        """
        Test customer creation with billing and shipping address
        """
        test_customer = execute_kw('res.partner', 'create_customer', [], {'customer_data': test_data.customer})
        assert test_customer.get('success')
        #  test add shipping address
        test_delivery = execute_kw('res.partner', 'add_address', [], {'address': test_data.shipping_address,
                                                                      'type_': 'delivery',
                                                                      'customer_id': test_customer.get('data').get('id')})
        assert test_delivery.get('success')
        #  test add billing address
        test_invoice = execute_kw('res.partner', 'add_address', [], {'address': test_data.billing_address,
                                                                     'type_': 'invoice',
                                                                     'customer_id': test_customer.get('data').get('id')})
        assert test_invoice.get('success')
    
    def test_create_sale_order(self, execute_kw: callable):
        """
        Test sale create, deliver, invoice and charge
        """
        # create product for testing
        test_product = execute_kw('product.template', 'mdk_create', [],{'product_data': test_data.product})
        assert test_product.get('success')
        # create test customer for sale 
        test_customer = execute_kw('res.partner', 'create_customer', [], {'customer_data': test_data.customer})
        assert test_customer.get('success')
        # create test sale order
        test_data.line_data['product_id'] = test_product.get('data').get('id')
        test_data.line_data['salesman_id'] = 1
        test_data.line_data['order_partner_id'] = test_customer.get('data').get('id')
        test_data.sale_data['partner_id'] = test_customer.get('data').get('id')
        test_sale = execute_kw('sale.order', 'mdk_create', [], {'order_data': test_data.sale_data, 'tax_rate': 16})
        assert test_sale.get('success')
        # deliver test sale order
        test_delivery = execute_kw('sale.order', 'deliver_order', [], {'order_id': test_sale.get('data').get('id'), 'state': 'done'})
        assert test_delivery.get('success')
        # invoice test sale order
        test_invoice = execute_kw('sale.order', 'invoice_order', [], {'order_id': test_sale.get('data').get('id')})
        assert test_invoice.get('success')
        # charge test invoce
        test_charge = execute_kw('sale.order', 'charge_invoice', [], {'invoice_id': test_invoice.get('data').get('id')})
        assert test_charge.get('success')
        # update order fields
        update_order_data = {'validity_date': str(date.today()), 'note': 'carrier: estafeta / tracking code: 8372681930'}
        test_order_update = execute_kw('sale.order', 'update_order', [], {'order_id': test_sale.get('data').get('id'), 'order_data': update_order_data})
        assert test_order_update.get('success')

    def test_cancel_sale_order(self, execute_kw: callable):
        """
        Test sale order cancelation
        Note. Confirmed order cannot been cancelled this is why the testing has his own testing flow
        """
        # create product for testing
        test_product = execute_kw('product.template', 'mdk_create', [],{'product_data': test_data.product})
        assert test_product.get('success')
        # create test customer for sale 
        test_customer = execute_kw('res.partner', 'create_customer', [], {'customer_data': test_data.customer})
        assert test_customer.get('success')
        # create test sale order
        test_data.line_data['product_id'] = test_product.get('data').get('id')
        test_data.line_data['salesman_id'] = 1
        test_data.line_data['order_partner_id'] = test_customer.get('data').get('id')
        test_data.sale_data['partner_id'] = test_customer.get('data').get('id')
        test_sale = execute_kw('sale.order', 'mdk_create', [], {'order_data': test_data.sale_data, 'tax_rate': 16})
        assert test_sale.get('success')
        # cancel new sale order
        test_cancel = execute_kw('sale.order', 'cancel_order', [], {'order_id': test_sale.get('data').get('id')})
        assert test_cancel.get('success')

    def test_order_different_warehouses(self, execute_kw: callable):
        """
        Test creation of orders in different warehouses
        """
        warehouses = execute_kw('stock.warehouse', 'search_read', [],{})
        """
        check that the available warehouses is bigger than 1,
        if this assertion fails you must create more warehouses for testing
        """
        assert len(warehouses) > 1
        # create product for testing
        test_product = execute_kw('product.template', 'mdk_create', [],{'product_data': test_data.product})
        assert test_product.get('success')
        # create test customer for sale 
        test_customer = execute_kw('res.partner', 'create_customer', [], {'customer_data': test_data.customer})
        assert test_customer.get('success')
        # create test sale order
        test_data.line_data['product_id'] = test_product.get('data').get('id')
        test_data.line_data['salesman_id'] = 1
        test_data.line_data['order_partner_id'] = test_customer.get('data').get('id')
        test_data.sale_data['partner_id'] = test_customer.get('data').get('id')
        # test one order for each warehouse
        for warehouse in warehouses:
            test_data.sale_data['warehouse_id'] = warehouse.get('id')
            test_sale = execute_kw('sale.order', 'mdk_create', [], {'order_data': test_data.sale_data, 'tax_rate': 16})
            assert test_sale.get('success')
            # test stock move (delivery)
            test_delivery = execute_kw('sale.order', 'deliver_order', [], {'order_id': test_sale.get('data').get('id'), 'state': 'done'})
            assert test_delivery.get('success')
