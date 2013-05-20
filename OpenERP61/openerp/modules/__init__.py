# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#    Copyright (C) 2010-2011 OpenERP s.a. (<http://openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

""" Modules (also called addons) management.

"""

import openerp.modules.db
import openerp.modules.graph
import openerp.modules.loading
import openerp.modules.migration
import openerp.modules.module

# TODO temporarily expose those things
from openerp.modules.module import \
    get_modules, get_modules_with_version, \
    load_information_from_description_file, \
    get_module_resource, zip_directory, \
    get_module_path, initialize_sys_path, \
    load_openerp_module, init_module_models

from openerp.modules.loading import load_modules


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: