# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Person(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, survived: bool=None, passenger_class: int=None, name: str=None, sex: str=None, age: int=None, siblings_or_spouses_aboard: int=None, parents_or_children_aboard: int=None, fare: float=None, uuid: str=None):  # noqa: E501
        """Person - a model defined in Swagger

        :param survived: The survived of this Person.  # noqa: E501
        :type survived: bool
        :param passenger_class: The passenger_class of this Person.  # noqa: E501
        :type passenger_class: int
        :param name: The name of this Person.  # noqa: E501
        :type name: str
        :param sex: The sex of this Person.  # noqa: E501
        :type sex: str
        :param age: The age of this Person.  # noqa: E501
        :type age: int
        :param siblings_or_spouses_aboard: The siblings_or_spouses_aboard of this Person.  # noqa: E501
        :type siblings_or_spouses_aboard: int
        :param parents_or_children_aboard: The parents_or_children_aboard of this Person.  # noqa: E501
        :type parents_or_children_aboard: int
        :param fare: The fare of this Person.  # noqa: E501
        :type fare: float
        :param uuid: The uuid of this Person.  # noqa: E501
        :type uuid: str
        """
        self.swagger_types = {
            'survived': bool,
            'passenger_class': int,
            'name': str,
            'sex': str,
            'age': int,
            'siblings_or_spouses_aboard': int,
            'parents_or_children_aboard': int,
            'fare': float,
            'uuid': str
        }

        self.attribute_map = {
            'survived': 'survived',
            'passenger_class': 'passengerClass',
            'name': 'name',
            'sex': 'sex',
            'age': 'age',
            'siblings_or_spouses_aboard': 'siblingsOrSpousesAboard',
            'parents_or_children_aboard': 'parentsOrChildrenAboard',
            'fare': 'fare',
            'uuid': 'uuid'
        }

        self._survived = survived
        self._passenger_class = passenger_class
        self._name = name
        self._sex = sex
        self._age = age
        self._siblings_or_spouses_aboard = siblings_or_spouses_aboard
        self._parents_or_children_aboard = parents_or_children_aboard
        self._fare = fare
        self._uuid = uuid

    @classmethod
    def from_dict(cls, dikt) -> 'Person':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Person of this Person.  # noqa: E501
        :rtype: Person
        """
        return util.deserialize_model(dikt, cls)

    @property
    def survived(self) -> bool:
        """Gets the survived of this Person.


        :return: The survived of this Person.
        :rtype: bool
        """
        return self._survived

    @survived.setter
    def survived(self, survived: bool):
        """Sets the survived of this Person.


        :param survived: The survived of this Person.
        :type survived: bool
        """

        self._survived = survived

    @property
    def passenger_class(self) -> int:
        """Gets the passenger_class of this Person.


        :return: The passenger_class of this Person.
        :rtype: int
        """
        return self._passenger_class

    @passenger_class.setter
    def passenger_class(self, passenger_class: int):
        """Sets the passenger_class of this Person.


        :param passenger_class: The passenger_class of this Person.
        :type passenger_class: int
        """

        self._passenger_class = passenger_class

    @property
    def name(self) -> str:
        """Gets the name of this Person.


        :return: The name of this Person.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Person.


        :param name: The name of this Person.
        :type name: str
        """

        self._name = name

    @property
    def sex(self) -> str:
        """Gets the sex of this Person.


        :return: The sex of this Person.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex: str):
        """Sets the sex of this Person.


        :param sex: The sex of this Person.
        :type sex: str
        """
        allowed_values = ["male", "female", "other"]  # noqa: E501
        if sex not in allowed_values:
            raise ValueError(
                "Invalid value for `sex` ({0}), must be one of {1}"
                .format(sex, allowed_values)
            )

        self._sex = sex

    @property
    def age(self) -> int:
        """Gets the age of this Person.


        :return: The age of this Person.
        :rtype: int
        """
        return self._age

    @age.setter
    def age(self, age: int):
        """Sets the age of this Person.


        :param age: The age of this Person.
        :type age: int
        """

        self._age = age

    @property
    def siblings_or_spouses_aboard(self) -> int:
        """Gets the siblings_or_spouses_aboard of this Person.


        :return: The siblings_or_spouses_aboard of this Person.
        :rtype: int
        """
        return self._siblings_or_spouses_aboard

    @siblings_or_spouses_aboard.setter
    def siblings_or_spouses_aboard(self, siblings_or_spouses_aboard: int):
        """Sets the siblings_or_spouses_aboard of this Person.


        :param siblings_or_spouses_aboard: The siblings_or_spouses_aboard of this Person.
        :type siblings_or_spouses_aboard: int
        """

        self._siblings_or_spouses_aboard = siblings_or_spouses_aboard

    @property
    def parents_or_children_aboard(self) -> int:
        """Gets the parents_or_children_aboard of this Person.


        :return: The parents_or_children_aboard of this Person.
        :rtype: int
        """
        return self._parents_or_children_aboard

    @parents_or_children_aboard.setter
    def parents_or_children_aboard(self, parents_or_children_aboard: int):
        """Sets the parents_or_children_aboard of this Person.


        :param parents_or_children_aboard: The parents_or_children_aboard of this Person.
        :type parents_or_children_aboard: int
        """

        self._parents_or_children_aboard = parents_or_children_aboard

    @property
    def fare(self) -> float:
        """Gets the fare of this Person.


        :return: The fare of this Person.
        :rtype: float
        """
        return self._fare

    @fare.setter
    def fare(self, fare: float):
        """Sets the fare of this Person.


        :param fare: The fare of this Person.
        :type fare: float
        """

        self._fare = fare

    @property
    def uuid(self) -> str:
        """Gets the uuid of this Person.


        :return: The uuid of this Person.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this Person.


        :param uuid: The uuid of this Person.
        :type uuid: str
        """

        self._uuid = uuid
