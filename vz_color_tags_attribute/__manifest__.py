{
    "name": """Color product variant tags""",
    "summary": """Color product variant tags""",
    "version": "18.0.8.0.1",
    "author": "Vitalii Zelinski",
    "license": "OPL-1",
    "depends": ["stock", "sale", "product"],
    
    "data": [
        'views/product_product_view.xml',
        'views/product_attribute_value_view.xml',
        'views/sale_order_view.xml',
        'views/purchase_order_view.xml',
        'views/stock_picking_view.xml',
    ],
    "assets": {
        "web.assets_backend": [
            "vz_color_tags_attribute/static/src/views/many2many_tags_hex/many2many_tags_hex.js",
            "vz_color_tags_attribute/static/src/views/many2many_tags_hex/many2many_tags_hex.xml",
            "vz_color_tags_attribute/static/src/views/many2many_tags_hex/many2many_tags_hex.scss",
        ],
    },
    "demo": [
        
    ],
    "qweb": [],
    "post_load": None,
    "application": False,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,
    "auto_install": False,
    "installable": True,
}