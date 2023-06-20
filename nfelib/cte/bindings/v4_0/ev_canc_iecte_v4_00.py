from dataclasses import dataclass, field
from enum import Enum
from typing import Optional

__NAMESPACE__ = "http://www.portalfiscal.inf.br/cte"


class EvCancIecteDescEvento(Enum):
    CANCELAMENTO_DO_INSUCESSO_DE_ENTREGA_DO_CT_E = "Cancelamento do Insucesso de Entrega do CT-e"


@dataclass
class EvCancIecte:
    """
    Schema XML de validação do evento cancelamento do insucesso de entrega
    eletrônico do CT-e 110191.

    :ivar descEvento: Descrição do Evento - “Cancelamento do Insucesso
        de Entrega do CT-e”
    :ivar nProt: Número do Protocolo de autorização do CT-e
    :ivar nProtIE: Número do Protocolo de autorização do evento a ser
        cancelado
    """
    class Meta:
        name = "evCancIECTe"
        namespace = "http://www.portalfiscal.inf.br/cte"

    descEvento: Optional[EvCancIecteDescEvento] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
        }
    )
    nProt: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
    nProtIE: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
            "white_space": "preserve",
            "pattern": r"[0-9]{15}",
        }
    )
