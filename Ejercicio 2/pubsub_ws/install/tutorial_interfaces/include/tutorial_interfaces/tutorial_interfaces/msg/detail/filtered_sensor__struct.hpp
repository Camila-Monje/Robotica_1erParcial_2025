// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from tutorial_interfaces:msg/FilteredSensor.idl
// generated code does not contain a copyright notice

#ifndef TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__STRUCT_HPP_
#define TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__tutorial_interfaces__msg__FilteredSensor __attribute__((deprecated))
#else
# define DEPRECATED__tutorial_interfaces__msg__FilteredSensor __declspec(deprecated)
#endif

namespace tutorial_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FilteredSensor_
{
  using Type = FilteredSensor_<ContainerAllocator>;

  explicit FilteredSensor_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->promedio = 0.0;
      this->valor_a = 0.0;
      this->valor_b = 0.0;
      this->valor_c = 0.0;
    }
  }

  explicit FilteredSensor_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->promedio = 0.0;
      this->valor_a = 0.0;
      this->valor_b = 0.0;
      this->valor_c = 0.0;
    }
  }

  // field types and members
  using _promedio_type =
    double;
  _promedio_type promedio;
  using _valor_a_type =
    double;
  _valor_a_type valor_a;
  using _valor_b_type =
    double;
  _valor_b_type valor_b;
  using _valor_c_type =
    double;
  _valor_c_type valor_c;

  // setters for named parameter idiom
  Type & set__promedio(
    const double & _arg)
  {
    this->promedio = _arg;
    return *this;
  }
  Type & set__valor_a(
    const double & _arg)
  {
    this->valor_a = _arg;
    return *this;
  }
  Type & set__valor_b(
    const double & _arg)
  {
    this->valor_b = _arg;
    return *this;
  }
  Type & set__valor_c(
    const double & _arg)
  {
    this->valor_c = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator> *;
  using ConstRawPtr =
    const tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__tutorial_interfaces__msg__FilteredSensor
    std::shared_ptr<tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__tutorial_interfaces__msg__FilteredSensor
    std::shared_ptr<tutorial_interfaces::msg::FilteredSensor_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FilteredSensor_ & other) const
  {
    if (this->promedio != other.promedio) {
      return false;
    }
    if (this->valor_a != other.valor_a) {
      return false;
    }
    if (this->valor_b != other.valor_b) {
      return false;
    }
    if (this->valor_c != other.valor_c) {
      return false;
    }
    return true;
  }
  bool operator!=(const FilteredSensor_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FilteredSensor_

// alias to use template instance with default allocator
using FilteredSensor =
  tutorial_interfaces::msg::FilteredSensor_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace tutorial_interfaces

#endif  // TUTORIAL_INTERFACES__MSG__DETAIL__FILTERED_SENSOR__STRUCT_HPP_
