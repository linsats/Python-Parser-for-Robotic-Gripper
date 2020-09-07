import os
from urdf_parser_py import urdf

xmls = [line for line in open('/home/lins/MetaGrasp/grippers/robotiq_arg85_description.URDF')]
urdf.Robot.from_xml_string(xmls)

