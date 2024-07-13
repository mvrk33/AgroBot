#include <rclcpp/rclcpp.hpp>
#include <lifecycle_msgs/msg/transition_point.hpp>
#include <lifecycle_msgs/srv/change_state.hpp>

using namespace std::placeholders;

class SimulationStopNode : public rclcpp::Node
{
public:
  SimulationStopNode() : Node("simulation_stop_node")
  {
    // Identify the lifecycle manager node (might vary)
    lifecycle_node_name_ = "/gazebo/change_state";

    // Create a service client to interact with the simulation manager
    client_ = create_client<lifecycle_msgs::srv::ChangeState>(lifecycle_node_name_);

    // Transition callback to be triggered when the node becomes active
    transition_callback_ = std::bind(&SimulationStopNode::on_transition, this, _1);
    lifecycle_manager_ = get_node_lifetime()->create_lifecycle_node(
        get_name(), transition_callback_);
  }

private:
  std::string lifecycle_node_name_;
  rclcpp::Client<lifecycle_msgs::srv::ChangeState>::SharedPtr client_;
  rclcpp::callback_group::CallbackGroup::WeakPtr transition_callback_group_;
  rclcpp::lifecycle::LifecycleNode::SharedPtr lifecycle_manager_;

  void on_transition(const lifecycle_msgs::msg::TransitionPoint::SharedPtr transition)
  {
    if (transition->id == lifecycle_msgs::msg::Transition::TRANSITION_CONFIGURE)
    {
      // No action needed in configure state
    }
    else if (transition->id == lifecycle_msgs::msg::Transition::TRANSITION_ACTIVATE)
    {
      // Send a service request to deactivate the simulation node (might vary)
      auto request = std::make_shared<lifecycle_msgs::srv::ChangeState>();
      request->goal_state.id = lifecycle_msgs::msg::State::STATE_INACTIVE;
      future_ = client_->async_send_request(request);
    }
  }
};

int main(int argc, char** argv)
{
  rclcpp::init(argc, argv);
  auto node = std::make_shared<SimulationStopNode>();
  rclcpp::spin(node);
  rclcpp::shutdown();
  return 0;
}
