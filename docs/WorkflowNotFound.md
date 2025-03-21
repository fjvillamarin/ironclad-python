# WorkflowNotFound

Workflow ID Not Found Request Error

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**param** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.workflow_not_found import WorkflowNotFound

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowNotFound from a JSON string
workflow_not_found_instance = WorkflowNotFound.from_json(json)
# print the JSON string representation of the object
print(WorkflowNotFound.to_json())

# convert the object into a dict
workflow_not_found_dict = workflow_not_found_instance.to_dict()
# create an instance of WorkflowNotFound from a dict
workflow_not_found_from_dict = WorkflowNotFound.from_dict(workflow_not_found_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


