product = {
    'name': 'Test penguin number 2',
    'default_code': 'TP2',
    'type': 'consu',
    'description': 'Test penguin number 2 description',
    'description_purchase': 'Test penguin number 2 description',
    'description_sale': 'Test penguin number 2 description',
    'list_price': 100.00,
    'company_id': 1,
    'description_picking': 'Test penguin number 2 description',
    'description_pickingout': 'Test penguin number 2 description',
    'description_pickingin': 'Test penguin number 2 description',
    'taxes': [16],
    'weight_unit': 'kg'
}


product_with_variations = {
    'id_product_madkting': 123,
    'name': 'mapaches venusinos',
    'default_code': 'MVM0001T',
    'type': 'consu',
    'description': 'mapaches venusinos :D',
    'description_purchase': 'mapaches venusinos :D',
    'description_sale': 'mapaches venusinos :D',
    'list_price': 1200.00,
    'company_id': 1,
    'description_picking': 'mapaches venusinos :D',
    'description_pickingout': 'mapaches venusinos :D',
    'description_pickingin': 'mapaches venusinos :D',
    'taxes': [16],
    'weight_unit': 'kg',
    'variation_attributes': {
        'color':['blue', 'black'],
        'size': ['S', 'L']
    },
    'variations': [
        {
            'id_product_madkting':1231,
            'default_code': 'MVM0001T-BLUES',
            'type': 'consu',
            'list_price': 1200.00,
            'company_id': 1,
            'cost': 800,
            'weight': 0.9,
            'color': 'blue',
            'size': 'S'
        },
        {
            'id_product_madkting':1232,
            'default_code': 'MTM0001T-BLUEL',
            'type': 'consu',
            'list_price': 1200.00,
            'company_id': 1,
            'cost': 800,
            'weight': 0.91,
            'color': 'blue',
            'size': 'L'
        },
        {
            'id_product_madkting':1233,
            'default_code': 'MVM0001T-BLACKS',
            'type': 'consu',
            'list_price': 1200.00,
            'company_id': 1,
            'cost': 800,
            'weight': 0.92,
            'color': 'black',
            'size': 'S'
        },
        {
            'id_product_madkting':1234,
            'default_code': 'MVM0001T-BLACKL',
            'type': 'consu',
            'list_price': 1200.00,
            'company_id': 1,
            'weight': 0.93,
            'cost': 800,
            'color': 'black',
            'size': 'L'
        }
    ]
}

product_update_fields = {
    'name': 'Hola crayola',
    'default_code': '123456',
    'description': 'crayola crayola crayola crayola crayola',
    'description_purchase': 'crayola crayola crayola crayola crayola',
    'description_sale': 'crayola crayola crayola crayola crayola',
    'list_price': 500.00,
    'description_picking': 'crayola crayola crayola crayola crayola',
    'description_pickingout': 'crayola crayola crayola crayola crayola',
    'description_pickingin': 'crayola crayola crayola crayola crayola',
    'type': 'consu',
    'id_product_madkting': None,
    'standard_price': 400.00
}

variation_update_fields = {
    'standard_price': 99.99
}

# a simple variation with color and size attributes
variation_color_size = {
    'default_code': 'MVM0001T-ORANGES',
    'type': 'consu',
    'list_price': 1200.00,
    'company_id': 1,
    'weight': 0.93,
    'cost': 800,
    'attributes': {
        'color': 'orange',
        'size': 'S'
    }
}

variation_color_size_2 = {
    'default_code': 'MVM0001T-ORANGEL',
    'type': 'consu',
    'list_price': 1200.00,
    'company_id': 1,
    'weight': 0.93,
    'cost': 800,
    'attributes': {
        'color': 'orange',
        'size': 'L'
    }
}

customer = {
    'name': 'Joe Doe',
    'tz': 'America/Mexico_City',
    'vat': 'DOAJI881224PL3',
    'comment': 'Test customer creation',
    'function': 'Testing customer',
    'street': 'Saltillo 15',
    'street2': None,
    'zip': '06100',
    'city': 'Ciudad de México',
    'country_code': 'MX',
    'email': 'joe.doe@yuju.io',
    'phone': '12345678333',
    'mobile': '5512345333',
    'company_id': 1,
    'company_name': 'Yuju',
    'additional_info': None
}

billing_address = {
    'name': 'Luchita Doe',
    'tz': 'America/Mexico_City',
    'vat': 'DOAJI881224PL3',
    'comment': 'test billing address',
    'street': 'Amsterdam 212',
    'street2': 'Piso 2',
    'zip': '',
    'city': 'Ciudad de México',
    'email': 'luchita@bb.com',
    'phone': '984837283',
    'l10n_mx_edi_colony': 'hipodromo',
    'l10n_mx_edi_locality': 'cuahutemoc'
}

shipping_address = {
    'name': 'Cosme Pechuguito',
    'tz': 'America/Mexico_City',
    'vat': 'DOAJI881224PL3',
    'comment': 'test billing address',
    'street': 'Amsterdam 213',
    'street2': 'Piso 1',
    'zip': '',
    'city': 'Ciudad de México',
    'email': 'luchita@bb.com',
    'phone': '984837283',
    'l10n_mx_edi_colony': 'hipodromo',
    'l10n_mx_edi_locality': 'cuahutemoc'
}

line_data = {
    'name': 'A great product',
    'sequence': 10,
    'invoice_status': 'to invoice',
    'price_unit': 100.00,
    'price_subtotal': 100.00,
    'price_tax': 0,
    'price_total': 100.00,
    'price_reduce': 100.00,
    'price_reduce_taxinc': 100.00,
    'price_reduce_taxexcl': 100.00,
    'discount': 0.00,
    'product_id': 40,
    'product_uom_qty': 1,
    'product_uom': 1,
    'qty_delivered_method': 'stock_move',
    'qty_delivered': 0.00,
    'qty_delivered_manual': 0.00,
    'qty_to_invoice': 0.00,
    'qty_invoiced': 0.00,
    'untaxed_amount_invoiced': 0.00,
    'untaxed_amount_to_invoice': 0.00,
    'salesman_id': 2,
    'currency_id': 33,
    'company_id': 1,
    'order_partner_id': 45,
    'is_expense': False,
    'is_downpayment': False,
    'state': 'sale',
    'customer_lead': 0,
}

note = {
    'state': 'draft',
    'name': 'lalalala super nota woooooo\n',
    'price_unit': 0.0,
    'discount': 0.0,
    'product_id': False,
    'product_uom_qty': 0.0,
    'is_expense': False,
    'is_downpayment': False,
    'customer_lead': 0.0,
    'display_type': 'line_note',
    'product_packaging': False,
    'route_id': False
}

sale_data = {
    'company_id': 1,
    'validity_date': '2019-03-13',
    'confirmation_date': '2019-03-13 11:51:00',
    'date_order': '2019-03-12 10:01:01',
    'note': 'such an order wow',
    'partner_id': 45,
    'require_signature': True,
    'require_payment': True,
    'pricelist_id': 1,
    'invoice_status': 'to invoice',
    'payment_term_id': 1,
    'warehouse_id': 1,
    'picking_policy': 'direct',
    'channel': 'Mercado Libre México',
    'channel_id': 13,
    'channel_order_reference': '8888999ML',
    'channel_order_id': '8888999ML',
    'state': 'sale',
    'lines': [line_data, note],
    'order_progress': 'paid > ready_to_ship > shipped > delivered',
    'payment_status': 'paid'
}

