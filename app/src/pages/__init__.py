from .points import Points
from .customers import Customer
from ..utils import Page

from typing import Dict, Type


PAGE_MAP: Dict[str, Type[Page]] = {
    "Análise do Programa de pontos": Points,
    "Análise de Clientes e Produtos": Customer,
}

__all__ = ["PAGE_MAP"]