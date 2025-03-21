# WorkflowResponseModelRolesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**display_name** | **str** |  | 
**assignees** | [**List[WorkflowResponseModelRolesInnerAssigneesInner]**](WorkflowResponseModelRolesInnerAssigneesInner.md) |  | 

## Example

```python
from openapi_client.models.workflow_response_model_roles_inner import WorkflowResponseModelRolesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowResponseModelRolesInner from a JSON string
workflow_response_model_roles_inner_instance = WorkflowResponseModelRolesInner.from_json(json)
# print the JSON string representation of the object
print(WorkflowResponseModelRolesInner.to_json())

# convert the object into a dict
workflow_response_model_roles_inner_dict = workflow_response_model_roles_inner_instance.to_dict()
# create an instance of WorkflowResponseModelRolesInner from a dict
workflow_response_model_roles_inner_from_dict = WorkflowResponseModelRolesInner.from_dict(workflow_response_model_roles_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


