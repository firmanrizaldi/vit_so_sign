# -*- coding: utf-8 -*-
from odoo import http

# class VitSoSign(http.Controller):
#     @http.route('/vit_so_sign/vit_so_sign/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_so_sign/vit_so_sign/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_so_sign.listing', {
#             'root': '/vit_so_sign/vit_so_sign',
#             'objects': http.request.env['vit_so_sign.vit_so_sign'].search([]),
#         })

#     @http.route('/vit_so_sign/vit_so_sign/objects/<model("vit_so_sign.vit_so_sign"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_so_sign.object', {
#             'object': obj
#         })