# Copyright (C) 2011-2012 CRS4.
#
# This file is part of Seal.
#
# Seal is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Seal is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Seal.  If not, see <http://www.gnu.org/licenses/>.

class HitProcessorChainLink(object):
    def __init__(self, next_link = None):
        self.next_link = next_link

    def set_next(self, link):
        self.next_link = link
        return link

    def process(self, pair):
        """
        Identity action.  Passes to the next link, if any.
        """
        if self.next_link:
            self.next_link.process(pair)
