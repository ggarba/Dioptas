# -*- coding: utf8 -*-
# Dioptas - GUI program for fast processing of 2D X-ray data
#     Copyright (C) 2014  Clemens Prescher (clemens.prescher@gmail.com)
#     GSECARS, University of Chicago
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
__author__ = 'Clemens Prescher'
import unittest
from Data.jcpds import jcpds
from Views.JcpdsEditorWidget import JcpdsEditorWidget
from PyQt4 import QtGui
import sys

class JcpdsDisplayTestAuAnderson(unittest.TestCase):
    def setUp(self):
        self.app = QtGui.QApplication(sys.argv)
        self.jcpds = jcpds()
        self.jcpds.read_file('Data/jcpds/au_Anderson.jcpds')

        self.jcpds_editor = JcpdsEditorWidget(self.jcpds)

    def tearDown(self):
        pass

    def test_filename_and_comment_are_shown_correctly(self):
        self.assertEqual(self.jcpds_editor.filename_txt.text(),
                         self.jcpds.filename)
        self.assertEqual(self.jcpds_editor.comments_txt.text(),
                         self.jcpds.comments)

    def test_all_lattice_parameters_are_shown_correctly(self):
        self.assertEqual(float(str(self.jcpds_editor.lattice_a_txt.text())),
                         self.jcpds.a0)
        self.assertEqual(float(str(self.jcpds_editor.lattice_b_txt.text())),
                         self.jcpds.b0)
        self.assertEqual(float(str(self.jcpds_editor.lattice_c_txt.text())),
                         self.jcpds.c0)
        self.assertEqual(float(str(self.jcpds_editor.lattice_c_txt.text())),
                         self.jcpds.v0)

        self.assertEqual(float(str(self.jcpds_editor.lattice_alpha_txt.text()),
                         self.jcpds.alpha)
        self.assertEqual(float(str(self.jcpds_editor.lattice_beta_txt.text())),
                         self.jcpds.beta0)
        self.assertEqual(float(str(self.jcpds_editor.lattice_gamma_txt.text()),
                         self.jcpds.gamma0)

        self.assertEqual(float(str(self.jcpds_editor.lattice_ab_txt.text()),
                         self.jcpds.a0/float(self.jcpds.b0))
        self.assertEqual(self.jcpds_editor.lattice_ca_txt.text(),
                         '1')
        self.assertEqual(self.jcpds_editor.lattice_cb_txt.text(),
                         '1')