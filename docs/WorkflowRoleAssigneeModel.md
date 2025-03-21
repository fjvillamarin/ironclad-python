# WorkflowRoleAssigneeModel



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.workflow_role_assignee_model import WorkflowRoleAssigneeModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRoleAssigneeModel from a JSON string
workflow_role_assignee_model_instance = WorkflowRoleAssigneeModel.from_json(json)
# print the JSON string representation of the object
print(WorkflowRoleAssigneeModel.to_json())

# convert the object into a dict
workflow_role_assignee_model_dict = workflow_role_assignee_model_instance.to_dict()
# create an instance of WorkflowRoleAssigneeModel from a dict
workflow_role_assignee_model_from_dict = WorkflowRoleAssigneeModel.from_dict(workflow_role_assignee_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


