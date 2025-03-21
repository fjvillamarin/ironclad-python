# WorkflowRoleModel



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**assignees** | [**List[WorkflowRoleAssigneeModel]**](WorkflowRoleAssigneeModel.md) |  | [optional] 

## Example

```python
from openapi_client.models.workflow_role_model import WorkflowRoleModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowRoleModel from a JSON string
workflow_role_model_instance = WorkflowRoleModel.from_json(json)
# print the JSON string representation of the object
print(WorkflowRoleModel.to_json())

# convert the object into a dict
workflow_role_model_dict = workflow_role_model_instance.to_dict()
# create an instance of WorkflowRoleModel from a dict
workflow_role_model_from_dict = WorkflowRoleModel.from_dict(workflow_role_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


