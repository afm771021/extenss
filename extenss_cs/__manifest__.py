{
    'name': 'Simple Credit',
    'version': '1.0',
    'summary': 'Definition of the Simple Credit',
    'description': 'Definition of the Simple Credit',
    'author': 'Mastermind Software Services',
    'depends': ['base','mail','extenss_credit','board','sale','extenss_request'],
    'application': True,
    'website': 'https://www.mss.mx',
    'category': 'Uncategorized',
    'data': [
        'security/extenss_cs_security.xml',
        'security/ir.model.access.csv',
        'views/credit_cs_view.xml',
        'views/credit_cs_pre_notice_view.xml',
        'views/credit_cs_amortization_view.xml',
        'views/credit_cs_exp_notice_view.xml',
        'views/credit_cs_early_set_view.xml',
        'views/credit_cs_adv_pay_view.xml',
        'views/credit_cs_moras_view.xml',
        'views/credit_cs_acct_portfolio_view.xml',
        'views/credit_cs_payment_balance_view.xml',
        'views/credit_cs_condonation_view.xml',
        'views/credit_cs_statement_account_view.xml',
        'views/credit_cs_account_view.xml',
        ],
}