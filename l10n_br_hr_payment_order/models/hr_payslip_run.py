# -*- coding: utf-8 -*-
# Copyright 2017 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, models


class HrPayslipRun(models.Model):
    _inherit = "hr.payslip.run"

    @api.multi
    def gerar_holerites(self):
        self.verificar_holerites_gerados()
        for contrato in self.contract_id:
            try:
                payslip_obj = self.env['hr.payslip']
                payslip = payslip_obj.create({
                    'contract_id': contrato.id,
                    'mes_do_ano': self.mes_do_ano,
                    'ano': self.ano,
                    'employee_id': contrato.employee_id.id,
                    'tipo_de_folha': self.tipo_de_folha,
                    'payslip_run_id': self.id,
                })
                payslip._compute_set_dates()
                payslip.compute_sheet()
                payslip.hr_verify_sheet()
            except:
                payslip.unlink()
                continue
        self.verificar_holerites_gerados()