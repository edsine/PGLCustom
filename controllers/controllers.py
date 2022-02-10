# -*- coding: utf-8 -*-
# from odoo import http


# class Pgl-custom(http.Controller):
#     @http.route('/pgl-custom/pgl-custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pgl-custom/pgl-custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pgl-custom.listing', {
#             'root': '/pgl-custom/pgl-custom',
#             'objects': http.request.env['pgl-custom.pgl-custom'].search([]),
#         })

#     @http.route('/pgl-custom/pgl-custom/objects/<model("pgl-custom.pgl-custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pgl-custom.object', {
#             'object': obj
#         })
