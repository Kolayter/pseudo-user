import asyncio
import logging

class EventManager:
    def __init__(self):
        self._listeners = {}
    
    def listen(self, event_type: str, listener):
        if event_type not in self._listeners:
            self._listeners[event_type] = []
        self._listeners[event_type].append(listener)

    async def emit(self, event_type: str, **kwargs):
        if event_type in self._listeners:
            tasks = [listener(**kwargs) for listener in self._listeners[event_type]]
            await asyncio.gather(*tasks, return_exceptions=True)