# -*- coding: utf-8 -*-
# from odoo import http


# class Copartners(http.Controller):
#     @http.route('/copartners/copartners', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/copartners/copartners/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('copartners.listing', {
#             'root': '/copartners/copartners',
#             'objects': http.request.env['copartners.copartners'].search([]),
#         })

#     @http.route('/copartners/copartners/objects/<model("copartners.copartners"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('copartners.object', {
#             'object': obj
#         })
