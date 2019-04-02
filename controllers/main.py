from odoo import http

from odoo.addons.portal.controllers.web import Home

class Website(Home):

    @http.route('/page/home', type='http', auth='public', website=True)
    def index(self, **kw):
        redirect = "http://www.precisionepllc.com/precisionepllc/"
        return http.redirect_with_hash(redirect,code=301)

class Redirects(http.Controller):

    @http.route('/page/contactus', type='http', auth='public', website=True)
    def contactus(self, **kw):
        redirect = "http://www.precisionepllc.com/precisionepllc/contact-us/"
        return http.redirect_with_hash(redirect,code=301)
