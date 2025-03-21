# LaunchedWorkflowModelSignatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | The state of the signatures. | [optional] [readonly] 
**url** | **str** | The url where signature information is located if it exists. | [optional] [readonly] 

## Example

```python
from openapi_client.models.launched_workflow_model_signatures import LaunchedWorkflowModelSignatures

# TODO update the JSON string below
json = "{}"
# create an instance of LaunchedWorkflowModelSignatures from a JSON string
launched_workflow_model_signatures_instance = LaunchedWorkflowModelSignatures.from_json(json)
# print the JSON string representation of the object
print(LaunchedWorkflowModelSignatures.to_json())

# convert the object into a dict
launched_workflow_model_signatures_dict = launched_workflow_model_signatures_instance.to_dict()
# create an instance of LaunchedWorkflowModelSignatures from a dict
launched_workflow_model_signatures_from_dict = LaunchedWorkflowModelSignatures.from_dict(launched_workflow_model_signatures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


