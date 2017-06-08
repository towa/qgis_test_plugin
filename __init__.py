# -*- coding: utf-8 -*-
"""
/***************************************************************************
 testplugin
                                 A QGIS plugin
 to test automated plugin deploy
                             -------------------
        begin                : 2017-06-08
        copyright            : (C) 2017 by Frank Nord
        email                : f@nord.de
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load testplugin class from file testplugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .testplugin import testplugin
    return testplugin(iface)
