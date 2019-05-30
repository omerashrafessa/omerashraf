# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleTask(models.Model):
    _name = 'sale.task'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _rec_name = 'company'

    line_ids = fields.One2many(comodel_name='sale.line', inverse_name='line_id', string='Sale Line')

    company = fields.Many2one(
        string=u'company',
        comodel_name='company.company',
        required=True,
        )

    quantity = fields.Integer(
        string=u'Credit Amount',
        )
    
    sale_no = fields.Integer(
        string=u'No',
        )
    
    types = fields.Selection(
        string=u'Type',required=True,
        selection=[('cre', 'Credit'), ('vou', 'Voucher')], default='cre'
        )
    
    remaining_balance_mtn = fields.Integer(string='Remaining Balance', compute='compute_remaining_balnca_mtn')    

    sum_total = fields.Integer(string='Total Balance', compute='compute_sum_total')

    @api.one
    def compute_sum_total(self):
        count = 0
        for i in self.line_ids:
            print (i, '/////////////////////')
            print (i.total, '/n/n')
            count += i.total
            print (count, 'Count')
        
        self.sum_total = count
        print (self.sum_total, '///////////Sum Total/////////')


    @api.onchange('quantity')
    def compute_remaining_balnca_mtn(self):
        balance_list = self.env['balance.balance'].search([])
        print (balance_list.balance_mtn, '////////// MTN Balance//////////')
        if self.quantity > balance_list.balance_mtn:
            raise exception.except_orm(_('Warning'),_('Credit amount is more than the available'))
        else:
            balance_list.balance_mtn -= self.quantity
        
        print (balance_list.balance_mtn, '////////// MTN Balance after deduction//////////')
        self.remaining_balance_mtn = balance_list.balance_mtn
        print (self.remaining_balance_mtn, '//////////after deduction//////////')




class sale_line(models.Model):
    _name = 'sale.line'

    line_id = fields.Many2one(comodel_name='sale.task', string='')
    

    voucher_amount = fields.Integer(
    string='Amount', 
    )
    quantity = fields.Integer(
    string='Quantity'
    )

    total = fields.Integer(
        string=u'Total', 
        readonly=True,
        compute='compute_total'
        
    )
    

    @api.depends('voucher_amount', 'quantity')
    def compute_total(self):
        for i in self:
            i.total = i.voucher_amount * i.quantity



class company(models.Model):
    _name = 'company.company'

    name = fields.Char(string='Name', required=True)
    address = fields.Char(string='Street')
    city = fields.Char(string='Citey')
    country = fields.Many2one(comodel_name='res.country', string='Country')
    




class balance(models.Model):
    _name = 'balance.balance'


    balance_mtn = fields.Integer(string='MTN Balance', 
    required=True,
    )
    balance_sudani = fields.Integer(string='Sudani Balance', 
    required=True,
    )
    balance_zain = fields.Integer(string='Zain Balalnce',
    required=True,
    )
    
