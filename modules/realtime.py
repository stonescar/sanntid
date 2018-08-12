#!/usr/bin/env python
# -*- coding: utf-8 -*-

from stop import Stop


class Realtime():
    def __init__(self, lines):
        self.lines = self.initializeStops(lines)

    def initializeStops(self, lines):
        stops = []
        for line in lines:
            if "destination" not in line:
                line["destination"] = ""
            stops.append(Stop(line["stop_id"],
                              line["line"],
                              line["destination"] or ""))
        return stops
