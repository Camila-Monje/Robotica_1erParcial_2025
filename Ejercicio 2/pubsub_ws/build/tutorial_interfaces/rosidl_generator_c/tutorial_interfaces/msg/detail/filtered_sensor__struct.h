// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from tutorial_interfaces:msg/FilteredSensor.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__STRUCT_H_
#define TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/FilteredSensor in the package tutorial_interfaces.
typedef struct tutorial_interfaces__msg__FilteredSensor
{
  double promedio;
  double valor_a;
  double valor_b;
  double valor_c;
} tutorial_interfaces__msg__FilteredSensor;

// Struct for a sequence of tutorial_interfaces__msg__FilteredSensor.
typedef struct tutorial_interfaces__msg__FilteredSensor__Sequence
{
  tutorial_interfaces__msg__FilteredSensor * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} tutorial_interfaces__msg__FilteredSensor__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__STRUCT_H_
