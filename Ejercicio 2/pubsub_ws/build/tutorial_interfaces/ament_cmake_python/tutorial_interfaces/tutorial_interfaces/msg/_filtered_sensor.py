# generated from rosidl_generator_py/resource/_idl.py.em
# with input from tutorial_interfaces:msg/FilteredSensor.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_FilteredSensor(type):
    """Metaclass of message 'FilteredSensor'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('tutorial_interfaces')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'tutorial_interfaces.msg.FilteredSensor')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__filtered_sensor
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__filtered_sensor
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__filtered_sensor
            cls._TYPE_SUPPORT = module.type_support_msg__msg__filtered_sensor
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__filtered_sensor

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class FilteredSensor(metaclass=Metaclass_FilteredSensor):
    """Message class 'FilteredSensor'."""

    __slots__ = [
        '_promedio',
        '_valor_a',
        '_valor_b',
        '_valor_c',
    ]

    _fields_and_field_types = {
        'promedio': 'double',
        'valor_a': 'double',
        'valor_b': 'double',
        'valor_c': 'double',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
        rosidl_parser.definition.BasicType('double'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.promedio = kwargs.get('promedio', float())
        self.valor_a = kwargs.get('valor_a', float())
        self.valor_b = kwargs.get('valor_b', float())
        self.valor_c = kwargs.get('valor_c', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.promedio != other.promedio:
            return False
        if self.valor_a != other.valor_a:
            return False
        if self.valor_b != other.valor_b:
            return False
        if self.valor_c != other.valor_c:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def promedio(self):
        """Message field 'promedio'."""
        return self._promedio

    @promedio.setter
    def promedio(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'promedio' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'promedio' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._promedio = value

    @builtins.property
    def valor_a(self):
        """Message field 'valor_a'."""
        return self._valor_a

    @valor_a.setter
    def valor_a(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'valor_a' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'valor_a' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._valor_a = value

    @builtins.property
    def valor_b(self):
        """Message field 'valor_b'."""
        return self._valor_b

    @valor_b.setter
    def valor_b(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'valor_b' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'valor_b' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._valor_b = value

    @builtins.property
    def valor_c(self):
        """Message field 'valor_c'."""
        return self._valor_c

    @valor_c.setter
    def valor_c(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'valor_c' field must be of type 'float'"
            assert not (value < -1.7976931348623157e+308 or value > 1.7976931348623157e+308) or math.isinf(value), \
                "The 'valor_c' field must be a double in [-1.7976931348623157e+308, 1.7976931348623157e+308]"
        self._valor_c = value
