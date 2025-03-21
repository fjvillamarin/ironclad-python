# WorkflowStateModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** |  | 
**url** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from openapi_client.models.workflow_state_model import WorkflowStateModel

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStateModel from a JSON string
workflow_state_model_instance = WorkflowStateModel.from_json(json)
# print the JSON string representation of the object
print(WorkflowStateModel.to_json())

# convert the object into a dict
workflow_state_model_dict = workflow_state_model_instance.to_dict()
# create an instance of WorkflowStateModel from a dict
workflow_state_model_from_dict = WorkflowStateModel.from_dict(workflow_state_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


