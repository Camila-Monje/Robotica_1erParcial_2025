// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from tutorial_interfaces:msg/FilteredSensor.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__BUILDER_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "tutorial_interfaces/msg/detail/filtered_sensor__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace tutorial_interfaces
{

namespace msg
{

namespace builder
{

class Init_FilteredSensor_valor_c
{
public:
  explicit Init_FilteredSensor_valor_c(::tutorial_interfaces::msg::FilteredSensor & msg)
  : msg_(msg)
  {}
  ::tutorial_interfaces::msg::FilteredSensor valor_c(::tutorial_interfaces::msg::FilteredSensor::_valor_c_type arg)
  {
    msg_.valor_c = std::move(arg);
    return std::move(msg_);
  }

private:
  ::tutorial_interfaces::msg::FilteredSensor msg_;
};

class Init_FilteredSensor_valor_b
{
public:
  explicit Init_FilteredSensor_valor_b(::tutorial_interfaces::msg::FilteredSensor & msg)
  : msg_(msg)
  {}
  Init_FilteredSensor_valor_c valor_b(::tutorial_interfaces::msg::FilteredSensor::_valor_b_type arg)
  {
    msg_.valor_b = std::move(arg);
    return Init_FilteredSensor_valor_c(msg_);
  }

private:
  ::tutorial_interfaces::msg::FilteredSensor msg_;
};

class Init_FilteredSensor_valor_a
{
public:
  explicit Init_FilteredSensor_valor_a(::tutorial_interfaces::msg::FilteredSensor & msg)
  : msg_(msg)
  {}
  Init_FilteredSensor_valor_b valor_a(::tutorial_interfaces::msg::FilteredSensor::_valor_a_type arg)
  {
    msg_.valor_a = std::move(arg);
    return Init_FilteredSensor_valor_b(msg_);
  }

private:
  ::tutorial_interfaces::msg::FilteredSensor msg_;
};

class Init_FilteredSensor_promedio
{
public:
  Init_FilteredSensor_promedio()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_FilteredSensor_valor_a promedio(::tutorial_interfaces::msg::FilteredSensor::_promedio_type arg)
  {
    msg_.promedio = std::move(arg);
    return Init_FilteredSensor_valor_a(msg_);
  }

private:
  ::tutorial_interfaces::msg::FilteredSensor msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::tutorial_interfaces::msg::FilteredSensor>()
{
  return tutorial_interfaces::msg::builder::Init_FilteredSensor_promedio();
}

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__BUILDER_HPP_
