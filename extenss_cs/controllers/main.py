from odoo import http
from odoo import http, _, fields
from odoo.http import request
from babel.dates import format_datetime, format_date
from datetime import datetime
from odoo.addons.website_sale.controllers.main import WebsiteSale

class ExtenssCSController(http.Controller):

    @http.route('/cs', website=True, auth='public')
    def crm_ff(self, **kw):
        return request.render("extenss_cs.cs_template_page", {})

    @http.route('/cs_send', auth='public', website=True)
    def cs_send_form(self, request, **kw):
        id_customer = request.env['res.partner'].sudo().create(
            {
                'name': kw.get('partner_id'),
                'email': kw.get('email_from'),
            })

        id_channel = request.env['extenss.request.sales_channel_id'].search([('name', '=', 'Website')])
        if not id_channel:
            id_channel = request.env['extenss.request.sales_channel_id'].sudo().create(
                {
                    'name': 'Website',
                    'shortcut': 'WS',
                })

        # id_prod = request.env['extenss.product.template'].search([('credit_type.shortcut', '=', 'cs')])

        request.env['crm.lead'].sudo().create(
            {
                'partner_id': id_customer.id,
                'type': 'opportunity',
                'product_name': 'cs',
                'sales_channel_id': id_channel.id,
                'description': kw.get('term_cred') +" "+  kw.get('frequency_cred'),
                'planned_revenue': kw.get('planned_revenue'),
            })

        return request.render("extenss_cs.cs_send_ok", {})
