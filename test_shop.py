#!/usr/bin/python3

from decimal import *
import shop
import pytest
from werkzeug.exceptions import NotFound

ITEM_TEST_1 = [
    {
        'title': "Turtle dove",
        'price': Decimal('12.25'),
        'inventory_count': 2
    },
    {
        'title': "Partridge in a pear tree",
        'price': Decimal('9.99'),
        'inventory_count': 1
    },
    {
        'title': "Chachalaca",
        'price': Decimal('3.50'),
        'inventory_count': 0
    }
]


class TestListItems:
    def test_request_all_items(self):
        shop.ITEMS = ITEM_TEST_1
        assert shop.list_items() == [
            {
                'title': "Chachalaca",
                'price': Decimal('3.50'),
                'inventory_count': 0
            },
            {
                'title': "Partridge in a pear tree",
                'price': Decimal('9.99'),
                'inventory_count': 1
            },
            {
                'title': "Turtle dove",
                'price': Decimal('12.25'),
                'inventory_count': 2
            }
        ]

    def test_request_in_stock_items(self):
        shop.ITEMS = ITEM_TEST_1
        assert shop.list_items(in_stock_only=True) == [
            {
                'title': "Partridge in a pear tree",
                'price': Decimal('9.99'),
                'inventory_count': 1
            },
            {
                'title': "Turtle dove",
                'price': Decimal('12.25'),
                'inventory_count': 2
            }
        ]

    def test_request_all_empty_store(self):
        shop.ITEMS = dict()
        assert shop.list_items() == []

    def test_request_in_stock_empty_store(self):
        shop.ITEMS = dict()
        assert shop.list_items(in_stock_only=True) == []


class TestFindOneItem:
    def test_itemname_exists(self):
        shop.ITEMS = ITEM_TEST_1
        assert shop.find_one_item("Turtle dove") == {
            'title': "Turtle dove",
            'price': Decimal('12.25'),
            'inventory_count': 2
        }

    def test_itemname_doesnt_exist(self):
        shop.ITEMS = ITEM_TEST_1
        with pytest.raises(NotFound):
            shop.find_one_item("Noisy crow")