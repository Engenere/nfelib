"""This file was generated by xsdata, v24.2.1, on 2024-02-24 11:16:25

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass
from nfelib.nfe_evento_cce.bindings.v1_0.leiaute_cce_v1_00 import TprocEvento

__NAMESPACE__ = "http://www.portalfiscal.inf.br/nfe"


@dataclass
class ProcEventoNfe(TprocEvento):
    """
    Schema XML de validação do proc Carta de Correção da NFe.
    """

    class Meta:
        name = "procEventoNFe"
        namespace = "http://www.portalfiscal.inf.br/nfe"