image_base_64 = '/9j/4AAQSkZJRgABAgEASABIAAD/4QB4RXhpZgAASUkqAAgAAAAEABIBAwABAAAAAQAAADEBAgAHAAAAPgAAABICAwACAAAAAQABAGmHBAABAAAARgAAAAAAAABHb29nbGUAAAMAAJAHAAQAAAAwMjIwAqAEAAEAAAAsAQAAA6AEAAEAAAAsAQAAAAAAAP/uAA5BZG9iZQBkQAAAAAH/2wCEAAQDAwMDAwQDAwQGBAMEBgcFBAQFBwgGBgcGBggKCAkJCQkICgoMDAwMDAoMDAwMDAwMDAwMDAwMDAwMDAwMDAwBBAUFCAcIDwoKDxQODg4UFA4ODg4UEQwMDAwMEREMDAwMDAwRDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDP/AABEIASwBLAMBEQACEQEDEQH/3QAEACb/xAGiAAAABwEBAQEBAAAAAAAAAAAEBQMCBgEABwgJCgsBAAICAwEBAQEBAAAAAAAAAAEAAgMEBQYHCAkKCxAAAgEDAwIEAgYHAwQCBgJzAQIDEQQABSESMUFRBhNhInGBFDKRoQcVsUIjwVLR4TMWYvAkcoLxJUM0U5KismNzwjVEJ5OjszYXVGR0w9LiCCaDCQoYGYSURUaktFbTVSga8uPzxNTk9GV1hZWltcXV5fVmdoaWprbG1ub2N0dXZ3eHl6e3x9fn9zhIWGh4iJiouMjY6PgpOUlZaXmJmam5ydnp+So6SlpqeoqaqrrK2ur6EQACAgECAwUFBAUGBAgDA20BAAIRAwQhEjFBBVETYSIGcYGRMqGx8BTB0eEjQhVSYnLxMyQ0Q4IWklMlomOywgdz0jXiRIMXVJMICQoYGSY2RRonZHRVN/Kjs8MoKdPj84SUpLTE1OT0ZXWFlaW1xdXl9UZWZnaGlqa2xtbm9kdXZ3eHl6e3x9fn9zhIWGh4iJiouMjY6Pg5SVlpeYmZqbnJ2en5KjpKWmp6ipqqusra6vr/2gAMAwEAAhEDEQA/AJzm4cV3XFXYq6nY4q3irupxV1MVcPHwxVv9XbFXYq3kSrsCuxV2KuxV2FDt8Vd3pirqYq7focIV1RhV2KuoO+KtfwxVxG9BiriAfbFFOp4Yq1Tvigt0xQ0cVdituxZAupigup27YoapirqVNMVaxVunfFX/0JyPbNw4rhire2KuxVrFW8VdirYNcVaxQW+uKt5Eq7FLsVdTFXYq7fFXfLFDsVcKYQru+2FXbDFXYq7FXYq7FXH8MVdirXXFW8VapixLVMUOxV3XpirqYq2AT0xZBcsLE9PpwWtK6WprSm+RJWlf6n8PTBaaf//RnPUbZuHFb26d8Va6dOmKuqaYq79eKu8ffFW8Vdirt8VcNsUFdirsVdirsVdirsVdirq9sVcx4ipNB49sUIC71vS7AVuruKMLuQzAHpy6fIVyJKaQH+NfK3wgarbqW2Uc6ffvkeMd7LhKa29/ZXcfq2s8c0Z7xMrCv0E5IG0EImoPTJIdih2KWh/birq4q7FXYq4jFiXAE74obEZPTfBaaVVtmYdN8FppWSzOC1pER2XgMBkmkXHZbDbIcSQEWlmP5fpwGSaVvqYpTBxJp//SnP4fLpm4cV3hirY6DFWiaVxVsdK9/DFWt+2Kt/rxV1a7jFXfLvirY3+jFBdt0xV22KuB+7FXHxHXFW6098VdXFVrOiKXc8VA3PywE0qVXOsOw42MfqqQxExNEFK/f0zHnnjFujiJeZecPMWoRM9vJfNRiwAjPFAKldu/TMGWpkXLjhA5vJ9a1V2VzzLEnbkxJYGgrufCuU8cj1Z8I6MVn1KOSRuTVcbKT0/XjZQV9p5k1DSZQ9ncvC4JPKNmAr8gTkxMjqwMQzby7+e+u6W0cV3Kb2HkC6z7MUHUKw6H55fDOQ1Sxg8nvXk38zPLXnSNVsZxBqRJrYTNSXxqp/a65mwyxlyceUCGZA1qV3B7/PLmtwxVwxVulOmKVwjY9BtkbVWW1ZsFqiEs+lBXBa0io7I/R8sjxJpEpZf5P3YDJNIlLLptg4lpEx2Y22yFrSJSzPhvjaUTHaClab+GRtIVvqopWm/SmC0v/9Odds3DiuHWuKtU2pire/0HFXbj6cVd0GKtdNx74q38+vbFXD3xQXVocVbrSuKuqNvfFXbYq4mnv8sVcNqkdMUOpKzBIk5yE9Ow+eVTyCIbIwJKjdaY8EP1i/fk56RqaBQDXf55q8uoJ5OfDCAwHXvOSWiTQoiBwHEYFNqHwO3bMQklyQAHgXnPzA+pXTzrI60HHrtUdcnENUiwK41KbnRZaqexPjllNZKBDTyueALs3YdT8skxtWj03VZVDpbStG1afC1D8jTFBSt5JI3+JShBIFRvWtMLG0z0/Vr7TrqO5t5nhnj+KORTxIPb9W+GyOS831R+VH5tWvmW3h0TXpBHrqrxR26XA+fiMzsWW9i4+TG9fAqSO4zKtopWSBzvgtKKjtOm3XI2lGRWe/TIkppGJZ0A2rg4k0io7KlKDIWmkXHZe2C00iUstumAlaV0tKb0wWildLUdKZElNK621O22C0qqQU7YLVU9AeHvjaX/1JzXNuXFbwK7CFd/nXrgKuGxP8cIVqtOmFWx49sVd79vDFXUA2OwxQXYq38sVdWnbfFXbVr1xV1fvPQYoVYLd7mZIYxWR+nyyrJkEQ2QjZZZaaRHp8JZl/edWZuvTNPkyGTsIQphnm5vUtpET4ZY1PI7k8SOtBmLIuSHzV58uPQnlZj+9GxA70FK/TkosJPH9U1AzkrEfh7U65eA0Epn5Y/L/U/MEsckiypC5BUKCzEN+0B4e+Sti+vfyw/InQotLSa9sIucvHnHKAxNFoSWP37ZWSzAeif8qZ8mWsJVrZPTJBEbbqp6bKwoNsFpphHmL8h/I+pfWeFnHHy7gAH1DuGAFaUrkrLCnzf+bH5HXHk2J9Y0rm9gq1mgILhWJ6gitBt07ZK0EPG4NRn066S4t5HhmiYOjKSCHU1BH45YL6MC+5vyb81xeffJlpqZK/pCA/Vb6EEEiZBWu3TkNxXNhCdhxZRovS4bLv1ByRkikdFZ0A2/DIWqMistwaVGC1RkdnShIyNsqRSWnSo98FpAREdqNzTI2qssAA6b4LTSoIQOgxtaVFh9sCrxF7YpXLGAd8VXcFxV/9WcjfNw4rsVbxQXA+ORKXbYFdWuSCu9/wAMKC7+OKu6/TirfvirXTpirfuMVa6e4xVw326g/fgK1bM/LejmOFrmdQJXFUPt4Zp82QkuwxxoIvVJgqVoSo2Kg/fmGS5IDzDzddTCB5G40CmmxBIqab5WWx8x/mFfJO5ArzFa9RSnXLotUywnyZoY8weZbazkobfkGlFaHjXpXrvlhLS+6fy+8h2Fnp0MX1ZVKgEEgV4/PIgpIekQzJpVrJbvQFN4x0+GnTFXjPnX88tB8s3v1DUL/wBO4AWVlEUknHlXiSUBpU8um/w5IRKmQ6qGmfm3pms2v1iyuUuoONFmhaqk1J3XtT3ywBgZJ9dvZ+YtPkt5wjW93CVkRlB69fHtkSh8B/mJpMOh+btV0i2qIrWdkUHb379hlgQWTfkx+ZWoflt5ljvlBn0O9pFqlkCPjRd+SAgjmtSV38R3yyMiC1kW/Q/RLrTtd0631fSp1utPu4xLBOhqGVt+vjWoOZN20EJ1HZ9ARkbTSKjtQO2RtNIlLeny8MFppWSCnbAlUEPf8MVX+mNq9MVdxA6YoXU7Yq7FDRxVby3xRb//1pztm4cV2KtjAVa79OmIVvEq7EK7fx2woLqbeGKuxV3+dcVdWpGKu6CmKuJIxVF6dCbi7ijP7RG2UZpVFsxiy9OSBIrZEpTany2zSyLsgxfWHZDJUjj49CKdcqLaHlHnm7jW1dhWlKBgQR4/RkGT5Z843BNxKgaqMCQp3NSa9cvi0STX8g4EvfPK25BaqkqCARVTyH45KTXF+hflq3jt7USNQkrQmnH8MiySDzvctGhaChkG608RvT5ZOLAl8bfm/wCRtd8y6kLzS7YT3kHNWgX4DLA557VIBZCD8wfbLwQGo7oHyB+XHnHyx6l9fxRxjUP3Z0/kfUQoQ3P4RQsakb125cviOQ4wSzEafR+k+r5f8t3mua6Y43trd3VFqARwLU36b7ZWZbsgHwp5m1VfMmv3usTqEa8maUrVjsOnXxAywMShrGGMOasDVT8NRH8YqB7EfFkrYh9sf84hebH1Ty7qXki9dxe6JKLmzWVeAa0ufhYJXqFYdv5h45bGTXIPptLagG2xpQnqR2P3ZJiqiDjT9WKqoioa0398VXcRirR26YoK2uKFtcVdyGKuqPbFWifvxQVnfCh//9ecDNw4rffFDvbwxVvFXYq7FXYq4U74q47/ACxV3virfXbsfDFXfRtirXt44qyLynbNLqCuwqq79K0zX6uVCnJwCyz68NIyCaEdDTbNWXPDAfMUxWJwTQEGjLtsfGpGQLYHhXnS9uCknF2AXlVDTlRR2FTTIhJOz5t8030080iRkPGK0LD4lHXc/TmVFxpF6h/zi3p0d55ou7iT7cCp6RH01yMyiL7ptWKRBE8P1YhJSPWbI3m7b+OEFiUls9GtvrSO8KMiVJDAVr9Pthu2Ib1KSGwne6s9PiacoEaYhUDIOzUBY7nIUzt8hfnP+bfnJrzU/K15JDBAG4MLQMAY2IogZgD08BT8csEUGVPAvUdzzCn6DvX5nrloDWSrQQy3LrFG49ckARMCpr82oPnXDTC3r/5Ual58/L7zVpWu6aixSqHtUt78GOyuornrF6+yAtQAMrfa49accN0tW++fyv8AzM0X8zdKnu7GJrDW9Nf0dc0aZg1xaXAJ6sNnjb9lwKN8+QFgNsCKZ1wANAKf1woWMSNj1wKsJwqtJ3xYqZb8MNKt5V2xpWq/hgVdhCC1ucKHUNcVf//QnA37/Rm4cVuhp03xVwrvX8MUN4FbocVdTFXUPhirqb4q6h/sxV1K+2KtEU/swq4V6dMVcK08affgQzzyXBwiaVqAHffr0zUamVydhgFBkt7RoyK/DQdMwi5Tz7zGitG77+otTx8T4ZEsnhXnWETGaNZD6oFSCaEDx27jwyILI8ng2r+VbuZ5JIgXjqWDCpJ3qcyAWghn/wCTnm7S/JVy1pqym0mc1W5pVWXsp8PnkSxAfUmg/mTompxx8LuMk1UBWBoRvQ79cFpT+41W3ngPpOprQjxockGJSmS/AP2+gNRk2KT3t+ZloAQWFBXwyQYl8+fnT+Wx8xo2t6Wpk1KEU+roAOaCpNT3I7ZNjb5sbR79JjD6bK6E80YUao67e2G1pl3lj8s/zC8zOn6A8t6hqRc0EltA7LSneTZRX/WGGyxoB7V5R/5xk/PSOwnaJI9HgcL6ml3l8nG4UjcPEodCR4ScR264aJCLD2X8t/y9/MnyV+ZmiXDad9X8uS291baneKYZEFuYCVST0n3/AHscRj+EUyMQQd0ykCH0iNl6bj5dcualJicKVNjigqLN37YQhYx8TthQWgRSg2xUN0xSqDIliXe2Kur9+Kv/0Z+tux7ZtbcVUW1r1xtVQWvhvgtV31b2xtW/q1N8bVsWvtjat/Vab9TjatfVK42ho2wr/HG1a+rV7Y2q023hthtVv1b2xtV8FiZpVQCtT0yMpULSBZekaNY/VLNKAVIpmkySs27SAoKtw8bKwP8AeDt02yltYlrqgRNyNZACQTTbIpDxfzHp91fTSiO25c/hND0I7r4nIs2Ly+V7q3NWj4nc7g05HapoOnjkwWBDHtT8p3ZvID9TS6ikqnCKtVLKTWvtTtk7YEJW/kvXrZ4rqBJ7H1pqJKrcUoykjZSdtqjG0Ms0HzF538pww21836TjkFWjckTInQfEetKdMIYl6Xovmqw1pFnjm9OcqecEnwyKfCh/Xk2so15udGrQU61rkw1lGaTor63fQ6dGPjnahJ6KB1JywC2N09H0j8lvy9024GoT6LbXup15NczRg/EO4AIH35YIhgZl6AqJHCsMaKkKgcUUcVovQBQAB1yTFulNhsO3hTFC2g+Z+7FVjEUwpUWYeGKkqTNXFCixySCsJrihsUwFIVF+/ClcMigtnFDqYq//0utpZe2bK3HVVsx4ffgtC8WY8MbSuFp7UwWq76n7Y2h31SnQY2rvqgHbG1d9UHWmNoWm0Hhjarfqte2G0Fo2p8NsbQsNpXtjapno2lNLcKQp2PX2zGzz2pyMUbLNXjMUdF22oNuw8c1hdiEgu4pGkkDbK+607ZVTO2OaorEsCa1FADgpNpClkpIYKAw61HXEIWtZQN8LKARWuwJ3GSCpPPpmn3DKyoiPGQyVG6SLtU+IP8cKEsv9Nsk4xW8ZgkUMTCaiMO29SCfiWu+3TCAwLHNWikjgKlEFzHShYUKMRUMOIrRupB9ssAYlhM9uvqmeJ2WQE/HGakt/NyHv1y2mssl8uatfSX1vZXNwPQkdEeRxUryNC23UjCAwL6m8meSV8ts13dTC4u2HBCg2Cjvv3brl4DSTbMSOtcLFbX26YoaJ+7tiq1jTCqkx8euKqLMQN8VUG69ckgrCK9OuAIcBhTS5RkVpeB7YpX+3TFAb/VilratcVf/T72LIbDM22heLLbcf1xtC8WYHbG1bFoBjatm1Fd/1Y2q36r7V98bVxtgdz18MbVr6qP7MbVabUDthtBaNt4jG0NfVfAY2rhZkkbbHbAZVumIsso0uxW1tw/RnFTmsyS4i7CEaCKnHw/5OUltCVXSAKW6jIs2F6tL+/bwHTAUhKJrhF71UdfDAtJfJc0B+KlK1HUkdunTFUDeTq9aJRiKy0PwKw7H51whCS3t1zjb92PViqtFB+EAkDfuMmGtjGoXhXnIsvphgduRep6dD0y0MCWMuiFi9QfCtKfcActa0XZVjkWRjuCKBdiPoAyUQxL7d0mb61pVjPU/vLaGT4utWQE9fc5a0oquLFquKrGYYVU2Pj0xVTZsVUS2EKpnEq1iFXADAVXhfHp28cVVAtKYFdirtsVUv2vbCr//U9Mi2HhmTbS2LYeGNq76vjau+r9sKCtMHtihr0KdsKtej7Y2hxh9hjatGAeGNpa9AHG1cLcbmm2K0idPsxNNyYfCm+Y2We1N+KHVOXIUU+4ZhEuWg5ZQtT298DIMe1PUSqsqb9siQyYHqks5Ysx416ZDhLKwxy71GWBwZB8PiDg3DJDjUvUTkWB9ga1/hhDFDS3K+o07vQjdVb4T3FR45MISO/ukT40mp0KqSy07EDlTbbYZIMCxnU7r1JiaLv0dDUnLw1SSwSUPiT9+TaiiLaVhKGAHI7qT45YGL7a8ryB/LOjyAmjWVuRXw9Ncm1FNCadvauKFNm7A9MKqbNim1jPTFiSou5+eEBCmThpVlSMVbHv1wFIVVGBKqBQYFb+eKupXFWj1/jhVZ3rXFX//V9VeiO/4ZfbW36Q+jG0FaUxtDXDvT6MKrTGPDbG1WmOnuMNoLgm24w2hr0+9PoxV3pDqRvirfp/2YLWlr7MIoxWQ9vn45GU6DZGNlMraFbeIClD3Oa+Urc0ClOeQH2A6HK2SS387gEA/B4YUsX1C9VAST7CnX78VLB9V1hObIuxAJrjS2xOTUo7ivJu9BU9/EY0m0snvfSDMj0Lboe2+RpNqL6vGABM37wkU5bUJBrv26YQEEpRqGpMit+99OlNuQJJPjlgDWSkMk7PIXYhkru1cuDUSpeqQSKipOwBrTJsCiIpCCCzEV34+BHh/HJhD6j/KD8wrXW9Mg0K54wX1lEsVsg+zLHEgGxPRtt8spqL1MmuBCxjTrilTZ/A4QxUWcDrkmNqJYnCi1pOKLd3xSF6iuAsldKZApVBQ7YpdQ4q7FVrHf2xQp/ThS/wD/1vWnE+FBl7WtYDr3xVaU7YFa4mm2KGinfG0NcKDw+eNq7j93hjau9MeH3YbVv0/pwWrUxEUZJpWm1cbSAp21Ih685Ck9j4fLMOciS5cY0Gp9SXdIhRf5jkKbEmudZhSoZ/i8a40qR32uI6EBth3wJDEdX1HmjAPRf8++KXm2uXonLUlECIC0jE1IA8fAYVYrLqT2jSvcPELUMomJfeOo+EslNxuCMaY2jbi/t3hJ3J4rwf8AYcMvUHbpjS2xu7vWD0lqCCCBv16HftkgGJKUy6i/xISCQfi/hkwGBKkt2JSDTkRtx8D9GWANZKt9bIFAfYjvX54UIhbgsAEO+258e+TCsm8sa3PpOowXVnI0VxCwdGB/aqNiPoyYY0+x/LWuxeZdEtdXiIKzqOaj9iQABl+g4CwKaMdqdcIYlQZ+3T2yVItRLYWFqDS126YaY20G+kYaVVHv0yKVZTiyCqlfoyBZKoIwMmz4d8VWE06YqpsffCFU+QrTFX//1/XRWuW2wKwpXbDaHemfpxVrgen6sVaKe2Ku9PwG+Ku9PFVKaa3t95nCEdurfdjYCaJQjatZjoGZR+1Sn68gcgZjGUsvNctSwYssar0rQ/qyqU7bIwrmlF15mgHJhIJGAqd8rpuY7qHm8ekaPQnalRjSLYje+apWkKBzUd/fDSLSxfM6T3BhNwvNQSykjt1yBCbWanqitbtIHAi4gVPQc/h+ivjgpbef3Wp27NcrbyhomnEUsy/3jVpVVPgv2WJ74UpFqUltbOeQV4OQErOtRJEw3VuX7Q/Zb+GEMUut9TNieXFpLX+7nSIkFR+zIgNfhPRhXb7P2DxWVMbVCsl6lbSRCgakci8VPxdRxopBr7ZIKSlWoJLBKCw4NQVUGrqKUr9OSDAoeCWhBUVptxqAAcmwRaspG60kJAI+XhiqvG68hTofs064QqaQTKgV+RAB3oOp7ZYEF6v+Xfn7UfLlIopOdgzAy27V4kbVoex+WS5sC+idF8xad5jsxe2DnjQeojU5Ix7Gm3yxprKPLVG3TucLEqEjmhGEMSok9NskxbBGKq6HapNRkSyVl6e+BmFVd8ilUDV2yK24tim1NmNd+uEIUmYYVWchXFX/0PX/AB8MsYtBdsVdxxVrj/t4q1xwoLuNKVwoS7VdUg02EcnHrNsq1FR70yMpUzjG2JvrVurmSclqmtT398xiSXJEaSDXvOFnHGY4WAfs334RFBNPMtR80XMszIZeS02bcb5YItZklU3mK9C7Sbn4BQ9j3yXCjiQEmsSNuZS1epr1I2x4VtIdV8xeiror0lO7OTtT+OCkWk+ka08k7MhCEkH63PRogoBYmnUUG9K5GQZAsrudWRLWFo3H1vgnCBlMaiRmFJDy3+BGL9enbKi2gpfqs1vHbPLFIgq1EjFVVj9ol1oACevw1+/IpYdLeidjGCjqCeIO7K24IJ6ZOmJSthOqols4hmqQzcS8NCa0NK/CSN/5TkmCO/R7GM31oR9bLBlWNqhid2HRfipXaprTFUTJ6d5Gr8SLh41ZdiqMxFOJ22bbG1SMfuJeJIElRxH2qGm9QetfHJgsCuSR0IOyipAJNWAySExjkPEBWNOxFNskFRwdBACG77jJBBT7TbrjGCNhUfqyYYlnPlbzhfaBeRXNpIKqAHjfdGB7MP49smxIe4aD+Yvl/W40SWYWd6TQxTbKT7P0P04KayKZKZI5fiidXQ9GU1H3jb7sIYFZ8+uLBcPEjbxwqrxe3XwwFkFdDkWSoOm3XIs267e+KtVBwqps3hgQpM2FFqfPthpbf//R9ihMmhorjatFabDChbTbFWqYqgtSvksLZpW+JjsqDuT/AEwSNbpjHiLzHW9XLTPK8nKVqli3QAZimRJcsCg8z80+ZJ5QEhf0+PgaE0yYDAlhcutSTKXdqsoPXfLxs1EpNJqzNKWIIpjbFbJfO4rU0O4Hj7YLVByXDgMxfiBsO4Fd9/HrjapLfwzO3FPsvUA1q4XxP04qv06zjUxr6Ya0JVpSSatxbkQfCtO2AhIZpeX4lsnnQIt3IGPNh125UIBp7bZSW4JNe3kADRyxlp5EUcKk8mQfF32oKN1GRASxO9twXeQFYWNCxT4dk9h398kxUAzGRBByik35HkVJpuaH+GTQUZZ201sz3WmXHrs3x3Vk4UqQwFTHz6HY+9ciVXRazBOXju0EF6lUlThxYMNxU7V8cBVBXCBpeCE/CCpLHfiCaEeGTiwKwIDIyn9sDfrTtljFEwrQlUANdhvvtk1TIIWtGLLx2Br3JrigpjZOEgr27g70+nJAsSjYr4KaDbfJgoRcepSq3JWPw/Eu/fG1ZFpHnnVtKp9Xu5IwCSQDsa+3TDxIMQ9I0L83S0aRX8SygEKZVorEHqT8sNtZxvRtI8x6PrI52Fyruf8AdTfDIfoOFrMaTyOtaDr02wFQqgjtkWS8Hb3xZB3IU98FLa0segwotReSgwotReTbGkWpepv13phpFv8A/9L2TT2pljFojscVW08MCVhGxwoWkhVLMaBd2+QwoYNrl680skzfCoqFBrsuYc5W5cI08j82anL6rJDTggPqMf7MQGRLy7WNTaReLP8AGRRAOtOuWhpKQTSyyHiGIrQADwpk7Y0r21iSQzVNAak7dMFopMrHQL7UJ1gtYHllqPhAJ2qOtMiZMhFH6v5X/RcIWQh7g05qv2V26ZHiZcLG3tAqFm2DGrV6+G2WAtZSe9uRZrVaEjZQfs7nwySEJ/iCOKPhIecFaN8RXY0+jb3yuQZiSMub9Ly1V4yTsDz/AJlpTotR9IyFM7SueWCdn4qQZNwtBt0BrTxrhVC8njcOCBIrLUbkMKmtK98IQjLJJ4kiklk4Mjn01dqK6sSWTZlIJG6n7Vfs+GJVFaklutn+ljG73EbKzGRfg9AGhruelDkFQMyc5Dc80aJhUHiKqCBSpy2LArGAZgQ6ghftEdadNhk2KJtnX7LGtBUHpklTZZA9mTSn7IU9adcKC1K3p2sdD9r4m+RwoQkdw0R3PzwKiF1GjUqafww2xVxfJ1B98Nqjra/KHkDscNsgnen+YLq1dXhlIIOxqRQj5ZIFBFvU/K/5xTWvp22tobu32X1AR6qj/iLU98NtZg9f0TzDpnmC1+t6ZOJU6Oh2kQ9gynphayKTSv0E9MihaX264ptSaSm4w0i1F5KA1OEBBKg0vhkqYkqXqD6clSLf/9P2Xkwho7b98KFh9sVWkU+nFBS/VpPTs2ANC9AfGhyMjQZQFl5j5o1MW0bqpqO9NzTtmE5vR4b5t12ewiklUBp2r6Sv1LNtlwDSWGyLcLGbi5+K4cfD4VIAoBlnRii9N06QzojRNNdSgEQrWvE9ST2yJKQLe3eTPycu9QMF7rSmKBQZPR6DoCqmvWu33ZSZFsEaZzqXlnT/AC9p7WtjF6YI+KWgDOepJJ6YAl4x5rVGuOFfic0p13yYYF5v5guo7NCoIqu23QnLg1F5xe6nJPI/I1H7K/PJsUvWfjy61ruo6nAqMgvDAystewK9DSoqPDI0ytWe66OCQSace3jvgTaIiuhLJHyNGU0JXbiae/WuKUQk0c6G3VUZXBDhxU7Ek0PY0GxH2TgVdHcalafDat61tyYy201OQStNmP2qCm3hhpFoUXNhFMRGptTJVuDAJHQ9lK1HboMkGBRDG341UmrftVBBHsRklVoAUpRwag8eXvhCpm0YVY0dtzuDWg6dKZJBUL6VWmFtWgiCo1BSpIr92+KEE0zKSu9EqD4H5YqozXXE1BA26Hriqmbo1WhpX7sVRltfPWlen68VTGPUPhDE/dvhtUVHqFDQN06jvjasl8vea9U0G7jvdNumhkXqRU1HcEdD175MFBFvozyH+YVp5ps1trorDrCLRowQscgXuteh8Rkg0GNM0Z9yRufHDTC1B5AOuGkWh3k8TsclTElDvKR9OTAYEqXqivvkqY2//9T2V/mMsYtHriq04qsJNPGmLFIfME5Q8OoUFqZTlOzfiDw7zrqEgLtA+4NCpFdhlA5t5eT2Gk3/AJz81QadZxGZlJlkCDlQL+oZe1F7Lpv5J6hdMJZzHHx+yj777dQPDKjIswA9L8p/lL5c8syPezJ9d1KQ1aaQVQAdgvbIbsmdsI44+JAC0oFG3TFWCecpV9JzzB2Ox7YQr5+8z3Xo+q3WZ6hNugp1yQYl4d5pu5HnY7siAhmFPtfP6ctaiwp5WDkgjl0oPbxyTErFapViBzO5pUUGEIRPKWhPEMtaBienyxKtiUqpWQBqmnHfly9+2NKreq4jUCgk2BAp1HyyNMrRUNyAQleIryWh2964KSCiXuTICvIhCAVZQCAaeHc++EIK+AiQlZFBUjbwP39MLFUUQRsVRSKn4UBrTJKjIVij4hieT9O5GKpmkgLgE9AByNTtX2yaCluvWk1teSc0KcqMDv0p1NcCpP8AWm+FW+KpA4964qsuJQ5qUBJqPcYoUtyKitaio77DscVRMLEOrEk7fH86dsVVfrTICGb4jtQYq6C+bmOe7ePtiqc2eoBzxJ28CcKsk0LWrmwuY5reUxSRnkhBIYMOhFO+EFat9OeRvOn+J7AJdMP0rEq+qAf7xaAcqePjlw3cacaZM8nv0ywBpJQ0knfJgMLQrS0J33ydMCVP1Pi6+9PfJUxf/9X2TWuWMVpPh1xVonxwKt8R0wsWJ+YJd5X2LDpmLkNuZjFB4r5nhmube+nrxKowXcDfIR5sinH5BeWJdNsb/wAyXaVmvFFvbOwq3AGpp9JzJBceXc95sYaQrWgJ3PjXKCd20I/iaDAyCWalcNHExBAoD1wFLyjzhq0gSRSQUAO64hJeBebNSLRsV+1KONfAA12yYay8f17iLldndCvxsNxvsAfDbLQ1lIHhKmifvIORUCvxL4e+FCwRcWLN9J6H6MWKoeKKCCasaDkev3A4QrZiDAONymz9zUnbwwqvAaPZxUVFD0IxVVJIC1/ZrUDc74FbQjdK7bbMaUwKi1ICMeJB2oOu2Koi3kpQ70UntvTCFV2m43ETciQapQ9iaUrhVNDxUsEIGwLbkUoBk0PeZvy3Tzz5J0vX7DimrG0jSaAH4JTCOHXoDQb5PgsNPHReLax+W+t6Te+nd2skUlSeLL3Hge+V0Q23aWt5U1FTX0HZepFD0+jBaWh5ZuwFZoWoftNxPv0woQ0+kvCgYVJ8O+KpXcxlAK7eIxVBrVatX5U8MVV4bkRMr1PHxxSn1neM7K6kFR9+RV6X5G80SaNqdpeBiyRsDKm+8fRh91Tl0CwmLD6W9dZ4o5Y2BjkUOpBqCpFRuPbMsBwCh5JBuK9cmGslDlq75JDu1e/TBav/1vY3IHJsWq4pa69NxhYlxPemK0xLXo24y9+tMxMnNy4cnkPmorb2fpsCGllVWAB3VmAORgyk9p0y2igsLC0t4lihESngmw2Hh75kS2DjR3LJoUooB2GY7kK71C+HzxKWO6yvKMlyQvsKYFePedIT6Unp1Iodz4Y2yLwLzBG1xc7BlSNXPIbU7UyYLAvPr+KUXCRCq8xQBzWtKgUJ3GWBqKSLEWLAE/B8KMxo9VYni1fcnJBipzAu677tUHuB9IwoKlItaeiocjr7UwhC+Fi5VCOEh3Wm4bjua4VV42juGc/yNVlbrSo6ePWuKt+iSPTQgOaDfaoHeuNKp8gsh5LRU2ZutfceOBURy/derQsAPhbp94xCrofWYmQgcBVtuhGFUfAkU07yn4CpVgBuD9BwhU4nERmPwhSRUHYV29tsJQH1T+Rl21x5Ijt2KgW80kYAJqVajCvbLYnZx8g3ejXFhaXiFLyFJl60ZQaH223yVhgFBPL2jqykWMAKggH01pQ+2DZlZVB5d0P0fQOnwel3Xgu9f9vBstli3mD8pPKetWjxRWi2U/ECKWHbiRXcjvgMQyEiHzn59/KLW/LMskrRmez6pcL9kjelfA9dshVNwkC8nudPlgbjICCNunSnjgSgWDKw/l7j3xQioL4W68j0qNhgKWUaZqCFlaNtjufo3xBV9Jfll5qTVtGGlTSc7qyXjHy6tDWo/wCBrTM3GbcHNCt2ZuxY1G/v45e4y5EJ3O/v4YCWQiremafxyNsqf//X9hA5Yxbr2xV1fwxVaSe2FBKR6zFyJ2O47ZiZublYi8J/Mu7nhkVEUcY3Qrv1o4yEGc3uPlid7ywtZ5FoREuw+WWTk1QiymN1A32PbKm1qaTqe3jXFUi1U84z+1t9nFIeYeZV9aOSMDjUEfTkSzp5Hd6OL5Zo/T4GrmvfbACxIeX+ZNGeMsZFIkFCtO3WlMvEmshhpsgHuRcqWDU4SoSKv2Pzyy2shAvBLayhUDSIac6/FxbvQ5JgpM0auXToenue+KFqSo3IfZkG4I67dh8++EK6GQu7Rl9mqTVf44bVwnnLBeqqaBhtSmKq6yCVTsa92PfFVdWPF1p8JXj8sVV4GCoEU8SopvuScVRKFF5EGjqAWPY/RiqJUM8kZLUqKg+59jk1fUP/ADjvdxy6FqNpyrKk6tQjqrLSv3jJxaZjd7WlDv8ARTCwpeASd8CaXrXCinEgkDxwoQ95a217C8F5Es0LA1RgCNh7/PGkPn78xPyQf95qPl1TOoBaWD9oe6+NMhKDbGfe+dtW0SazmeOVSjoeJDChqNjkG5j88ZQOjGhG1QKn/PfAVV9Ov3iMcZ+Ltv1yCvUfIHmOfSdSt7tHNUYB46/aQ7Efdl8JU1zjxB9QW8sVzDHPCeUUqh0I7hhyH4ZnW6/hpFxJkCWYCI4fDkLbKf/Q9gcq998sYuHTbbFXE+P4YqtrhQUBqagw8qVpWo75TlFhtxHd4H+aET+oHQFlZgaDY7HxzHg5EntXlAj9A2b8SGaMYkoAZFzqw36YEqcsldiTUb5EpSm+flE4H2vDFLznzEnFHHL4wDsMDJ5xIZSrqrGI7gnqfi2NBkQrHLuzS/WQGMMiMUDgcTQAGu/zyQLEvMdc0Wazn4gFoZZCre1RUU9/DLxJrIY9fq8amFQRU1ceNOhHzyYLWQx/grymNm4lR0AIO5+/JsF5ggopdqsAeJ71+jCELJGFFUChHWRgSPwwq0JHr8dBX7LL/TFUTEOQ2IY7fD74qjET92FkFKnpiqsVEElFbZt1GKosxRSLUkrIQGDU226g5IKuiUNKgVqqor4dT2wq+jP+ccrhFl1Wzr8XGNwpNNuRFcIa5voNSNu1MkwVhSmKW2NBQbHFBWV/DCxKwtt1yYYKTkMKEVB6jxwqXk/5tfltYeYdKn1TTrYJrNrGzlYhx9YdaUHffbIGNs4TIfHupQNDJJ6n94nwcD1rTplDkpPE7CYwqnwgj94Dtt4ZBWYaBcFJhU/FXfvkgVfVn5ban+k/LsMbsGms29A/6nVfwzNhLZwskd2bxigA+75dvwxJUBFfDwyFs6f/0fXtctprbxpVpbwwqtLYqoT0eF061HfARYUGnh3nsNPqUWncKTSyheI7b9cwSOEuaDYe0eXrQ2mlWkD/AG0jUHw2FMCUyagrvTAVQ0sq0NT7YEpVdzKFYHYkbA9TilgnmNC4YFeNe48MCQ81vYpA0kSbvxPFz0BPjgDJI5JAlpJbmMRRkjkgHSoNTUn2rihieo2ScVLuEmRtgxHGStPh2Fdx3yQYlhGu6XeQzJJaQNNG3IMo6gUABFBv9OXAtRCRLAssRkVfTkHL4XFGFNiKdqHrlgLAhKriB1YBm3PWnf2Pj9GSYKht4kj9Un02qBxNSrH2GEIaAIZVanFehHTCqpEqGQhqA136nFUbwWKgBryIoRvSmKr1kDUPDxoTiqYJRokB2J2BOwrkgrUQdTH0AoQT4muFXun/ADj9dBPMF1GV+GaBviH+Sa4Rza5vpZGNMm1qwY7Dp74E216gOFiSps1N65IBhaznXCi1pb78UKEpqpU78gdj0FQRhCvkr89fIg0PXBrVjHx02+JcKNgko+0tPDeuUzjRtyccrDxO7jCENGuybsO/hlJbU10WbkysCNiKHEK+k/yWuXEl3bE1WWMP0NAwPWuZEC0ZBs9mTrt9Ay0tQRfH4Kd/DK+rb0f/0vXXLLml3L78VWlsVUyfowhWidq9sKpTNpOnXupR3MtsklxEaiQjevzzGygORjJZDEqhKUAHhmM5ClPIAOKipORKUBcEqprTFUmuX6mnxb0oK4sgxDX+ZDd6d+mBLz6/DGRiBVab1NNz74qwu99WK6MbOaMykKKMOu9K/QMVQt5BDM7fCTKH9N2NWO1dwen3YoLGbyJ7SaW1hkYsAeYJavHuePSo98sDAsY1OGNQJOA+vV+Nm+HnUgE7FaGnjlgaykl4YJIlaNgbkU6EM/LatRWuTYFAyK/qFHSrjqCDWp77dtxkmC4q6fAaNT7NOtMIVyrKGHj06g74VRsRd/hrWnXl0+jFUdbRuqNUck7L1+nFV6fAkoX4QKFT1AJyQV0bPTkCaVHIeAqN8Kvbv+cfXC+YJEqOTW7UJPy2GSi1z5PplWHuMspotdzp/XGltaz/AO3hpiSps9MNMVpY0rjSrS58cNKpO/34aQSxXzz5ch80+X7rTWA9dhzt3NCVkHQj9X04JCwmEqL4k8y6Rf6NrV1ol9EYZ4gZJAewbf7sw5CnOBtT0MqXVYwPhI/DAEvpD8loZDe3UpXiEg+LfapYZkY+bTlOz26MdNvnlhaQUXQceuRZv//T9bFsvppW1HQ40q1mAw0q0v3/ABxRa0vQEnww0tqNgtZnkbtuMwspcvGNk1/Y9/bbKW5CT0Via0ORSgJJAfmfpwJQNxFUE+PT54UhieuoHR1pQN0wJYFqsAAWNm2NQT0xVheqwxtBKoYVU14Hc7EAgD/KrSuKpVLcJI0syMYCODiQEqa7UqpBGwNaU/hirGb48/rFzEwAXeICj0aoG2/Q0/hkgwLEL8DUJpJGZlP2gQW+BPEkbH7O+XNZQEK28SKJviFOKyNvR260r75JjTp7V5ZhI4IULwAHxEqDuRTrSm+EFiVhiCqu3Ekbcqg+I/XkghQ4mReWyzIfhY1ofbfwyTEq8TLRjxoSNiPxxVE268mquwI2ruN/EDFUTECYiX6ivIA/dtkgqtblC/MHcALRu9ceqvVvyJlMXm1BQl2jkU71FPbJx5teTk+plaor29vllziNM1OnX3xVYST13GSpVtfxxQ1y+jCrRNMUWosSanFCkR2+W/bfJK+Vf+cgtOFv5xW8UVNzbIr92qGI3p8sxcg3czFyed+XtKkW4jPYUBJ71yhufWX5YeX30jQ/rdzHwub1gwDAg+mOla+O+ZUA4uSW7PEotMmWsK9fhr2yLN//1PWdcyGpaTihTLdanCGJWFjthQslaik/dXAUhU01SIyx35E5gTO7nwGyYcqHp9OVM0s1KVv2RUH9rKyWcUqE4Vt/kDgBZl0jsykg/LJsWI67KGYqGpvirBNVcGcRkVIGw2O+KsR1W2CK0jivNiAo9z128KYpYpcJDLcSq4UrGV+AvxBai0rt7AYsSld9E0NsWiiWaE0Dqa9V3BpQdKZIMUgsVc38aycI5JWZmaYVXhWjADx9tunXJWxpLNatTBcGOBP9GDFl6c96/DQ7kmh+femWgsSoXE/qrbmGHlDAoUr8TngTv8Q7+2FiUYttMH41QWjKWZgAeI22Pc+G2IKpVqFtCSBDKSytVTvQd/pywNZWxRnizcgzfIjChXhkMVa9Dt8OKphDFyTiprJsykk/caYQqpblmkr0DEgmpNDir0b8qvWi822npkqzPQVYjkCN8sjza58n1krHiBXp1y5xHH3yQVb0+WFDR8cVUyaHFiVpP3YoWtT6cVWNv8skUhgnn78sdM88rFNLMba/h/u5gOQIP7LDw3yqUbDdCdIXyp+T/l/y66XV4zalerQqXVUiQjoQlN6e5yEcbKWS3oVKUHWv0CnTxy1pXLRSSR0xLJU5fD12yLJ//9X1ntmQ1LGPbFiVJj27YUKffbCxKlMSV3Pw98BZRRdhRYQBTNdLm7CPJWaU/T0ypmluoP8Au2YdB1yJZhIEmHqVO57HsMiGavLKViNTuRljBieoFWevcE/I4qw/VYwswcg8eoFafKo+eKsP1K5lkUUB4oeYJ8Buak+wxW2JTRie8e5K0hkYxKGB7KakDueuLFR1aItC4SYopDEQgKAUIoKU98IQl+hxwQems/EM7OY5E4grKp3BBrtUfa6ZKkMOlv7rUL5nkRQ7sX+DapFafflrXa2dWtmAdAYGQPxOwDNTwwoTmN7W9tFTgiGOpQt4sANqkDtgSkN5CqUoaOeobrWtPE5YGBDUMRUdQQBvX+uSDFfyIPAp8J6GoOFBRVlyYBQaE9sVVJDx9RwT1oB3rirNPy4l/wCdj015n4lZkKv0IplkObCXJ9jRgsil/tEAk9MvcRs7ZIIWE+OFDTYoKi9O3bCELOWSpWq1xVrIlWl64FC4n7sWSxtq4qt3r7DFFrt+PXbrgZW//9b1l29syGlTbxHbFBUm8MKFNmp0wsVKUgqS3QDcDFI5qtrKqwCnbNZk5uyhyUzOQSQfkD1zHtupB3jGROA/aB6YpS5YuP2qHxxAUqdzPRCvYdMmxY1fc3qe3cH9eFWIal9YQkqOKjcd99/8xirFdVV5IZAyq0pU/EfhCkkbdNjigsajWahSOTeHkwbjUs9ATXpTanbw98UJNdTlVVOQovJkALE0YHpU7dd6nJAISa+tLQweozmOZtkVPtIeVAzmgoGIPIHlkmJYyoC3TGRCg5MQdgATupA9qZY1p/Jbx3UCTlOLsAIwaENQEj6O2C2SCaRI+PpR8FtyFljNQzV2am9NsIYlLLn97J6ld6n0/wDKHieIp0ywMSoqCD8dAoFCASTXJBCMSrxBWHY0agOFiVWHqjDcqOw6/dhCrwtQxpUNuKHCrJvJdwYtb06TiGVJ4yATTo29foyQLGXJ9rW9Ht42HQqD9+XOIW3BOEIU6U98naCFjmo8PfFCg57ZIMCpV7HpkmLdcU27AlcBXAldxrt9OC0haV7DbAlsRkn2wWoVPS+GnvkbTT//1/WPsdsvLUVje+2IQVFsmGKk1ehxYoeb4lp+PyxULrZh6H+WTTNZk5uzx8lsiEMXJ2HTMduCGdgGp2HhhSl80x5Mo6eOKoCYk7t9ByQQl06ji1SDyG+FDENWmHIxhwEU0PWoHX8cVYlqDwiXg1WRWFFB6tUVBrigsZaZXSeIyBWR3IStKgDfp92EIDE7yP8A0iS6LViYnenQH4TufsjcfKmTDFREEdzDLAZCJR8aGn2lIoQd/v2+ziqWXFgrXFFA9ZTxIP7QpUHoO5yQLGllnJJbolrc1XnVWB6Lv9tDQ1oKgrhYoR2DIscahakEg7gEg12yQQg2jnSkLgMikkMvuBtkwwVaxyopA5FT1O1KfryQYlERDgu1Kk02wquiQryKnde5G3XwxVWXf41BXj3/ALMVT3yepbX7JSQo9VCS24+0MnHmxlyfb1soFvGorQKBU/LLg4q5h4U8MLFQbbJBCg52ybAod23yYYEqe9a9sWIXiuLJUVGOAlkAqBKnfKyWdKnp+2C0gLhETsR9OC00vWHASkBV9IUr9GRtnT//0PT412zOw5fdlzXRVF1OykWizBW8G+HCEEN/WIGHwyKfkckCxpSaROzD51wsaKGklRlPFgdtqHCSilS0IKUzWZObssfJVnUlaKenXKC3JfOSa9qdciyS6UFm2+0OvywqgJy7MV5fCNvpyQQlWoufT9NT0ruNtx/nvhQwjVELqVi2LGjMo33qep+WBWLXkEdv600zHodz7CpJ+WFBYq8BnMl79iorxX7NOlQPfY5IMWN3TS2TGRwSefKUBeJ+IfEDTtk2JK+04TI9zNy9JByqrVp2B361PhkSoS27lkrLGQeYUmh6/FUbHwrhClJpDKVUI5KoGqD0pWn075YwLZfgiQyMGaMBC46kDcE/QckEK6hLm2NsUKChYn9l96gE+2FBWCExycACQ1aGv6z3OSayrJ0YKaMN6HwySq8FWjCk7neoxVxqFPI96U74qyXyVbm41yxjU7mZOtSKVruB8snHmxPJ9rWXL6pEORI4gUO9D4V75a469ttj1yTAoZ9zkwxQ7mtQMmGBUWQ13yVsaXpET2+jASoCukJPbIEsxFXS3PTvkLZ0qi3+/vkbTS8Q+HTG2QC8QnwyJLKlwiNaY2mlT09qZC2VP//R9BbpQlRXpzy5ja9YxKtJAFA79zgVsWCSbW7Mp6ksQRjaVn1GZaVmG3WopgtW2s1QVD706gYrs3bXTWwK82avWu+RMAWQkQi5L9mj+BjvkPDCeModpDIACdz1UimPhRTxlTeOMhi1Kb1U9MfCiviFSaCzK7Ma0xOKKfEKFm0exmjPJ3rvQqR3weDFPili+o+UJHasdyFQ19MkE7Gla0P8Mh4CfGYprHkbXiDDAY7i3f8AdqkZCsEO29QKnxxOEjkkZQwjV/KHm63IS10aWeWtXSNaiooAQVNNtzkeCTLiCWP5H86X0hjh0K5+sA8JWkj4Kwp15MevTpkuCTEyCHj/ACo/MSKVgulSLbMgqOcRNRUkU5bUJwnGUCQSnVfI3mvS5S0ui3dI1ALLEXTYA9U5V74BEhlxBis+nXkEayTwyWrxbusqsKNTlQVFdx198aLBDlAwlMIDKByPH9ljsfmtRkgqxZZIwFpxNQeQFN/kemFCLjcOOQpXv/n2whgqCNSTxoQew3IwoVoyigkbn7vpwhVGZ9u/PwPhhVn/AOUlhNqHmO3VP91n1PHcZODCXJ9gWUbJbIj7sN9umWNLcnj9OTDWUM465Jip8K7Uw2im1h70r88Fp4UQkFe2+AyZCKLjtx2GQJZiKJW29t8hbPhXGCg6UxteF3okDYdcFsqa9MgD2642rRXfBau4e+KX/9L0ByLMTyBB2Ay+mBRHoNUKHU/LwwFQptFT7Lnbqa0xCuV1pwYGvucVtUUNup6nYDFKk8QjI5PxPfauKrBLGNk+KnU40i15mFKg0PbbGlttFlkU91PU+2KVBrVGY0JA71/hgVywLThGzChrWhpTFVKS1nIoCoXvhtaW/VZoiKkFW6eJxtVaNCTRlPyNQPDAlsK6MDxNT3O+K2vZyahht323xW1qoGZuyHuPDBSLan0uynQrJEkvMUPqor1H07Y0m2MX/wCWPkzU3Ml1otm01OJkWMRHf/jGVxpbYXrv/OPHlfUS/wCj559OcmohUrNAD2osm4G3jgoJtJ4v+caAsVG19pJuhBgUCg7j4q1x4VtWj/5xvCyqP0yxXo1YgT9BrjSo8/8AOOOnngserT135VVentTHZUBdf842cvii1tkYGgDRhiR17EY7Ky38vPyxl8lzzvcXC3yThRUpwKgGu1Cd8lGgxkLeoterCoURniPh45O2vhU2vEelGp7HHiRwLTNHSobcnYYOIp4A4y0qyEMPDHiKeEN/XWVQTAK+OJtaC9tV9PdUFe+2CinZtNcmHWJSK40thEHzBQCkO/TbBSbCvba5BIeE6FD2I3GNLYRR1CzG/P6aUxootYb+0atJBX32xpXevCdw6/fjSHerH/MMVf/T9Evp6BAXkCsT2y22NLBCUNFl5EbYbUBYYTWi74Qgtqswag3GJQrK8kZHwk1wJWmKSTkSwAPUYq4W5CjhSgB+nG1pels4PselemC004Qur8KbHuOmKVUwtHs1T4AYEOVHoQoNT2OKuNsxYArQnrXFXPbyKwY0KrsMaVaIDIKlQadBhVp4OI6gU6DCgrUtwx3kqD1GKHPZwx/EpqfDFWvSQgVHxdOvbFXPDDGPEnc4rakfiPwjbucVtsQmv2jvvQYrbvSlVqLUA9cVVeNwvToK0OClsuBbnR68uuFbbDE0Xjt7DFbbktfWb4hQDFVVbKGNKsor74qhZIqEALRevhihwUEUUb4qtdWX4W3r0A3whCwQb7qeXhja0r+gqr8QNfA42mmhDCKk7HG1bgiVpCa4CUh0qgGimp98IQVIW7sdwKd64VWtBxOxoTvQHFaXek/H7R+/Faf/1PTMnD0zypTelcsQg/3Hqmn0/PChcPSrt+GKtnoONK9sKtJ6vI16e+Kqvw8TWlO+BVJK1+D7PvhVXH1jbhTl/DFVrepT370x2Q38e3OuBIVH+0ONcCuX1OXw/a98Urm5ch6nTFXNw4nh+GKEE/pf7s5VrkkOT06nhXFCqOFPi64qtk40HHriqkeH7dcUqiehXFCqvCvwUriq8cO+Ku+DanTFXfu960riq1PR/pgVWFN616ClMVWSV/ariqi1eOFCyCnqCla+/TFVw5eoeVPbFK5ft/FTlikLpOp6YqULL07UxYrBx71+jCErfD8MBQVX46b1p7dMULV9Op5dcUhd8Ff8n8cKX//Z'
