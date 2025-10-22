// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from tutorial_interfaces:msg/FilteredSensor.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__TRAITS_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "tutorial_interfaces/msg/detail/filtered_sensor__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace tutorial_interfaces
{

namespace msg
{

inline void to_flow_style_yaml(
  const FilteredSensor & msg,
  std::ostream & out)
{
  out << "{";
  // member: promedio
  {
    out << "promedio: ";
    rosidl_generator_traits::value_to_yaml(msg.promedio, out);
    out << ", ";
  }

  // member: valor_a
  {
    out << "valor_a: ";
    rosidl_generator_traits::value_to_yaml(msg.valor_a, out);
    out << ", ";
  }

  // member: valor_b
  {
    out << "valor_b: ";
    rosidl_generator_traits::value_to_yaml(msg.valor_b, out);
    out << ", ";
  }

  // member: valor_c
  {
    out << "valor_c: ";
    rosidl_generator_traits::value_to_yaml(msg.valor_c, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FilteredSensor & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: promedio
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "promedio: ";
    rosidl_generator_traits::value_to_yaml(msg.promedio, out);
    out << "\n";
  }

  // member: valor_a
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "valor_a: ";
    rosidl_generator_traits::value_to_yaml(msg.valor_a, out);
    out << "\n";
  }

  // member: valor_b
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "valor_b: ";
    rosidl_generator_traits::value_to_yaml(msg.valor_b, out);
    out << "\n";
  }

  // member: valor_c
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "valor_c: ";
    rosidl_generator_traits::value_to_yaml(msg.valor_c, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FilteredSensor & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace tutorial_interfaces

namespace rosidl_generator_traits
{

[[deprecated("use tutorial_interfaces::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const tutorial_interfaces::msg::FilteredSensor & msg,
  std::ostream & out, size_t indentation = 0)
{
  tutorial_interfaces::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use tutorial_interfaces::msg::to_yaml() instead")]]
inline std::string to_yaml(const tutorial_interfaces::msg::FilteredSensor & msg)
{
  return tutorial_interfaces::msg::to_yaml(msg);
}

template<>
inline const char * data_type<tutorial_interfaces::msg::FilteredSensor>()
{
  return "tutorial_interfaces::msg::FilteredSensor";
}

template<>
inline const char * name<tutorial_interfaces::msg::FilteredSensor>()
{
  return "tutorial_interfaces/msg/FilteredSensor";
}

template<>
struct has_fixed_size<tutorial_interfaces::msg::FilteredSensor>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<tutorial_interfaces::msg::FilteredSensor>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<tutorial_interfaces::msg::FilteredSensor>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__TRAITS_HPP_
