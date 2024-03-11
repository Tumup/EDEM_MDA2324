# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Robot(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id_sensor: str=None, fechamuestreo: str=None, unidad: str=None, medicion: float=None):  # noqa: E501
        """Robot - a model defined in Swagger

        :param id_sensor: The id_sensor of this Robot.  # noqa: E501
        :type id_sensor: str
        :param fechamuestreo: The fechamuestreo of this Robot.  # noqa: E501
        :type fechamuestreo: str
        :param unidad: The unidad of this Robot.  # noqa: E501
        :type unidad: str
        :param medicion: The medicion of this Robot.  # noqa: E501
        :type medicion: float
        """
        self.swagger_types = {
            'id_sensor': str,
            'fechamuestreo': str,
            'unidad': str,
            'medicion': float
        }

        self.attribute_map = {
            'id_sensor': 'id_sensor',
            'fechamuestreo': 'fechamuestreo',
            'unidad': 'unidad',
            'medicion': 'medicion'
        }
        self._id_sensor = id_sensor
        self._fechamuestreo = fechamuestreo
        self._unidad = unidad
        self._medicion = medicion

    @classmethod
    def from_dict(cls, dikt) -> 'Robot':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Robot of this Robot.  # noqa: E501
        :rtype: Robot
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id_sensor(self) -> str:
        """Gets the id_sensor of this Robot.


        :return: The id_sensor of this Robot.
        :rtype: str
        """
        return self._id_sensor

    @id_sensor.setter
    def id_sensor(self, id_sensor: str):
        """Sets the id_sensor of this Robot.


        :param id_sensor: The id_sensor of this Robot.
        :type id_sensor: str
        """

        self._id_sensor = id_sensor

    @property
    def fechamuestreo(self) -> str:
        """Gets the fechamuestreo of this Robot.


        :return: The fechamuestreo of this Robot.
        :rtype: str
        """
        return self._fechamuestreo

    @fechamuestreo.setter
    def fechamuestreo(self, fechamuestreo: str):
        """Sets the fechamuestreo of this Robot.


        :param fechamuestreo: The fechamuestreo of this Robot.
        :type fechamuestreo: str
        """

        self._fechamuestreo = fechamuestreo

    @property
    def unidad(self) -> str:
        """Gets the unidad of this Robot.


        :return: The unidad of this Robot.
        :rtype: str
        """
        return self._unidad

    @unidad.setter
    def unidad(self, unidad: str):
        """Sets the unidad of this Robot.


        :param unidad: The unidad of this Robot.
        :type unidad: str
        """

        self._unidad = unidad

    @property
    def medicion(self) -> float:
        """Gets the medicion of this Robot.


        :return: The medicion of this Robot.
        :rtype: float
        """
        return self._medicion

    @medicion.setter
    def medicion(self, medicion: float):
        """Sets the medicion of this Robot.


        :param medicion: The medicion of this Robot.
        :type medicion: float
        """

        self._medicion = medicion