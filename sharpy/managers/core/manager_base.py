import logging
import string

from sc2 import Result, UnitTypeId

import sc2
from sc2.client import Client
from typing import TYPE_CHECKING

from sharpy.general.component import Component

if TYPE_CHECKING:
    from sharpy.knowledges import Knowledge, KnowledgeBot
    from sharpy.managers.core import UnitCacheManager, UnitValue


class ManagerBase(Component):
    async def update(self):
        pass

    def real_type(self, type_id: UnitTypeId) -> UnitTypeId:
        return self.unit_values.real_type(type_id)

    async def post_update(self):
        pass

    async def on_end(self, game_result: Result):
        pass
